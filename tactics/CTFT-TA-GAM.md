# GAM — Game / Protocol Automation (GamePwn)

> **Tactic ID:** `CTFT-TA-GAM`  
> **HTB mapping:** HTB: GamePwn  
> **Techniques:** 5

## Description

Challenges built around a game binary or networked game server. The author hides the flag behind game mechanics that require automation, binary patching, memory manipulation, AI defeat, or protocol sequence exploitation rather than raw exploit code.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-GAM-001](../techniques/CTFTTE-GAM-001.md) | Networked game / protocol automation | [CTFTCTE-GAM-001](../countertechniques/CTFTCTE-GAM-001.md) | Script a client to beat the protocol | No ATT&CK equivalent. |
| [CTFTTE-GAM-002](../techniques/CTFTTE-GAM-002.md) | Game save-state / memory manipulation | [CTFTCTE-GAM-002](../countertechniques/CTFTCTE-GAM-002.md) | Hex-edit the save file or patch in-memory values | No ATT&CK equivalent. |
| [CTFTTE-GAM-003](../techniques/CTFTTE-GAM-003.md) | Bot-vs-AI / ML-opponent challenge | [CTFTCTE-GAM-003](../countertechniques/CTFTCTE-GAM-003.md) | Exploit AI weaknesses or craft adversarial inputs | No ATT&CK equivalent. |
| [CTFTTE-GAM-004](../techniques/CTFTTE-GAM-004.md) | Game binary win-condition bypass | [CTFTCTE-GAM-004](../countertechniques/CTFTCTE-GAM-004.md) | Patch the jump / comparison to force a win state | Complements T1027 with CTF binary-patching detail. |
| [CTFTTE-GAM-005](../techniques/CTFTTE-GAM-005.md) | Protocol sequence replay / race | [CTFTCTE-GAM-005](../countertechniques/CTFTCTE-GAM-005.md) | Record, replay, or race the server sequence precisely | No ATT&CK equivalent. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
