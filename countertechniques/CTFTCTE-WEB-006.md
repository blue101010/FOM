# CTFTCTE-WEB-006 — Deobfuscate and dynamically analyze JS

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-006`](../techniques/CTFTTE-WEB-006.md) — Client-side obfuscated logic

---

## Offensive Recovery (CTF practitioner / solver)

Beautify and trace the code, or set breakpoints to read the computed value at runtime.

## Forensic / Blue-Team Perspective (DFIR analyst)

Reconstructing the client logic documents how the value was derived without a server call.

## Tools

- browser devtools
- de4js
- Node

## References

- Add challenge write-up link