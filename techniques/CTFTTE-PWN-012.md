# CTFTTE-PWN-012 — Author-gifted pointer leak

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-012`](../countertechniques/CTFTCTE-PWN-012.md) — Compute the target address from the leaked pointer

---

## How the challenge author hides

The binary deliberately prints a raw pointer before reading input — a stack address
(leaking ASLR/stack layout, enabling stack shellcode or ret2win without guessing) or
a `.data`/`.bss` address (leaking the PIE image base so `win`'s runtime address can
be computed). Hardening stays on (PIE/ASLR) but the author hands the one leak needed
to defeat it, and the solver must do the offset arithmetic.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Gifted leaks echo disclosed-memory exploitation primitives. |

## Tools

- [pwntools](../tools/CTFTTOU-053.md)
- [checksec](../tools/CTFTTOU-289.md)
- [GDB (pwndbg/GEF)](../tools/CTFTTOU-290.md)

## MCP

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — compute the symbol-to-leak offset (win − leaked global) statically

## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-3>
- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-4>
- <https://github.com/TCP1P/TCP1P-Playground-365-2025/tree/main/Pwn/ret2win-4>
