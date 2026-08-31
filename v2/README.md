# CTFT v2 — reference implementation (Forensics slice)

> **FROZEN — v2 reference slice.** Superseded by [`../v3/`](../v3/README.md) and
> [`../SCHEMA_V3.md`](../SCHEMA_V3.md). Kept unchanged so the published v2 objects and the
> Forensics proof-of-concept stay reproducible. **Do not edit, and do not run the scripts in
> this directory** — `v2/render_taxonomy_docs.py` and `v2/catalog_audit.py` still write the
> root `CORRELATION.md`, `HIERARCHY.md` and `index.json`, and would revert them to v2 output.
> Use the `v3/` equivalents.

Working proof that [`../SCHEMA_V2.md`](../SCHEMA_V2.md) is executable, not just descriptive.
Covers 7 curated Forensics techniques end to end: taxonomy → indicators → executable playbooks →
retrieval → agent loop.

## Files

| File | Layer | What it is |
|---|---|---|
| `schemas/*.schema.json` | — | JSON Schema (draft 2020-12) for each object type |
| `tools.json` | 1 | 8 tool bindings (invocation templates + output parsers) |
| `indicators.json` | 2 | 10 observable signals with weights + detectors |
| `techniques.for.json` | 0/2 | 6 design/hide techniques, enriched with indicators + prevalence |
| `playbooks.for.json` | 1 | 6 executable counter-techniques (triggers, steps, fallbacks) |
| `fingerprints.examples.json` | 2 | 3 challenge fingerprints (queries) |
| `solve.py` | 3 | engine: observe → retrieve → select → plan |

## Run

```bash
python v2/solve.py                 # run all 3 example fingerprints
python v2/solve.py --index 0       # single case
python v2/solve.py --validate      # JSON-Schema-validate every object + check references
python v2/catalog_audit.py --write --write-index --check
python v2/catalog_audit.py --write-catalog
```

Expected: `VALIDATION OK: 34 objects schema-valid; indicator/tool references resolve.` then a ranked
candidate list + tool-bound step plan per fingerprint.

## Catalogue integrity

`catalog_audit.py` is an offline gate between the Markdown taxonomy and the
machine-readable inventory. It records source hashes, validates every pair in
`CORRELATION.md`, regenerates the compatible `index.json`, and writes
`catalog_manifest.json`. It does not create a missing technique, relationship,
or playbook. The manifest separates structural consistency from content maturity:
the typed v2 slice remains the six curated Forensics entries until other tactics
receive reviewed indicators, preconditions, tools, and references.

`--write-catalog` creates `catalog.json` for every complete pair and
`curation_queue.json` for every entry that remains `taxonomy_only`. This gives
consumers a complete, stable identifier catalogue without falsely treating an
uncurated technique as a runnable playbook.

## What this demonstrates (maps to the 3 v2 upgrades)

1. **Execution semantics** — each playbook is a branching step graph bound to real tool invocations,
   with `priority`, `cost`, `confidence_prior`, `success_criteria`, `fallbacks`.
2. **Case-based retrieval** — `rank()` scores techniques from a fingerprint's evidence
   (`Σ weight·match · prevalence`, normalized), no tactic browsing.
3. **Agent interoperability** — typed IO, tool contracts, and a deterministic loop an autonomous
   solver can drive; `SolverState` (SCHEMA_V2 §5) is the memory it would persist between steps.

## Next to generalize beyond this slice

- Resolve placeholders and curate typed v2 objects tactic by tactic, starting with
   Forensics, Steganography, Reverse Engineering, Cryptography, and Web.
- Add cross-tactic fingerprints (e.g. image → Forensics *and* Steganography candidates).
- Keep the v2 solver simulated. Tool execution belongs outside CMEP and requires a
   separately authorized laboratory runner.
