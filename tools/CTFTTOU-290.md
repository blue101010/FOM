# CTFTTOU-290 — GDB (pwndbg/GEF)

> **Tool ID:** `CTFTTOU-290`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTTE-PWN-006, CTFTTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-001, CTFTCTE-PWN-006, CTFTCTE-PWN-011, CTFTCTE-PWN-012

## Description

The standard dynamic triage debugger for pwn challenges, run with an exploit-dev
layer — pwndbg (`gdb-pwndbg`) or GEF (`gdb-gef`) — for cyclic-pattern offsets,
stack/telescope views, register context on crash, and heap introspection. Kali ships
pwndbg (`apt install gdb pwndbg`). Typical flow: crash on `cyclic(200)`, read the
RIP value (`cyclic -l 0x...` for the offset), set breakpoints at the win gate to
verify magic constants and alignment.

## URL

<https://github.com/pwndbg/pwndbg>

## Related Techniques

CTFTTE-PWN-001, CTFTTE-PWN-006, CTFTTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-001, CTFTCTE-PWN-006, CTFTCTE-PWN-011, CTFTCTE-PWN-012
