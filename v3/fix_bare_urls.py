#!/usr/bin/env python3
"""Wrap bare URLs in angle brackets across the markdown corpus (markdownlint MD034).

Per AGENTS.md "Markdown cleanup": never leave a bare URL. This tool wraps any
`https?://` occurrence that is not already inside `<...>`, a `[label](...)`
link, or a Markdown link target, preserving trailing punctuation outside the
brackets. Idempotent.

Usage:
    python v3/fix_bare_urls.py            # dry run: list violations
    python v3/fix_bare_urls.py --write    # apply fixes
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

URL_RE = re.compile(r"(?<![(<])https?://[^\s<>()]+")
TRAILING = ".,;:!?"

TARGETS = [
    ROOT / "techniques",
    ROOT / "countertechniques",
    ROOT / "tactics",
    ROOT / "tools",
    ROOT / "to_categorize",
    ROOT / "v3",
]
ROOT_FILES = ["README.md", "TODO.md", "SCHEMA_V3.md", "AGENTS.md", "CLAUDE.md",
              "CORRELATION.md", "HIERARCHY.md"]


FENCE_RE = re.compile(r"^\s*(```|~~~)")


def fix_line(line: str) -> str:
    def repl(match: re.Match[str]) -> str:
        url = match.group(0)
        trailing = ""
        while url and url[-1] in TRAILING:
            trailing = url[-1] + trailing
            url = url[:-1]
        return f"<{url}>{trailing}"
    return URL_RE.sub(repl, line)


def fix_text(text: str) -> str:
    """Rewrite outside fenced code blocks only.

    MD034 does not apply inside a code fence, and angle brackets there would corrupt
    JSON and shell examples.
    """
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        out.append(line if in_fence else fix_line(line))
    return "\n".join(out)


def markdown_files() -> list[Path]:
    files = [ROOT / name for name in ROOT_FILES if (ROOT / name).exists()]
    for target in TARGETS:
        if target.exists():
            files.extend(sorted(target.rglob("*.md")))
    return [f for f in files if "backup" not in f.parts]


def scan(path: Path) -> list[tuple[int, str]]:
    hits, in_fence = [], False
    for lineno, line in enumerate(
        path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
    ):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and URL_RE.search(line):
            hits.append((lineno, line.strip()))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply fixes (default: dry run)")
    args = parser.parse_args()

    files = markdown_files()
    changed, total = [], 0
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        new = fix_text(text)
        if text.endswith("\n"):
            new += "\n"
        if new != text:
            hits = scan(path)
            total += len(hits)
            changed.append(path)
            if args.write:
                path.write_text(new, encoding="utf-8", newline="\n")
            else:
                first = hits[0] if hits else ("-", "")
                print(f"{len(hits):>3}  {path.relative_to(ROOT)}  e.g. L{first[0]}: {first[1][:80]}")

    mode = "Fixed" if args.write else "Would fix"
    print(f"{mode} {total} bare URL(s) across {len(changed)} file(s).")

    # Dry run is the CI gate: violations must fail the build. Without this the step
    # always exited 0 and could never catch anything.
    if not args.write and total:
        print("Run `python v3/fix_bare_urls.py --write` to fix them.")
        return 1

    if args.write:
        remaining = [(p, h) for p in files for h in [scan(p)] if h]
        print(f"Remaining violations: {sum(len(h) for _, h in remaining)}")
        for p, h in remaining:
            for lineno, line in h[:5]:
                print(f"  {p.relative_to(ROOT)}:{lineno}: {line[:80]}")
        if remaining:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
