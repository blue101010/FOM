# CTFTCTE-MSC-001 — Escape the Python sandbox

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MSC`](../tactics/CTFT-TA-MSC.md) — Misc / Jail / Coding / Fullpwn  
> **Counters technique:** [`CTFTTE-MSC-001`](../techniques/CTFTTE-MSC-001.md) — Python jail (pyjail) confinement

---

## Offensive Recovery (CTF practitioner / solver)

Reach builtins/attributes via object traversal to import os/open and read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

The escape chain documents the incomplete sandboxing of the eval context.

## Tools

- python
- pyjail cheat references

## References

- Add challenge write-up link