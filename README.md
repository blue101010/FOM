# CTFT - Capture-The-Flag Techniques

An **ontology of CTF solving behaviour**: how a challenge author conceals a flag or artifact,
and how a solver recovers it.

Every entry **pairs**:

- a **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) - the concealment the author builds, and
- a **Resolution-Technique** (`CTFTCTE-<CAT>-NNN`) - the recovery that defeats it, split into:
  - **Offensive Recovery** - the CTF practitioner / solver, and
  - **Forensic Perspective** - the blue-team / DFIR analyst.

The pair is the editorial unit: nothing enters the catalogue as a concealment without a
documented recovery.

## Positioning

CTFT models **challenge-craft** - the forensic, cryptographic, steganographic and puzzle detail
that makes a CTF challenge solvable - at the level of a reusable, tool-independent solver action.

It **relates to** the existing standards without being derived from any of them, and it is not a
parallel ATT&CK:

| Framework | What it models | Role in CTFT |
| --- | --- | --- |
| MITRE ATT&CK | real adversary behaviour at campaign level | anchor, per entry |
| CAPEC / CWE | attack patterns and weaknesses | anchor, per entry |
| OWASP WSTG | versioned web test scenarios | anchor, per entry |
| STIX 2.1 | interchange format | export |

External identifiers are **anchors carried per entry with a confidence and a justification**, not
the definition of an entry. An entry is defined by the behaviour it names and by the challenges
that attest it - see [SCHEMA_V3.md](SCHEMA_V3.md) §8 for the promotion criteria. Every technique
and resolution-technique page carries its own `Related MITRE ATT&CK` table; the `ATT&CK` column on
a domain page is an orientation excerpt of those tables, nothing more.

Entries are described along axes that vary independently - **domain** (subject), **artifact**
(what the flag hides in), **format** (competition shape) and the player-objective axis, which is
deliberately still underived. Conflating the subject with the objective was the defect v3 exists
to fix.

## Nomenclature

| Object | ID format | Example |
| --- | --- | --- |
| Domain (category) | `CTFT-TA-<CAT>` | `CTFT-TA-FOR` |
| Design / Hide technique | `CTFTTE-<CAT>-NNN` | `CTFTTE-FOR-001` |
| Resolution-technique | `CTFTCTE-<CAT>-NNN` | `CTFTCTE-FOR-001` |

v3 vocabulary: what v1 called a *tactic* is a **domain** (a subject), and a *counter-technique* is
a **resolution-technique** (it *solves* a challenge, it does not *mitigate* a threat). The
identifiers, the file paths and the `countertechniques/` directory are unchanged - renaming them
would break every published link for no semantic gain. The player-objective axis that the word
"tactic" implies is tracked separately and is deliberately still underived; see
[SCHEMA_V3.md](SCHEMA_V3.md).

## Domains (19 active categories)

Order and short labels follow the challenge-category picker.

| # | Domain | Label | Name | HTB | Pairs |
| --- | --- | --- | --- | --- | --- |
| 1 | [CTFT-TA-FOR](tactics/CTFT-TA-FOR.md) | Forensics | Forensics | HTB: Forensics | 27 |
| 2 | [CTFT-TA-WEB](tactics/CTFT-TA-WEB.md) | Web | Web Exploitation | HTB: Web | 17 |
| 3 | [CTFT-TA-CRY](tactics/CTFT-TA-CRY.md) | Crypto | Cryptography | HTB: Crypto | 13 |
| 4 | [CTFT-TA-PWN](tactics/CTFT-TA-PWN.md) | Binary | Binary Exploitation | HTB: Pwn | 8 |
| 5 | [CTFT-TA-REV](tactics/CTFT-TA-REV.md) | Reverse | Reverse Engineering | HTB: Reversing | 9 |
| 6 | [CTFT-TA-STE](tactics/CTFT-TA-STE.md) | Stego | Steganography | HTB: Forensics/Misc (Stego) | 11 |
| 7 | [CTFT-TA-OSI](tactics/CTFT-TA-OSI.md) | OSINT | OSINT | HTB: OSINT | 8 |
| 8 | [CTFT-TA-CLD](tactics/CTFT-TA-CLD.md) | Cloud | Cloud | HTB: Cloud | 8 |
| 9 | [CTFT-TA-BLK](tactics/CTFT-TA-BLK.md) | Blockchain | Blockchain | HTB: Blockchain | 5 |
| 10 | [CTFT-TA-AIM](tactics/CTFT-TA-AIM.md) | AI/ML | AI / ML | HTB: AI-ML | 7 |
| 11 | [CTFT-TA-ICS](tactics/CTFT-TA-ICS.md) | ICS/SCADA | ICS / SCADA | HTB: ICS | 5 |
| 12 | [CTFT-TA-MOB](tactics/CTFT-TA-MOB.md) | Mobile | Mobile | HTB: Mobile | 5 |
| 13 | [CTFT-TA-JAL](tactics/CTFT-TA-JAL.md) | Jail escape | Jail / Sandbox Escape | HTB: Misc (Jail) | 6 |
| 14 | [CTFT-TA-GAM](tactics/CTFT-TA-GAM.md) | Game/Proto | Game / Protocol Automation | HTB: GamePwn | 6 |
| 15 | [CTFT-TA-COD](tactics/CTFT-TA-COD.md) | Coding | Coding / Programming Puzzle | HTB: Coding | 7 |
| 16 | [CTFT-TA-NET](tactics/CTFT-TA-NET.md) | Network | Network | HTB: Misc (Network) | 7 |
| 17 | [CTFT-TA-FPN](tactics/CTFT-TA-FPN.md) | Full Pwn | Full Pwn / Multi-Stage | HTB: Fullpwn | 10 |
| 18 | [CTFT-TA-HWR](tactics/CTFT-TA-HWR.md) | Hardware | Hardware | HTB: Hardware | 2 |
| 19 | [CTFT-TA-SDR](tactics/CTFT-TA-SDR.md) | SDR / RF | Software-Defined Radio | HTB: Hardware | 1 |
| | | | **Total** | | **162** |

**Retired:** `CTFT-TA-MSC` (Misc) is **removed**. It was a catch-all and every entry
it held duplicated a precise tactic. Do not create `MSC` entries; file the challenge
under `JAL` (jail/sandbox), `COD` (coding/esolang), `GAM` (game/protocol automation)
or `FPN` (multi-stage host compromise). The supersession map is in
[CORRELATION.md](CORRELATION.md#retired-categories).

## Layout

```
FOM/
  README.md                   this file
  CORRELATION.md              master technique ↔ counter-technique cross-reference - GENERATED
  HIERARCHY.md                flat design ↔ counter listing - GENERATED, local only (gitignored)
  index.json                  machine-readable index (pairs/by_id maps) - GENERATED
  SCHEMA_V3.md                active data model
  SCHEMA_V2.md                previous data model - frozen, kept for reproducibility
  LICENSE
  ctft-generator.py           guarded legacy fixture generator
  fom-migrate.py              migration utility
  v3/                         ACTIVE model layer - schemas, generators, typed objects
    render_taxonomy_docs.py   renders CORRELATION.md, HIERARCHY.md and the tactic pages
    catalog_audit.py          index, catalogue, relations, integrity + semantic lint
    render_stix.py            STIX 2.1 bundles from index.json
    build_evidence.py         seeds evidence.json from write-up links in the corpus
    solve.py                  retrieval engine, validation, precision@k
    core.json                 the 35-entry normative profile
    evidence.json             attestation records
    relations.json            derived `solves` + curated cross-domain edges
  v2/                         FROZEN reference slice - do not edit, do not run
  .github/workflows/ci.yml    catalogue gate (drift, integrity, lint, schemas, STIX)
  tactics/                    tactic pages (CTFT-TA-<CAT>.md), 19 active - GENERATED
  techniques/                 design/hide techniques (CTFTTE-<CAT>-NNN.md)
    subtechniques.md          sub-technique index
  countertechniques/          counter-techniques (CTFTCTE-<CAT>-NNN.md)
  tools/                      tool reference sheets
    tools.md                  tool index
    CTFTTOU-NNN.md            individual tool pages
  to_categorize/              staging area for uncategorized entries
  stix/
    ctft-bundle.json          full STIX 2.1 bundle
    by-category/              one STIX bundle per tactic (CTFT-<CAT>.json)
  backup/                     point-in-time snapshots of prior versions (untracked)
    deprecated-msc/           retired MSC entries, superseded by JAL/COD/GAM/FPN
    tactics/
    techniques/
    countertechniques/
    tools/
    to_categorize/
```

## Quick pair lookup example

| Technique | Hides | Counter-technique | Recovers |
| --- | --- | --- | --- |
| `CTFTTE-WEB-001` | Obscured endpoint / source-comment hiding | `CTFTCTE-WEB-001` | Content discovery and source review |
| `CTFTTE-FOR-001` | Magic-byte / file-signature tampering | `CTFTCTE-FOR-001` | Recover the legitimate file signature |

See [CORRELATION.md](CORRELATION.md) for the complete matrix.

## STIX 2.1 mapping

- Design technique  -> `attack-pattern` (kill_chain_name `ctft`, phase = domain), `x_ctft_role: design-hide`
- Counter-technique -> `course-of-action`, `x_ctft_role: resolution`
- Link              -> `relationship` of type `mitigates` **plus** `x_ctft_relation: "solves"`
- Domain            -> custom `x-ctft-tactic`
- ATT&CK anchor     -> `external_references[source_name: mitre-attack]`

`mitigates` is semantically wrong for a CTF - a counter-technique *solves* a puzzle, it does not
mitigate a threat - but it is kept so ATT&CK Navigator and OpenCTI can still read the graph;
`x_ctft_relation` carries the correct meaning.

IDs are deterministic (`uuid5`) and timestamps are fixed, so regenerating an unchanged corpus
produces no diff. Regenerate with `python v3/render_stix.py --write`.

## Catalogue integrity

The corpus contains **162 complete technique/counter-technique pairs** across 19 domains.
`CORRELATION.md`, `HIERARCHY.md` **and every tactic page** are generated, never hand-edited: the
markdown entry files are the source of truth, so a renamed technique cannot drift from the matrix.
After adding or renaming an entry:

```bash
python v3/render_taxonomy_docs.py --write
python v3/catalog_audit.py --write --write-index --write-catalog --write-relations --check
python v3/render_stix.py --write
```

The renderer refuses to run if a tactic directory is missing from its `CANONICAL_ORDER` list, or
if a retired tactic (`MSC`) reappears, so a new domain has to be declared deliberately rather than
drifting in. Generated documents carry a **corpus fingerprint** instead of a timestamp, so
`--check` detects real drift and an unchanged regeneration is a git no-op.

`--check` gates structural integrity (unpaired entries, matrix/index divergence), the relation
graph, and a semantic lint (tool names or implementation details in technique titles, placeholder
counter names, dangling evidence or core references).

### Maturity

One vocabulary, computed - never stored on an entry, so the catalogue and the evidence cannot
disagree:

| Maturity | Meaning | Count today |
| --- | --- | --- |
| `taxonomy_only` | identifiers and paired prose only | 155 |
| `attested` | >= 2 independent CTF events + curated positives, negatives, boundaries | 0 |
| `typed` | schema-valid typed objects, participates in retrieval | 7 |

No maturity level authorizes automatic execution. A consumer may display a tool reference or a
human-readable step; execution belongs to a separately authorized laboratory runner.

### Known coverage debt

- **Evidence is the bottleneck.** 238 of 324 entry files still carry the `Add challenge write-up
  link` marker, and the 35-entry core profile (`v3/core.json`) has 0 entries backed by two
  independent CTF events - across the whole corpus only `FOR-008` cites two distinct CTFs. The
  promotion pipeline is built and enforced; what is missing is collected evidence.
- **`v3/holdout.json` is empty**, so `precision@k` is undefined. A case may only be added if its
  write-up was not used while curating the technique it targets - otherwise the metric measures
  memorisation.
- **The resolution-tactic axis is underived** (`v3/tactic_map.json`, `status: "underived"`). The
  six candidate objectives are a hypothesis to test against labelled evidence, not a decision.

## License

Recommended: BSD-2-Clause
