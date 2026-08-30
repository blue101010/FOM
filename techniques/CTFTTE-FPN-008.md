# CTFTTE-FPN-008 — Linux local privesc chain (SUID, ACLs, sudo, capabilities)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-008`](../countertechniques/CTFTCTE-FPN-008.md) — Enumerate and chain Linux privesc vectors

---

## How the challenge author hides

The flag is root-only; escalation requires chaining SUID binaries, ACLs, sudo rules or capabilities.

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

- https://gtfobins.github.io/
- Add challenge write-up link
