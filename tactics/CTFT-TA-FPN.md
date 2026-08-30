# FPN — Full Pwn / Multi-Stage

> **Tactic ID:** `CTFT-TA-FPN`  
> **HTB mapping:** HTB: Fullpwn  
> **Techniques:** 10

## Description

Challenges that require a complete host or infrastructure compromise across multiple stages — reconnaissance, foothold, and privilege escalation — before the flag is reachable. This tactic is where CTFT most directly links to full ATT&CK kill-chain sequences.

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
| [CTFTTE-FPN-001](../techniques/CTFTTE-FPN-001.md) | Multi-stage chained challenge | [CTFTCTE-FPN-001](../countertechniques/CTFTCTE-FPN-001.md) | Chain enumeration, foothold and privilege escalation | Links to full ATT&CK chains. |
| [CTFTTE-FPN-002](../techniques/CTFTTE-FPN-002.md) | Windows Active Directory fullpwn | [CTFTCTE-FPN-002](../countertechniques/CTFTCTE-FPN-002.md) | Enumerate AD, abuse delegation or ACL paths to the DC | Complements TA0006, T1558 (Kerberoasting) with CTF AD-chain detail. |
| [CTFTTE-FPN-003](../techniques/CTFTTE-FPN-003.md) | Multi-hop network pivot | [CTFTCTE-FPN-003](../countertechniques/CTFTCTE-FPN-003.md) | Tunnel through compromised hosts to reach the flag | Complements T1572 (Protocol Tunneling) with CTF pivot detail. |
| [CTFTTE-FPN-004](../techniques/CTFTTE-FPN-004.md) | Container / service misconfiguration chain | [CTFTCTE-FPN-004](../countertechniques/CTFTCTE-FPN-004.md) | Chain service misconfig and container escape to host | Complements T1611 with multi-step CTF container-chain detail. |
| [CTFTTE-FPN-005](../techniques/CTFTTE-FPN-005.md) | Cloud-integrated fullpwn | [CTFTCTE-FPN-005](../countertechniques/CTFTCTE-FPN-005.md) | Pivot from on-prem to cloud IAM to retrieve the secret | Complements T1552.005 (Cloud Instance Metadata) with CTF pivot detail. |
| [CTFTTE-FPN-006](../techniques/CTFTTE-FPN-006.md) | Chained database trust-context escalation | [CTFTCTE-FPN-006](../countertechniques/CTFTCTE-FPN-006.md) | Map database trust contexts and privilege boundaries | CTF service-trust graph. |
| [CTFTTE-FPN-007](../techniques/CTFTTE-FPN-007.md) | Uninventoried dual-stack management path | [CTFTCTE-FPN-007](../countertechniques/CTFTCTE-FPN-007.md) | Reconcile dual-stack management exposure | CTF inventory-completeness condition. |
| [CTFTTE-FPN-008](../techniques/CTFTTE-FPN-008.md) | Linux local privesc chain (SUID, ACLs, sudo, capabilities) | [CTFTCTE-FPN-008](../countertechniques/CTFTCTE-FPN-008.md) | Enumerate and chain Linux privesc vectors | T1068 / T1548 |
| [CTFTTE-FPN-009](../techniques/CTFTTE-FPN-009.md) | Redis/NoSQL service misconfiguration chain | [CTFTCTE-FPN-009](../countertechniques/CTFTCTE-FPN-009.md) | Enumerate Redis/Mongo/MySQL, dump or RCE | T1213 |
| [CTFTTE-FPN-010](../techniques/CTFTTE-FPN-010.md) | Reverse-shell delivery & listener operations | [CTFTCTE-FPN-010](../countertechniques/CTFTCTE-FPN-010.md) | Catch, upgrade and persist reverse shells | T1059 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
