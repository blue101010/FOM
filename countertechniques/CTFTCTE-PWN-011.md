# CTFTCTE-PWN-011 — Control argument registers, then redirect

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-011`](../techniques/CTFTTE-PWN-011.md) — Argument-gated target function

---

## Offensive Recovery (CTF practitioner / solver)

Read the expected values from the decompiled argument checks, then deliver them at
the moment of the jump: assemble a register-setting chain from the available
gadgets (`pop reg; ret`), fall back to call-oriented setup (ret2csu-style) when an
individual gadget is missing, keep stack alignment for callees using SSE, and on
i386 pass the arguments on the stack instead. Map parameters to registers by ABI
order (rdi, rsi, rdx, rcx, r8, r9), never by which constant "looks like" which
register.

## Forensic / Blue-Team Perspective (DFIR analyst)

The exploit path documents the argument-forgery chain preceding the guarded call,
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

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — confirm gadget addresses and the target's argument checks before building the chain

## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-2>
