# CTFTCTE-PWN-006 — Leak canary/PIE base, ret2libc

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-006`](../techniques/CTFTTE-PWN-006.md) — Stack canary / PIE / ASLR hardening puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Leak the canary and PIE base via format/read leaks, then ret2libc to the win path.

## Forensic / Blue-Team Perspective (DFIR analyst)

Exploit-development notes document the bypass chain; mitigations are the defensive counterpart.

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

