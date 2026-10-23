#!/usr/bin/env python3
"""Inventory, render, hunt and diff Gerber (RS-274X) PCB fabrication layers.

Companion tool for CTFTTE-HWR-003 / CTFTCTE-HWR-003 (PCB fabrication-layer
concealment). Standard library only — no pip install, safe on Kali (PEP 668).

Usage:
  gerber-layer-inspect.py info DIR_OR_FILES...         # layer inventory, flags inner layers
  gerber-layer-inspect.py render F.gbr -o out.png      # raster (PNG) or vector (.svg)
        [--window X1,Y1,X2,Y2] [--ppmm 40] [--mirror] [--rotate 90]
  gerber-layer-inspect.py hunt DIR_OR_FILES... [--png-dir crops/]
        # copper strokes touching no pad/via/pour: drawn text / art candidates
  gerber-layer-inspect.py diff SUSPECT.gbr REFERENCE.gbr [--png-dir crops/]
        # primitives added/removed vs the original design (open-source boards)
  gerber-layer-inspect.py --selftest

Why not a plain "X..Y..D0n" regex: coordinates are modal (X or Y may be
omitted), D-code numbers are per-file (diffing must key on the aperture
definition), arcs (G02/G03), regions (G36/G37) and clear polarity (%LPC%)
all change what is actually copper. Coordinates are reported in file units
(mm for KiCad exports) in board space: Y up, as in the Gerber file.

--rotate is counter-clockwise; text running bottom-to-top along Y reads with
--rotate 270, top-to-bottom with --rotate 90. Bottom-layer text placed the KiCad
way reads mirrored from above (--mirror), but CTF authors often draw it
unmirrored, so hunt/diff crops are never mirrored automatically.
"""
from __future__ import annotations

import argparse
import math
import re
import struct
import sys
import tempfile
import zlib
from pathlib import Path

GERBER_EXT = {".gbr", ".ger", ".gtl", ".gbl", ".gto", ".gbo", ".gts", ".gbs",
              ".gtp", ".gbp", ".gko", ".gm1", ".g1", ".g2", ".g3", ".g4", ".gml"}
TOKEN_RE = re.compile(r"%[^%]*%|[^*%]+\*")
OP_RE = re.compile(r"^(?:G0?([123]))?(?:X([+-]?\d+))?(?:Y([+-]?\d+))?"
                   r"(?:I([+-]?\d+))?(?:J([+-]?\d+))?(?:D0?([123]))?$")
ADD_RE = re.compile(r"ADD(\d+)([A-Za-z_.$][\w.$-]*)(?:,(.*))?")
SNAP = 1e-3  # 1 µm in mm: endpoint identity / diff tolerance


class Layer:
    """Flattened copper primitives of one Gerber file."""

    def __init__(self, path: str):
        self.path = path
        self.function = ""          # TF.FileFunction attribute, e.g. "Copper,L2,Inr"
        self.apertures: dict[int, tuple] = {}
        self.segments: list[tuple] = []   # (x1, y1, x2, y2, width, dark)
        self.flashes: list[tuple] = []    # (x, y, aperture, dark)
        self.regions: list[tuple] = []    # (points, dark)
        self.warnings: list[str] = []

    def bbox(self):
        xs, ys = [], []
        for x1, y1, x2, y2, w, _ in self.segments:
            xs += [x1, x2]; ys += [y1, y2]
        for x, y, _, _ in self.flashes:
            xs.append(x); ys.append(y)
        for pts, _ in self.regions:
            xs += [p[0] for p in pts]; ys += [p[1] for p in pts]
        if not xs:
            return (0.0, 0.0, 1.0, 1.0)
        return (min(xs), min(ys), max(xs), max(ys))


def parse_aperture(shape: str, params: str | None) -> tuple:
    vals = [float(v) for v in params.split("X")] if params else []
    if shape == "C":
        return ("C", vals[0])
    if shape in ("R", "O"):
        return (shape, vals[0], vals[1])
    if shape == "P":
        return ("C", vals[0])               # polygon ~ circumscribed circle
    if shape == "RoundRect" and len(vals) >= 9:   # KiCad 6+: radius, 4 corner centres
        xs, ys = vals[1:9:2], vals[2:9:2]
        r = vals[0]
        return ("R", max(xs) - min(xs) + 2 * r, max(ys) - min(ys) + 2 * r)
    size = 2 * max((abs(v) for v in vals), default=0.25)
    return ("C", size)                      # unknown macro: coarse disc


def parse(path: str, text: str | None = None) -> Layer:
    layer = Layer(path)
    if text is None:
        text = Path(path).read_text(errors="replace")
    int_digits, dec_digits = 4, 6
    scale = 1.0                              # inches -> mm when %MOIN%
    x = y = 0
    interp, quadrant, dcode = 1, "multi", 2
    aperture = None
    dark = True
    region: list | None = None
    contour: list = []

    def coord(raw):
        return int(raw) / 10 ** dec_digits * scale

    def close_contour():
        nonlocal contour
        if region is not None and len(contour) > 2:
            region.append(contour)
        contour = []

    for tok in TOKEN_RE.findall(text):
        tok = tok.strip()
        if tok.startswith("%"):
            body = tok.strip("%")
            for stmt in (s.strip() for s in body.split("*") if s.strip()):
                if stmt.startswith("FS"):
                    m = re.search(r"X(\d)(\d)", stmt)
                    if m:
                        int_digits, dec_digits = int(m.group(1)), int(m.group(2))
                    if "T" in stmt[2:4]:
                        layer.warnings.append("trailing-zero omission (FST) not supported")
                elif stmt == "MOIN":
                    scale = 25.4
                elif stmt == "LPC":
                    dark = False
                elif stmt == "LPD":
                    dark = True
                elif stmt.startswith("TF.FileFunction"):
                    layer.function = stmt.split(",", 1)[1] if "," in stmt else ""
                elif stmt.startswith("ADD"):
                    m = ADD_RE.match(stmt)
                    if m:
                        layer.apertures[int(m.group(1))] = parse_aperture(m.group(2), m.group(3))
            continue
        stmt = tok[:-1].strip()
        if stmt.startswith("G04 #@! TF.FileFunction,"):   # KiCad writes X2 attributes as comments
            layer.function = stmt.split(",", 1)[1]
        if not stmt or stmt.startswith("G04") or stmt.startswith("G4 "):
            continue
        if stmt in ("G36",):
            region, contour = [], []
            continue
        if stmt in ("G37",):
            close_contour()
            layer.regions += [(c, dark) for c in (region or [])]
            region = None
            continue
        if stmt in ("G74", "G75"):
            quadrant = "single" if stmt == "G74" else "multi"
            continue
        if stmt.startswith("M0"):
            break
        m = re.fullmatch(r"(?:G54)?D(\d+)", stmt)
        if m and int(m.group(1)) >= 10:
            aperture = layer.apertures.get(int(m.group(1)))
            continue
        m = OP_RE.match(stmt)
        if not m:
            continue
        g, xs, ys, is_, js, d = m.groups()
        if g:
            interp = int(g)
        if d:
            dcode = int(d)
        if not any((xs, ys, is_, js, d)):
            continue                         # bare G01/G02/G03 mode switch
        nx = coord(xs) if xs else x
        ny = coord(ys) if ys else y
        if dcode == 1:
            pts = [(x, y), (nx, ny)]
            if interp in (2, 3):
                pts = arc_points(x, y, nx, ny, coord(is_ or "0"), coord(js or "0"),
                                 interp == 2, quadrant)
            if region is not None:
                if not contour:
                    contour = [(x, y)]
                contour += pts[1:]
            else:
                width = aperture[1] if aperture else 0.0
                for (ax, ay), (bx, by) in zip(pts, pts[1:]):
                    layer.segments.append((ax, ay, bx, by, width, dark))
        elif dcode == 2:
            close_contour()
        elif dcode == 3 and aperture:
            layer.flashes.append((nx, ny, aperture, dark))
        x, y = nx, ny
    return layer


def arc_points(x1, y1, x2, y2, i, j, clockwise, quadrant, step_deg=10):
    if quadrant == "single":   # signs of I/J unknown: pick the centre equidistant to both ends
        cands = [(x1 + si * abs(i), y1 + sj * abs(j)) for si in (1, -1) for sj in (1, -1)]
        cx, cy = min(cands, key=lambda c: abs(math.dist(c, (x1, y1)) - math.dist(c, (x2, y2))))
    else:
        cx, cy = x1 + i, y1 + j
    r = math.dist((cx, cy), (x1, y1))
    a1 = math.atan2(y1 - cy, x1 - cx)
    a2 = math.atan2(y2 - cy, x2 - cx)
    sweep = a2 - a1
    if clockwise and sweep >= 0:
        sweep -= 2 * math.pi
    if not clockwise and sweep <= 0:
        sweep += 2 * math.pi
    n = max(2, int(abs(math.degrees(sweep)) / step_deg))
    pts = [(cx + r * math.cos(a1 + sweep * k / n), cy + r * math.sin(a1 + sweep * k / n))
           for k in range(n)]
    return pts + [(x2, y2)]


# --------------------------------------------------------------------------- render

def transform(layer: Layer, mirror: bool, rotate: int) -> Layer:
    def t(x, y):
        if mirror:
            x = -x
        for _ in range((rotate // 90) % 4):
            x, y = -y, x
        return x, y

    def ta(ap):   # rotating swaps rectangular aperture axes
        if ap[0] in ("R", "O") and (rotate // 90) % 2:
            return (ap[0], ap[2], ap[1])
        return ap

    out = Layer(layer.path)
    out.function = layer.function
    for x1, y1, x2, y2, w, dk in layer.segments:
        out.segments.append((*t(x1, y1), *t(x2, y2), w, dk))
    for x, y, ap, dk in layer.flashes:
        out.flashes.append((*t(x, y), ta(ap), dk))
    for pts, dk in layer.regions:
        out.regions.append(([t(*p) for p in pts], dk))
    return out


def window_of(layer, window, mirror, rotate, margin=0.5):
    if window:
        x1, y1, x2, y2 = window
        probe = Layer("")
        probe.flashes = [(x1, y1, ("C", 0), True), (x2, y2, ("C", 0), True)]
        b = transform(probe, mirror, rotate).bbox()
    else:
        b = layer.bbox()
    return (b[0] - margin, b[1] - margin, b[2] + margin, b[3] + margin)


def rasterize(layer: Layer, win, ppmm: float):
    x0, y0, x1, y1 = win
    w = max(1, int((x1 - x0) * ppmm))
    h = max(1, int((y1 - y0) * ppmm))
    img = bytearray(w * h)

    def px(x):
        return (x - x0) * ppmm

    def py(y):
        return (y1 - y) * ppmm

    def capsule(ax, ay, bx, by, r, val):
        ax, ay, bx, by, r = px(ax), py(ay), px(bx), py(by), max(r * ppmm, 0.5)
        lo_x, hi_x = int(max(0, min(ax, bx) - r)), int(min(w - 1, max(ax, bx) + r))
        lo_y, hi_y = int(max(0, min(ay, by) - r)), int(min(h - 1, max(ay, by) + r))
        if lo_x > hi_x or lo_y > hi_y:
            return
        dx, dy = bx - ax, by - ay
        ll = dx * dx + dy * dy or 1e-12
        r2 = r * r
        for row in range(lo_y, hi_y + 1):
            cy = row + 0.5
            base = row * w
            for col in range(lo_x, hi_x + 1):
                cx = col + 0.5
                t = max(0.0, min(1.0, ((cx - ax) * dx + (cy - ay) * dy) / ll))
                ex, ey = cx - ax - t * dx, cy - ay - t * dy
                if ex * ex + ey * ey <= r2:
                    img[base + col] = val

    def polygon(pts, val):
        pp = [(px(x), py(y)) for x, y in pts]
        lo_y = int(max(0, min(p[1] for p in pp)))
        hi_y = int(min(h - 1, max(p[1] for p in pp)))
        edges = list(zip(pp, pp[1:] + pp[:1]))
        for row in range(lo_y, hi_y + 1):
            cy = row + 0.5
            xs = sorted(ax + (cy - ay) * (bx - ax) / (by - ay)
                        for (ax, ay), (bx, by) in edges
                        if (ay <= cy < by) or (by <= cy < ay))
            for a, b in zip(xs[::2], xs[1::2]):
                lo, hi = int(max(0, math.ceil(a - 0.5))), int(min(w - 1, math.floor(b - 0.5)))
                if lo <= hi:
                    img[row * w + lo: row * w + hi + 1] = bytes([val]) * (hi - lo + 1)

    def flash(x, y, ap, val):
        if ap[0] == "C":
            capsule(x, y, x, y, ap[1] / 2, val)
        elif ap[0] == "R":
            hw, hh = ap[1] / 2, ap[2] / 2
            polygon([(x - hw, y - hh), (x + hw, y - hh), (x + hw, y + hh), (x - hw, y + hh)], val)
        elif ap[0] == "O":
            r = min(ap[1], ap[2]) / 2
            if ap[1] >= ap[2]:
                capsule(x - ap[1] / 2 + r, y, x + ap[1] / 2 - r, y, r, val)
            else:
                capsule(x, y - ap[2] / 2 + r, x, y + ap[2] / 2 - r, r, val)

    # Gerber is order-dependent for clear polarity; regions/flashes/draws are
    # kept per kind here, so clear objects are painted last (KiCad pours only).
    for dk_pass in (True, False):
        val = 255 if dk_pass else 0
        for pts, dk in layer.regions:
            if dk == dk_pass:
                polygon(pts, val)
        for x, y, ap, dk in layer.flashes:
            if dk == dk_pass:
                flash(x, y, ap, val)
        for ax, ay, bx, by, sw, dk in layer.segments:
            if dk == dk_pass:
                capsule(ax, ay, bx, by, sw / 2, val)
    return w, h, img


def write_png(path, w, h, img):
    raw = b"".join(b"\x00" + bytes(img[r * w:(r + 1) * w]) for r in range(h))

    def chunk(kind, data):
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF))

    Path(path).write_bytes(b"\x89PNG\r\n\x1a\n"
                           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0))
                           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def write_svg(path, layer, win, highlight=()):
    x0, y0, x1, y1 = win
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {-y1} {x1 - x0} {y1 - y0}" '
           f'width="{(x1 - x0) * 10:.0f}mm" height="{(y1 - y0) * 10:.0f}mm">',
           f'<rect x="{x0}" y="{-y1}" width="{x1 - x0}" height="{y1 - y0}" fill="black"/>',
           '<g stroke-linecap="round" fill="#c87533" stroke="#c87533">']
    for pts, dk in layer.regions:
        d = "M" + " L".join(f"{x:.4f},{-y:.4f}" for x, y in pts) + " Z"
        out.append(f'<path d="{d}" stroke="none"{"" if dk else " fill=\"black\""}/>')
    for x, y, ap, dk in layer.flashes:
        fill = "" if dk else ' fill="black"'
        if ap[0] == "C":
            out.append(f'<circle cx="{x:.4f}" cy="{-y:.4f}" r="{ap[1] / 2}" stroke="none"{fill}/>')
        else:
            rx = min(ap[1], ap[2]) / 2 if ap[0] == "O" else 0
            out.append(f'<rect x="{x - ap[1] / 2:.4f}" y="{-y - ap[2] / 2:.4f}" width="{ap[1]}" '
                       f'height="{ap[2]}" rx="{rx}" stroke="none"{fill}/>')
    for x1_, y1_, x2_, y2_, sw, dk in layer.segments:
        out.append(f'<line x1="{x1_:.4f}" y1="{-y1_:.4f}" x2="{x2_:.4f}" y2="{-y2_:.4f}" '
                   f'stroke-width="{max(sw, 0.01)}"{"" if dk else " stroke=\"black\""}/>')
    out.append("</g>")
    for x1_, y1_, x2_, y2_, sw, _ in highlight:
        out.append(f'<line x1="{x1_:.4f}" y1="{-y1_:.4f}" x2="{x2_:.4f}" y2="{-y2_:.4f}" '
                   f'stroke="#ff2040" stroke-linecap="round" stroke-width="{max(sw, 0.05)}"/>')
    out.append("</svg>")
    Path(path).write_text("\n".join(out))


def render(layer, out, window=None, ppmm=None, mirror=False, rotate=0, highlight=()):
    t = transform(layer, mirror, rotate)
    win = window_of(layer, window, mirror, rotate)
    if str(out).lower().endswith(".svg"):
        hl = transform(Layer(""), mirror, rotate)
        hl.segments = list(highlight)
        write_svg(out, t, win, transform(hl, mirror, rotate).segments if highlight else ())
        return out
    if ppmm is None:   # fit the long side in ~2000 px
        ppmm = min(80.0, 2000 / max(win[2] - win[0], win[3] - win[1]))
    w, h, img = rasterize(t, win, ppmm)
    write_png(out, w, h, img)
    return out


# --------------------------------------------------------------------------- hunt / diff

def snap(v):
    return round(v / SNAP)


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)


def point_in_poly(x, y, pts):
    inside = False
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + pts[:1]):
        if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay):
            inside = not inside
    return inside


def cluster_segments(segs, gap):
    """Group segments whose bounding boxes lie within `gap` of each other (grid-hashed)."""
    dsu = DSU(len(segs))
    cell = max(gap, 0.5)
    grid: dict[tuple, list[int]] = {}
    for k, (x1, y1, x2, y2, w, _) in enumerate(segs):
        lx, ly = min(x1, x2) - w / 2 - gap, min(y1, y2) - w / 2 - gap
        hx, hy = max(x1, x2) + w / 2 + gap, max(y1, y2) + w / 2 + gap
        for gx in range(int(lx // cell), int(hx // cell) + 1):
            for gy in range(int(ly // cell), int(hy // cell) + 1):
                for other in grid.setdefault((gx, gy), []):
                    o = segs[other]
                    if not (max(o[0], o[2]) + o[4] / 2 < lx or min(o[0], o[2]) - o[4] / 2 > hx or
                            max(o[1], o[3]) + o[4] / 2 < ly or min(o[1], o[3]) - o[4] / 2 > hy):
                        dsu.union(k, other)
                grid[(gx, gy)].append(k)
    groups: dict[int, list] = {}
    for k in range(len(segs)):
        groups.setdefault(dsu.find(k), []).append(segs[k])
    return list(groups.values())


def describe(group):
    xs = [v for s in group for v in (s[0], s[2])]
    ys = [v for s in group for v in (s[1], s[3])]
    widths = sorted({round(s[4], 3) for s in group})
    lengths = sorted(math.dist(s[:2], s[2:4]) for s in group)
    bw, bh = max(xs) - min(xs), max(ys) - min(ys)
    hint = "vertical: try --rotate 90/270" if bh > 2.5 * bw else "horizontal"
    return {"n": len(group), "bbox": (min(xs), min(ys), max(xs), max(ys)),
            "size": (bw, bh), "widths": widths, "median_len": lengths[len(lengths) // 2],
            "hint": hint}


def hunt(layer: Layer, min_segments=8, gap=0.6):
    """Copper strokes whose connected component touches no flash (pad/via) and no pour.

    Real traces terminate on pads, vias or zones; text and artwork drawn in
    copper do not. Survivors are clustered spatially into candidate glyph runs.
    """
    segs = [s for s in layer.segments if s[5]]
    dsu = DSU(len(segs))
    ends: dict[tuple, int] = {}
    for k, (x1, y1, x2, y2, *_ ) in enumerate(segs):
        for p in ((snap(x1), snap(y1)), (snap(x2), snap(y2))):
            if p in ends:
                dsu.union(k, ends[p])
            else:
                ends[p] = k
    cell = 1.0
    fgrid: dict[tuple, list] = {}
    for x, y, ap, dk in layer.flashes:
        if dk:
            fgrid.setdefault((int(x // cell), int(y // cell)), []).append((x, y, ap))
    pours = [(pts, (min(p[0] for p in pts), min(p[1] for p in pts),
                    max(p[0] for p in pts), max(p[1] for p in pts)))
             for pts, dk in layer.regions if dk]

    def anchored(x, y):
        for gx in (int(x // cell) - 1, int(x // cell), int(x // cell) + 1):
            for gy in (int(y // cell) - 1, int(y // cell), int(y // cell) + 1):
                for fx, fy, ap in fgrid.get((gx, gy), ()):
                    half = ap[1] / 2 if ap[0] == "C" else max(ap[1], ap[2]) / 2
                    if abs(fx - x) <= half + SNAP and abs(fy - y) <= half + SNAP:
                        return True
        return any(b[0] <= x <= b[2] and b[1] <= y <= b[3] and point_in_poly(x, y, pts)
                   for pts, b in pours)

    tied = set()
    for k, (x1, y1, x2, y2, *_ ) in enumerate(segs):
        root = dsu.find(k)
        if root not in tied and (anchored(x1, y1) or anchored(x2, y2)):
            tied.add(root)
    loose = [s for k, s in enumerate(segs) if dsu.find(k) not in tied]
    found = [describe(g) for g in cluster_segments(loose, gap) if len(g) >= min_segments]
    return sorted(found, key=lambda c: -c["n"]), loose


def prim_keys(layer: Layer):
    keys = {}
    for s in layer.segments:
        a, b = (snap(s[0]), snap(s[1])), (snap(s[2]), snap(s[3]))
        keys[("S", min(a, b), max(a, b), round(s[4], 4), s[5])] = s
    for x, y, ap, dk in layer.flashes:
        keys[("F", snap(x), snap(y), tuple(round(v, 4) if isinstance(v, float) else v
                                           for v in ap), dk)] = (x, y, x, y, 0.2, dk)
    return keys


def diff(suspect: Layer, reference: Layer, gap=0.6, min_segments=1):
    """Primitives keyed by geometry + aperture definition (D-code numbers are per-file).

    A reference exported by another CAD version re-encodes zone fills (KiCad 5
    strokes them, KiCad 6 emits G36 regions) and pad outlines: expect REMOVED
    noise and small ADDED clusters; raise min_segments to keep drawn text only.
    """
    s, r = prim_keys(suspect), prim_keys(reference)
    added = [s[k] for k in s.keys() - r.keys()]
    removed = [r[k] for k in r.keys() - s.keys()]
    return ([describe(g) for g in cluster_segments(added, gap) if len(g) >= min_segments],
            [describe(g) for g in cluster_segments(removed, gap) if len(g) >= min_segments],
            added, removed)


# --------------------------------------------------------------------------- CLI

def gerber_files(items):
    out = []
    for item in items:
        p = Path(item)
        if p.is_dir():
            out += sorted(f for f in p.rglob("*") if f.suffix.lower() in GERBER_EXT
                          and "__MACOSX" not in f.parts)
        else:
            out.append(p)
    return out


def fmt_box(b):
    return f"x[{b[0]:.3f}, {b[2]:.3f}] y[{b[1]:.3f}, {b[3]:.3f}]"


def report_clusters(title, clusters, layer, png_dir, tag, bottom):
    print(f"  {title}: {len(clusters)} cluster(s)")
    for i, c in enumerate(clusters, 1):
        print(f"    #{i}: {c['n']} segs  {fmt_box(c['bbox'])}  "
              f"{c['size'][0]:.2f}x{c['size'][1]:.2f}  width {c['widths']}  {c['hint']}")
        if png_dir:
            Path(png_dir).mkdir(parents=True, exist_ok=True)
            # text running along Y can read either way: write both orientations
            rots = (90, 270) if c["size"][1] > 2.5 * c["size"][0] else (0,)
            for rot in rots:
                suffix = f"_r{rot}" if rot else ""
                out = Path(png_dir) / f"{Path(layer.path).stem}_{tag}{i}{suffix}.png"
                render(layer, out, window=c["bbox"], rotate=rot)
                print(f"        -> {out}")
            if bottom:
                print("        bottom layer: if glyphs read reversed, re-render with --mirror")


def is_bottom(layer):
    name = Path(layer.path).name.lower()
    return "bot" in layer.function.lower() or "b_cu" in name or name.endswith(".gbl")


def cmd_info(args):
    for f in gerber_files(args.paths):
        layer = parse(str(f))
        fn = layer.function or "?"
        inner = ",Inr" in fn or re.search(r"in\d+_cu|\.g\d$", f.name.lower())
        print(f"{f.name:34} {fn:24} draws={len(layer.segments):6} flashes={len(layer.flashes):5} "
              f"regions={len(layer.regions):4} apertures={len(layer.apertures):3} "
              f"{fmt_box(layer.bbox())}" + ("  <-- INNER: invisible on the finished board"
                                             if inner else ""))
        for w in layer.warnings:
            print(f"    warning: {w}")


def cmd_render(args):
    layer = parse(args.file)
    win = tuple(map(float, args.window.split(","))) if args.window else None
    out = render(layer, args.out, win, args.ppmm, args.mirror, args.rotate)
    print("saved", out)


def cmd_hunt(args):
    for f in gerber_files(args.paths):
        layer = parse(str(f))
        if "copper" not in layer.function.lower() and not re.search(
                r"_cu\.|\.g(tl|bl|\d)$", f.name.lower()):
            continue
        clusters, _ = hunt(layer, args.min_segments, args.gap)
        print(f"{f.name} ({layer.function or 'copper'})")
        report_clusters("unanchored stroke clusters", clusters, layer, args.png_dir,
                        "hunt", is_bottom(layer))


def cmd_diff(args):
    sus, ref = parse(args.suspect), parse(args.reference)
    added, removed, *_ = diff(sus, ref, args.gap, args.min_segments)
    print(f"{Path(args.suspect).name} vs {Path(args.reference).name}")
    report_clusters("ADDED in suspect", sorted(added, key=lambda c: -c["n"]), sus,
                    args.png_dir, "added", is_bottom(sus))
    report_clusters("REMOVED from reference", sorted(removed, key=lambda c: -c["n"]), ref,
                    None, "removed", False)


def selftest():
    ref = """%FSLAX46Y46*%%MOMM*%%LPD*%G01*%ADD10C,0.250000*%%ADD11C,0.800000*%
D11*X0Y0D03*X10000000Y0D03*D10*X0Y0D02*X10000000D01*M02*"""
    # same board + an isolated "L" stroke drawn with modal (X-only / Y-only) coordinates
    sus = ref.replace("M02*", "X2000000Y5000000D02*Y2000000D01*X4000000D01*M02*")
    r, s = parse("ref", ref), parse("sus", sus)
    assert len(r.segments) == 1 and r.segments[0][:4] == (0, 0, 10, 0), r.segments
    clusters, _ = hunt(s, min_segments=2)
    assert len(clusters) == 1 and clusters[0]["n"] == 2, clusters
    assert not hunt(r, min_segments=1)[0], "trace pad-to-pad must be anchored"
    added, removed, *_ = diff(s, r)
    assert len(added) == 1 and added[0]["n"] == 2 and not removed, (added, removed)
    with tempfile.TemporaryDirectory() as d:
        out = render(s, Path(d) / "t.png", ppmm=10)
        data = Path(out).read_bytes()
        assert data[:8] == b"\x89PNG\r\n\x1a\n"
        _, _, img = rasterize(s, window_of(s, None, False, 0), 10)
        assert sum(1 for v in img if v) > 100
        render(s, Path(d) / "t.svg")
    arc = parse("arc", "%FSLAX46Y46*%%MOMM*%%ADD10C,0.1*%D10*G75*X1000000Y0D02*"
                       "G03X-1000000Y0I-1000000J0D01*M02*")
    assert all(abs(math.hypot(a, b) - 1) < 1e-6 for a, b, *_ in arc.segments)
    assert max(sg[1] for sg in arc.segments) > 0.99, "ccw arc from +x to -x passes +y"
    print("selftest OK")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("info", help="layer inventory")
    p.add_argument("paths", nargs="+")
    p.set_defaults(func=cmd_info)
    p = sub.add_parser("render", help="render one layer to PNG or SVG")
    p.add_argument("file")
    p.add_argument("-o", "--out", required=True)
    p.add_argument("--window", help="X1,Y1,X2,Y2 in file units (board coords)")
    p.add_argument("--ppmm", type=float, help="pixels per mm (PNG); default fits ~2000 px")
    p.add_argument("--mirror", action="store_true", help="mirror X (read bottom layers)")
    p.add_argument("--rotate", type=int, default=0, choices=(0, 90, 180, 270))
    p.set_defaults(func=cmd_render)
    p = sub.add_parser("hunt", help="find copper strokes not tied to any pad/via/pour")
    p.add_argument("paths", nargs="+")
    p.add_argument("--min-segments", type=int, default=8)
    p.add_argument("--gap", type=float, default=0.6, help="cluster gap in mm")
    p.add_argument("--png-dir", help="write a zoomed PNG per cluster")
    p.set_defaults(func=cmd_hunt)
    p = sub.add_parser("diff", help="primitives added/removed vs a reference layer")
    p.add_argument("suspect")
    p.add_argument("reference")
    p.add_argument("--min-segments", type=int, default=8)
    p.add_argument("--gap", type=float, default=0.6)
    p.add_argument("--png-dir")
    p.set_defaults(func=cmd_diff)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
