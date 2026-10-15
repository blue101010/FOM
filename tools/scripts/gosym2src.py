#!/usr/bin/env python3
"""Pivot from Go/Rust binary symbols to public source repositories.

Companion tool for CTFTTE-REV-010 / CTFTCTE-REV-010 (retained build-path
symbol-to-source anchor). Go binaries keep full package paths in their symbol
table; a single strings pass turns a RE challenge into a repo lookup and a
branch diff.

Usage:
  gosym2src.py guntar                       # list embedded repo/package paths
  gosym2src.py guntar --verbose             # show every match, not just repos
  gosym2src.py guntar --diff ./guntar-src   # local clone: find + diff a
                                            # challenge-looking branch

Extraction only reads the binary. --diff runs git locally against the clone
you already have; it never clones or fetches anything.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

PATH_RE = re.compile(
    rb"(?<![\w.\-/])((?:github|gitlab|bitbucket|gitee|codeberg|sr\.ht)"
    rb"\.com/[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)*)"
)
BRANCH_RE = re.compile(r"ctf|challenge|flag|hack|pwn", re.I)


def extract(data: bytes) -> dict[str, set[str]]:
    repos: dict[str, set[str]] = defaultdict(set)
    for match in PATH_RE.finditer(data):
        parts = match.group(1).decode("latin-1").rstrip("/.").split("/")
        repo = "/".join(parts[:3])
        repos[repo].add("/".join(parts[3:]) if len(parts) > 3 else "(repo root)")
    return repos


def git(repo: str, *args: str) -> str:
    proc = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "git failed")
    return proc.stdout


def diff_challenge_branch(repo: str) -> int:
    try:
        head = git(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()
        branches = [b.strip() for b in git(repo, "branch", "-a").splitlines() if b.strip()]
    except (RuntimeError, FileNotFoundError) as exc:
        print(f"cannot inspect {repo}: {exc}", file=sys.stderr)
        return 1
    hits = [b for b in branches if BRANCH_RE.search(b) and "HEAD" not in b]
    print(f"HEAD: {head}")
    if not hits:
        print("no challenge-looking branch found; all branches:")
        for b in branches:
            print(f"  {b}")
        return 0
    for hit in hits:
        print(f"\n=== candidate branch: {hit} ===")
        print(git(repo, "diff", "--stat", head, hit))
        print(git(repo, "diff", head, hit))
    return 0


def main() -> int:
    _doc_lines = (__doc__ or "").strip().splitlines()
    ap = argparse.ArgumentParser(description=_doc_lines[0] if _doc_lines else None)
    ap.add_argument("binary", help="path to the binary to scan")
    ap.add_argument("--verbose", action="store_true", help="list every package path")
    ap.add_argument("--diff", metavar="REPO", help="local clone: diff challenge-like branches")
    args = ap.parse_args()

    try:
        data = Path(args.binary).read_bytes()
    except OSError as exc:
        print(f"cannot read {args.binary}: {exc}", file=sys.stderr)
        return 1

    repos = extract(data)
    if not repos:
        print("no code-host paths found; binary may be stripped or statically pure")
        return 1

    for repo, packages in sorted(repos.items()):
        print(f"{repo}  ->  https://{repo}")
        if args.verbose:
            for pkg in sorted(packages):
                print(f"    {pkg}")
    print("\nnext steps:")
    print("  1. clone the repo, list ALL branches (challenge code often sits off default)")
    print("  2. diff the challenge branch against default — the delta is the planted flaw")

    if args.diff:
        return diff_challenge_branch(args.diff)
    return 0


if __name__ == "__main__":
    sys.exit(main())
