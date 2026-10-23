#!/usr/bin/env python3
"""Plot Gerber layers with matplotlib: quick look at every copper/silk layer.

Companion tool for CTFTTE-HWR-003 / CTFTCTE-HWR-003 (PCB fabrication-layer
concealment). Generalised from the CTFBase "Critical Flight" write-up script
(local solve: 2026/HB/TRY/Critical_Flight/solve_visualize.py): regex-parse
X<n>Y<n>D0<n> operations, draw D01 strokes as lines and D03 flashes as dots,
one PNG per layer.

Requires matplotlib (Kali: `sudo apt install python3-matplotlib`, or the
~/.venvs/ctfml venv).

Usage:
  gerber-matplotlib-plot.py DIR_OR_FILES...                  # one PNG per layer
  gerber-matplotlib-plot.py In1_Cu.gbr --window X1,Y1,X2,Y2  # zoom (file units)
  gerber-matplotlib-plot.py ... --out-dir plots/ --dpi 300

Window coordinates are in file units: mm for KiCad, so pass them as mm. The
raw integers are scaled from the %FS format (4.6 -> /1e6).

Limits (by design, it is the baseline): lines that omit X or Y (modal
coordinates) are skipped, aperture widths, arcs, regions (G36/G37) and clear
polarity are ignored. Use gerber-layer-inspect.py (CTFTTOU-310) for faithful
rendering, reference-free hunting and diffing.
"""
import argparse
import re
import sys
from pathlib import Path

GERBER_EXT = {".gbr", ".ger", ".gtl", ".gbl", ".gto", ".gbo", ".gts", ".gbs",
              ".gtp", ".gbp", ".gko", ".gm1", ".g1", ".g2", ".g3", ".g4"}
OP_RE = re.compile(r'X(-?\d+)Y(-?\d+)D0?(\d)\*')


def parse_gerber(filepath):
    """Extract (x1, y1, x2, y2, action) in file units from a Gerber file."""
    content = Path(filepath).read_text(errors="replace")
    fs = re.search(r'%FS[LT][AI]X(\d)(\d)Y\d\d\*%', content)
    div = 10 ** int(fs.group(2)) if fs else 10 ** 6
    coordinates = []
    current_x, current_y = 0.0, 0.0
    for match in OP_RE.finditer(content):
        x, y = int(match.group(1)) / div, int(match.group(2)) / div
        d_code = int(match.group(3))
        if d_code == 1:
            coordinates.append((current_x, current_y, x, y, 'draw'))
        elif d_code == 3:
            coordinates.append((x, y, x, y, 'flash'))
        current_x, current_y = x, y
    return coordinates


def visualize_layer(filepath, out_dir, window=None, dpi=300):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 10))
    for x1, y1, x2, y2, action in parse_gerber(filepath):
        if action == 'draw':
            ax.plot([x1, x2], [y1, y2], 'w-', linewidth=0.8)
        else:
            ax.plot(x1, y1, 'w.', markersize=1.5)
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    ax.set_aspect('equal')
    if window:
        ax.set_xlim(window[0], window[2])
        ax.set_ylim(window[1], window[3])
    ax.axis('off')
    suffix = "_zoom" if window else ""
    out = Path(out_dir) / f"{Path(filepath).stem}{suffix}.png"
    plt.savefig(out, dpi=dpi, facecolor='black')
    plt.close(fig)
    print("saved", out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--window", help="X1,Y1,X2,Y2 zoom in file units (mm for KiCad)")
    ap.add_argument("--out-dir", default=".")
    ap.add_argument("--dpi", type=int, default=300)
    args = ap.parse_args()
    window = tuple(map(float, args.window.split(","))) if args.window else None
    files = []
    for item in map(Path, args.paths):
        if item.is_dir():
            files += sorted(f for f in item.rglob("*") if f.suffix.lower() in GERBER_EXT
                            and "__MACOSX" not in f.parts)
        else:
            files.append(item)
    if not files:
        sys.exit("no Gerber files found")
    Path(args.out_dir).mkdir(parents=True, exist_ok=True)
    for f in files:
        visualize_layer(f, args.out_dir, window, args.dpi)


if __name__ == "__main__":
    main()
