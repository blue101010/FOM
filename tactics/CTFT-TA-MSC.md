# MSC — Misc / Jail / Coding / Fullpwn

> **Tactic ID:** `CTFT-TA-MSC`  
> **HTB mapping:** HTB: Misc, Coding, GamePwn, Fullpwn  
> **Techniques:** 5

## Description

Escapes, automation and multi-stage chains that do not fit one category.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-MSC-001](../techniques/CTFTTE-MSC-001.md) | Python jail (pyjail) confinement | [CTFTCTE-MSC-001](../countertechniques/CTFTCTE-MSC-001.md) | Escape the Python sandbox | No ATT&CK equivalent. |
| [CTFTTE-MSC-002](../techniques/CTFTTE-MSC-002.md) | Restricted-shell confinement | [CTFTCTE-MSC-002](../countertechniques/CTFTCTE-MSC-002.md) | Escape the restricted shell | Complements T1059 conceptually with CTF restricted-shell-esc |
| [CTFTTE-MSC-003](../techniques/CTFTTE-MSC-003.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-MSC-003](../countertechniques/CTFTCTE-MSC-003.md) | Interpret or transpile the encoding | No ATT&CK equivalent. |
| [CTFTTE-MSC-004](../techniques/CTFTTE-MSC-004.md) | Networked game / protocol automation (GamePwn) | [CTFTCTE-MSC-004](../countertechniques/CTFTCTE-MSC-004.md) | Script a client to beat the protocol | No ATT&CK equivalent. |
| [CTFTTE-MSC-005](../techniques/CTFTTE-MSC-005.md) | Multi-stage chained challenge (Fullpwn) | [CTFTCTE-MSC-005](../countertechniques/CTFTCTE-MSC-005.md) | Chain enumeration, foothold and privilege escalation | This is where CTFT links to full ATT&CK chains |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
