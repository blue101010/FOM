# FPN — Full Pwn / Multi-Stage

> **Domain ID:** `CTFT-TA-FPN`  
> **HTB mapping:** HTB: Fullpwn  
> **Techniques:** 10

## Description

Challenges that require a complete host or infrastructure compromise across multiple stages — reconnaissance, foothold, and privilege escalation — before the flag is reachable. The flag is reachable only at the end of the chain, so no single technique solves the challenge.

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
| [CTFTTE-FPN-001](../techniques/CTFTTE-FPN-001.md) | Multi-stage chained challenge | [CTFTCTE-FPN-001](../countertechniques/CTFTCTE-FPN-001.md) | Chain enumeration, foothold and privilege escalation | T1190, T1078 |
| [CTFTTE-FPN-002](../techniques/CTFTTE-FPN-002.md) | Windows Active Directory fullpwn | [CTFTCTE-FPN-002](../countertechniques/CTFTCTE-FPN-002.md) | Enumerate AD, abuse delegation or ACL paths to the DC | T1558, T1482 |
| [CTFTTE-FPN-003](../techniques/CTFTTE-FPN-003.md) | Multi-hop network pivot | [CTFTCTE-FPN-003](../countertechniques/CTFTCTE-FPN-003.md) | Tunnel through compromised hosts to reach the flag | T1572, T1090 |
| [CTFTTE-FPN-004](../techniques/CTFTTE-FPN-004.md) | Container / service misconfiguration chain | [CTFTCTE-FPN-004](../countertechniques/CTFTCTE-FPN-004.md) | Chain service misconfig and container escape to host | T1611, T1190 |
| [CTFTTE-FPN-005](../techniques/CTFTTE-FPN-005.md) | Cloud-integrated fullpwn | [CTFTCTE-FPN-005](../countertechniques/CTFTCTE-FPN-005.md) | Pivot from on-prem to cloud IAM to retrieve the secret | T1078.004, T1552.005 |
| [CTFTTE-FPN-006](../techniques/CTFTTE-FPN-006.md) | Chained database trust-context escalation | [CTFTCTE-FPN-006](../countertechniques/CTFTCTE-FPN-006.md) | Map database trust contexts and privilege boundaries | T1213 |
| [CTFTTE-FPN-007](../techniques/CTFTTE-FPN-007.md) | Uninventoried dual-stack management path | [CTFTCTE-FPN-007](../countertechniques/CTFTCTE-FPN-007.md) | Reconcile dual-stack management exposure | T1083 |
| [CTFTTE-FPN-008](../techniques/CTFTTE-FPN-008.md) | Linux local privesc chain (SUID, ACLs, sudo, capabilities) | [CTFTCTE-FPN-008](../countertechniques/CTFTCTE-FPN-008.md) | Enumerate and chain Linux privesc vectors | T1068, T1548 |
| [CTFTTE-FPN-009](../techniques/CTFTTE-FPN-009.md) | Redis/NoSQL service misconfiguration chain | [CTFTCTE-FPN-009](../countertechniques/CTFTCTE-FPN-009.md) | Enumerate Redis/Mongo/MySQL, dump or RCE | T1213 |
| [CTFTTE-FPN-010](../techniques/CTFTTE-FPN-010.md) | Reverse-shell delivery & listener operations | [CTFTCTE-FPN-010](../countertechniques/CTFTCTE-FPN-010.md) | Catch, upgrade and persist reverse shells | T1059 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
