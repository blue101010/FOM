# CTFTCTE-PWN-005 — Open-Read-Write the flag under seccomp

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-005`](../techniques/CTFTTE-PWN-005.md) — seccomp-restricted shell puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Build an ORW chain (open, read, write) via ROP/shellcode to read the flag file directly.

## Forensic / Blue-Team Perspective (DFIR analyst)

Reading the seccomp policy reveals the allowed syscall surface that the solve relied on.

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