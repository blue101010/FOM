# CTFTTE-PWN-011 — Argument-gated target function

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-011`](../countertechniques/CTFTCTE-PWN-011.md) — Control argument registers, then redirect

---

## How the challenge author hides

The sensitive routine (flag print, shell spawn, privileged call) validates its
arguments — equality against constants, value ranges, or pointer identity — and
bails out otherwise. A saved-return-address overwrite alone lands in the bail-out
path: the solver must also place the expected values in the argument registers
(rdi, rsi, rdx on x86-64; stack on i386), turning a one-gadget redirect into a
register-setting problem. The required gadgets may be planted in the binary or
must be hunted anywhere in the image or libc.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Argument validation echoes guarded exploitation paths. |

## Tools

- [ROPgadget](../tools/CTFTTOU-288.md)
- [pwntools](../tools/CTFTTOU-053.md)
- [GDB (pwndbg/GEF)](../tools/CTFTTOU-290.md)

## MCP

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — recover the target's argument checks and the available gadgets statically

## Notes

Seen in TCP1P Playground 365 ret2win-2: win(long a, long b, long c) requires three magic constants; a gadgets() helper plants pop rdi/rsi/rdx in the binary.

Solved 2026-10-21: TCP1P ret2win-2 offset to saved RIP = 120 (buf[100]); ROPgadget finds the planted gadgets at pop rdi 0x40121e, pop rsi 0x401220, pop rdx 0x401222, ret 0x40101a; chain with alignment ret lands win 0x401227. Solve script: ctf-skills-main/ctf-pwn-win-arg-gate/solve.py
## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-2>
- <https://github.com/TCP1P/TCP1P-Playground-365-2025/blob/main/Pwn/ret2win-2/src/ret2win.c>
