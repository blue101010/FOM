# ICS — ICS / SCADA

> **Domain ID:** `CTFT-TA-ICS`  
> **HTB mapping:** HTB: ICS  
> **Techniques:** 9

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
| [CTFTTE-ICS-006](../techniques/CTFTTE-ICS-006.md) | Physical controller-label default credentials | [CTFTCTE-ICS-006](../countertechniques/CTFTCTE-ICS-006.md) | Read the device label and vendor documentation for default credentials | T0859 |
| [CTFTTE-ICS-007](../techniques/CTFTTE-ICS-007.md) | Engineering-tool process takeover | [CTFTCTE-ICS-007](../countertechniques/CTFTCTE-ICS-007.md) | Connect the vendor engineering tool and drive the process | T0843, T0855 |
| [CTFTTE-ICS-008](../techniques/CTFTTE-ICS-008.md) | Industrial firewall weak credential behind a controller pivot | [CTFTCTE-ICS-008](../countertechniques/CTFTCTE-ICS-008.md) | Pivot through the controller and brute-force the firewall manager | T0859, T0886 |
| [CTFTTE-ICS-009](../techniques/CTFTTE-ICS-009.md) | Field-device identity takeover through MAC-addressed naming | [CTFTCTE-ICS-009](../countertechniques/CTFTCTE-ICS-009.md) | Map device names to MAC addresses and rename the target | T0855 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
