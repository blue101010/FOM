#!/usr/bin/env python3
"""Render CORRELATION.md and HIERARCHY.md from the taxonomy files on disk.

Both documents are derived views: the technique and counter-technique markdown
files are the source of truth, so a name can never drift between a page and the
matrix. Category order follows CANONICAL_ORDER (the challenge-category picker),
not alphabetical order.

    python v2/render_taxonomy_docs.py            # print a summary, write nothing
    python v2/render_taxonomy_docs.py --write    # rewrite both documents
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TACTIC_RE = re.compile(r"^CTFT-TA-([A-Z]{3})\.md$")
TECHNIQUE_RE = re.compile(r"^CTFTTE-([A-Z]{3})-(\d{3})\.md$")
COUNTER_RE = re.compile(r"^CTFTCTE-([A-Z]{3})-(\d{3})\.md$")
HTB_RE = re.compile(r"\*\*HTB mapping:\*\*\s*(.+?)\s*$", re.M)

# Canonical category order and short picker label. Adding a tactic means adding
# it here first: an unlisted tactic directory is a hard error.
CANONICAL_ORDER: list[tuple[str, str]] = [
    ("FOR", "Forensics"),
    ("WEB", "Web"),
    ("CRY", "Crypto"),
    ("PWN", "Binary"),
    ("REV", "Reverse"),
    ("STE", "Stego"),
    ("OSI", "OSINT"),
    ("CLD", "Cloud"),
    ("BLK", "Blockchain"),
    ("AIM", "AI/ML"),
    ("ICS", "ICS/SCADA"),
    ("MOB", "Mobile"),
    ("JAL", "Jail escape"),
    ("GAM", "Game/Proto"),
    ("COD", "Coding"),
    ("NET", "Network"),
    ("FPN", "Full Pwn"),
    ("HWR", "Hardware"),
    ("SDR", "SDR / RF"),
]
# Declared but not offered in the picker and currently empty.
RESERVED: list[tuple[str, str]] = []

# Retired categories, kept only so the matrix can explain where they went.
RETIRED = {
    "MSC": [
        ("MSC-001", "JAL-001", "Python jail (pyjail) confinement"),
        ("MSC-002", "JAL-002", "Restricted-shell confinement"),
        ("MSC-003", "COD-001", "Esolang / unusual-encoding puzzle"),
        ("MSC-004", "GAM-001", "Networked game / protocol automation"),
        ("MSC-005", "FPN-001", "Multi-stage chained challenge"),
    ],
}

# Curated pair-review notes: the counter file does not answer the technique file
# it is paired with. Recorded here rather than silently renamed, because fixing
# them is an editorial decision on the entry content.
REVIEW_NOTES = {
    "FOR-010": "technique is the generic parent (visual machine-readable encoding); counter answers QR only",
    "FOR-011": "technique covers QR codes; counter answers rMQR codes",
    "FOR-012": "technique covers rMQR codes; counter answers JAB (colour) codes",
    "FOR-013": "technique is the generic parent (diagram encoding); counter answers Mengenlehreuhr only",
}


def title(path: Path, prefix: str) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return re.sub(rf"^{re.escape(prefix)}\s*[-–—]+\s*", "", line[2:]).strip()
    return path.stem


def htb_mapping(path: Path) -> str:
    match = HTB_RE.search(path.read_text(encoding="utf-8", errors="replace"))
    return match.group(1).strip() if match else ""


def entries(directory: Path, pattern: re.Pattern[str]) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in sorted(directory.glob("*.md")):
        if match := pattern.match(path.name):
            found[f"{match.group(1)}-{match.group(2)}"] = path
    return found


class Corpus:
    def __init__(self) -> None:
        self.tactics = {
            match.group(1): path
            for path in sorted((ROOT / "tactics").glob("*.md"))
            if (match := TACTIC_RE.match(path.name))
        }
        self.techniques = entries(ROOT / "techniques", TECHNIQUE_RE)
        self.counters = entries(ROOT / "countertechniques", COUNTER_RE)
        self.order = [code for code, _ in CANONICAL_ORDER + RESERVED]
        self.labels = dict(CANONICAL_ORDER + RESERVED)

        unlisted = sorted(set(self.tactics) - set(self.order))
        if unlisted:
            raise SystemExit(
                "tactic(s) missing from CANONICAL_ORDER: " + ", ".join(unlisted)
            )
        retired_present = sorted(set(self.tactics) & set(RETIRED))
        if retired_present:
            raise SystemExit(
                "retired tactic(s) still present: " + ", ".join(retired_present)
            )

    def keys(self, code: str) -> list[str]:
        return sorted(
            key for key in set(self.techniques) & set(self.counters)
            if key.startswith(f"{code}-")
        )

    @property
    def paired(self) -> list[str]:
        return sorted(set(self.techniques) & set(self.counters))

    def tactic_name(self, code: str) -> str:
        path = self.tactics.get(code)
        return title(path, code) if path else self.labels[code]

    def unpaired(self) -> tuple[list[str], list[str]]:
        return (
            sorted(set(self.techniques) - set(self.counters)),
            sorted(set(self.counters) - set(self.techniques)),
        )


def render_correlation(corpus: Corpus) -> str:
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    active = [code for code, _ in CANONICAL_ORDER]
    total = len(corpus.paired)

    out: list[str] = [
        "# CTFT Correlation Matrix",
        "",
        "Every **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) and the",
        "**Counter-Technique** (`CTFTCTE-<CAT>-NNN`) that recovers it, grouped by tactic.",
        "IDs pair one-to-one: `CTFTTE-FOR-004` is always answered by `CTFTCTE-FOR-004`.",
        "",
        f"> Generated from the files in `techniques/` and `countertechniques/` on {stamp}",
        f"> by `v2/render_taxonomy_docs.py`. **{total} complete pairs** across"
        f" **{len(active)} active tactics**. Do not hand-edit: rename the entry, then re-render.",
        "",
        "---",
        "",
        "## Tactics at a glance",
        "",
        "Order follows the challenge-category picker.",
        "",
        "| # | Code | Picker label | Tactic | Pairs |",
        "| --- | --- | --- | --- | --- |",
    ]
    for position, code in enumerate(active, start=1):
        count = len(corpus.keys(code))
        out.append(
            f"| {position} | [`{code}`](#ctft-ta-{code.lower()}) |"
            f" {corpus.labels[code]} | {corpus.tactic_name(code)} | {count} |"
        )
    out.append(f"| | | | **Total** | **{total}** |")
    out.append("")

    reserved_rows = [
        f"- `{code}` — {corpus.tactic_name(code)}"
        f" ({len(corpus.keys(code))} pairs, not offered in the picker)"
        for code, _ in RESERVED if code in corpus.tactics
    ]
    if reserved_rows:
        out += ["**Reserved / not yet populated**", "", *reserved_rows, ""]

    out += [
        "**Retired — do not use.** `MSC` (Misc) was a catch-all whose entries all",
        "duplicated a precise tactic; file those challenges under `JAL`, `COD`, `GAM`",
        "or `FPN` instead. See the [supersession map](#retired-categories) below.",
        "",
        "---",
        "",
    ]

    for code in active:
        keys = corpus.keys(code)
        anchor = f'<a id="ctft-ta-{code.lower()}"></a>'
        out.append(f"## {anchor}`CTFT-TA-{code}` — {corpus.tactic_name(code)}")
        out.append("")
        htb = htb_mapping(corpus.tactics[code]) if code in corpus.tactics else ""
        meta = [f"[tactic page](tactics/CTFT-TA-{code}.md)", f"{len(keys)} pairs"]
        if htb:
            meta.append(htb)
        out.append("> " + " · ".join(meta))
        out.append("")
        if not keys:
            out += ["_No entries yet._", "", ""]
            continue
        out += [
            "| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |",
            "| --- | --- | --- | --- | --- |",
        ]
        for position, key in enumerate(keys, start=1):
            technique = title(corpus.techniques[key], f"CTFTTE-{key}")
            counter = title(corpus.counters[key], f"CTFTCTE-{key}")
            flag = " ⚠" if key in REVIEW_NOTES else ""
            out.append(
                f"| {position} | [CTFTTE-{key}](techniques/CTFTTE-{key}.md) | {technique} |"
                f" [CTFTCTE-{key}](countertechniques/CTFTCTE-{key}.md) | {counter}{flag} |"
            )
        out.append("")
        out.append("")

    out += ["---", "", '<a id="retired-categories"></a>', "## Retired categories", ""]
    for code, rows in RETIRED.items():
        out += [
            f"### `CTFT-TA-{code}` — retired",
            "",
            f"Removed from the corpus; the originals are kept out-of-tree under"
            f" `backup/deprecated-{code.lower()}/`. Never reuse these IDs.",
            "",
            "Retired IDs are written bare (`MSC-001`) so that the integrity audit,",
            "which scans this file for `CTFTTE-*` / `CTFTCTE-*` pairs, does not read",
            "them back as live entries.",
            "",
            "| Retired pair | Superseded by | Name |",
            "| --- | --- | --- |",
        ]
        for old, new, name in rows:
            out.append(
                f"| `{old}` |"
                f" [`CTFTTE-{new}`](techniques/CTFTTE-{new}.md) /"
                f" [`CTFTCTE-{new}`](countertechniques/CTFTCTE-{new}.md) | {name} |"
            )
        out.append("")

    out += ["---", "", "## Pairs flagged for review", ""]
    orphan_techniques, orphan_counters = corpus.unpaired()
    placeholder = [
        key for key in corpus.paired
        if title(corpus.counters[key], f"CTFTCTE-{key}").lower().startswith(
            ("counter - ", "counter — ", "counter – ")
        )
    ]
    if REVIEW_NOTES:
        out += [
            "⚠ **Subject mismatch** — the counter-technique does not answer the"
            " technique it is paired with. Fixing this is an editorial change to the"
            " entry content, not to this matrix.",
            "",
            "| Pair | Issue |",
            "| --- | --- |",
        ]
        for key, note in sorted(REVIEW_NOTES.items()):
            out.append(f"| `CTFTTE-{key}` / `CTFTCTE-{key}` | {note} |")
        out.append("")
    if placeholder:
        out += [
            "**Placeholder counter names** — titled `Counter — <technique name>`"
            " instead of naming the recovery action:",
            "",
            *(f"- `CTFTCTE-{key}`" for key in placeholder),
            "",
        ]
    if orphan_techniques or orphan_counters:
        out += ["**Unpaired entries** (break the one-to-one rule):", ""]
        out += [f"- `CTFTTE-{key}` has no counter-technique" for key in orphan_techniques]
        out += [f"- `CTFTCTE-{key}` has no technique" for key in orphan_counters]
        out.append("")
    if not (REVIEW_NOTES or placeholder or orphan_techniques or orphan_counters):
        out += ["None.", ""]

    out += [
        "---",
        "",
        "## Adding an entry",
        "",
        "1. Pick a category from the table above — never `MSC`, never a new catch-all.",
        "2. Create `techniques/CTFTTE-<CAT>-NNN.md` **and**"
        " `countertechniques/CTFTCTE-<CAT>-NNN.md` with the same `NNN`.",
        "3. Add the row to `tactics/CTFT-TA-<CAT>.md`.",
        "4. Re-render and re-index:",
        "",
        "```bash",
        "python v2/render_taxonomy_docs.py --write",
        "python v2/catalog_audit.py --write --write-index --write-catalog --check",
        "```",
        "",
        "See [README.md](README.md) for the model, and `HIERARCHY.md` (rendered"
        " locally by the same script) for the flat listing.",
        "",
    ]
    return "\n".join(out)


def render_hierarchy(corpus: Corpus) -> str:
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    active = [code for code, _ in CANONICAL_ORDER]
    total = len(corpus.paired)
    out = [
        "# CTFT Hierarchy",
        "",
        f"Design techniques: **{len(corpus.techniques)}**"
        f"  |  Counter-techniques: **{len(corpus.counters)}**"
        f"  |  Complete pairs: **{total}**"
        f"  |  Active tactics: **{len(active)}**",
        "",
        f"> Generated on {stamp} by `v2/render_taxonomy_docs.py`."
        " See [CORRELATION.md](CORRELATION.md) for the linked matrix.",
        "",
    ]
    for code in active + [c for c, _ in RESERVED if c in corpus.tactics]:
        htb = htb_mapping(corpus.tactics[code]) if code in corpus.tactics else ""
        suffix = f"  _({htb})_" if htb else ""
        out.append(f"## CTFT-TA-{code} - {corpus.tactic_name(code)}{suffix}")
        out.append("")
        keys = corpus.keys(code)
        if not keys:
            out += ["_No entries yet._", ""]
            continue
        for key in keys:
            technique = title(corpus.techniques[key], f"CTFTTE-{key}")
            counter = title(corpus.counters[key], f"CTFTCTE-{key}")
            out.append(
                f"- **CTFTTE-{key}** {technique}  ->  **CTFTCTE-{key}** {counter}"
            )
        out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render CORRELATION.md and HIERARCHY.md.")
    parser.add_argument("--write", action="store_true",
                        help="rewrite CORRELATION.md and HIERARCHY.md")
    args = parser.parse_args()

    corpus = Corpus()
    documents = {
        ROOT / "CORRELATION.md": render_correlation(corpus),
        ROOT / "HIERARCHY.md": render_hierarchy(corpus),
    }
    for path, text in documents.items():
        if args.write:
            path.write_text(text, encoding="utf-8", newline="\n")
        print(f"{'wrote' if args.write else 'would write'} {path.name}: {len(text)} chars")

    orphan_techniques, orphan_counters = corpus.unpaired()
    print(f"tactics={len(corpus.tactics)} pairs={len(corpus.paired)} "
          f"unpaired_techniques={len(orphan_techniques)} "
          f"unpaired_counters={len(orphan_counters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
