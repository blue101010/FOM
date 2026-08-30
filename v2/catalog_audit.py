#!/usr/bin/env python3
"""Audit the local CTFT catalogue without fetching or executing any tool.

The manifest distinguishes the broad v1 taxonomy from the smaller, typed v2
slice. It deliberately reports discrepancies instead of repairing prose or
inventing execution semantics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "v2"
TACTIC_RE = re.compile(r"^CTFT-TA-([A-Z]{3})\.md$")
TECHNIQUE_RE = re.compile(r"^CTFTTE-([A-Z]{3})-(\d{3})\.md$")
COUNTER_RE = re.compile(r"^CTFTCTE-([A-Z]{3})-(\d{3})\.md$")
PAIR_RE = re.compile(
    r"CTFTTE-([A-Z]{3})-(\d{3}).*?CTFTCTE-([A-Z]{3})-(\d{3})"
)
PLACEHOLDER_RE = re.compile(r"add challenge write-up link|\b(?:todo|tbd)\b", re.I)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _entries(directory: Path, pattern: re.Pattern[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in sorted(directory.glob("*.md")):
        match = pattern.match(path.name)
        if match:
            result[f"{match.group(1)}-{match.group(2)}"] = path
    return result


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _v2_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in (
        "techniques.for.json",
        "playbooks.for.json",
        "indicators.json",
        "tools.json",
    ):
        data = _load_json(V2 / name)
        counts[name.removesuffix(".json")] = len(data.get("items", []))
    return counts


def _title(path: Path, prefix: str) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return re.sub(rf"^{re.escape(prefix)}\s*[--]+\s*", "", line[2:]).strip()
    return path.stem


def build_legacy_index() -> dict[str, Any]:
    """Build the compatible v1 index from the local taxonomy and paired files."""
    tactics = {
        match.group(1): path
        for path in sorted((ROOT / "tactics").glob("*.md"))
        if (match := TACTIC_RE.match(path.name))
    }
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    complete = sorted(set(techniques) & set(counters))
    by_tactic = Counter(key.split("-", 1)[0] for key in complete)
    entries = [
        {
            "tactic": f"CTFT-TA-{key.split('-', 1)[0]}",
            "category": key.split("-", 1)[0],
            "technique": {
                "id": f"CTFTTE-{key}",
                "name": _title(techniques[key], f"CTFTTE-{key}"),
                "path": techniques[key].relative_to(ROOT).as_posix(),
            },
            "counter": {
                "id": f"CTFTCTE-{key}",
                "name": _title(counters[key], f"CTFTCTE-{key}"),
                "path": counters[key].relative_to(ROOT).as_posix(),
            },
        }
        for key in complete
    ]
    return {
        "model": "CTFT",
        "version": "1.2",
        "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "complements": "MITRE ATT&CK",
        "tactics": [
            {
                "id": f"CTFT-TA-{code}",
                "name": _title(path, code),
                "path": path.relative_to(ROOT).as_posix(),
                "count": by_tactic.get(code, 0),
            }
            for code, path in sorted(tactics.items())
        ],
        "total_techniques": len(complete),
        "techniques": entries,
        "pairs": {
            item["technique"]["id"]: item["counter"]["id"] for item in entries
        },
        "by_technique_id": {
            item["technique"]["id"]: {
                "name": item["technique"]["name"],
                "counter_id": item["counter"]["id"],
                "counter_name": item["counter"]["name"],
                "tactic": item["tactic"],
                "path": item["technique"]["path"],
            }
            for item in entries
        },
        "by_counter_id": {
            item["counter"]["id"]: {
                "name": item["counter"]["name"],
                "technique_id": item["technique"]["id"],
                "technique_name": item["technique"]["name"],
                "tactic": item["tactic"],
                "path": item["counter"]["path"],
            }
            for item in entries
        },
    }


def build_v2_catalog() -> dict[str, Any]:
    """Build a safe, machine-readable catalogue for every paired v1 entry.

    Taxonomy-level entries are intentionally not promoted to executable
    playbooks. Their ``maturity`` records exactly what must be curated next.
    """
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    typed = {
        item.get("id", "")
        for item in _load_json(V2 / "playbooks.for.json").get("items", [])
    }
    items = []
    for key in sorted(set(techniques) & set(counters)):
        category = key.split("-", 1)[0]
        counter_id = f"CTFTCTE-{key}"
        is_typed = counter_id in typed
        items.append({
            "id": f"CTFTPAIR-{key}",
            "schema_version": "2.0",
            "tactic": f"CTFT-TA-{category}",
            "technique": {
                "id": f"CTFTTE-{key}",
                "name": _title(techniques[key], f"CTFTTE-{key}"),
                "path": techniques[key].relative_to(ROOT).as_posix(),
            },
            "counter_technique": {
                "id": counter_id,
                "name": _title(counters[key], counter_id),
                "path": counters[key].relative_to(ROOT).as_posix(),
            },
            "maturity": "typed" if is_typed else "taxonomy_only",
            "missing_for_typed_recommendation": [] if is_typed else [
                "indicators", "preconditions", "reviewed_tool_bindings",
                "evaluation_case",
            ],
        })
    return {
        "model": "CTFT",
        "schema_version": "2.0",
        "collection": "catalog",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_sha256": _sha256(ROOT / "CORRELATION.md"),
        "items": items,
    }


def build_curation_queue(catalog: dict[str, Any]) -> dict[str, Any]:
    """Return the typed-v2 curation backlog grouped by tactic."""
    pending = [item for item in catalog["items"] if item["maturity"] != "typed"]
    return {
        "model": "CTFT",
        "schema_version": "2.0",
        "collection": "curation_queue",
        "generated_at": catalog["generated_at"],
        "source_sha256": catalog["source_sha256"],
        "pending_count": len(pending),
        "by_tactic": {
            tactic: [
                {
                    "pair_id": item["id"],
                    "counter_technique": item["counter_technique"]["id"],
                    "missing": item["missing_for_typed_recommendation"],
                }
                for item in pending if item["tactic"] == tactic
            ]
            for tactic in sorted({item["tactic"] for item in pending})
        },
    }


def audit() -> dict[str, Any]:
    tactics = {
        match.group(1): path
        for path in sorted((ROOT / "tactics").glob("*.md"))
        if (match := TACTIC_RE.match(path.name))
    }
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    correlation_path = ROOT / "CORRELATION.md"
    correlation = correlation_path.read_text(encoding="utf-8")
    pairs = [match.groups() for match in PAIR_RE.finditer(correlation)]
    pair_ids = {(f"{left_cat}-{left_num}", f"{right_cat}-{right_num}")
                for left_cat, left_num, right_cat, right_num in pairs}
    matching_pairs = {(key, key) for key in set(techniques) & set(counters)}

    placeholder_paths = []
    for path in sorted([*techniques.values(), *counters.values()]):
        if PLACEHOLDER_RE.search(path.read_text(encoding="utf-8", errors="replace")):
            placeholder_paths.append(path.relative_to(ROOT).as_posix())

    legacy_index = _load_json(ROOT / "index.json")
    indexed_tactics = {item.get("id", "") for item in legacy_index.get("tactics", [])}
    indexed_pairs = {
        (item.get("technique", {}).get("id", "").removeprefix("CTFTTE-"),
         item.get("counter", {}).get("id", "").removeprefix("CTFTCTE-"))
        for item in legacy_index.get("techniques", [])
    }
    stix = _load_json(ROOT / "stix" / "ctft-bundle.json")
    objects = stix.get("objects", []) if isinstance(stix.get("objects", []), list) else []
    stix_types = Counter(obj.get("type", "unknown") for obj in objects if isinstance(obj, dict))

    return {
        "model": "CTFT",
        "schema_version": "2.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": {
            "correlation_sha256": _sha256(correlation_path),
            "legacy_index_sha256": _sha256(ROOT / "index.json"),
        },
        "taxonomy": {
            "tactics": sorted(tactics),
            "tactic_count": len(tactics),
            "technique_count": len(techniques),
            "counter_technique_count": len(counters),
            "complete_pairs": len(matching_pairs),
            "by_tactic": dict(sorted(Counter(key.split("-", 1)[0] for key in techniques).items())),
        },
        "coverage": {
            "typed_v2": _v2_counts(),
            "stix_object_types": dict(sorted(stix_types.items())),
            "placeholder_entries": placeholder_paths,
        },
        "integrity": {
            "techniques_without_counter": sorted(set(techniques) - set(counters)),
            "counters_without_technique": sorted(set(counters) - set(techniques)),
            "correlation_pair_count": len(pair_ids),
            "correlation_pairs_missing_from_files": sorted(
                f"{left}->{right}" for left, right in pair_ids
                if left not in techniques or right not in counters
            ),
            "correlation_pairs_not_identity": sorted(
                f"{left}->{right}" for left, right in pair_ids if left != right
            ),
            "pairs_missing_from_correlation": sorted(
                f"{left}->{right}" for left, right in matching_pairs - pair_ids
            ),
            "legacy_index_tactics_missing_from_files": sorted(
                tactic.removeprefix("CTFT-TA-") for tactic in indexed_tactics
                if tactic.removeprefix("CTFT-TA-") not in tactics
            ),
            "tactics_missing_from_legacy_index": sorted(
                f"CTFT-TA-{tactic}" for tactic in set(tactics)
                if f"CTFT-TA-{tactic}" not in indexed_tactics
            ),
            "legacy_index_pair_count": len(indexed_pairs),
            "legacy_index_pairs_missing_from_files": sorted(
                f"{left}->{right}" for left, right in indexed_pairs
                if left not in techniques or right not in counters
            ),
        },
    }


def has_integrity_failures(report: dict[str, Any]) -> bool:
    integrity = report["integrity"]
    return any(integrity[key] for key in (
        "techniques_without_counter",
        "counters_without_technique",
        "correlation_pairs_missing_from_files",
        "correlation_pairs_not_identity",
        "pairs_missing_from_correlation",
        "legacy_index_tactics_missing_from_files",
        "tactics_missing_from_legacy_index",
        "legacy_index_pairs_missing_from_files",
    ))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the local CTFT catalogue.")
    parser.add_argument("--write", action="store_true", help="write v2/catalog_manifest.json")
    parser.add_argument("--write-index", action="store_true", help="regenerate index.json from local files")
    parser.add_argument("--write-catalog", action="store_true", help="write v2/catalog.json and curation_queue.json")
    parser.add_argument("--check", action="store_true", help="fail when catalogue integrity diverges")
    args = parser.parse_args()
    if args.write_index:
        (ROOT / "index.json").write_text(
            json.dumps(build_legacy_index(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    report = audit()
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        (V2 / "catalog_manifest.json").write_text(rendered, encoding="utf-8")
    if args.write_catalog:
        catalog = build_v2_catalog()
        (V2 / "catalog.json").write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (V2 / "curation_queue.json").write_text(
            json.dumps(build_curation_queue(catalog), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(rendered, end="")
    return 1 if args.check and has_integrity_failures(report) else 0


if __name__ == "__main__":
    raise SystemExit(main())