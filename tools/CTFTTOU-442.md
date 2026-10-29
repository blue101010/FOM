# CTFTTOU-442 — Caido workflow catalogue (caido-community/workflows)

> **Tool ID:** `CTFTTOU-442`  
> **Related techniques/counters:** CTFTTE-WEB-007, CTFTCTE-WEB-007, CTFTTE-WEB-009, CTFTCTE-WEB-009, CTFTTE-WEB-012, CTFTCTE-WEB-012, CTFTTE-WEB-023, CTFTCTE-WEB-023, CTFTTE-WEB-026, CTFTCTE-WEB-026

## Description

The rule set that turns a recording proxy into a **scanner**. A Caido instance
ships almost no detection logic on its own: the Findings panel is fed by
workflows (and by plugins), not by the traffic you happen to replay, so a fresh
install stays empty while looking busy with conversion codecs.

The catalogue collects one small workflow per signal class, and the value is the
**granularity**: each rule answers one question and reports under its own
reporter name, so a triage read is "which reporter fired once" rather than "is
anything in this scroll".

Three tiers, and only the first is free of effort:

- **passive** — runs on every response as it is proxied: flag and token shapes,
  secret prefixes, hostname echo, reflection, header hygiene, parameter classes.
  This is the tier that finds a signal buried in a bulk corpus.
- **active** — fired on demand against one request: schema introspection, CORS
  policy, WAF-bypass payload sizes, single-request scans.
- **convert** — codecs invoked from Replay; utility rather than detection.

Each workflow is a node graph plus a script. The catalogue is the graph; the
behaviour is the script, and the two are distributed separately — which is the
single most common reason an installed rule stays silent.

## URL

- <https://github.com/caido-community/workflows>
- <https://docs.caido.io/app/concepts/workflows>

## Installation

Two routes, and the first is the safe one:

1. **Store plugin.** Caido UI → Workflows → store/templates → install. The
   plugin compiles the script for you and is the reference behaviour.
2. **Scripted bulk import.** A local importer that clones the catalogue, injects
   each `javascript.ts` into the `code` input of its `definition.json`, and
   creates the workflow through the instance API. Idempotent: rerunning it
   repairs rather than duplicates.

```bash
# per-entry layout in the catalogue repository
packages/workflows/src/<slug>/definition.json   # node graph, ships with "code": ""
packages/workflows/src/<slug>/javascript.ts     # the actual rule
packages/workflows/src/<slug>/manifest.json     # name, kind, description
```

The install traps, in the order they bite:

- **`"code": ""` in `definition.json`.** Installed verbatim, the workflow is
  listed, enabled, and never fires. The script must be injected into the input
  whose alias is `code`.
- **The script must be an ES module exporting `run`.** `export async function
  run({request, response}, sdk)` produces a real `runState`; a bare declaration
  or a CommonJS assignment produces `runState: null` and a silent no-op.
- **Half the catalogue is real TypeScript.** Type annotations (`HttpInput`,
  `Record<string, any>`) are not valid JavaScript and surface as `Eval error` at
  run time; transpile before injecting.
- **Some entries are multi-file.** A `javascript.ts` that re-exports `./src`
  needs its whole folder bundled, not transpiled — the largest of them carries
  hundreds of kilobytes of pattern data.

## Usage

Rules only see **proxied** traffic. Traffic sent through a replay API bypasses
the workflow pipeline entirely, so the corpus has to be generated through the
proxy, and the scope has to name the challenge host — an unscoped passive rule
set spends its budget on fonts, analytics and CDN telemetry.

```bash
# validate a definition without touching the target: passive test on synthetic
# request/response (raw bodies are base64, connectionInfo is required)
testWorkflowPassive(definition, {raw: <b64>, connectionInfo: {host, port, isTLS}}, {raw: <b64>})
```

Authoring rules that decide whether a rule survives contact with a real target:

- `export async function run({request, response}, sdk)` only.
- Wrap every SDK call in `try/catch`: a throwing rule logs a runtime error and
  stops reporting without disabling itself.
- `request.getHeader("X")` returns an **array**.
- Always set `dedupeKey` in `sdk.findings.create({title, description, request,
  reporter, dedupeKey})`, otherwise every page load re-adds the same finding and
  the count stops meaning anything.
- One reporter per rule; triage by reporter is what makes a noisy catalogue
  usable.

## Related Techniques

CTFTTE-WEB-007, CTFTCTE-WEB-007, CTFTTE-WEB-009, CTFTCTE-WEB-009, CTFTTE-WEB-012,
CTFTCTE-WEB-012, CTFTTE-WEB-023, CTFTCTE-WEB-023, CTFTTE-WEB-026, CTFTCTE-WEB-026

## References

- <https://github.com/caido-community/workflows>
- <https://docs.caido.io/app/concepts/workflows>
- <https://docs.caido.io/app/concepts/findings>
