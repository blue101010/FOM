# CLD — Cloud

> **Domain ID:** `CTFT-TA-CLD`  
> **HTB mapping:** HTB: Cloud  
> **Techniques:** 8

## Description

Cloud misconfiguration concealment and enumeration-based recovery.

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
| [CTFTTE-CLD-001](../techniques/CTFTTE-CLD-001.md) | Misconfigured object-storage exposure | [CTFTCTE-CLD-001](../countertechniques/CTFTCTE-CLD-001.md) | Enumerate and list public buckets | T1530 |
| [CTFTTE-CLD-002](../techniques/CTFTTE-CLD-002.md) | Over-permissive IAM role | [CTFTCTE-CLD-002](../countertechniques/CTFTCTE-CLD-002.md) | Enumerate and assume reachable roles | T1078.004 |
| [CTFTTE-CLD-003](../techniques/CTFTTE-CLD-003.md) | Instance metadata service exposure | [CTFTCTE-CLD-003](../countertechniques/CTFTCTE-CLD-003.md) | Retrieve credentials via SSRF to IMDS | T1552.005 |
| [CTFTTE-CLD-004](../techniques/CTFTTE-CLD-004.md) | Secrets in function config / layers | [CTFTCTE-CLD-004](../countertechniques/CTFTCTE-CLD-004.md) | Dump serverless configuration and layers | T1552 |
| [CTFTTE-CLD-005](../techniques/CTFTTE-CLD-005.md) | Container image / registry leak | [CTFTCTE-CLD-005](../countertechniques/CTFTCTE-CLD-005.md) | Pull and inspect image layers | T1613 |
| [CTFTTE-CLD-006](../techniques/CTFTTE-CLD-006.md) | Cross-account role chaining / trust abuse | [CTFTCTE-CLD-006](../countertechniques/CTFTCTE-CLD-006.md) | Chain sts:AssumeRole across accounts | T1078.004 |
| [CTFTTE-CLD-007](../techniques/CTFTTE-CLD-007.md) | Cloud NoSQL-store misconfiguration | [CTFTCTE-CLD-007](../countertechniques/CTFTCTE-CLD-007.md) | Enumerate and query exposed cloud databases | T1213 |
| [CTFTTE-CLD-008](../techniques/CTFTTE-CLD-008.md) | Azure management-plane misconfiguration | [CTFTCTE-CLD-008](../countertechniques/CTFTCTE-CLD-008.md) | Enumerate Azure AD/VM/storage from credentials | T1078.004 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
