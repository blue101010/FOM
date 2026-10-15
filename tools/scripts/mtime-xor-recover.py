#!/usr/bin/env python3
"""Recover a repeating-key XOR whose key is the file's write timestamp.

Companion tool for CTFTTE-CRY-014 / CTFTCTE-CRY-014 (timestamp-keyed XOR). The
ciphertext file is hex text; the key is the decimal string of the epoch
seconds at which the writer last touched the file — recoverable from the
file's own mtime.

Usage:
  mtime-xor-recover.py --file flag.txt                # key from st_mtime
  mtime-xor-recover.py --file flag.txt --window 120   # sweep ±120 s
  mtime-xor-recover.py --file flag.txt --mtime "2025-10-17 09:52:24.884370256 +0000"
  mtime-xor-recover.py --file ct.txt --key-str 1760704344   # fixed key

Scoring: candidates are ranked by printable-ASCII ratio; matches containing a
flag-like token (word{...} or word-...) are reported first.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys

FLAG_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]{1,}[-{][!-~]{4,}")


def xor(data: bytes, key: bytes) -> bytes:
    if not key:
        return data
    rep = (len(data) + len(key) - 1) // len(key)
    return bytes(a ^ b for a, b in zip(data, key * rep))


def score(data: bytes) -> tuple[float, bool]:
    if not data:
        return 0.0, False
    printable = sum(1 for b in data if 32 <= b < 127 or b in (9, 10, 13))
    flag_hit = bool(FLAG_RE.search(data.decode("latin-1")))
    return printable / len(data), flag_hit


def candidates(base_epoch: int | None, window: int, key_str: str | None):
    if key_str:
        yield f"fixed:{key_str}", key_str.encode()
        return
    if base_epoch is None:
        return
    if window == 0:
        yield f"epoch:{base_epoch}", str(base_epoch).encode()
        return
    for off in range(-window, window + 1):
        epoch = base_epoch + off
        yield f"epoch±{off:+d}:{epoch}", str(epoch).encode()


def main() -> int:
    _doc_lines = (__doc__ or "").strip().splitlines()
    ap = argparse.ArgumentParser(description=_doc_lines[0] if _doc_lines else None)
    ap.add_argument("--file", help="ciphertext file (hex text or raw bytes)")
    ap.add_argument("--data", help="inline hex ciphertext (alternative to --file)")
    ap.add_argument("--mtime", help="override write time, any parseable format")
    ap.add_argument("--window", type=int, default=0,
                    help="brute-force ±N seconds around the mtime (default: 0)")
    ap.add_argument("--key-str", help="use this exact key string, skip time derivation")
    ap.add_argument("--top", type=int, default=10, help="show top N candidates")
    args = ap.parse_args()

    if args.file:
        raw = open(args.file, "rb").read()
    elif args.data:
        raw = args.data.encode()
    else:
        ap.error("provide --file or --data")

    text = raw.decode("latin-1").strip()
    try:
        ct = bytes.fromhex("".join(text.split()))
    except ValueError:
        ct = raw
        print("note: content is not clean hex; using raw bytes", file=sys.stderr)

    if args.mtime:
        base = None
        if re.fullmatch(r"\d+", args.mtime.strip()):
            base = int(args.mtime.strip())  # already an epoch value
        else:
            try:
                base = int(dt.datetime.fromisoformat(args.mtime).timestamp())
            except ValueError:
                import dateutil.parser  # type: ignore
                base = int(dateutil.parser.parse(args.mtime).timestamp())
        base_epoch = base
    elif args.file:
        base_epoch = int(os.stat(args.file).st_mtime)
    else:
        base_epoch = None

    results = []
    for label, key in candidates(base_epoch, args.window, args.key_str):
        plain = xor(ct, key)
        ratio, flag_hit = score(plain)
        results.append((flag_hit, ratio, label, plain))

    results.sort(key=lambda r: (r[0], r[1]), reverse=True)
    if not results:
        print("no key candidates: pass --mtime, --window or --key-str", file=sys.stderr)
        return 1

    shown = 0
    for flag_hit, ratio, label, plain in results:
        if shown >= args.top or (not flag_hit and ratio < 0.85):
            continue
        tag = "FLAG-LIKE" if flag_hit else f"printable {ratio:.0%}"
        print(f"[{tag}] key {label}")
        print(f"  {plain.decode('latin-1', errors='replace')}")
        shown += 1
    if shown == 0:
        print(f"no candidate above threshold; best printable ratio was "
              f"{results[0][1]:.0%} (key {results[0][2]})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
