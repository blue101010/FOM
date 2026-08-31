#!/usr/bin/env python3
"""Audit the local CTFT catalogue without fetching or executing any tool.

The manifest distinguishes the broad v1 taxonomy from the smaller, typed v3
slice. It deliberately reports discrepancies instead of repairing prose or
inventing execution semantics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from functools import lru_cache
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "v3"
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


def _v3_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in (
        "techniques.for.json",
        "playbooks.for.json",
        "indicators.json",
        "tools.json",
    ):
        data = _load_json(V3 / name)
        counts[name.removesuffix(".json")] = len(data.get("items", []))
    return counts


def _title(path: Path, prefix: str) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return re.sub(rf"^{re.escape(prefix)}\s*[-–—]+\s*", "", line[2:]).strip()
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
        # v3 positioning: external catalogues are per-entry anchors, not the model CTFT
        # complements. `complements` is kept as a deprecated alias for v1 consumers.
        "relates_to": ["MITRE ATT&CK", "CAPEC", "CWE", "OWASP WSTG"],
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


def _evidence_status() -> dict[str, dict[str, Any]]:
    """Per-technique evidence summary from v3/evidence.json (TODO 0.4 + 1.1).

    Independence is counted in distinct CTF events, never in URLs: three write-ups
    of the same challenge are one event.
    """
    summary: dict[str, dict[str, Any]] = {}
    for record in _load_json(V3 / "evidence.json").get("items", []):
        challenges = record.get("challenges", [])
        events = {c.get("ctf") for c in challenges if c.get("ctf")}
        summary[record.get("technique", "")] = {
            "independent_events": len(events),
            "write_ups": len(challenges),
            "has_positives": bool(record.get("positives")),
            "has_negatives": bool(record.get("negatives")),
            "has_boundaries": bool(record.get("boundaries")),
            "status": record.get("status", "seeded"),
        }
    return summary


def _maturity(technique_id: str, counter_id: str, typed: set[str],
              evidence: dict[str, dict[str, Any]]) -> tuple[str, list[str]]:
    """Single maturity vocabulary: taxonomy_only < attested < typed (SCHEMA_V3 §1.1).

    Never promotes on its own: `attested` requires curated positives, negatives and
    boundaries plus two independent CTF events, which only a human can supply.
    """
    if counter_id in typed:
        return "typed", []
    record = evidence.get(technique_id)
    missing = []
    if not record:
        missing.append("evidence_record")
    else:
        if record["independent_events"] < 2:
            missing.append("second_independent_challenge")
        for field in ("positives", "negatives", "boundaries"):
            if not record[f"has_{field}"]:
                missing.append(field)
    if not missing:
        return "attested", ["indicators", "reviewed_tool_bindings", "evaluation_case"]
    return "taxonomy_only", missing


def build_v3_catalog() -> dict[str, Any]:
    """Build a safe, machine-readable catalogue for every paired v1 entry.

    Taxonomy-level entries are intentionally not promoted to executable
    playbooks. Their ``maturity`` records exactly what must be curated next.
    """
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    typed = {
        item.get("id", "")
        for item in _load_json(V3 / "playbooks.for.json").get("items", [])
    }
    evidence = _evidence_status()
    core = {
        item.get("technique", "")
        for item in _load_json(V3 / "core.json").get("items", [])
    }
    items = []
    for key in sorted(set(techniques) & set(counters)):
        category = key.split("-", 1)[0]
        counter_id = f"CTFTCTE-{key}"
        technique_id = f"CTFTTE-{key}"
        maturity, missing = _maturity(technique_id, counter_id, typed, evidence)
        items.append({
            "id": f"CTFTPAIR-{key}",
            "schema_version": "3.0",
            "domain": category,
            "tactic": f"CTFT-TA-{category}",
            "in_core": technique_id in core,
            "technique": {
                "id": technique_id,
                "name": _title(techniques[key], technique_id),
                "path": techniques[key].relative_to(ROOT).as_posix(),
            },
            "counter_technique": {
                "id": counter_id,
                "name": _title(counters[key], counter_id),
                "path": counters[key].relative_to(ROOT).as_posix(),
                "role": "resolution",
            },
            "maturity": maturity,
            "missing_for_typed_recommendation": missing,
        })
    return {
        "model": "CTFT",
        "schema_version": "3.0",
        "collection": "catalog",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_sha256": _sha256(ROOT / "CORRELATION.md"),
        "items": items,
    }


def build_curation_queue(catalog: dict[str, Any]) -> dict[str, Any]:
    """Return the typed-v3 curation backlog grouped by tactic."""
    pending = [item for item in catalog["items"] if item["maturity"] != "typed"]
    return {
        "model": "CTFT",
        "schema_version": "3.0",
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


def build_relations() -> dict[str, Any]:
    """Merge the derived `solves` edges with the curated ones (TODO 3.1).

    The markdown pairing stays the single source of truth for `solves`; curated
    edges may only express what the pairing cannot. A curated `solves` is rejected.
    """
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    derived = [
        {
            "id": f"REL-SOLVES-{key}",
            "schema_version": "3.0",
            "type": "solves",
            "source": f"CTFTCTE-{key}",
            "target": f"CTFTTE-{key}",
            "origin": "derived",
            "confidence": "high",
        }
        for key in sorted(set(techniques) & set(counters))
    ]
    curated = _load_json(V3 / "relations.curated.json").get("items", [])
    return {
        "model": "CTFT",
        "schema_version": "3.0",
        "collection": "relations",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "note": "Generated. Derived `solves` edges come from the markdown pairing; edit "
                "v3/relations.curated.json for anything else.",
        "counts": {"derived": len(derived), "curated": len(curated)},
        "items": derived + curated,
    }


def relation_problems() -> list[str]:
    """Structural checks on the relation graph (TODO 3.1 guard rail)."""
    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    tools = {path.stem for path in (ROOT / "tools").glob("CTFTTOU-*.md")}
    known = ({f"CTFTTE-{key}" for key in techniques}
             | {f"CTFTCTE-{key}" for key in counters} | tools)

    problems: list[str] = []
    curated = _load_json(V3 / "relations.curated.json").get("items", [])
    for item in curated:
        ident = item.get("id", "<no id>")
        if item.get("type") == "solves":
            problems.append(f"{ident}: `solves` is derived, not curated")
        if item.get("origin") != "curated":
            problems.append(f"{ident}: curated file must carry origin=curated")
        for side in ("source", "target"):
            if item.get(side) not in known:
                problems.append(f"{ident}: unknown {side} {item.get(side)!r}")

    generated = _load_json(V3 / "relations.json")
    if generated:
        published = {item.get("id") for item in generated.get("items", [])}
        expected = {item["id"] for item in build_relations()["items"]}
        for missing in sorted(expected - published):
            problems.append(f"{missing}: derived edge missing from v3/relations.json")
    return problems


def _tool_tokens() -> set[str]:
    """Distinctive tool tokens. Tools whose name is an ordinary English word (`file`,
    `strings`, `struct`) are excluded: matching them in prose is noise, not a finding."""
    # Ordinary English words, plus language names — a language legitimately qualifies an
    # artifact or an environment (`Python jail`, `Python bytecode`). A language used as the
    # *implementation of the technique* is caught by IMPLEMENTATION_RE instead.
    generic = {"file", "strings", "struct", "find", "sort", "date", "time",
               "head", "tail", "analyzer", "metadata", "ntfs",
               "python", "java", "ruby", "perl", "bash"}
    tokens: set[str] = set()
    for item in _load_json(V3 / "tools.json").get("items", []):
        for token in re.split(r"[\s/]+", (item.get("name") or "").lower()):
            if len(token) >= 4 and token not in generic:
                tokens.add(token)
    return tokens


# Implementation detail that must not appear in a technique title (editorial rule B1:
# a technique is tool-independent; the tool belongs to the procedure).
IMPLEMENTATION_RE = re.compile(
    r"\b(?:via|using|with|in)\s+(?:a\s+)?"
    r"(python|bash|powershell|perl|ruby|golang|java|c\+\+|script)\b", re.I
)


README_ROW_RE = re.compile(
    r"^\|\s*\d+\s*\|\s*\[CTFT-TA-([A-Z]{3})\][^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|", re.M
)
README_TOTAL_RE = re.compile(r"\*\*Total\*\*\s*\|\s*\|\s*\*\*(\d+)\*\*")
README_PROSE_RE = re.compile(r"\*\*(\d+) complete technique/counter-technique pairs\*\*")
README_MATURITY_RE = r"`{level}`[^|\n]*\|[^|\n]*\|\s*(\d+)\s*\|"
README_DEBT_RE = re.compile(r"(\d+) of (\d+) entry files")
WRITEUP_MARKER = "Add challenge write-up link"


def readme_problems() -> list[str]:
    """Every count asserted in README.md must match the corpus.

    The README is hand-written prose around machine facts; without this check the
    facts drift silently, which is exactly what happened between v2 and v3.
    """
    path = ROOT / "README.md"
    if not path.exists():
        return []
    readme = path.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []

    techniques = _entries(ROOT / "techniques", TECHNIQUE_RE)
    counters = _entries(ROOT / "countertechniques", COUNTER_RE)
    paired = sorted(set(techniques) & set(counters))
    by_domain = Counter(key.split("-", 1)[0] for key in paired)

    claimed = {code: int(count) for code, count in README_ROW_RE.findall(readme)}
    if not claimed:
        return ["README.md: domain table not found or unparseable"]
    for code in sorted(set(by_domain) | set(claimed)):
        if claimed.get(code) != by_domain.get(code):
            problems.append(
                f"README.md: {code} claims {claimed.get(code)} pairs, corpus has {by_domain.get(code)}"
            )

    for regex, label in ((README_TOTAL_RE, "domain-table total"),
                         (README_PROSE_RE, "pair count in prose")):
        match = regex.search(readme)
        if match and int(match.group(1)) != len(paired):
            problems.append(
                f"README.md: {label} says {match.group(1)}, corpus has {len(paired)}"
            )

    maturity = Counter(item["maturity"] for item in build_v3_catalog()["items"])
    for level in ("taxonomy_only", "attested", "typed"):
        match = re.search(README_MATURITY_RE.format(level=level), readme)
        if match and int(match.group(1)) != maturity.get(level, 0):
            problems.append(
                f"README.md: maturity `{level}` says {match.group(1)}, "
                f"computed {maturity.get(level, 0)}"
            )

    if match := README_DEBT_RE.search(readme):
        files = [*techniques.values(), *counters.values()]
        with_marker = sum(
            1 for p in files if WRITEUP_MARKER in p.read_text(encoding="utf-8", errors="replace")
        )
        if (int(match.group(1)), int(match.group(2))) != (with_marker, len(files)):
            problems.append(
                f"README.md: coverage debt says {match.group(1)} of {match.group(2)} entry "
                f"files, corpus has {with_marker} of {len(files)}"
            )
    return problems


# Framing retired by v3. CTFT is an ontology of solving behaviour that *relates to*
# external catalogues; it is not defined by its distance from ATT&CK, and the subject
# axis is a domain, not a tactic. Numeric checks never catch this class of drift, so
# the retired wording is named explicitly. Frozen v2 material is exempt.
RETIRED_WORDING = {
    "ATT&CK-**complementary** knowledge base": "state what CTFT is, not what it is not",
    "does **not** duplicate MITRE ATT&CK": "ATT&CK is a per-entry anchor, not the definition",
    "CTFT tactics are a CTF-specific layer": "v1 domain-page boilerplate",
    "CTFT never re-labels an existing ATT&CK technique": "v1 domain-page boilerplate",
    "complementary to MITRE ATT&CK": "v1 framing",
    "techniques complement ATT&CK": "a domain description must describe its subject",
    "Tactics at a glance": "the subject axis is a domain",
    "active tactics": "the subject axis is a domain",
    "**Tactic ID:**": "the subject axis is a domain",
}
WORDING_SCOPE = ("README.md", "SCHEMA_V3.md", "CORRELATION.md", "HIERARCHY.md")
WORDING_DIRS = ("tactics", "techniques", "countertechniques", "v3")


def wording_problems() -> list[str]:
    """Fail on framing that v3 retired (TODO positioning statement)."""
    paths = [ROOT / name for name in WORDING_SCOPE]
    for directory in WORDING_DIRS:
        base = ROOT / directory
        if base.exists():
            paths += sorted(base.glob("*.md")) + sorted(base.glob("*.py"))

    problems: list[str] = []
    for path in paths:
        # frozen v2 material keeps its own wording; this file *is* the blocklist
        if (not path.exists() or "backup" in path.parts or "v2" in path.parts
                or path.resolve() == Path(__file__).resolve()):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase, why in RETIRED_WORDING.items():
            if phrase in text:
                problems.append(
                    f"{path.relative_to(ROOT).as_posix()}: retired wording {phrase!r} ({why})"
                )
    return problems


MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SELF_URL_RE = re.compile(
    r"https?://github\.com/blue101010/FOM/(?:blob|tree)/[^/]+/([^)\s>\]]+)"
)


@lru_cache(maxsize=1)
def _unpublished_paths() -> frozenset[str]:
    """Repo-relative paths git excludes, i.e. what an external reader never receives.

    One `git check-ignore` call for the whole tree — invoking it per link is minutes
    of process spawning. Returns an empty set when git is unavailable, so the audit
    stays runnable offline in a plain directory copy.
    """
    candidates = [
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.parts
    ]
    # NUL-separated, in bytes: text mode would translate the separators to CRLF on
    # Windows and git would receive every path with a trailing CR.
    try:
        result = subprocess.run(
            ["git", "check-ignore", "-z", "--stdin"],
            cwd=ROOT, input="\0".join(candidates).encode("utf-8"),
            capture_output=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return frozenset()
    return frozenset(
        chunk.decode("utf-8", "replace").replace("\\", "/")
        for chunk in result.stdout.split(b"\0") if chunk
    )


def _is_unpublished(path: Path) -> bool:
    try:
        return path.resolve().relative_to(ROOT).as_posix() in _unpublished_paths()
    except ValueError:      # outside the repository
        return False


def link_problems() -> list[str]:
    """Every link that can be checked offline must resolve.

    Two classes, and the second is the one a naive checker skips: a link that points
    back at this repository through its GitHub URL is verifiable locally, and 59 of
    them were dead after the FOM -> CTFT rename because nothing checked them.
    """
    problems: list[str] = []
    pages = [ROOT / "README.md", ROOT / "SCHEMA_V3.md", ROOT / "CORRELATION.md",
             ROOT / "TODO.md"]
    for directory in ("techniques", "countertechniques", "tactics", "tools", "to_categorize"):
        base = ROOT / directory
        if base.exists():
            pages += sorted(base.rglob("*.md"))

    for page in pages:
        if not page.exists() or "backup" in page.parts:
            continue
        text = page.read_text(encoding="utf-8", errors="replace")

        for target in MD_LINK_RE.findall(text):
            if target.startswith(("http", "#", "mailto:")):
                continue
            resolved = (page.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                problems.append(
                    f"{page.relative_to(ROOT).as_posix()}: dead relative link {target!r}"
                )
            elif _is_unpublished(resolved) and not _is_unpublished(page):
                # resolves locally, 404 for anyone who only has the published repo
                problems.append(
                    f"{page.relative_to(ROOT).as_posix()}: links to {target!r}, which is "
                    "git-ignored and therefore absent from the published repository"
                )

        for repo_path in SELF_URL_RE.findall(text):
            if not (ROOT / repo_path.rstrip(").,")).exists():
                problems.append(
                    f"{page.relative_to(ROOT).as_posix()}: self-link to a path that no "
                    f"longer exists: {repo_path!r} (use a relative link)"
                )
    return problems


def schema_problems() -> list[str]:
    """Cross-schema invariants that no single schema can express."""
    problems: list[str] = []
    technique = _load_json(V3 / "schemas" / "technique.schema.json")
    fingerprint = _load_json(V3 / "schemas" / "fingerprint.schema.json")
    left = technique.get("properties", {}).get("artifact_types", {}).get("items", {}).get("enum")
    right = fingerprint.get("properties", {}).get("artifact_type", {}).get("enum")
    if left is None or right is None:
        problems.append("artifact vocabulary: enum missing from technique or fingerprint schema")
    elif list(left) != list(right):
        only_left = sorted(set(left) - set(right))
        only_right = sorted(set(right) - set(left))
        problems.append(
            "artifact vocabulary diverged between technique.artifact_types and "
            f"fingerprint.artifact_type (technique-only: {only_left}, "
            f"fingerprint-only: {only_right}); retrieval cannot match them"
        )
    return problems


def lint_problems() -> list[str]:
    """Semantic lint over entry titles and evidence (TODO 3.3)."""
    tool_tokens = _tool_tokens()
    problems: list[str] = []

    for key, path in sorted(_entries(ROOT / "techniques", TECHNIQUE_RE).items()):
        name = _title(path, f"CTFTTE-{key}")
        for tool in sorted(tool_tokens):
            if re.search(rf"\b{re.escape(tool)}\b", name, re.I):
                problems.append(f"CTFTTE-{key}: tool name {tool!r} in a technique title")
        if match := IMPLEMENTATION_RE.search(name):
            problems.append(
                f"CTFTTE-{key}: implementation detail {match.group(0)!r} in a technique "
                "title; a technique is tool-independent"
            )

    for key, path in sorted(_entries(ROOT / "countertechniques", COUNTER_RE).items()):
        name = _title(path, f"CTFTCTE-{key}")
        if re.match(r"^counter\b", name, re.I):
            problems.append(f"CTFTCTE-{key}: placeholder title {name!r}; name the recovery action")

    known = {f"CTFTTE-{key}" for key in _entries(ROOT / "techniques", TECHNIQUE_RE)}
    for record in _load_json(V3 / "evidence.json").get("items", []):
        if record.get("technique") not in known:
            problems.append(f"{record.get('id')}: unknown technique {record.get('technique')!r}")
    for item in _load_json(V3 / "core.json").get("items", []):
        if item.get("technique") not in known:
            problems.append(f"core.json: unknown technique {item.get('technique')!r}")

    tactic_map = _load_json(V3 / "tactic_map.json")
    if tactic_map.get("items") and tactic_map.get("status") == "underived":
        problems.append(
            "tactic_map.json: objectives assigned while status is 'underived' "
            "(derive the axis from labelled evidence first — TODO 2.4)"
        )
    return problems


def _maturity_counts() -> dict[str, int]:
    catalog = build_v3_catalog()
    return dict(sorted(Counter(item["maturity"] for item in catalog["items"]).items()))


def _core_coverage() -> dict[str, Any]:
    """How much of the curated core is actually backed by evidence."""
    core = [item.get("technique", "") for item in _load_json(V3 / "core.json").get("items", [])]
    evidence = _evidence_status()
    return {
        "size": len(core),
        "with_evidence_record": sum(1 for t in core if t in evidence),
        "with_two_independent_events": sum(
            1 for t in core if evidence.get(t, {}).get("independent_events", 0) >= 2
        ),
        "placeholder_free": sum(
            1 for t in core
            if not PLACEHOLDER_RE.search(
                (ROOT / "techniques" / f"{t}.md").read_text(encoding="utf-8", errors="replace")
            )
        ),
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
        "schema_version": "3.0",
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
            "typed_v3": _v3_counts(),
            "maturity": _maturity_counts(),
            "core": _core_coverage(),
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
            "relation_problems": relation_problems(),
            "lint_problems": lint_problems(),
            "readme_problems": readme_problems(),
            "schema_problems": schema_problems(),
            "wording_problems": wording_problems(),
            "link_problems": link_problems(),
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
        "relation_problems",
        "lint_problems",
        "readme_problems",
        "schema_problems",
        "wording_problems",
        "link_problems",
    ))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the local CTFT catalogue.")
    parser.add_argument("--write", action="store_true", help="write v3/catalog_manifest.json")
    parser.add_argument("--write-index", action="store_true", help="regenerate index.json from local files")
    parser.add_argument("--write-catalog", action="store_true", help="write v3/catalog.json and curation_queue.json")
    parser.add_argument("--write-relations", action="store_true",
                        help="write v3/relations.json (derived solves + curated edges)")
    parser.add_argument("--check", action="store_true", help="fail when catalogue integrity diverges")
    args = parser.parse_args()
    if args.write_index:
        (ROOT / "index.json").write_text(
            json.dumps(build_legacy_index(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8", newline="\n",
        )
    if args.write_relations:
        (V3 / "relations.json").write_text(
            json.dumps(build_relations(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8", newline="\n",
        )
    report = audit()
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        (V3 / "catalog_manifest.json").write_text(
            rendered, encoding="utf-8", newline="\n"
        )
    if args.write_catalog:
        catalog = build_v3_catalog()
        (V3 / "catalog.json").write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
        )
        (V3 / "curation_queue.json").write_text(
            json.dumps(build_curation_queue(catalog), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8", newline="\n",
        )
    print(rendered, end="")
    return 1 if args.check and has_integrity_failures(report) else 0


if __name__ == "__main__":
    raise SystemExit(main())