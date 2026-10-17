#!/usr/bin/env python3
"""Decode USB HID boot-keyboard reports into typed text.

Companion tool for CTFTTE-HWR-001 / CTFTCTE-HWR-001 (USB HID keystroke
concealment). Standard library only — no pip install, safe on Kali (PEP 668).

Usage:
  usbhid-keystroke-decode.py reports.txt              # one 8-byte report per line
  usbhid-keystroke-decode.py --layout fr.txt reports.txt
  usbhid-keystroke-decode.py --selftest              # synthetic reports, no files

Input formats (auto-detected per line):
  - "00 00 04 00 00 00 00 00"   space-separated hex bytes
  - "0000040000000000"          continuous hex
  - tshark export of usb.capdata / usbhid.data fields

Report layout: [modifier][reserved][key1..key6]. Modifier bits 0x02/0x20 are
Left/Right Shift. Each key is emitted once per press (autorepeat duplicates are
suppressed); releases between identical keys produce repeated characters.

--layout FILE overrides the built-in US ANSI map: one line per usage
  "<usage> <normal> [<shifted>]"   e.g. "0x04 a A"  — usage in hex or decimal.
"""
from __future__ import annotations

import argparse
import sys

# US ANSI boot keyboard: usage id -> (normal, shifted)
US_ANSI = {
    0x04: ("a", "A"), 0x05: ("b", "B"), 0x06: ("c", "C"), 0x07: ("d", "D"),
    0x08: ("e", "E"), 0x09: ("f", "F"), 0x0A: ("g", "G"), 0x0B: ("h", "H"),
    0x0C: ("i", "I"), 0x0D: ("j", "J"), 0x0E: ("k", "K"), 0x0F: ("l", "L"),
    0x10: ("m", "M"), 0x11: ("n", "N"), 0x12: ("o", "O"), 0x13: ("p", "P"),
    0x14: ("q", "Q"), 0x15: ("r", "R"), 0x16: ("s", "S"), 0x17: ("t", "T"),
    0x18: ("u", "U"), 0x19: ("v", "V"), 0x1A: ("w", "W"), 0x1B: ("x", "X"),
    0x1C: ("y", "Y"), 0x1D: ("z", "Z"),
    0x1E: ("1", "!"), 0x1F: ("2", "@"), 0x20: ("3", "#"), 0x21: ("4", "$"),
    0x22: ("5", "%"), 0x23: ("6", "^"), 0x24: ("7", "&"), 0x25: ("8", "*"),
    0x26: ("9", "("), 0x27: ("0", ")"),
    0x28: ("[Enter]", "[Enter]"), 0x29: ("[Esc]", "[Esc]"),
    0x2A: ("[Backspace]", "[Backspace]"), 0x2B: ("[Tab]", "[Tab]"),
    0x2C: (" ", " "), 0x2D: ("-", "_"), 0x2E: ("=", "+"), 0x2F: ("[", "{"),
    0x30: ("]", "}"), 0x31: ("\\", "|"), 0x32: (";", ":"), 0x33: ("'", '"'),
    0x34: ("`", "~"), 0x35: (",", "<"), 0x36: (".", ">"), 0x37: ("/", "?"),
    0x38: ("[CapsLock]", "[CapsLock]"),
}

SHIFT_BITS = 0x02 | 0x20


def parse_report(line: str) -> list[int] | None:
    tokens = line.replace(",", " ").split()
    if not tokens:
        return None
    try:
        if len(tokens) > 1:
            return [int(t, 16) for t in tokens]
        blob = tokens[0]
        if len(blob) % 2 or not all(c in "0123456789abcdefABCDEF" for c in blob):
            return None
        return [int(blob[i:i + 2], 16) for i in range(0, len(blob), 2)]
    except ValueError:
        return None


def load_layout(path: str) -> dict[int, tuple[str, str]]:
    layout = dict(US_ANSI)
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            parts = raw.split("#")[0].split()
            if len(parts) < 2:
                continue
            usage = int(parts[0], 0)
            layout[usage] = (parts[1], parts[2] if len(parts) > 2 else parts[1])
    return layout


def decode(reports: list[list[int]], layout: dict[int, tuple[str, str]]) -> str:
    out: list[str] = []
    prev: set[int] = set()
    for report in reports:
        if len(report) < 2:
            continue
        shift = bool(report[0] & SHIFT_BITS)
        keys = {k for k in report[2:8] if k}
        for usage in sorted(keys - prev):
            normal, shifted = layout.get(usage, (f"[\\x{usage:02x}]",) * 2)
            out.append(shifted if shift else normal)
        prev = keys
    return "".join(out)


def _selftest() -> int:
    lines = [
        "00 00 00 00 00 00 00 00",   # idle
        "02 00 0b 00 00 00 00 00",   # Shift + h -> H
        "00 00 0c 00 00 00 00 00",   # i
        "00 00 1e 00 00 00 00 00",   # 1
        "00 00 00 00 00 00 00 00",   # release
        "00 00 1e 00 00 00 00 00",   # 1 again (repeat needs the release)
        "0000040000000000",          # continuous hex: a
        "00 00 2c 00 00 00 00 00",   # space
        "00 00 00 00 00 00 00 00",   # release
        "02 00 2f 00 00 00 00 00",   # Shift + [ -> {
    ]
    reports = [r for r in (parse_report(l) for l in lines) if r]
    text = decode(reports, US_ANSI)
    expected = "Hi11a {"
    print(f"decoded: {text!r}")
    ok = text == expected
    # custom layout: AZERTY-style swap a<->q
    fr = dict(US_ANSI)
    fr[0x04] = ("q", "Q")
    fr[0x14] = ("a", "A")
    fr_text = decode(reports, fr)
    print(f"custom layout: {fr_text!r}")
    ok = ok and fr_text == "Hi11q {"
    print("SELFTEST:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input", nargs="?", help="report dump file (omit with --selftest)")
    ap.add_argument("--layout", help="custom layout file: '<usage> <normal> [<shifted>]'")
    ap.add_argument("--selftest", action="store_true", help="run synthetic tests")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()
    if not args.input:
        ap.error("provide an input file or --selftest")

    layout = load_layout(args.layout) if args.layout else US_ANSI
    reports = []
    with open(args.input, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            report = parse_report(line.strip())
            if report:
                reports.append(report)
    print(decode(reports, layout))
    return 0


if __name__ == "__main__":
    sys.exit(main())
