# CTFTTE-WEB-006 — Client-side obfuscated logic

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-006`](../countertechniques/CTFTCTE-WEB-006.md) — Deobfuscate and dynamically analyze JS

---

## How the challenge author hides

A minified/packed JS bundle computes or gates the flag entirely in the browser.

## ATT\&CK Complementarity

No direct ATT&CK technique.

## Tools

- browser devtools
- de4js
- Node

## References

- Add challenge write-up link