# CTFTTE-PWN-002 — Format-string information hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-002`](../countertechniques/CTFTCTE-PWN-002.md) — Leak and overwrite via format string

---

## How the challenge author hides

A user-controlled format string both leaks memory (secrets/canary) and enables targeted writes.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- pwntools
- GDB+pwndbg

## References

- Add challenge write-up link