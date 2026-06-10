# WEB — Web Exploitation

> **Tactic ID:** `CTFT-TA-WEB`  
> **HTB mapping:** HTB: Web  
> **Techniques:** 6

## Description

Hiding/recovering flags inside web applications, APIs and client-side code.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-WEB-001](../techniques/CTFTTE-WEB-001.md) | Obscured endpoint / source-comment hiding | [CTFTCTE-WEB-001](../countertechniques/CTFTCTE-WEB-001.md) | Content discovery and source review | Complements T1083/T1595 (discovery/recon) but is CTF content |
| [CTFTTE-WEB-002](../techniques/CTFTTE-WEB-002.md) | IDOR / predictable object obscurity | [CTFTCTE-WEB-002](../countertechniques/CTFTCTE-WEB-002.md) | Enumerate insecure direct object references | No direct ATT&CK technique |
| [CTFTTE-WEB-003](../techniques/CTFTTE-WEB-003.md) | JWT misconfiguration | [CTFTCTE-WEB-003](../countertechniques/CTFTCTE-WEB-003.md) | Forge or downgrade a JSON Web Token | No direct ATT&CK technique. |
| [CTFTTE-WEB-004](../techniques/CTFTTE-WEB-004.md) | Blind / WAF-evaded SQL injection | [CTFTCTE-WEB-004](../countertechniques/CTFTCTE-WEB-004.md) | Extract data via blind injection | No direct ATT&CK technique |
| [CTFTTE-WEB-005](../techniques/CTFTTE-WEB-005.md) | Server-side template injection | [CTFTCTE-WEB-005](../countertechniques/CTFTCTE-WEB-005.md) | Exploit template evaluation | No direct ATT&CK technique. |
| [CTFTTE-WEB-006](../techniques/CTFTTE-WEB-006.md) | Client-side obfuscated logic | [CTFTCTE-WEB-006](../countertechniques/CTFTCTE-WEB-006.md) | Deobfuscate and dynamically analyze JS | No direct ATT&CK technique. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
