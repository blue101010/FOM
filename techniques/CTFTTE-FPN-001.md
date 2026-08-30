# CTFTTE-FPN-001 — Multi-stage chained challenge

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-001`](../countertechniques/CTFTCTE-FPN-001.md) — Chain enumeration, foothold and privilege escalation

---

## How the challenge author hides

The flag(s) require a full host compromise: external reconnaissance, initial foothold, and privilege escalation — each gate concealed by a separate vulnerability or design decision.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Initial access. |
| T1078 | Valid Accounts | Foothold and movement. |

## Tools

- nmap
- feroxbuster
- netexec
- linpeas / winpeas

## References

- Add challenge write-up link
