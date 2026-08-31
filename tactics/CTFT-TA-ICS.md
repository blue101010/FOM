# ICS — ICS / SCADA

> **Domain ID:** `CTFT-TA-ICS`  
> **HTB mapping:** HTB: ICS  
> **Techniques:** 5

## Description

Industrial-protocol register/memory hiding and protocol-level extraction.

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
| [CTFTTE-ICS-001](../techniques/CTFTTE-ICS-001.md) | Modbus holding-register concealment | [CTFTCTE-ICS-001](../countertechniques/CTFTCTE-ICS-001.md) | Read Modbus registers | T0861 |
| [CTFTTE-ICS-002](../techniques/CTFTTE-ICS-002.md) | S7comm PLC memory hiding | [CTFTCTE-ICS-002](../countertechniques/CTFTCTE-ICS-002.md) | Read S7 data blocks | T0861 |
| [CTFTTE-ICS-003](../techniques/CTFTTE-ICS-003.md) | Proprietary-protocol capture concealment | [CTFTCTE-ICS-003](../countertechniques/CTFTCTE-ICS-003.md) | Dissect industrial protocol captures | T0842 |
| [CTFTTE-ICS-004](../techniques/CTFTTE-ICS-004.md) | HMI project-file secrets | [CTFTCTE-ICS-004](../countertechniques/CTFTCTE-ICS-004.md) | Parse HMI/SCADA project files | T0843 |
| [CTFTTE-ICS-005](../techniques/CTFTTE-ICS-005.md) | DNP3 / BACnet object enumeration | [CTFTCTE-ICS-005](../countertechniques/CTFTCTE-ICS-005.md) | Enumerate protocol objects | T0861 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
