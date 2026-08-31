# AIM — AI / ML

> **Domain ID:** `CTFT-TA-AIM`  
> **HTB mapping:** HTB: AI-ML  
> **Techniques:** 7

## Description

Secrets inside models/prompts/serialized artifacts and their extraction.

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
| [CTFTTE-AIM-001](../techniques/CTFTTE-AIM-001.md) | Secret embedded in model weights | [CTFTCTE-AIM-001](../countertechniques/CTFTCTE-AIM-001.md) | Extract tensors and inspect weights | T1552 |
| [CTFTTE-AIM-002](../techniques/CTFTTE-AIM-002.md) | Prompt-injection-gated flag | [CTFTCTE-AIM-002](../countertechniques/CTFTCTE-AIM-002.md) | Extract the flag via crafted prompts | T1190 |
| [CTFTTE-AIM-003](../techniques/CTFTTE-AIM-003.md) | Adversarial-input requirement | [CTFTCTE-AIM-003](../countertechniques/CTFTCTE-AIM-003.md) | Generate an adversarial example | — |
| [CTFTTE-AIM-004](../techniques/CTFTTE-AIM-004.md) | Malicious / opaque serialized model | [CTFTCTE-AIM-004](../countertechniques/CTFTCTE-AIM-004.md) | Safely inspect serialized model files | T1190 |
| [CTFTTE-AIM-005](../techniques/CTFTTE-AIM-005.md) | Training-data leakage via queries | [CTFTCTE-AIM-005](../countertechniques/CTFTCTE-AIM-005.md) | Recover secrets through model inversion | T1213 |
| [CTFTTE-AIM-006](../techniques/CTFTTE-AIM-006.md) | Self-hosted LLM platform misconfiguration | [CTFTCTE-AIM-006](../countertechniques/CTFTCTE-AIM-006.md) | Audit ollama/oobabooga deployments for exposed endpoints | T1190 |
| [CTFTTE-AIM-007](../techniques/CTFTTE-AIM-007.md) | Agent / tool-calling guardrail bypass | [CTFTCTE-AIM-007](../countertechniques/CTFTCTE-AIM-007.md) | Bypass agent tool policies | — |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
