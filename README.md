# CTFT - Capture-The-Flag Techniques

A MITRE ATT&CK-**complementary** knowledge base of specialized CTF techniques.

Every entry **pairs**:

- a **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) - how a challenge author conceals a flag or artifact, and
- a **Counter-Technique** (`CTFTCTE-<CAT>-NNN`) - how it is recovered, split into:
  - **Offensive Recovery** - the CTF practitioner / solver, and
  - **Forensic Perspective** - the blue-team / DFIR analyst.

CTFT does **not** duplicate MITRE ATT&CK: each technique carries an explicit *complementarity* note
explaining the CTF-specific (forensic / cryptographic / steganographic /
puzzle-craft) detail ATT&CK omits, and the nearest ATT&CK anchor where one exists.

## Nomenclature

| Object | ID format | Example |
| --- | --- | --- |
| Tactic (category) | `CTFT-TA-<CAT>` | `CTFT-TA-FOR` |
| Design / Hide technique | `CTFTTE-<CAT>-NNN` | `CTFTTE-FOR-001` |
| Counter-technique | `CTFTCTE-<CAT>-NNN` | `CTFTCTE-FOR-001` |

## Tactics (18 categories)

| Tactic | Name | HTB | Count |
| --- | --- | --- | --- |
| [CTFT-TA-WEB](tactics/CTFT-TA-WEB.md) | Web Exploitation | HTB: Web | 6 |
| [CTFT-TA-PWN](tactics/CTFT-TA-PWN.md) | Binary Exploitation | HTB: Pwn | 5 |
| [CTFT-TA-REV](tactics/CTFT-TA-REV.md) | Reverse Engineering | HTB: Reversing | 5 |
| [CTFT-TA-CRY](tactics/CTFT-TA-CRY.md) | Cryptography | HTB: Crypto | 6 |
| [CTFT-TA-FOR](tactics/CTFT-TA-FOR.md) | Forensics | HTB: Forensics | 17 |
| [CTFT-TA-STE](tactics/CTFT-TA-STE.md) | Steganography | HTB: Forensics/Misc (Stego) | 8 |
| [CTFT-TA-HWR](tactics/CTFT-TA-HWR.md) | Hardware | HTB: Hardware | 0 |
| [CTFT-TA-MOB](tactics/CTFT-TA-MOB.md) | Mobile | HTB: Mobile | 5 |
| [CTFT-TA-OSI](tactics/CTFT-TA-OSI.md) | OSINT | HTB: OSINT | 5 |
| [CTFT-TA-BLK](tactics/CTFT-TA-BLK.md) | Blockchain | HTB: Blockchain | 5 |
| [CTFT-TA-CLD](tactics/CTFT-TA-CLD.md) | Cloud | HTB: Cloud | 5 |
| [CTFT-TA-ICS](tactics/CTFT-TA-ICS.md) | ICS / SCADA | HTB: ICS | 5 |
| [CTFT-TA-AIM](tactics/CTFT-TA-AIM.md) | AI / ML | HTB: AI-ML | 5 |
| [CTFT-TA-JAL](tactics/CTFT-TA-JAL.md) | Jail / Sandbox Escape | HTB: Misc (Jail) | 5 |
| [CTFT-TA-COD](tactics/CTFT-TA-COD.md) | Coding / Programming Puzzle | HTB: Coding | 5 |
| [CTFT-TA-GAM](tactics/CTFT-TA-GAM.md) | Game / Protocol Automation | HTB: GamePwn | 5 |
| [CTFT-TA-FPN](tactics/CTFT-TA-FPN.md) | Full Pwn / Multi-Stage | HTB: Fullpwn | 5 |
| [CTFT-TA-MSC](tactics/CTFT-TA-MSC.md) | Misc / Jail / Coding / Fullpwn | HTB: Misc, Coding, GamePwn, Fullpwn | 5 |


## Layout

```
FOM/
  README.md                   this file
  HIERARCHY.md                full design ↔ counter listing
  CORRELATION.md              master technique ↔ counter-technique cross-reference
  index.json                  machine-readable index (pairs/by_id maps)
  ctft-generator.py           guarded legacy fixture generator
  v2/catalog_audit.py          synchronizes index.json and writes coverage manifest
  fom-migrate.py              migration utility
  tactics/                    18 tactic pages (CTFT-TA-<CAT>.md)
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
  backup/                     point-in-time snapshots of prior versions
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

The current corpus contains 18 tactics and 102 complete technique/counter-technique
pairs. Run the offline audit after editing taxonomy files; it generates a fingerprinted
manifest and synchronizes `index.json` without inventing entries:

```bash
python v2/catalog_audit.py --write --write-index --check
python v2/catalog_audit.py --write-catalog
```

`--check` validates structural consistency only. It deliberately reports placeholders
and the smaller typed v2 slice as coverage debt until curated entries are available.
The legacy generator is guarded because its embedded 14-tactic corpus is incomplete;
use it only with `--legacy-rebuild` to generate an isolated fixture.

`catalog.json` contains every complete pair with a maturity marker. Only entries marked
`typed` have validated indicators and playbook metadata; entries marked `taxonomy_only`
remain discoverable but are not executable recommendations.

## License

Recommended: BSD-2-Clause
