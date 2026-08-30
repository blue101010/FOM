# AIM — AI / ML

> **Tactic ID:** `CTFT-TA-AIM`  
> **HTB mapping:** HTB: AI-ML  
> **Techniques:** 5

## Description

Secrets inside models/prompts/serialized artifacts and their extraction.

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
| [CTFTTE-AIM-001](../techniques/CTFTTE-AIM-001.md) | Secret embedded in model weights | [CTFTCTE-AIM-001](../countertechniques/CTFTCTE-AIM-001.md) | Extract tensors and inspect weights | No ATT&CK equivalent. |
| [CTFTTE-AIM-002](../techniques/CTFTTE-AIM-002.md) | Prompt-injection-gated flag | [CTFTCTE-AIM-002](../countertechniques/CTFTCTE-AIM-002.md) | Extract the flag via crafted prompts | No ATT&CK equivalent |
| [CTFTTE-AIM-003](../techniques/CTFTTE-AIM-003.md) | Adversarial-input requirement | [CTFTCTE-AIM-003](../countertechniques/CTFTCTE-AIM-003.md) | Generate an adversarial example | No ATT&CK equivalent. |
| [CTFTTE-AIM-004](../techniques/CTFTTE-AIM-004.md) | Malicious / opaque serialized model | [CTFTCTE-AIM-004](../countertechniques/CTFTCTE-AIM-004.md) | Safely inspect serialized model files | Complements T1204/T1027 conceptually |
| [CTFTTE-AIM-005](../techniques/CTFTTE-AIM-005.md) | Training-data leakage via queries | [CTFTCTE-AIM-005](../countertechniques/CTFTCTE-AIM-005.md) | Recover secrets through model inversion | No ATT&CK equivalent. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
