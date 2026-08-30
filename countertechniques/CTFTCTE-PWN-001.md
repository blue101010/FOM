# CTFTCTE-PWN-001 — Redirect execution to the win function

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-001`](../techniques/CTFTTE-PWN-001.md) — Hidden win-function backdoor

---

## Offensive Recovery (CTF practitioner / solver)

Overflow saved control data and redirect execution (ret2win), defeating any leak/canary first.

## Forensic / Blue-Team Perspective (DFIR analyst)

The exploit path documents the missing bounds check enabling control-flow hijack.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Win-function backdoors echo privilege-escalation exploitation. |

## Tools

- pwntools
- GDB+pwndbg
- checksec
- ROPgadget

## References

- https://github.com/Gallopsled/pwntools
- Add challenge write-up link