# ICS — ICS / SCADA

> **Tactic ID:** `CTFT-TA-ICS`  
> **HTB mapping:** HTB: ICS  
> **Techniques:** 5

## Description

Industrial-protocol register/memory hiding and protocol-level extraction.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-ICS-001](../techniques/CTFTTE-ICS-001.md) | Modbus holding-register concealment | [CTFTCTE-ICS-001](../countertechniques/CTFTCTE-ICS-001.md) | Read Modbus registers | No direct ATT&CK technique |
| [CTFTTE-ICS-002](../techniques/CTFTTE-ICS-002.md) | S7comm PLC memory hiding | [CTFTCTE-ICS-002](../countertechniques/CTFTCTE-ICS-002.md) | Read S7 data blocks | No direct ATT&CK technique. |
| [CTFTTE-ICS-003](../techniques/CTFTTE-ICS-003.md) | Proprietary-protocol capture concealment | [CTFTCTE-ICS-003](../countertechniques/CTFTCTE-ICS-003.md) | Dissect industrial protocol captures | No direct ATT&CK technique. |
| [CTFTTE-ICS-004](../techniques/CTFTTE-ICS-004.md) | HMI project-file secrets | [CTFTCTE-ICS-004](../countertechniques/CTFTCTE-ICS-004.md) | Parse HMI/SCADA project files | No direct ATT&CK technique. |
| [CTFTTE-ICS-005](../techniques/CTFTTE-ICS-005.md) | DNP3 / BACnet object enumeration | [CTFTCTE-ICS-005](../countertechniques/CTFTCTE-ICS-005.md) | Enumerate protocol objects | No direct ATT&CK technique. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
