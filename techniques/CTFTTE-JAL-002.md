# CTFTTE-JAL-002 — Restricted-shell confinement

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-002`](../countertechniques/CTFTCTE-JAL-002.md) — Escape the restricted shell

---

## How the challenge author hides

A limited shell (rbash, menu shell, or custom restricted interpreter) is placed between the player and the flag, blocking path traversal and forbidden commands.

## ATT\&CK Complementarity

Complements T1059 conceptually with CTF restricted-shell-escape detail that ATT&CK omits (GTFOBins escape paths, PATH hijacking).

## Tools

- GTFOBins references
- standard shells

## References

- https://gtfobins.github.io/
- Add challenge write-up link
