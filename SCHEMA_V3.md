# CTFT / FOM — v3 Schema

> **Positioning.** CTFT is an ontology of CTF solving behaviour. It relates to MITRE ATT&CK,
> CAPEC, CWE and OWASP WSTG without deriving from them: external identifiers are anchors
> carried per entry with a confidence and a justification (§8), never the definition of an
> entry. CTFT is not a parallel ATT&CK.
>
> Status: **active model.** [`SCHEMA_V2.md`](SCHEMA_V2.md) and [`v2/`](v2/README.md) are frozen
> and kept for reproducibility; every new object is v3.
>
> Backward compatible by construction: every `CTFTTE-*`, `CTFTCTE-*` and `CTFT-TA-*` identifier
> survives unchanged as a stable primary key, and `countertechniques/` keeps its name. v3 renames
> vocabulary and adds axes; it does not renumber, move or delete entries.

---

## 1. What changes vs. v2

| Area | v2 | v3 |
| --- | --- | --- |
| Subject axis | `tactic` (`CTFT-TA-FOR`) — a *subject* wearing the name of an *objective* | `domain`, **derived** from the ID prefix; `tactic` kept as a deprecated alias |
| Player objective | conflated with the subject | separate axis, deliberately **underived** until evidence supports it (§3.9) |
| Artifact | free-form `artifact_types` strings | controlled vocabulary, shared with `fingerprint.artifact_type` (§3.7) |
| Competition format | absent | `format` axis, only on evidence-backed entries (§3.8) |
| Counter-technique | "counters" prose | `role: "resolution"` — a resolution-technique; ID and directory unchanged (§3.2) |
| Graph | implicit 1:1 pairing only | explicit relation objects: derived `solves` + curated cross-domain edges (§4) |
| Maturity | `taxonomy_only \| typed` in the schema, a second `draft→reviewed→stable` vocabulary in the backlog | **one** vocabulary: `taxonomy_only → attested → typed`, plus `superseded` (§1.1) |
| Evidence | write-up links buried in prose | typed `evidence` records with independence counting (§5) |
| Tactic pages | hand-maintained, drifting (truncated names, missing columns) | generated from the corpus like `CORRELATION.md` |
| STIX | `mitigates` only, corpus frozen at 63 pairs | regenerated from `index.json`; `mitigates` **and** `x_ctft_relation: "solves"` (§4.3) |
| Evaluation | none | `precision@k` over a labelled hold-out (§6.2) |

```text
Layer 0  Taxonomy      domain, technique, resolution-technique   (v1.1 identifiers — kept)
Layer 1  Execution     playbook, step, indicator, tool
Layer 2  Retrieval     fingerprint, ranking, precision@k
Layer 3  Agent runtime solver-state, evidence, verdict
Cross    Provenance    evidence, core profile, relations
```

All objects are JSON Schema **draft 2020-12**, carry `schema_version: "3.0"` and a stable `id`.
The Markdown entry files remain the editorial source of truth; every JSON collection under `v3/`
is either generated from them or explicitly hand-curated, never both.

### 1.1 Maturity — one vocabulary

| Maturity | Meaning | Who sets it |
| --- | --- | --- |
| `taxonomy_only` | Stable identifiers and paired prose exist. Nothing is attested. | default |
| `attested` | ≥ 2 **independent CTF events** cited, plus curated positives, negatives and boundaries. | computed from `v3/evidence.json` |
| `typed` | Schema-valid typed objects exist; participates in deterministic retrieval. | computed from `v3/playbooks.for.json` |
| `superseded` | Replaced by another entry; identifier never reused (e.g. the retired `MSC` family). | curator |

Maturity is **never stored on an entry**. `v3/catalog_audit.py` computes it, so the catalogue and
the evidence can not disagree. Independence is counted in distinct CTF events, never in URLs:
three write-ups of one challenge are one event.

No maturity level authorizes automatic execution. A consumer may display a tool reference or a
human-readable step; execution belongs to a separately authorized laboratory runner.

### 1.2 The four axes

An entry is described by axes that vary independently. Conflating them was the v1/v2 defect.

| Axis | Question | Where it lives | Status |
| --- | --- | --- | --- |
| `domain` | *what subject?* | derived from the ID prefix | active, 19 values |
| `artifact` | *what is the flag hidden in?* | `artifact_types` on the technique | active, controlled vocab |
| `format` | *what competition shape?* | `format`, evidence-backed entries only | active, 3 values |
| resolution tactic | *what is the player trying to achieve?* | `v3/tactic_map.json` | **underived** — see §3.9 |

---

## 2. Envelope

`index.json` stays the v1-compatible flat pair list (generated). The v3 collections are separate
files so each can ship independently:

| File | Kind | Content |
| --- | --- | --- |
| `v3/catalog.json` | generated | every complete pair with computed `maturity`, `domain`, `in_core` |
| `v3/curation_queue.json` | generated | what each non-`typed` pair is missing |
| `v3/catalog_manifest.json` | generated | hashes, counts, integrity and lint findings |
| `v3/relations.json` | generated | derived `solves` + merged curated edges |
| `v3/relations.curated.json` | **curated** | hand-written edges only |
| `v3/evidence.json` | seeded then curated | attestation records |
| `v3/core.json` | **curated** | the ~35-entry normative profile |
| `v3/tactic_map.json` | **curated** | resolution-tactic assignments (empty by design) |
| `v3/techniques.for.json`, `playbooks.for.json`, `indicators.json`, `tools.json` | curated | the typed slice |
| `v3/fingerprints.examples.json`, `v3/holdout.json` | curated | retrieval queries; the hold-out is the only valid baseline |
| `v3/schemas/*.schema.json` | — | JSON Schema for every object type |

---

## 3. Objects

### 3.1 `technique` (design/hide)

```jsonc
{
  "id": "CTFTTE-FOR-001",                       // unchanged primary key
  "schema_version": "3.0",
  "name": "Magic-byte / file-signature tampering",
  "domain": "FOR",                              // v3 subject axis — derived, never hand-written
  "tactic": "CTFT-TA-FOR",                      // deprecated alias, kept for compatibility
  "paired_counter": "CTFTCTE-FOR-001",
  "summary": "Author corrupts/swaps the file magic header so type detection and viewers fail.",
  "artifact_types": ["file", "image", "archive"],  // controlled vocabulary, §3.7
  "format": ["jeopardy"],                          // only from a cited challenge, §3.8
  "attack_related": [
    { "id": "T1027", "name": "Obfuscated Files or Information",
      "note": "ATT&CK omits the byte-level magic-header recovery detail." }
  ],
  "indicators": ["IND-FOR-magic-mismatch", "IND-FOR-ext-type-conflict"],
  "difficulty": 2,
  "prevalence": 0.7,
  "references": ["https://www.garykessler.net/library/file_sigs.html"]
}
```

`required`: `id`, `schema_version`, `name`, `domain`, `paired_counter`, `indicators`.

**Editorial rule.** A technique is *an observable action, phrased verb + object, independent of any
tool, reusable across challenges.* A tool or language name in a title is an implementation detail
and belongs to the procedure — `v3/catalog_audit.py` enforces this (§7.3). A language legitimately
qualifying an artifact or environment (`Python jail`, `Python bytecode`) is not a violation.

### 3.2 `playbook` — the resolution-technique

The counter-technique is a **Playbook**: a decision graph an expert or an agent can run.

```jsonc
{
  "id": "CTFTCTE-FOR-001",                        // unchanged primary key
  "schema_version": "3.0",
  "name": "Recover the legitimate file signature",
  "domain": "FOR",
  "role": "resolution",                           // v3 vocabulary; the key stays CTFTCTE-*
  "counters": "CTFTTE-FOR-001",
  "triggers": { "all_of": ["IND-FOR-magic-mismatch"],
                "any_of": ["IND-FOR-ext-type-conflict", "IND-FOR-file-cmd-unknown"],
                "none_of": [] },
  "preconditions": [
    { "id": "have-raw-bytes", "desc": "Raw file is available for byte inspection" }
  ],
  "inputs":  { "$ref": "#/io/file-artifact" },
  "outputs": { "type": "object",
               "properties": { "true_type": { "type": "string" },
                               "patched_file": { "type": "string" } },
               "required": ["true_type"] },
  "steps": [
    { "id": "s1-detect", "action": "Compare leading bytes against a signature table.",
      "tool": "TOOL-file", "produces": ["observed_magic", "declared_ext"],
      "validates": "observed_magic != expected(declared_ext)",
      "on_true": "s2-identify", "on_false": "FALLBACK" },
    { "id": "s2-identify", "action": "Identify true type from internal structure/footers.",
      "tool": "TOOL-binwalk", "produces": ["true_type"],
      "on_true": "s3-patch", "on_false": "s3-patch" },
    { "id": "s3-patch", "action": "Patch the header to the true signature.",
      "tool": "TOOL-python-struct", "produces": ["patched_file"],
      "success_when": "file(patched_file) == true_type" }
  ],
  "priority": 8, "cost": "low", "automation": "full", "confidence_prior": 0.75,
  "false_positives": ["Polyglots legitimately carry two valid signatures."],
  "success_criteria": "Recovered file opens as its true type and yields the next artifact.",
  "fallbacks": ["CTFTCTE-FOR-002", "CTFTCTE-STE-001"],
  "tools": ["TOOL-xxd", "TOOL-file", "TOOL-binwalk", "TOOL-python-struct"]
}
```

`required`: `id`, `schema_version`, `name`, `domain`, `counters`, `triggers`, `steps`, `priority`.

Both the **offensive** and **blue-team** framings from v1.1 are preserved on the Markdown page;
nothing in the corpus is lost by typing an entry.

> **Naming.** `resolution-technique` is the v3 term: a CTF counter-technique *solves* a puzzle, it
> does not *mitigate* a threat. The public identifier stays `CTFTCTE-*` and the directory stays
> `countertechniques/` — renaming those would break every published link for no semantic gain.

### 3.3 `indicator`

```jsonc
{
  "id": "IND-FOR-magic-mismatch",
  "schema_version": "3.0",
  "name": "File magic bytes do not match declared extension",
  "applies_to": ["file", "image", "archive"],
  "signal_type": "boolean",
  "detector": { "method": "tool", "tool": "TOOL-file",
                "expr": "file(x).type != mimetype_of(extension(x))" },
  "weight": 0.9
}
```

### 3.4 `tool`

```jsonc
{
  "id": "TOOL-binwalk",
  "schema_version": "3.0",
  "name": "binwalk",
  "kind": "cli",
  "platforms": ["linux", "wsl", "macos"],
  "install": "pip install binwalk",
  "invocation": { "cmd": "binwalk --extract {file}",
                  "params": { "file": { "type": "string", "required": true } } },
  "input_types": ["file"],
  "output_parser": { "format": "regex-lines",
                     "captures": { "offset": "^(\\d+)", "type": "\\s+(\\w[\\w ]+)$" } },
  "produces": ["embedded_files", "true_type"]
}
```

### 3.5 Per-entry MITRE ATT&CK display

`attack_related` is the per-entry source of truth for ATT&CK relations; the tactic page carries an
`ATT&CK` column for orientation only. Every technique and resolution-technique page renders:

```markdown
## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | ATT&CK omits the byte-level magic-header recovery detail. |
```

When nothing is related, the table carries one explicit empty row (`| — | — | No direct ATT&CK
equivalent. |`) so the absence is machine-checkable rather than assumed. Maintained by
`v3/attach_attack_related.py`.

> **No D3FEND mapping.** D3FEND normalises defensive countermeasures; a resolution-technique is
> offensive recovery, and only the blue-team half of a page would map. ATT&CK anchoring is already
> loose — 61 distinct IDs across 162 entries, `T1027` used 24 times — so a second approximate
> mapping would add noise, not precision. CAPEC and CWE are the intended next anchors, per entry,
> with a confidence and a justification (§8).

### 3.6 `domain` — derived, never written

The subject axis is the three-letter code already embedded in every identifier.
`v3/catalog_audit.py` computes it; hand-writing it is forbidden, because a stored copy can drift
from the ID. `tactic` (`CTFT-TA-<CAT>`) remains as a `deprecated` alias so existing consumers keep
working.

The 19 active domains and their canonical order live in `CANONICAL_ORDER` inside
`v3/render_taxonomy_docs.py` — the order of the challenge-category picker, not alphabetical. A
tactic directory absent from that list is a hard error, so a new domain must be declared
deliberately.

### 3.7 `artifact` — controlled vocabulary

What the flag is hidden *in*. Shared verbatim by `technique.artifact_types` and
`fingerprint.artifact_type` so retrieval can match them:

```text
http-service | elf | pe | apk | pcap | memory-image | disk-image | qr | audio | image
| video | archive | document | contract | firmware | rf-capture | source-code
| binary-blob | file | web | text
```

Required for `typed` entries. Adding a value means editing both schemas in the same change.

### 3.8 `format` — competition shape

`jeopardy | attack-defense | wargame`. Optional, and set **only** from a challenge actually cited
in that entry's evidence record. An unattested entry has no `format`: guessing it would make the
axis measure the guesser.

### 3.9 Resolution tactics — deliberately underived

The player-objective axis is the one v2 was missing, and the one most easily faked. The
hypothesis under test is:

```text
Discover | Reveal | Gain Access | Gain Control | Expand Reach | Capture Objective
```

It is **not** a decision. `v3/tactic_map.json` ships with `status: "underived"` and an empty
`items` map, and `catalog_audit.py` fails if objectives are assigned while that status holds.

Admission rules, applied after labelling the core against real write-ups:

1. an objective is admitted only if it covers **≥ 5 core techniques**;
2. an objective that is **constant across a whole domain** is not an axis — it is that domain's
   restatement, and is rejected;
3. labelling is free text first, grouped afterwards. Grouping into the six values above before
   labelling would confirm the hypothesis by construction.

The map is an external table keyed by technique id, not front-matter on 162 files: if the axis
turns out wrong, one file is discarded instead of a corpus-wide migration being reversed.

---

## 4. Relations

### 4.1 Derived vs curated

| Edge | Origin | Source of truth |
| --- | --- | --- |
| `solves` | derived | the 1:1 Markdown pairing |
| `is-a`, `implements`, `can-follow`, `uses-tool`, `requires`, `related-to` | curated | `v3/relations.curated.json` |

`v3/relations.json` is the merge of both and is **generated**. A curated `solves` edge is rejected
by the audit: two sources for one fact is how catalogues drift.

The 1:1 pair stays the **editorial unit** — it is what forces every concealment to have a
documented recovery. The graph is layered on top; it does not replace it.

### 4.2 Cross-domain overlap

Title similarity finds almost nothing (5 near-duplicates, all intra-domain and benign). The real
overlaps are cross-domain and invisible to a title comparison, so they are recorded explicitly:

| A | B | Overlap |
| --- | --- | --- |
| `CTFTTE-PWN-005` | `CTFTTE-JAL-005` | seccomp syscall filter |
| `CTFTTE-COD-005` | `CTFTTE-REV-005` | constraint solving with Z3 / angr |
| `CTFTTE-COD-003` | `CTFTTE-GAM-001` | protocol automation |
| `CTFTTE-JAL-003` | `CTFTTE-FPN-004` | container escape |

### 4.3 STIX 2.1 mapping

| CTFT | STIX |
| --- | --- |
| technique | `attack-pattern` (`kill_chain_name: ctft`, `phase_name` = domain), `x_ctft_domain`, `x_ctft_role: "design-hide"` |
| resolution-technique | `course-of-action`, `x_ctft_role: "resolution"` |
| pairing | `relationship` — `relationship_type: "mitigates"` **plus** `x_ctft_relation: "solves"` |
| domain | `x-ctft-tactic` |
| ATT&CK anchor | `external_references[source_name: "mitre-attack"]` |

`mitigates` is semantically wrong for a CTF but is kept so ATT&CK Navigator and OpenCTI can still
read the graph; `x_ctft_relation` carries the correct meaning. Object IDs are `uuid5` over the
original namespace and timestamps are a fixed constant, so regenerating an unchanged corpus
produces no diff. Generated by `v3/render_stix.py`.

---

## 5. Evidence and the core profile

### 5.1 `evidence`

```jsonc
{
  "id": "EVID-FOR-001",
  "schema_version": "3.0",
  "technique": "CTFTTE-FOR-001",
  "challenges": [ { "ctf": "LEVELEFFECTCDA2024", "challenge": "Magic_repairman",
                    "year": 2024, "writeup": "<url>" } ],
  "references": [ { "label": "File signature table", "url": "<url>" } ],
  "positives":  ["magic bytes replaced by 00 00 00 00, rest of the container intact"],
  "negatives":  ["file merely renamed .png, header untouched"],
  "boundaries": ["distinct from CTFTTE-STE-002: data appended after EOF, header intact"],
  "abstraction": "technique",
  "external_mappings": [ { "framework": "CWE", "id": "CWE-...", "confidence": "medium",
                           "justification": "..." } ],
  "status": "seeded"
}
```

`v3/build_evidence.py` seeds records from links **already present** in the corpus — it parses CTF,
challenge and year out of the write-up URL path and invents nothing. Everything it cannot read
stays empty, which is why a seeded record is not an attested one.

### 5.2 The core profile

`v3/core.json` lists ~35 promotion candidates, one per recurring solver behaviour. It is a
**profile, not a restructuring**: the other entries stay exactly where they are, and membership
carries no maturity of its own. A small attested core plus a large descriptive index is the
intended shape of the catalogue — breadth stays useful for lookup while credibility is built on
what is verified.

---

## 6. Layer 2 — retrieval

### 6.1 Ranking

A **fingerprint** is a query built from what the solver observed, not something authored per
technique. Candidates are eligible when their playbook's `triggers` fire; the score is

```text
score = Σ (indicator.weight × evidence_match)  ×  technique.prevalence      (+0.15 artifact prior)
```

normalised to 0..1, ties broken by authored `priority`.

### 6.2 Evaluation

```bash
python v3/solve.py --evaluate                       # v3/holdout.json
python v3/solve.py --evaluate fingerprints.examples.json
```

reports `precision@1/3/5`, overall and per domain. A case counts only if it carries `expected`.

**A case belongs in the hold-out only if its write-up was not consulted while curating the
technique it targets.** Otherwise `precision@k` measures memorisation; the tool labels in-sample
runs as `[IN-SAMPLE: not a baseline]` so the number can never be quoted as one.

`v3/holdout.json` is empty today, and that is the correct state: an empty hold-out reports an
undefined metric, which is honest, whereas a fabricated one reports a false success.

---

## 7. Layer 3 — agent runtime and integrity gates

### 7.1 Solver loop

`observe → retrieve → select → plan → report`, driven by `v3/solve.py`. `SolverState` is the memory
an autonomous solver persists between steps. Tool execution stays simulated: it belongs to a
separately authorized laboratory runner.

### 7.2 Structural gates

`v3/catalog_audit.py --check` fails on: unpaired entries, `CORRELATION.md` pairs missing from the
files, non-identity pairs, pairs missing from the matrix, index/taxonomy divergence, relation
problems and lint problems.

### 7.3 Semantic lint

- a distinctive tool name in a technique title (ordinary words like `file` or `strings`, and
  language names, are excluded — they collide with prose);
- an implementation detail in a technique title (`via python script`);
- a resolution-technique still titled `Counter — <technique name>` instead of naming the action;
- an `evidence` or `core` record pointing at an unknown technique;
- objectives assigned in `tactic_map.json` while its status is `underived`.

Title similarity is reported as information, never as a failure: on this corpus it finds four
benign intra-domain pairs and none of the real cross-domain overlaps.

### 7.4 Drift gate

`v3/render_taxonomy_docs.py --check` exits non-zero when any generated document differs from what
the corpus would produce. Generated documents carry a **corpus fingerprint**, not a timestamp, so
an unchanged regeneration is a no-op in git and the gate is meaningful.

---

## 8. Curation — promotion criteria

An entry moves `taxonomy_only → attested` only when all of the following hold:

1. **≥ 2 independent challenges or write-ups** — independent means different CTF events;
2. **positive examples and counter-examples**;
3. **explicit boundaries** with neighbouring techniques, each naming the neighbour's ID;
4. **declared abstraction level** — `technique | subtechnique | procedure`;
5. **synonyms** and any superseded identifier;
6. **typed external mapping** to CWE, CAPEC, WSTG or ATT&CK, each with a confidence and a
   justification;
7. **one curator plus two independent public sources.** The repository is single-maintainer; a
   two-curator rule would be unenforceable, and an unenforceable criterion discredits the others.

`attested → typed` additionally requires reviewed indicators, tool bindings and an evaluation case.

---

## 9. Migration and compatibility

| Artefact | State |
| --- | --- |
| `CTFTTE-*`, `CTFTCTE-*`, `CTFT-TA-*` | unchanged, stable, never reused |
| `techniques/`, `countertechniques/`, `tactics/` | unchanged paths |
| `index.json` | v1-compatible, generated |
| `SCHEMA_V2.md`, `v2/` | **frozen** — do not edit, do not run its scripts (they still write the root generated documents) |
| `ctft-generator.py` | legacy; no longer the STIX source |
| `CTFT-TA-MSC` | superseded — `JAL` / `COD` / `GAM` / `FPN` |

v3 renames vocabulary in schemas and documentation only. Nothing in the corpus was renumbered,
moved or deleted by the v3 migration.

---

## 9bis. Scope: detection and telemetry challenges

Detection-focused events (DEATHCON-style hunting labs, purple-team ranges) sit inside CTFT, with
one boundary.

**In scope.** A challenge where an adversary action was performed and the player must find it in
telemetry has exactly the CTFT shape: something was placed to be missed, something recovers it.
The technique describes the concealment — volume, channel choice, cleared logs, an unremarkable
provider; the resolution-technique describes the recovery — normalise, pivot, correlate. The
artifact is a log or telemetry stream, which the `artifact` vocabulary already carries. This is
what `CTFTTE-FOR-028` records.

**Out of scope.** Detection *engineering* as a deliverable: writing a Sigma rule, tuning a SIEM,
measuring coverage against a framework. Those produce a control, not a recovered flag, and they
are already normalised elsewhere (Sigma, ATT&CK coverage tooling). CTFT would add nothing and
would inherit a second taxonomy to keep in sync.

**The test.** If removing the concealment makes the challenge trivial, it is CTFT. If the
challenge is graded on the quality of a rule the player wrote, it is not.

A consequence worth stating: the blue-team half of every resolution-technique page already carries
the analyst framing. Detection challenges enrich that half; they do not justify a new domain.

---

## 10. Deliberate non-goals

| Not done | Why |
| --- | --- |
| D3FEND mapping | defensive catalogue for an offensive-recovery object; would double an already loose mapping (§3.5) |
| Renaming `CTFT-TA-*` to `CTFT-DOM-*` | cosmetic; breaks every published link |
| Five-axis front-matter on all 162 entries | ~800 fields over a corpus whose median entry body is a few hundred characters; derived fields would be measured as if curated |
| Replacing the 1:1 pair with a free N:M graph | the pairing is what forces every concealment to have a recovery; the graph is layered above it (§4.1) |
| Assigning the six resolution tactics now | postulated, not observed; must be derived from labelled evidence (§3.9) |
| Consolidating `WEB-004` with `WEB-016` under CWE-89 | `WEB-016` is NoSQL injection — CWE-943 / CAPEC-676. Consolidating before evidence manufactures errors |

---

## 11. Commands

```bash
# regenerate every derived document (CORRELATION, HIERARCHY, tactic pages)
python v3/render_taxonomy_docs.py --write

# index, catalogue, curation queue, relations, manifest — then gate
python v3/catalog_audit.py --write --write-index --write-catalog --write-relations --check

# STIX bundles
python v3/render_stix.py --write

# evidence seeding, typed-object validation, retrieval evaluation
python v3/build_evidence.py --write
python v3/solve.py --validate
python v3/solve.py --evaluate

# CI gate (same steps, no writes)
python v3/render_taxonomy_docs.py --check
python v3/catalog_audit.py --check
python v3/fix_bare_urls.py
```
