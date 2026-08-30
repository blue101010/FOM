# CTFTTE-PWN-006 — Stack canary / PIE / ASLR hardening puzzle

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-006`](../countertechniques/CTFTCTE-PWN-006.md) — Leak canary/PIE base, ret2libc

---

## How the challenge author hides

The flag requires defeating canary, PIE and ASLR in a binary with a stack overflow.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Mitigation-bypass exploitation; ATT&CK omits the mechanics. |

## Tools

- pwntools
- gdb
- pwninit
- one_gadget

## References

- <https://github.com/Gallopsled/pwntools>
- Add challenge write-up link
