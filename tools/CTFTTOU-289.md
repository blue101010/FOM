# CTFTTOU-289 — checksec

> **Tool ID:** `CTFTTOU-289`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTTE-PWN-006, CTFTCTE-PWN-001, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTTE-PWN-012

## Description

Reports binary hardening: PIE, NX, canary, RELRO, symbols. Drives the exploitation
strategy before any gadget work — No PIE + No canary means direct saved-RIP
overwrites (ret2win), PIE + canary means leaks come first. Shipped inside pwntools
(`pwn checksec ./target` / `checksec --file=`), so the shared pwn venv covers it.

## URL

<https://github.com/luke-goddard/checksec.py> (pwntools variant: <https://docs.pwntools.com>)

## Related Techniques

CTFTTE-PWN-001, CTFTTE-PWN-006, CTFTCTE-PWN-001, CTFTCTE-PWN-006, CTFTTE-PWN-011, CTFTTE-PWN-012
