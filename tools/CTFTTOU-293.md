# CTFTTOU-293 — GEF

> **Tool ID:** `CTFTTOU-293`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012, CTFTTE-REV-001, CTFTCTE-REV-001

## Description

GDB Enhanced Features: a single-file GDB Python extension adding context views, memory and heap inspection commands, and multi-architecture support.

## Install (Kali WSL)

Kali apt package: `sudo apt install gef` (2026.01-0kali2) installs `/usr/share/gdb/gef.py`
(identical to upstream tag `2026.01`) and the launcher `gef` (`gdb -ex "source
/usr/share/gdb/gef.py"`); `gdb-gef` in `~/.local/bin` is the same with `-q`. Nothing is
added to `~/.gdbinit`, so plain gdb stays vanilla. Check: `gef -batch -ex "gef config"`.

## AGENT & SKILLS

- [mdb-mcp](../../ctf-skills-main/mdb-mcp/SKILL.md) — debugger sessions over MCP, GEF launcher

## URL

<https://github.com/hugsy/gef>

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012, CTFTTE-REV-001, CTFTCTE-REV-001
