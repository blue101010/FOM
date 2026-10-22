# CTFTTOU-291 — lldb

> **Tool ID:** `CTFTTOU-291`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001

## Description

LLVM debugger, the second dynamic-analysis view next to gdb: breakpoints, register and
memory reads, backtraces, with a precise stop reason on crashes (`stop reason = signal
SIGSEGV: address not mapped to object (fault address=0x10)`). Scriptable through its
embedded Python (`script`), which needs the `python3-lldb` package of the **same**
version as `lldb` on Debian/Kali (`sudo apt install lldb python3-lldb`). pwndbg also
ships an lldb flavour (`pwndbg-lldb` release assets). Common commands: `b main`,
`process launch -i input.bin`, `register read`, `memory read -fx -s8 -c16 $rsp`,
`image lookup -r -s <regex>`, `disassemble -n <func>`, `image list` (PIE base).

## URL

<https://lldb.llvm.org/>

## MCP

- [MDB-MCP (GDB/LLDB)](../mcp/CTFTTMOU-003.md) — `debugger_start {debugger: "lldb"}`

## AGENT & SKILLS

- [mdb-mcp](../../ctf-skills-main/mdb-mcp/SKILL.md) — drive gdb/lldb sessions over MCP, gdb↔lldb command map

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001
