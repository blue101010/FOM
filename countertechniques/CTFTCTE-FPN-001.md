# CTFTCTE-FPN-001 — Chain enumeration, foothold and privilege escalation

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-001`](../techniques/CTFTTE-FPN-001.md) — Multi-stage chained challenge

---

## Offensive Recovery (CTF practitioner / solver)

Run port and service enumeration, exploit the exposed service for a foothold, then run local enumeration scripts (linpeas/winpeas) to identify the privilege-escalation path. Chain each stage methodically until the root/administrator flag is reached.

## Forensic / Blue-Team Perspective (DFIR analyst)

The full chain documents the complete attack path; DFIR reconstruction uses log correlation across each stage to build a timeline, and each CTFT entry in the chain links to the relevant ATT&CK technique for structured reporting.

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
