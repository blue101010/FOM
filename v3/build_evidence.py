#!/usr/bin/env python3
"""Harvest the write-up links that already exist in the corpus into v3/evidence.json.

This script only *moves* facts that are already in the repository into a typed
form. It never invents a challenge, a CTF name or a URL: every field is either
read from a markdown file or parsed out of the URL path itself. Entries it
produces are `status: "seeded"` — links exist, curation has not happened.

An entry reaches `attested` only through the promotion criteria in SCHEMA_V3
(§Curation), which require a human to write positives, negatives and boundaries.

    python v3/build_evidence.py            # report
    python v3/build_evidence.py --write    # write v3/evidence.json
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "v3"

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>")
WRITEUPS_RE = re.compile(r"\*\*Writeups\*\*\n+(.*?)(?:\n\*\*|\n## |\Z)", re.S)
SOURCES_RE = re.compile(r"\*\*Sources\*\*\n+(.*?)(?:\n\*\*|\n## |\Z)", re.S)
# https://github.com/<owner>/writeups/blob/main/<year>/<CTF>/<challenge>/...
WRITEUP_PATH_RE = re.compile(
    r"github\.com/[^/]+/writeups/blob/[^/]+/(\d{4})/([^/]+)/([^/]+)/"
)


def links(chunk: str) -> list[tuple[str, str]]:
    found = []
    for match in LINK_RE.finditer(chunk):
        url = match.group(2) or match.group(3)
        if url:
            found.append((match.group(1) or "", url.rstrip(").,")))
    return found


def challenge_from(url: str, label: str, origin: str) -> dict[str, Any]:
    """Fields parsed out of the URL itself — never guessed."""
    entry: dict[str, Any] = {
        "ctf": None, "challenge": None, "year": None,
        "writeup": url, "extracted_from": origin,
    }
    if match := WRITEUP_PATH_RE.search(url):
        year, ctf, challenge = match.groups()
        entry |= {"ctf": ctf, "challenge": challenge, "year": int(year)}
    elif label:
        entry["challenge"] = label.strip()
    return entry


def harvest() -> list[dict[str, Any]]:
    index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    records = []
    for item in index["techniques"]:
        key = item["technique"]["id"].removeprefix("CTFTTE-")
        challenges: list[dict[str, Any]] = []
        references: list[dict[str, str]] = []
        seen: set[str] = set()

        for path_key in ("technique", "counter"):
            path = ROOT / item[path_key]["path"]
            text = path.read_text(encoding="utf-8", errors="replace")
            origin = item[path_key]["path"]
            for chunk in WRITEUPS_RE.findall(text):
                for label, url in links(chunk):
                    if url not in seen:
                        seen.add(url)
                        challenges.append(challenge_from(url, label, origin))
            for chunk in SOURCES_RE.findall(text):
                for label, url in links(chunk):
                    if url not in seen:
                        seen.add(url)
                        references.append({"label": label.strip() or url, "url": url})

        if not challenges and not references:
            continue

        events = {c["ctf"] for c in challenges if c["ctf"]}
        records.append({
            "id": f"EVID-{key}",
            "schema_version": "3.0",
            "technique": item["technique"]["id"],
            "challenges": challenges,
            "references": references,
            "positives": [],
            "negatives": [],
            "boundaries": [],
            "synonyms": [],
            "external_mappings": [],
            "curator": None,
            "reviewed_on": None,
            "status": "seeded",
            "_independent_events": len(events),
        })
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write v3/evidence.json")
    args = parser.parse_args()

    records = harvest()
    independent = [r for r in records if r.pop("_independent_events", 0) >= 2]
    for record in records:
        record.pop("_independent_events", None)

    payload = {
        "model": "CTFT",
        "schema_version": "3.0",
        "collection": "evidence",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "note": "Auto-seeded from links already present in the corpus. No entry is "
                "attested until a curator supplies positives, negatives and boundaries.",
        "items": records,
    }
    if args.write:
        (V3 / "evidence.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
        )
    verb = "wrote" if args.write else "would write"
    hosts = {urlparse(c["writeup"]).netloc
             for r in records for c in r["challenges"]}
    print(f"{verb} v3/evidence.json: {len(records)} seeded records, "
          f"{sum(len(r['challenges']) for r in records)} write-up links, "
          f"{len(hosts)} distinct hosts")
    print(f"records already citing >=2 independent CTF events: {len(independent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
