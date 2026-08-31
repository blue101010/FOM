# GAM — Game / Protocol Automation (GamePwn)

> **Domain ID:** `CTFT-TA-GAM`  
> **HTB mapping:** HTB: GamePwn  
> **Techniques:** 6

## Description

Challenges built around a game binary or networked game server. The author hides the flag behind game mechanics that require automation, binary patching, memory manipulation, AI defeat, or protocol sequence exploitation rather than raw exploit code.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-GAM-001](../techniques/CTFTTE-GAM-001.md) | Networked game / protocol automation | [CTFTCTE-GAM-001](../countertechniques/CTFTCTE-GAM-001.md) | Script a client to beat the protocol | T1071 |
| [CTFTTE-GAM-002](../techniques/CTFTTE-GAM-002.md) | Game save-state / memory manipulation | [CTFTCTE-GAM-002](../countertechniques/CTFTCTE-GAM-002.md) | Hex-edit the save file or patch in-memory values | T1213 |
| [CTFTTE-GAM-003](../techniques/CTFTTE-GAM-003.md) | Bot-vs-AI / ML-opponent challenge | [CTFTCTE-GAM-003](../countertechniques/CTFTCTE-GAM-003.md) | Exploit AI weaknesses or craft adversarial inputs | — |
| [CTFTTE-GAM-004](../techniques/CTFTTE-GAM-004.md) | Game binary win-condition bypass | [CTFTCTE-GAM-004](../countertechniques/CTFTCTE-GAM-004.md) | Patch the jump / comparison to force a win state | T1055 |
| [CTFTTE-GAM-005](../techniques/CTFTTE-GAM-005.md) | Protocol sequence replay / race | [CTFTCTE-GAM-005](../countertechniques/CTFTCTE-GAM-005.md) | Record, replay, or race the server sequence precisely | T1071 |
| [CTFTTE-GAM-006](../techniques/CTFTTE-GAM-006.md) | Chatbot / choice-path bot puzzle | [CTFTCTE-GAM-006](../countertechniques/CTFTCTE-GAM-006.md) | Script a bot interaction to reach the win branch | T1071 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
