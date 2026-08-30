# CTFTTE-PWN-001 — Hidden win-function backdoor

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-001`](../countertechniques/CTFTCTE-PWN-001.md) — Redirect execution to the win function

---

## How the challenge author hides

An unreferenced function prints the flag/spawns a shell, gated behind a vulnerable input.

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

- <https://github.com/Gallopsled/pwntools>
- Add challenge write-up link