# CTFT / FOM — Proposed v2 Schema

> Status: **proposal with a curated Forensics reference slice**. Turns the three v2 upgrades
> — *execution semantics*, *case-based retrieval*, *agent-grade interoperability* — into a
> concrete, machine-checkable data model.
> Backward compatible: every v1.1 ID (`CTFTTE-*`, `CTFTCTE-*`, `CTFT-TA-*`) survives unchanged as a
> stable primary key. v2 does not rewrite the corpus; it *promotes* each prose entry into a typed
> object and adds two new layers on top.

---

## 1. What changes vs. v1.1

| Layer | v1.1 (today) | v2 (proposed) |
|---|---|---|
| **Knowledge** | prose `.md` per technique/counter; `index.json` pairs of `{id,name,path}` | same entries, but each carries a **structured body** (front-matter JSON) with execution semantics |
| **Retrieval** | browse by tactic | **Fingerprint** objects: map observed evidence → ranked candidate techniques |
| **Interop** | STIX export (IDs + relationships) | **Playbook / Step / Tool / SolverState** contracts: typed IO, tool bindings, replayable state |

The model is layered so each can ship independently:

```
Layer 0  Taxonomy        tactic, technique, counter        (v1.1 — keep)
Layer 1  Execution       playbook, step, indicator, tool   (upgrade #1)
Layer 2  Retrieval       fingerprint, symptom-vector       (upgrade #2)
Layer 3  Agent runtime   solver-state, evidence, verdict   (upgrade #3)
```

All objects are JSON Schema **draft 2020-12**. Every object has `schema_version: "2.0"` and a stable
`id`. Until a pair is curated, its Markdown remains the editorial source for taxonomy and the generated
`v2/catalog.json` records it as `taxonomy_only`. A pair becomes source-of-truth v2 only when its typed
objects validate. Markdown generation from v2 is a future migration, not a claim about the current corpus.

### 1.1 Catalogue integrity and maturity

`v2/catalog_audit.py` generates three offline artefacts from the local repository:

- `catalog_manifest.json`: hashes, counts and discrepancies across files, `CORRELATION.md`,
  `index.json` and STIX;
- `catalog.json`: every complete technique/counter-technique pair, including its maturity;
- `curation_queue.json`: the explicit backlog of fields needed before a pair becomes a typed
  recommendation candidate.

The maturity vocabulary is deliberately narrow:

| Maturity | Meaning |
| --- | --- |
| `taxonomy_only` | Stable identifiers and paired prose exist, but no reviewed typed indicators, preconditions, tool bindings and evaluation case exist. |
| `typed` | The pair has schema-valid typed objects and can participate in deterministic retrieval. |

Neither level authorizes automatic execution. A consumer may display a tool reference or a
human-readable step, but execution belongs to a separately authorized laboratory runner.

---

## 2. Envelope

`index.json` (v2) becomes a manifest of typed collections rather than one flat pair list:

```json
{
  "model": "CTFT",
  "schema_version": "2.0",
  "generated": "2026-07-11T00:00:00Z",
  "complements": ["MITRE ATT&CK", "Sigma"],
  "collections": {
    "tactics":      { "path": "v2/tactics.json",      "count": 14 },
    "techniques":   { "path": "v2/techniques.json",   "count": 82 },
    "playbooks":    { "path": "v2/playbooks.json",    "count": 82 },
    "indicators":   { "path": "v2/indicators.json",   "count": 140 },
    "tools":        { "path": "v2/tools.json",        "count": 60 },
    "fingerprints": { "path": "v2/fingerprints.json", "count": 40 }
  },
  "$schemas": "v2/schemas/"
}
```

---

## 3. Layer 1 — Execution semantics (upgrade #1)

The counter-technique stops being a paragraph and becomes a **Playbook**: a small decision graph an
expert *or* agent can run. This is the core of the upgrade — it converts a catalog into a decision
engine.

### 3.1 `technique` (design/hide) — enriched

```jsonc
// techniques[*]  — schemas/technique.schema.json
{
  "id": "CTFTTE-FOR-001",                       // unchanged primary key
  "schema_version": "2.0",
  "name": "Magic-byte / file-signature tampering",
  "tactic": "CTFT-TA-FOR",
  "category": "FOR",
  "paired_counter": "CTFTCTE-FOR-001",
  "summary": "Author corrupts/swaps the file magic header so type detection and viewers fail.",
  "artifact_types": ["file", "image", "archive"], // what this hides inside (controlled vocab)
  "attack_complement": {                          // was free prose; now structured
    "closest": "T1027",
    "note": "ATT&CK omits the byte-level magic-header recovery detail."
  },
  "indicators": ["IND-FOR-magic-mismatch", "IND-FOR-ext-type-conflict"], // -> Layer 2 retrieval
  "difficulty": 2,                                // 1..5, author-effort / obscurity
  "prevalence": 0.7,                              // 0..1, how common in real CTFs (retrieval prior)
  "references": ["https://www.garykessler.net/library/file_sigs.html"]
}
```

### 3.2 `playbook` (the enriched counter-technique)

```jsonc
// playbooks[*]  — schemas/playbook.schema.json
{
  "id": "CTFTCTE-FOR-001",                        // unchanged primary key
  "schema_version": "2.0",
  "name": "Recover the legitimate file signature",
  "tactic": "CTFT-TA-FOR",
  "counters": "CTFTTE-FOR-001",

  // --- when should this fire? (indicators + preconditions) ---
  "triggers": {                                   // boolean expr over indicator ids
    "all_of": ["IND-FOR-magic-mismatch"],
    "any_of": ["IND-FOR-ext-type-conflict", "IND-FOR-file-cmd-unknown"],
    "none_of": []
  },
  "preconditions": [
    { "id": "have-raw-bytes", "desc": "Raw file is available for byte inspection" }
  ],

  // --- typed IO contract ---
  "inputs":  { "$ref": "#/io/file-artifact" },    // JSON Schema of accepted input
  "outputs": {                                    // JSON Schema of expected produced artifact(s)
    "type": "object",
    "properties": {
      "true_type": { "type": "string" },
      "patched_file": { "type": "string", "description": "path to repaired artifact" }
    },
    "required": ["true_type"]
  },

  // --- the decision graph ---
  "steps": [
    {
      "id": "s1-detect",
      "action": "Compare leading bytes against a signature table.",
      "tool": "TOOL-file",
      "produces": ["observed_magic", "declared_ext"],
      "validates": "observed_magic != expected(declared_ext)",
      "on_true": "s2-identify",
      "on_false": "FALLBACK"                       // signature intact -> different technique
    },
    {
      "id": "s2-identify",
      "action": "Identify true type from internal structure/footers.",
      "tool": "TOOL-binwalk",
      "produces": ["true_type"],
      "on_true": "s3-patch",
      "on_false": "s3-patch"
    },
    {
      "id": "s3-patch",
      "action": "Patch header with hex editor / python struct to the true signature.",
      "tool": "TOOL-python-struct",
      "produces": ["patched_file"],
      "success_when": "file(patched_file) == true_type"
    }
  ],

  // --- scoring / planning knobs for the agent ---
  "priority": 8,                                  // 1..10 default ordering when multiple fire
  "cost": "low",                                  // low|medium|high  (time/tooling)
  "automation": "full",                           // full|assisted|manual
  "confidence_prior": 0.75,                       // P(this is the path | triggers matched)
  "false_positives": [
    "Polyglot files legitimately carry two valid signatures (see CTFTTE-FOR appended-data)."
  ],
  "success_criteria": "Recovered file opens as its true type and yields the next artifact.",
  "fallbacks": ["CTFTCTE-FOR-appended-data", "CTFTCTE-STE-lsb"],  // next best playbooks
  "tools": ["TOOL-xxd", "TOOL-file", "TOOL-binwalk", "TOOL-python-struct"],
  "references": ["https://www.garykessler.net/library/file_sigs.html"]
}
```

Both **offensive** and **blue-team** framings from v1.1 are preserved as `perspectives[]` (omitted
above for brevity) so nothing in the current corpus is lost.

### 3.3 `indicator` — the observable that links evidence to technique

```jsonc
// indicators[*]  — schemas/indicator.schema.json
{
  "id": "IND-FOR-magic-mismatch",
  "schema_version": "2.0",
  "name": "File magic bytes do not match declared extension",
  "applies_to": ["file", "image", "archive"],
  "signal_type": "boolean",
  "detector": {                                   // how an agent computes it (Sigma-like)
    "method": "tool",
    "tool": "TOOL-file",
    "expr": "file(x).type != mimetype_of(extension(x))"
  },
  "weight": 0.9                                    // contribution to candidate ranking
}
```

### 3.4 `tool` — the invocation contract

```jsonc
// tools[*]  — schemas/tool.schema.json
{
  "id": "TOOL-binwalk",
  "schema_version": "2.0",
  "name": "binwalk",
  "kind": "cli",
  "platforms": ["linux", "wsl", "macos"],
  "install": "pip install binwalk",
  "invocation": {                                 // templated; agent fills params
    "cmd": "binwalk --extract {file}",
    "params": { "file": { "type": "string", "required": true } }
  },
  "input_types": ["file"],
  "output_parser": {                              // how to turn stdout into typed evidence
    "format": "regex-lines",
    "captures": { "offset": "^(\\d+)", "type": "\\s+(\\w[\\w ]+)$" }
  },
  "produces": ["embedded_files", "true_type"]
}
```

---

## 4. Layer 2 — Case-based retrieval (upgrade #2)

A **Fingerprint** is a *query* built from what the solver has observed. It is not authored per
technique; it is the shape of a challenge. Ranking is derived: match the fingerprint's evidence
against every technique's `indicators` (weighted).

```jsonc
// fingerprint (query object)  — schemas/fingerprint.schema.json
{
  "schema_version": "2.0",
  "artifact_type": "image",           // controlled vocab: file|image|archive|binary|web|contract|pcap|...
  "protocol": null,                   // http|tls|dns|... when relevant
  "runtime": null,                    // js|python|jvm|evm|elf|pe|apk|...
  "protections": ["corrupted-magic"], // observed defenses
  "hints": ["'look closer'"],         // author text/hints
  "evidence": [                       // raw observations already extracted
    { "indicator": "IND-FOR-magic-mismatch", "value": true },
    { "indicator": "IND-FOR-abnormal-eof-size", "value": true }
  ]
}
```

**Retrieval contract** (`GET candidates(fingerprint) -> ranked[]`), computed, not stored:

```jsonc
{
  "query": { "artifact_type": "image", "protections": ["corrupted-magic"] },
  "candidates": [
    { "technique": "CTFTTE-FOR-001", "playbook": "CTFTCTE-FOR-001", "score": 0.91,
      "why": ["IND-FOR-magic-mismatch(0.9)", "prevalence(0.7)"] },
    { "technique": "CTFTTE-FOR-appended", "playbook": "CTFTCTE-FOR-appended", "score": 0.62,
      "why": ["IND-FOR-abnormal-eof-size(0.6)"] },
    { "technique": "CTFTTE-STE-001", "playbook": "CTFTCTE-STE-001", "score": 0.30,
      "why": ["artifact_type=image prior"] }
  ]
}
```

Score = `Σ(indicator.weight · evidence_match) · technique.prevalence`, normalized 0..1. This is the
cross-category reasoning layer that lets an agent go from *symptoms* → *ranked next test* without
browsing tactics. It deliberately crosses tactic boundaries (Forensics + Steganography above).

---

## 5. Layer 3 — Agent runtime contract (upgrade #3)

STIX gives portable IDs; it does not give a *solver loop*. `SolverState` is the replayable memory an
autonomous agent reads and writes as it works a single challenge.

```jsonc
// solver-state  — schemas/solver-state.schema.json
{
  "schema_version": "2.0",
  "challenge_id": "ctf2026-forensics-03",
  "fingerprint": { "...": "see §4" },
  "evidence": {                                    // append-only observation store
    "observed_magic": "00 00 00 00",
    "true_type": "PNG"
  },
  "attempts": [                                    // what was tried — prevents loops
    { "step": "CTFTCTE-FOR-001/s1-detect", "outcome": "success", "at": "T+00:02" },
    { "step": "CTFTCTE-FOR-001/s3-patch",  "outcome": "success", "at": "T+00:05" }
  ],
  "ruled_out": [                                    // negative knowledge — why a path is dead
    { "technique": "CTFTTE-STE-001", "reason": "LSB extraction produced high-entropy noise" }
  ],
  "beliefs": [                                      // live confidence, updated each step
    { "technique": "CTFTTE-FOR-001", "confidence": 0.95 }
  ],
  "next": [                                         // planner output
    { "playbook": "CTFTCTE-FOR-001", "step": "s3-patch", "expected": "patched_file" }
  ],
  "status": "in_progress"                           // in_progress|solved|stuck|abandoned
}
```

**Loop contract** an agent implements against the model:

```
1. observe   -> compute indicators -> update fingerprint.evidence
2. retrieve  -> candidates(fingerprint)                    (§4)
3. select    -> highest score not in attempts/ruled_out
4. execute   -> run playbook.steps via tool bindings       (§3)
5. update    -> append evidence/attempts; adjust beliefs
6. branch    -> on_true/on_false/fallbacks; goto 1 until status=solved
```

---

## 6. Worked example — the two cases from the brief

**Case A — "suspicious image, corrupted magic bytes."**
`fingerprint{artifact_type:image, protections:[corrupted-magic], evidence:[magic-mismatch, abnormal-eof]}`
→ `candidates()` returns `CTFTTE-FOR-001 (0.91)` over `appended-data (0.62)` over `LSB (0.30)`.
Agent runs `CTFTCTE-FOR-001` steps `s1→s2→s3`, writes `true_type=PNG`, `patched_file`, records the
attempt, and if the repaired PNG still hides data, `fallbacks` route it to `CTFTCTE-STE-lsb`.

**Case B — "web challenge, minified JS, no source map, hidden API calls."**
`fingerprint{artifact_type:web, runtime:js, protections:[minified,eval], evidence:[hidden-endpoints]}`
→ top candidate `CTFTCTE-WEB-006 (Deobfuscate & dynamically analyze JS)` whose playbook is
`beautify → extract-endpoints → runtime-hook → replay-requests`, each step bound to a tool with typed
output — exactly the compact playbook the brief asked for.

---

## 7. Migration path (non-breaking)

1. **Generate, don't rewrite.** Extend `ctft-generator.py` to emit `v2/*.json` from the existing
   `.md` corpus + a small per-entry YAML front-matter block authors fill in incrementally.
2. **Seed indicators/tools** from the `Tools` sections already in every file (they map 1:1 to
   `TOOL-*`). This bootstraps ~60 tool objects for free.
3. **Backfill priority order:** high-prevalence tactics first (FOR=17, STE=8, WEB=6).
4. **Keep STIX export.** Add `x-ctft-playbook`, `x-ctft-indicator` custom SDOs so the graph stays
   portable; `steps`/`beliefs` live in the JSON contract, not STIX.
5. **Validation in CI:** `schemas/*.schema.json` + a linter asserting every `technique.indicators`
   resolves, every `playbook.tools` resolves, and every `step.on_*` targets an existing step id.

---

## 8. Minimum viable v2

If shipping incrementally, the highest-leverage slice is **Layer 1 + the indicator link**: add
`triggers`, `steps`, `priority`, `fallbacks` to counters and `indicators` to techniques. That alone
makes the model agent-runnable; Layers 2–3 are then thin computed views over it.
```
