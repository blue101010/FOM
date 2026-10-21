# CTFTTE-PWN-011 — Win-function argument gate

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-011`](../countertechniques/CTFTCTE-PWN-011.md) — Set argument registers via gadgets, then redirect

---

## How the challenge author hides

The win function exists but only prints the flag when caller-controlled argument
registers hold magic constants (e.g. `rdi == 0xdeadbeefdeadbeef`), so a plain
saved-RIP overwrite jumps straight into the `No hacking!` exit path. The author
often plants a gadget helper function (`pop rdi; ret`, `pop rsi; ret`,
`pop rdx; ret`) in the binary so the intended chain exists but must be assembled.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Argument-gated win echoes guarded exploitation paths. |

## Tools

- [ROPgadget](../tools/CTFTTOU-288.md)
- [pwntools](../tools/CTFTTOU-053.md)
- [GDB (pwndbg/GEF)](../tools/CTFTTOU-290.md)

## MCP

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — recover the win prototype's argument constants and the planted gadget function statically

## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-2>
- <https://github.com/TCP1P/TCP1P-Playground-365-2025/tree/main/Pwn/ret2win-2>
