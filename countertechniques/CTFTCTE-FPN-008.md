# CTFTCTE-FPN-008 — Enumerate and chain Linux privesc vectors

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-008`](../techniques/CTFTTE-FPN-008.md) — Linux local privesc chain (SUID, ACLs, sudo, capabilities)

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate privesc vectors (linpeas), exploit one or chain several, and read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Privilege-boundary audits list SUID/capability drift; escalation paths leave execve logs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Escalation exploitation. |
| T1548 | Abuse Elevation Control Mechanism | SUID/sudo/capability abuse. |

## Tools

- linpeas
- pspy
- GTFOBins

## References

- <https://gtfobins.github.io/>

