#!/usr/bin/env python3
"""Render CORRELATION.md, HIERARCHY.md and the domain pages from the files on disk.

These are derived views: the technique and resolution-technique markdown files are
the source of truth, so a name can never drift between a page and the matrix.
Domain order follows CANONICAL_ORDER (the challenge-category picker), not the
alphabet.

    python v3/render_taxonomy_docs.py            # print a summary, write nothing
    python v3/render_taxonomy_docs.py --write    # rewrite every generated document
"""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TACTIC_RE = re.compile(r"^CTFT-TA-([A-Z]{3})\.md$")
TECHNIQUE_RE = re.compile(r"^CTFTTE-([A-Z]{3})-(\d{3})\.md$")
COUNTER_RE = re.compile(r"^CTFTCTE-([A-Z]{3})-(\d{3})\.md$")
HTB_RE = re.compile(r"\*\*HTB mapping:\*\*\s*(.+?)\s*$", re.M)

# Canonical domain order and short picker label. Adding a domain means adding it
# here first: an unlisted domain directory is a hard error.
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

# Retired domains, kept only so the matrix can explain where they went.
RETIRED = {
    "MSC": [
        ("MSC-001", "JAL-001", "Python jail (pyjail) confinement"),
        ("MSC-002", "JAL-002", "Restricted-shell confinement"),
        ("MSC-003", "COD-001", "Esolang / unusual-encoding puzzle"),
        ("MSC-004", "GAM-001", "Networked game / protocol automation"),
        ("MSC-005", "FPN-001", "Multi-stage chained challenge"),
    ],
}

# Curated pair-review notes: the resolution file does not answer the technique file
# it is paired with. Recorded here rather than silently renamed, because fixing
# them is an editorial decision on the entry content.
# Emptied in v3 phase 0.1 — the FOR-010..014 shift was corrected in the entries.
REVIEW_NOTES: dict[str, str] = {}

# Boilerplate shared by every generated domain page. States the v3 positioning:
# CTFT is an ontology of solving behaviour that *relates to* external catalogues,
# it is not defined by its distance from ATT&CK.
TACTIC_ATTACK_NOTE = """A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more."""

ATTACK_TABLE_RE = re.compile(r"## Related MITRE ATT.?&CK\n+(.*?)(?:\n## |\Z)", re.S)
ATTACK_ROW_RE = re.compile(r"^\|\s*(T\d{4}(?:\.\d{3})?)\s*\|([^|]*)\|([^|]*)\|", re.M)
DESCRIPTION_RE = re.compile(r"## Description\n+(.*?)\n+## ", re.S)


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
                "domain(s) missing from CANONICAL_ORDER: " + ", ".join(unlisted)
            )
        retired_present = sorted(set(self.tactics) & set(RETIRED))
        if retired_present:
            raise SystemExit(
                "retired domain(s) still present: " + ", ".join(retired_present)
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

    def fingerprint(self) -> str:
        """Content hash of the pair list. Changes only when the corpus changes, so a
        regeneration produces no diff and `--check` can gate CI."""
        payload = "\n".join(
            f"{key}|{title(self.techniques[key], f'CTFTTE-{key}')}"
            f"|{title(self.counters[key], f'CTFTCTE-{key}')}"
            for key in self.paired
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def unpaired(self) -> tuple[list[str], list[str]]:
        return (
            sorted(set(self.techniques) - set(self.counters)),
            sorted(set(self.counters) - set(self.techniques)),
        )


def render_correlation(corpus: Corpus) -> str:
    active = [code for code, _ in CANONICAL_ORDER]
    total = len(corpus.paired)
    digest = corpus.fingerprint()

    out: list[str] = [
        "# CTFT Correlation Matrix",
        "",
        "Every **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) and the",
        "**Resolution-Technique** (`CTFTCTE-<CAT>-NNN`) that recovers it, grouped by domain.",
        "IDs pair one-to-one: `CTFTTE-FOR-004` is always answered by `CTFTCTE-FOR-004`.",
        "",
        f"> Generated from the files in `techniques/` and `countertechniques/`"
        f" — corpus fingerprint `{digest}`",
        f"> by `v3/render_taxonomy_docs.py`. **{total} complete pairs** across"
        f" **{len(active)} active domains**. Do not hand-edit: rename the entry, then re-render.",
        "",
        "---",
        "",
        "## Domains at a glance",
        "",
        "Order follows the challenge-category picker.",
        "",
        "| # | Code | Picker label | Domain | Pairs |",
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
        "duplicated a precise domain; file those challenges under `JAL`, `COD`, `GAM`",
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
        meta = [f"[domain page](tactics/CTFT-TA-{code}.md)", f"{len(keys)} pairs"]
        if htb:
            meta.append(htb)
        out.append("> " + " · ".join(meta))
        out.append("")
        if not keys:
            out += ["_No entries yet._", "", ""]
            continue
        out += [
            "| # | Technique ID | Hide / Design name | Resolution-technique ID | Recovery action |",
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
            "⚠ **Subject mismatch** — the resolution-technique does not answer the"
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
            "**Placeholder resolution names** — titled `Counter — <technique name>`"
            " instead of naming the recovery action:",
            "",
            *(f"- `CTFTCTE-{key}`" for key in placeholder),
            "",
        ]
    if orphan_techniques or orphan_counters:
        out += ["**Unpaired entries** (break the one-to-one rule):", ""]
        out += [f"- `CTFTTE-{key}` has no resolution-technique" for key in orphan_techniques]
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
        "python v3/render_taxonomy_docs.py --write",
        "python v3/catalog_audit.py --write --write-index --write-catalog --check",
        "```",
        "",
        "See [README.md](README.md) for the model, and `HIERARCHY.md` (rendered"
        " locally by the same script) for the flat listing.",
        "",
    ]
    return "\n".join(out)


def attack_ids(path: Path) -> list[tuple[str, str, str]]:
    """Return [(attack_id, attack_name, relation_note)] from an entry's ATT&CK table."""
    match = ATTACK_TABLE_RE.search(path.read_text(encoding="utf-8", errors="replace"))
    if not match:
        return []
    return [
        (aid, name.strip(), note.strip())
        for aid, name, note in ATTACK_ROW_RE.findall(match.group(1))
    ]


def description(path: Path) -> str:
    """The hand-written Description section of a tactic page — the only editorial part."""
    match = DESCRIPTION_RE.search(path.read_text(encoding="utf-8", errors="replace"))
    return match.group(1).strip() if match else ""


def render_tactic_page(corpus: Corpus, code: str) -> str:
    """Regenerate one domain page, preserving only its hand-written Description."""
    path = corpus.tactics[code]
    keys = corpus.keys(code)
    htb = htb_mapping(path)
    out = [
        f"# {code} — {corpus.tactic_name(code)}",
        "",
        f"> **Domain ID:** `CTFT-TA-{code}`  ",
    ]
    if htb:
        out.append(f"> **HTB mapping:** {htb}  ")
    out += [
        f"> **Techniques:** {len(keys)}",
        "",
        "## Description",
        "",
        description(path) or "_No description yet._",
        "",
        "## Positioning and external anchors",
        "",
        TACTIC_ATTACK_NOTE,
        "",
        "## Techniques ↔ Resolution-techniques",
        "",
        "| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |",
        "| --- | --- | --- | --- | --- |",
    ]
    for key in keys:
        anchored = attack_ids(corpus.techniques[key])
        attack = ", ".join(aid for aid, _, _ in anchored) or "—"
        out.append(
            f"| [CTFTTE-{key}](../techniques/CTFTTE-{key}.md)"
            f" | {title(corpus.techniques[key], f'CTFTTE-{key}')}"
            f" | [CTFTCTE-{key}](../countertechniques/CTFTCTE-{key}.md)"
            f" | {title(corpus.counters[key], f'CTFTCTE-{key}')}"
            f" | {attack} |"
        )
    if not keys:
        out.append("| _none yet_ | | | | |")
    out += [
        "",
        "---",
        "*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*",
        "",
    ]
    return "\n".join(out)


def render_hierarchy(corpus: Corpus) -> str:
    active = [code for code, _ in CANONICAL_ORDER]
    total = len(corpus.paired)
    out = [
        "# CTFT Hierarchy",
        "",
        f"Design techniques: **{len(corpus.techniques)}**"
        f"  |  Resolution-techniques: **{len(corpus.counters)}**"
        f"  |  Complete pairs: **{total}**"
        f"  |  Active domains: **{len(active)}**",
        "",
        f"> Generated by `v3/render_taxonomy_docs.py`"
        f" — corpus fingerprint `{corpus.fingerprint()}`."
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
    parser = argparse.ArgumentParser(description="Render CORRELATION.md, HIERARCHY.md and the domain pages.")
    parser.add_argument("--write", action="store_true",
                        help="rewrite CORRELATION.md, HIERARCHY.md and tactics/*.md")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 if any generated document has drifted from the corpus")
    args = parser.parse_args()

    corpus = Corpus()
    documents = {
        ROOT / "CORRELATION.md": render_correlation(corpus),
        ROOT / "HIERARCHY.md": render_hierarchy(corpus),
    }
    documents.update({
        corpus.tactics[code]: render_tactic_page(corpus, code)
        for code in corpus.tactics
    })
    drifted: list[str] = []
    for path, text in documents.items():
        if args.write:
            path.write_text(text, encoding="utf-8", newline="\n")
        elif path.read_text(encoding="utf-8").replace("\r\n", "\n") != text:
            drifted.append(path.name)
        print(f"{'wrote' if args.write else 'would write'} {path.name}: {len(text)} chars")

    if args.check and drifted:
        print(f"DRIFT: {len(drifted)} document(s) differ from the corpus: "
              + ", ".join(sorted(drifted)))
        print("Run `python v3/render_taxonomy_docs.py --write`.")
        return 1

    orphan_techniques, orphan_counters = corpus.unpaired()
    print(f"tactics={len(corpus.tactics)} pairs={len(corpus.paired)} "
          f"unpaired_techniques={len(orphan_techniques)} "
          f"unpaired_counters={len(orphan_counters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
