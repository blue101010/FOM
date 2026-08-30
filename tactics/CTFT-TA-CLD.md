# CLD — Cloud

> **Tactic ID:** `CTFT-TA-CLD`  
> **HTB mapping:** HTB: Cloud  
> **Techniques:** 8

## Description

Cloud misconfiguration concealment and enumeration-based recovery.

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
| [CTFTTE-CLD-001](../techniques/CTFTTE-CLD-001.md) | Misconfigured object-storage exposure | [CTFTCTE-CLD-001](../countertechniques/CTFTCTE-CLD-001.md) | Enumerate and list public buckets | Complements T1530 (Data from Cloud Storage) with CTF enumera |
| [CTFTTE-CLD-002](../techniques/CTFTTE-CLD-002.md) | Over-permissive IAM role | [CTFTCTE-CLD-002](../countertechniques/CTFTCTE-CLD-002.md) | Enumerate and assume reachable roles | Complements T1078.004 (Cloud Accounts) with CTF permission-m |
| [CTFTTE-CLD-003](../techniques/CTFTTE-CLD-003.md) | Instance metadata service exposure | [CTFTCTE-CLD-003](../countertechniques/CTFTCTE-CLD-003.md) | Retrieve credentials via SSRF to IMDS | Complements T1552.005 (Cloud Instance Metadata API) with the |
| [CTFTTE-CLD-004](../techniques/CTFTTE-CLD-004.md) | Secrets in function config / layers | [CTFTCTE-CLD-004](../countertechniques/CTFTCTE-CLD-004.md) | Dump serverless configuration and layers | No direct ATT&CK technique. |
| [CTFTTE-CLD-005](../techniques/CTFTTE-CLD-005.md) | Container image / registry leak | [CTFTCTE-CLD-005](../countertechniques/CTFTCTE-CLD-005.md) | Pull and inspect image layers | No direct ATT&CK technique. |
| [CTFTTE-CLD-006](../techniques/CTFTTE-CLD-006.md) | Cross-account role chaining / trust abuse | [CTFTCTE-CLD-006](../countertechniques/CTFTCTE-CLD-006.md) | Chain sts:AssumeRole across accounts | T1078.004 |
| [CTFTTE-CLD-007](../techniques/CTFTTE-CLD-007.md) | Cloud NoSQL-store misconfiguration | [CTFTCTE-CLD-007](../countertechniques/CTFTCTE-CLD-007.md) | Enumerate and query exposed cloud databases | T1213 |
| [CTFTTE-CLD-008](../techniques/CTFTTE-CLD-008.md) | Azure management-plane misconfiguration | [CTFTCTE-CLD-008](../countertechniques/CTFTCTE-CLD-008.md) | Enumerate Azure AD/VM/storage from credentials | T1078.004 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
