# CTFT - Capture-The-Flag Techniques

A MITRE ATT&CK-**complementary** knowledge base of specialized CTF techniques.

Every entry **pairs**:

- a **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) - how a challenge author conceals a flag or artifact, and
- a **Counter-Technique** (`CTFTCTE-<CAT>-NNN`) - how it is recovered, split into:
  - **Offensive Recovery** - the CTF practitioner / solver, and
  - **Forensic Perspective** - the blue-team / DFIR analyst.

CTFT does **not** duplicate MITRE ATT&CK: every technique **and** counter-technique page
carries a `Related MITRE ATT&CK` table listing potentially related ATT&CK techniques with a
*complementarity* note — the CTF-specific (forensic / cryptographic / steganographic /
puzzle-craft) detail ATT&CK omits, and the nearest ATT&CK anchor where one exists.

## Nomenclature

| Object | ID format | Example |
| --- | --- | --- |
| Tactic (category) | `CTFT-TA-<CAT>` | `CTFT-TA-FOR` |
| Design / Hide technique | `CTFTTE-<CAT>-NNN` | `CTFTTE-FOR-001` |
| Counter-technique | `CTFTCTE-<CAT>-NNN` | `CTFTCTE-FOR-001` |

## Tactics (19 active categories)

Order and short labels follow the challenge-category picker.

| # | Tactic | Label | Name | HTB | Pairs |
| --- | --- | --- | --- | --- | --- |
| 1 | [CTFT-TA-FOR](tactics/CTFT-TA-FOR.md) | Forensics | Forensics | HTB: Forensics | 26 |
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
| | | | **Total** | | **161** |

**Retired:** `CTFT-TA-MSC` (Misc) is **removed**. It was a catch-all and every entry
it held duplicated a precise tactic. Do not create `MSC` entries; file the challenge
under `JAL` (jail/sandbox), `COD` (coding/esolang), `GAM` (game/protocol automation)
or `FPN` (multi-stage host compromise). The supersession map is in
[CORRELATION.md](CORRELATION.md#retired-categories).

## Layout

```
FOM/
  README.md                   this file
  HIERARCHY.md                full design ↔ counter listing
  CORRELATION.md              master technique ↔ counter-technique cross-reference
  index.json                  machine-readable index (pairs/by_id maps)
  ctft-generator.py           guarded legacy fixture generator
  fom-migrate.py              migration utility
  v2/render_taxonomy_docs.py  renders CORRELATION.md and HIERARCHY.md from the files
  v2/catalog_audit.py         synchronizes index.json and writes coverage manifest
  tactics/                    tactic pages (CTFT-TA-<CAT>.md), 19 active
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

- Design technique  -> `attack-pattern` (kill_chain_name `ctft`, phase = category)
- Counter-technique -> `course-of-action`
- Link              -> `relationship` of type `mitigates` (counter mitigates design)
- Tactic            -> custom `x-ctft-tactic`

IDs are deterministic (`uuid5`) so regeneration is stable and diff-friendly.

## Catalogue integrity

The corpus contains **161 complete technique/counter-technique pairs** across 19 active
tactics. `CORRELATION.md` and `HIERARCHY.md` are
**generated**, never hand-edited: the markdown entry files are the source of truth, so a
renamed technique can never drift from the matrix. After adding or renaming an entry:

```bash
python v2/render_taxonomy_docs.py --write
python v2/catalog_audit.py --write --write-index --write-catalog --check
```

The renderer refuses to run if a tactic directory is missing from its `CANONICAL_ORDER`
list, or if a retired tactic (`MSC`) reappears - so a new category has to be declared
deliberately rather than drifting in.

`--check` validates structural consistency only. It deliberately reports placeholders
and the smaller typed v2 slice as coverage debt until curated entries are available.
The legacy generator is guarded because its embedded 14-tactic corpus is incomplete;
use it only with `--legacy-rebuild` to generate an isolated fixture.

`catalog.json` contains every complete pair with a maturity marker. Only entries marked
`typed` have validated indicators and playbook metadata; entries marked `taxonomy_only`
remain discoverable but are not executable recommendations.

### Known coverage debt

- The STIX bundle under `stix/` predates the current corpus: it carries 63 pairs and 13
  tactics against the 105 pairs and 16 tactics in the markdown taxonomy. `MSC` has been
  purged from it, but it still needs a full regeneration from `index.json`.
- `CORRELATION.md` lists the pairs whose counter-technique does not answer the technique
  it is filed against, and the counters still named `Counter - <technique name>`. Both
  need an editorial pass on the entry content.

## License

Recommended: BSD-2-Clause
