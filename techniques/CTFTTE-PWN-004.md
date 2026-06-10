# CTFTTE-PWN-004 — Stripped/static gadget search

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-004`](../countertechniques/CTFTCTE-PWN-004.md) — Build a ROP chain from available gadgets

---

## How the challenge author hides

A stripped, statically linked binary forces a return-oriented chain instead of a simple call.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- ROPgadget
- ropper
- pwntools

## References

- https://github.com/JonathanSalwan/ROPgadget
- Add challenge write-up link