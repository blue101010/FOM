# CTFTCTE-FPN-002 — Enumerate AD, abuse delegation or ACL paths to the DC

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-002`](../techniques/CTFTTE-FPN-002.md) — Windows Active Directory fullpwn

---

## Offensive Recovery (CTF practitioner / solver)

Run BloodHound/SharpHound to map the AD graph; identify shortest attack paths (Kerberoastable service accounts, ACL GenericWrite, unconstrained delegation). Follow the path: crack the hash → lateral movement → DCSync or SeBackupPrivilege to dump NTDS.

## Forensic / Blue-Team Perspective (DFIR analyst)

BloodHound attack-path analysis is also a defensive tool; DFIR teams use it to identify the paths an attacker traversed and recommend ACL clean-up to prevent recurrence.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1558 | Steal or Forge Kerberos Tickets | AD ticket abuse. |
| T1482 | Domain Trust Discovery | Domain mapping. |

## Tools

- bloodhound / sharphound
- impacket
- kerbrute
- evil-winrm

## References

- https://github.com/BloodHoundAD/BloodHound
- https://github.com/fortra/impacket
- Add challenge write-up link
