#!/usr/bin/env python3
"""Render the STIX 2.1 bundles from the markdown corpus and index.json.

Replaces the STIX output of the legacy `ctft-generator.py`, whose embedded corpus
is frozen at 14 tactics. Object IDs stay deterministic (uuid5 over the same
namespace the legacy generator used), and timestamps are a fixed constant, so a
regeneration that changes no content produces no diff.

Relation semantics (TODO 0.3 / archive A-8): a counter-technique *solves* a design
technique, it does not mitigate it. The bundle emits both — `relationship_type:
"mitigates"` so ATT&CK Navigator and OpenCTI still read the graph, plus
`x_ctft_relation: "solves"` carrying the correct semantics.

    python v3/render_stix.py            # report what would be written
    python v3/render_stix.py --write    # write stix/ctft-bundle.json + by-category/
"""
from __future__ import annotations

import argparse
import json
import re
import uuid
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STIX = ROOT / "stix"

# Same namespace as ctft-generator.py, so the objects already published keep their IDs.
NS = uuid.UUID("6f1a4c2e-0000-4000-8000-000000000abc")
# Fixed stamp: regeneration is byte-stable unless the corpus itself changed.
STAMP = "2026-06-10T18:01:52.000Z"

TECHNIQUE_BODY_RE = re.compile(r"## How the challenge author hides\n+(.*?)(?:\n## |\Z)", re.S)
COUNTER_BODY_RE = re.compile(
    r"## Offensive Recovery \(CTF practitioner / solver\)\n+(.*?)(?:\n## |\Z)", re.S
)
DESCRIPTION_RE = re.compile(r"## Description\n+(.*?)\n+## ", re.S)
HTB_RE = re.compile(r"\*\*HTB mapping:\*\*\s*(.+?)\s*$", re.M)
ATTACK_TABLE_RE = re.compile(r"## Related MITRE ATT.?&CK\n+(.*?)(?:\n## |\Z)", re.S)
ATTACK_ROW_RE = re.compile(r"^\|\s*(T\d{4}(?:\.\d{3})?)\s*\|([^|]*)\|", re.M)


def det_uuid(prefix: str, key: str) -> str:
    return f"{prefix}--{uuid.uuid5(NS, prefix + key)}"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def collapse(text: str) -> str:
    """One-line, table- and placeholder-free prose for a STIX description."""
    lines = [
        line.strip() for line in text.strip().splitlines()
        if line.strip() and not line.lstrip().startswith("|")
    ]
    joined = " ".join(lines)
    joined = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", joined)   # unwrap md links
    joined = re.sub(r"[*`_]+", "", joined)
    return re.sub(r"\s+", " ", joined).strip()


def attack_refs(path: Path) -> list[dict[str, str]]:
    match = ATTACK_TABLE_RE.search(read(path))
    if not match:
        return []
    seen: dict[str, str] = {}
    for attack_id, name in ATTACK_ROW_RE.findall(match.group(1)):
        seen.setdefault(attack_id, name.strip())
    return [
        {"source_name": "mitre-attack", "external_id": attack_id, "description": name}
        for attack_id, name in seen.items()
    ]


def base(obj_type: str, key: str, identity_id: str | None = None) -> dict[str, Any]:
    obj: dict[str, Any] = {
        "type": obj_type,
        "spec_version": "2.1",
        "id": det_uuid(obj_type, key),
        "created": STAMP,
        "modified": STAMP,
    }
    if identity_id:
        obj["created_by_ref"] = identity_id
    return obj


def build() -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))

    identity = base("identity", "ctft-maintainer")
    identity |= {
        "name": "CTFT Project",
        "identity_class": "organization",
        "description": "Capture-The-Flag Techniques - an ontology of CTF solving "
                       "behaviour. Relates to MITRE ATT&CK, CAPEC and CWE as per-entry "
                       "anchors; not a parallel ATT&CK. Generalized from FOM.",
    }
    identity_id = identity["id"]

    objects: list[dict[str, Any]] = [identity]
    by_category: dict[str, list[dict[str, Any]]] = {}

    for tactic in index["tactics"]:
        code = tactic["id"].removeprefix("CTFT-TA-")
        page = ROOT / tactic["path"]
        description = DESCRIPTION_RE.search(read(page))
        htb = HTB_RE.search(read(page))
        obj = base("x-ctft-tactic", code, identity_id)
        obj |= {
            "name": tactic["name"].split("—", 1)[-1].strip(),
            "x_ctft_shortname": code.lower(),
            "x_ctft_domain": code,
            "description": (collapse(description.group(1)) if description else tactic["name"])
                           + (f" ({htb.group(1).strip()})" if htb else ""),
            "external_references": [{"source_name": "ctft", "external_id": tactic["id"]}],
        }
        objects.append(obj)
        by_category.setdefault(code, []).append(obj)

    for entry in index["techniques"]:
        code = entry["category"]
        technique, counter = entry["technique"], entry["counter"]
        technique_path, counter_path = ROOT / technique["path"], ROOT / counter["path"]

        body = TECHNIQUE_BODY_RE.search(read(technique_path))
        pattern = base("attack-pattern", technique["id"], identity_id)
        pattern |= {
            "name": f"{technique['id']} - {technique['name']}",
            "description": collapse(body.group(1)) if body else technique["name"],
            "kill_chain_phases": [{"kill_chain_name": "ctft", "phase_name": code.lower()}],
            "x_ctft_category": code,
            "x_ctft_domain": code,
            "x_ctft_role": "design-hide",
            "external_references": [
                {"source_name": "ctft", "external_id": technique["id"]},
                *attack_refs(technique_path),
            ],
        }

        recovery = COUNTER_BODY_RE.search(read(counter_path))
        action = base("course-of-action", counter["id"], identity_id)
        action |= {
            "name": f"{counter['id']} - {counter['name']}",
            "description": collapse(recovery.group(1)) if recovery else counter["name"],
            "x_ctft_category": code,
            "x_ctft_domain": code,
            "x_ctft_role": "resolution",
            "external_references": [
                {"source_name": "ctft", "external_id": counter["id"]},
                *attack_refs(counter_path),
            ],
        }

        link = base("relationship", f"{counter['id']}->{technique['id']}", identity_id)
        link |= {
            "relationship_type": "mitigates",
            "x_ctft_relation": "solves",
            "source_ref": action["id"],
            "target_ref": pattern["id"],
            "description": "Counter-technique recovers/defeats the paired design technique. "
                           "`mitigates` is kept for STIX-consumer compatibility; the CTFT "
                           "semantics are carried by x_ctft_relation.",
        }

        trio = [pattern, action, link]
        objects.extend(trio)
        by_category.setdefault(code, []).extend(trio)

    return objects, by_category


def bundle(key: str, objects: list[dict[str, Any]]) -> dict[str, Any]:
    return {"type": "bundle", "id": det_uuid("bundle", key), "objects": objects}


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the CTFT STIX 2.1 bundles.")
    parser.add_argument("--write", action="store_true", help="write the bundles to stix/")
    args = parser.parse_args()

    objects, by_category = build()
    identity = objects[0]
    full = bundle("ctft-full", objects)

    targets: dict[Path, dict[str, Any]] = {STIX / "ctft-bundle.json": full}
    for code, subset in sorted(by_category.items()):
        targets[STIX / "by-category" / f"CTFT-{code}.json"] = bundle(code, [identity, *subset])

    if args.write:
        (STIX / "by-category").mkdir(parents=True, exist_ok=True)
        stale = {
            path for path in (STIX / "by-category").glob("CTFT-*.json")
        } - set(targets)
        for path in sorted(stale):
            path.unlink()
            print(f"removed stale {path.relative_to(ROOT).as_posix()}")
        for path, payload in targets.items():
            path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )

    from collections import Counter
    counts = Counter(obj["type"] for obj in objects)
    verb = "wrote" if args.write else "would write"
    print(f"{verb} stix/ctft-bundle.json: {len(objects)} objects {dict(sorted(counts.items()))}")
    print(f"{verb} {len(by_category)} per-category bundles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
