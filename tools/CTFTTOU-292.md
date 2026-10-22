# CTFTTOU-292 — pwndbg

> **Tool ID:** `CTFTTOU-292`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-002, CTFTCTE-PWN-002, CTFTTE-PWN-003, CTFTCTE-PWN-003, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012

## Description

GDB/LLDB plugin that adds context views (registers, stack, disassembly), memory and heap inspection commands, and binary metadata checks to the debugger.

## Install (Kali WSL)

Kali rolling has no `pwndbg` apt package. Installed from the release
`pwndbg_2026.09.15_x86_64-portable.tar.xz` (sha256 checked) into `~/TOOLS/pwndbg`
(bundles its own gdb 17.2 + Python 3.13); launcher `gdb-pwndbg` in `~/.local/bin`.
`~/.gdbinit` stays vanilla. Check: `gdb-pwndbg -q -batch -ex version`.

pwndbg has no MCP server of its own. As a gdb plugin it can be loaded into the gdb that
the gdb/lldb MCP server drives (see [`CTFTTOU-163`](CTFTTOU-163.md) — gdb), by pointing
`MDB_GDB_PATH` at `gdb-pwndbg` (registered as server `mdb-pwndbg`).

## AGENT & SKILLS

- [mdb-mcp](../../ctf-skills-main/mdb-mcp/SKILL.md) — debugger sessions over MCP, pwndbg launcher

## URL

<https://github.com/pwndbg/pwndbg>

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-002, CTFTCTE-PWN-002, CTFTTE-PWN-003, CTFTCTE-PWN-003, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012
