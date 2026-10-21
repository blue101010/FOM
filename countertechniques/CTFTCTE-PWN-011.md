# CTFTCTE-PWN-011 — Set argument registers via gadgets, then redirect

> **Type:** Counter-technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-011`](../techniques/CTFTTE-PWN-011.md) — Win-function argument gate

---

## Offensive Recovery (CTF practitioner / solver)

Find the `pop <reg>; ret` gadgets (planted helper or ROPgadget scan), then overflow
into a chain: `pop rdi; ret` → magic1 → `pop rsi; ret` → magic2 → `pop rdx; ret` →
magic3 → win. Watch x86-64 stack alignment (an extra `ret` gadget if `win` uses
`movaps`). Verify the constants from the win prototype in the decompiler, not from
guessing.

## Forensic / Blue-Team Perspective (DFIR analyst)

The exploit path documents the register-set chain preceding the guarded call,
evidence of a deliberate control-flow hijack rather than accidental corruption.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Gadget chaining echoes staged exploitation. |

## Tools

- [ROPgadget](../tools/CTFTTOU-288.md)
- [pwntools](../tools/CTFTTOU-053.md)
- [GDB (pwndbg/GEF)](../tools/CTFTTOU-290.md)

## MCP

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — confirm gadget addresses and win's argument constants before building the chain

## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-2>
