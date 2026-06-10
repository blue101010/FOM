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

## Tactics (17 HackTheBox categories)

| Tactic | Name | HTB | Count |
| --- | --- | --- | --- |
| [CTFT-TA-WEB](tactics/CTFT-TA-WEB.md) | Web Exploitation | HTB: Web | 6 |
| [CTFT-TA-PWN](tactics/CTFT-TA-PWN.md) | Binary Exploitation | HTB: Pwn | 5 |
| [CTFT-TA-REV](tactics/CTFT-TA-REV.md) | Reverse Engineering | HTB: Reversing | 5 |
| [CTFT-TA-CRY](tactics/CTFT-TA-CRY.md) | Cryptography | HTB: Crypto | 6 |
| [CTFT-TA-FOR](tactics/CTFT-TA-FOR.md) | Forensics | HTB: Forensics | 6 |
| [CTFT-TA-STE](tactics/CTFT-TA-STE.md) | Steganography | HTB: Forensics/Misc (Stego) | 5 |
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


## Layout

```
CTFT/
  README.md
  HIERARCHY.md          full design<->counter listing
  CORRELATION.md        master technique <-> counter-technique cross-reference
  index.json            machine-readable index (includes pairs/by_id maps)
  tactics/              tactic pages (CTFT-TA-<CAT>.md)
  techniques/           design/hide techniques (CTFTTE-<CAT>-NNN.md)
  countertechniques/    counter-techniques   (CTFTCTE-<CAT>-NNN.md)
  stix/
    ctft-bundle.json    full STIX 2.1 bundle
    by-category/        one STIX bundle per tactic
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

## License

Recommended: BSD-2-Clause
