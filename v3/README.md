# CTFT v3 — active model layer

Implements [`../SCHEMA_V3.md`](../SCHEMA_V3.md). Everything the catalogue derives from the
Markdown corpus is generated here, and everything a human curates is a separate, clearly marked
file — never both for the same fact.

[`../v2/`](../v2/README.md) is frozen: it keeps the published v2 objects and the original
Forensics proof-of-concept reproducible. Do not run its scripts, they still write the root
generated documents.

## Files

| File | Kind | What it is |
| --- | --- | --- |
| `schemas/*.schema.json` | — | JSON Schema (draft 2020-12) per object type |
| `catalog.json` | generated | every complete pair with computed `maturity`, `domain`, `in_core` |
| `curation_queue.json` | generated | what each non-`typed` pair is missing |
| `catalog_manifest.json` | generated | hashes, counts, integrity and lint findings |
| `relations.json` | generated | derived `solves` edges merged with the curated ones |
| `relations.curated.json` | **curated** | hand-written edges (cross-domain overlap, `can-follow`, …) |
| `evidence.json` | seeded → curated | attestation records, seeded from links already in the corpus |
| `core.json` | **curated** | the 35-entry normative profile |
| `tactic_map.json` | **curated** | resolution-tactic assignments — empty by design (SCHEMA_V3 §3.9) |
| `techniques.for.json`, `playbooks.for.json`, `indicators.json`, `tools.json` | curated | the typed Forensics slice |
| `fingerprints.examples.json` | curated | in-sample retrieval queries |
| `holdout.json` | curated | evaluation set — the only valid `precision@k` baseline |

## Scripts

| Script | Role |
| --- | --- |
| `render_taxonomy_docs.py` | renders `CORRELATION.md`, `HIERARCHY.md` **and the 19 tactic pages**; `--check` gates drift |
| `catalog_audit.py` | index, catalogue, curation queue, relations, manifest; integrity + semantic lint |
| `render_stix.py` | STIX 2.1 bundles from `index.json`, deterministic IDs |
| `build_evidence.py` | seeds `evidence.json` from write-up links already present in the corpus |
| `attach_attack_related.py` | per-entry `Related MITRE ATT&CK` tables |
| `create_todo_entries.py` | scaffolds new pairs |
| `fix_bare_urls.py` | MD034, fence-aware |
| `solve.py` | retrieval engine, schema validation, `precision@k` evaluation |

## Run

```bash
python v3/render_taxonomy_docs.py --write
python v3/catalog_audit.py --write --write-index --write-catalog --write-relations --check
python v3/render_stix.py --write
python v3/build_evidence.py --write
python v3/solve.py --validate
python v3/solve.py --evaluate
```

The same commands without `--write` are the CI gate (`.github/workflows/ci.yml`).

## What the numbers say today

`catalog_audit.py --check` on the current corpus:

- **162 complete pairs, 19 domains**, structural integrity clean, semantic lint clean;
- maturity: **155 `taxonomy_only`, 7 `typed`, 0 `attested`**;
- core profile: 35 selected, **0 backed by two independent CTF events**;
- `holdout.json`: empty, so `precision@k` is undefined.

Those zeros are the point. The pipeline that would promote an entry is built and enforced; what is
missing is evidence, and evidence cannot be generated — it has to be collected from real
write-ups. An empty hold-out reporting an undefined metric is the honest state; a populated one
built from the same write-ups used during curation would report a meaningless success.

## Design rules this layer enforces

1. **Derived beats stored.** `domain`, `solves` edges and maturity are computed, never written, so
   they cannot drift from the corpus.
2. **One source per fact.** A curated `solves` edge is rejected; `relations.json` is generated.
3. **No fabricated attestation.** `build_evidence.py` parses CTF, challenge and year out of the
   URL path and leaves everything else empty.
4. **Fingerprints, not timestamps.** Generated documents carry a corpus hash, so regenerating an
   unchanged corpus is a git no-op and `--check` is a meaningful gate.
5. **Simulation only.** No script executes a CTF tool; execution belongs to a separately
   authorized laboratory runner.
