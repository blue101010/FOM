# CTFTTE-PWN-005 — seccomp-restricted shell puzzle

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-005`](../countertechniques/CTFTCTE-PWN-005.md) — Open-Read-Write the flag under seccomp

---

## How the challenge author hides

execve is filtered, so a shell is impossible; only file I/O syscalls remain.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | seccomp-restricted ORW shellcraft is CTF-specific. |

## Tools

- seccomp-tools
- pwntools
- ROPgadget

## References

- https://github.com/david942j/seccomp-tools
- Add challenge write-up link