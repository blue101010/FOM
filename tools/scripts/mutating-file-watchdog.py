#!/usr/bin/env python3
"""Detect and hunt a read-triggered file mutator (guardian process).

Companion tool for CTFTTE-FOR-030 / CTFTCTE-FOR-030. A guardian daemon that
re-encrypts a file on every access betrays itself through repeated identical
reads producing different bytes (content often doubling in size). Naive triage
burns instance re-provisionings; this tool makes the detection a single command.

Usage:
  mutating-file-watchdog.py flag.txt                 # probe: read N times, diff
  mutating-file-watchdog.py flag.txt --reads 5 --hunt --snapshot .

Probe: reads the file --reads times, hashing each read; reports MUTATES or
STABLE and the size progression. Exit code 2 when the file mutates.

--hunt (Linux): lists processes holding the file or its directory open
(/proc/*/fd) and processes with inotify watches on it (/proc/*/fdinfo).
--snapshot: copies the current bytes to <file>.snapshot-<epoch> so decoding can
proceed off the watched path.

No network access, no writes outside --snapshot dir.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import time


def read_snapshot(path: str) -> tuple[bytes, str]:
    with open(path, "rb") as fh:
        data = fh.read()
    return data, hashlib.sha256(data).hexdigest()[:16]


def hunt(path: str) -> list[str]:
    """Best-effort guardian hunt via /proc. Returns human-readable findings."""
    findings: list[str] = []
    if not os.path.isdir("/proc"):
        findings.append("hunt unsupported on this platform (no /proc); use ps and lsof manually")
        return findings
    real = os.path.realpath(path)
    parent_dir = os.path.dirname(real) + os.sep
    procs = filter(str.isdigit, os.listdir("/proc"))
    for pid in procs:
        cmdline = ""
        try:
            with open(f"/proc/{pid}/cmdline", "rb") as fh:
                cmdline = fh.read().replace(b"\x00", b" ").decode(errors="replace").strip()
        except OSError:
            continue
        try:
            fds = os.listdir(f"/proc/{pid}/fd")
        except OSError:
            continue
        for fd in fds:
            try:
                target = os.readlink(f"/proc/{pid}/fd/{fd}")
            except OSError:
                continue
            if target == real or target.startswith(parent_dir):
                findings.append(f"pid {pid}: open fd {fd} -> {target} :: {cmdline}")
            if "inotify" in fd:
                findings.append(f"pid {pid}: inotify watch fd {fd} :: {cmdline}")
    return sorted(set(findings)) or ["no process holds the file or watches its directory"]


def main() -> int:
    _doc_lines = (__doc__ or "").strip().splitlines()
    ap = argparse.ArgumentParser(description=_doc_lines[0] if _doc_lines else None)
    ap.add_argument("file", help="file to probe (e.g. flag.txt)")
    ap.add_argument("--reads", type=int, default=3, help="number of probe reads (default: 3)")
    ap.add_argument("--interval", type=float, default=0.3,
                    help="seconds between reads (default: 0.3)")
    ap.add_argument("--hunt", action="store_true", help="list processes holding/watching the file")
    ap.add_argument("--snapshot", metavar="DIR", help="copy current bytes into DIR")
    args = ap.parse_args()

    reads: list[tuple[bytes, str]] = []
    for i in range(max(2, args.reads)):
        try:
            reads.append(read_snapshot(args.file))
        except OSError as exc:
            print(f"read {i} failed: {exc}", file=sys.stderr)
            return 1
        print(f"read {i + 1}: {len(reads[-1][0])} bytes, sha256:{reads[-1][1]}")
        if i < args.reads - 1:
            time.sleep(args.interval)

    hashes = {h for _, h in reads}
    sizes = [len(d) for d, _ in reads]
    if len(hashes) > 1:
        print("verdict: MUTATES on read (guardian process suspected)")
        verdict = 2
    else:
        print("verdict: STABLE across reads")
        verdict = 0
    print(f"size progression: {sizes}")

    if args.hunt:
        print("\nguardian hunt:")
        for line in hunt(args.file):
            print(f"  {line}")

    if args.snapshot:
        dest = os.path.join(args.snapshot,
                            f"{os.path.basename(args.file)}.snapshot-{int(time.time())}")
        shutil.copyfile(args.file, dest)
        print(f"\nsnapshot written: {dest}")
    return verdict


if __name__ == "__main__":
    sys.exit(main())
