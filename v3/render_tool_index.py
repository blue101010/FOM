#!/usr/bin/env python3
"""Render ``tools/tools.md`` from the tool sheets.

The index is a *view* of ``tools/CTFTTOU-*.md`` and nothing more:

| column  | source                                                 |
| ------- | ------------------------------------------------------ |
| id      | the sheet filename                                     |
| name    | the sheet H1, after the id and the dash                |
| url     | the first autolink in the sheet, ``—`` when it has none |
| used in | the ``Related techniques/counters`` line of the header |

Hand-maintaining it lets rows drift out of the corpus (rows going stale, whole ID ranges
never indexed at all). This renderer rebuilds the table in ID order; ``--check`` exits
non-zero when the file on disk differs, so the drift is visible instead of silent.

Usage:
    python3 v3/render_tool_index.py --check
    python3 v3/render_tool_index.py --write
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
INDEX = TOOLS / "tools.md"

HEADER = (
    "# CTFT Tools\n"
    "\n"
    "Reference tools used across CTFT techniques and counter-techniques.\n"
    "\n"
    "| Tool ID | Name | URL | Used in |\n"
    "| --- | --- | --- | --- |\n"
)

SHEET_GLOB = "CTFTTOU-*.md"
H1_RE = re.compile(r"^#\s+(CTFTTOU-\d+)\s*[—–-]\s*(.+?)\s*$", re.M)
RELATED_RE = re.compile(
    r"^>?\s*\*\*Related techniques/counters:?\*\*\s*(.+?)\s*$", re.M
)
URL_RE = re.compile(r"<(https?://[^>\s]+)>")
ENTRY_ID_RE = re.compile(r"CTFT(?:TE|CTE)-[A-Z]{3}-\d{3}")
TOOL_ID_RE = re.compile(r"CTFTTOU-\d{3}")
EMPTY = "—"


def sheet_number(path: Path) -> int:
    match = re.search(r"CTFTTOU-(\d+)", path.stem)
    return int(match.group(1)) if match else 10**6


def sheet_name(text: str, fallback: str) -> str:
    match = H1_RE.search(text)
    if match:
        return match.group(2).strip()
    return fallback


def sheet_url(text: str) -> str:
    match = URL_RE.search(text)
    return match.group(1) if match else EMPTY


def corpus_references() -> dict[str, list[str]]:
    """tool id -> entry ids that cite it, built in one pass over the corpus."""
    references: dict[str, list[str]] = {}
    for folder, prefix in (("techniques", "CTFTTE"), ("countertechniques", "CTFTCTE")):
        for path in sorted((ROOT / folder).glob(f"{prefix}-*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            for tool_id in dict.fromkeys(TOOL_ID_RE.findall(text)):
                references.setdefault(tool_id, []).append(path.stem)
    return references


def sheet_uses(text: str, tool_id: str, references: dict[str, list[str]]) -> str:
    """Entry ids that cite the tool: the sheet header first, then the corpus.

    The header is hand-typed and drifts behind the corpus, so the two sources are unioned;
    the corpus pass makes a newly linked technique appear without anyone editing the sheet.
    """
    match = RELATED_RE.search(text)
    declared = ENTRY_ID_RE.findall(match.group(1)) if match else []
    ids = list(dict.fromkeys(declared))
    for entry in references.get(tool_id, []):
        if entry not in ids:
            ids.append(entry)
    return ", ".join(ids) if ids else EMPTY


def cell(value: str) -> str:
    return value.replace("|", r"\|")


def build_index() -> str:
    references = corpus_references()
    rows: list[str] = []
    for path in sorted(TOOLS.glob(SHEET_GLOB), key=sheet_number):
        text = path.read_text(encoding="utf-8", errors="replace")
        tool_id = path.stem
        url = sheet_url(text)
        url_cell = f"<{url}>" if url != EMPTY else EMPTY
        rows.append(
            f"| [{tool_id}]({path.name}) "
            f"| {cell(sheet_name(text, tool_id))} "
            f"| {cell(url_cell)} "
            f"| {cell(sheet_uses(text, tool_id, references))} |"
        )
    return HEADER + "\n".join(rows) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="rewrite tools/tools.md")
    mode.add_argument("--check", action="store_true", help="fail when the index is stale")
    parser.add_argument("--show", type=int, default=0, help="print the first N differing lines")
    args = parser.parse_args(argv)

    rendered = build_index()
    current = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""

    if args.write:
        if rendered == current:
            print("tools/tools.md already up to date")
            return 0
        INDEX.write_text(rendered, encoding="utf-8")
        rows = rendered.count("\n| [CTFTTOU-")
        print(f"wrote tools/tools.md: {rows} rows")
        return 0

    if rendered == current:
        print(f"tools/tools.md up to date: {rendered.count(chr(10) + '| [CTFTTOU-')} rows")
        return 0

    import difflib

    diff = list(
        difflib.unified_diff(
            current.splitlines(),
            rendered.splitlines(),
            fromfile="tools/tools.md (on disk)",
            tofile="tools/tools.md (rendered)",
            lineterm="",
            n=0,
        )
    )
    shown = diff if args.show <= 0 else diff[: args.show]
    print("\n".join(shown))
    print(f"\ntools/tools.md is stale: {sum(1 for l in diff if l.startswith(('+', '-'))) - 2} differing lines")
    return 1


if __name__ == "__main__":
    sys.exit(main())
