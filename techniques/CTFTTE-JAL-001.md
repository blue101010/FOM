# CTFTTE-JAL-001 — Python jail (pyjail) confinement

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-001`](../countertechniques/CTFTCTE-JAL-001.md) — Escape the Python sandbox

---

## How the challenge author hides

Input is eval'd or exec'd in a restricted Python namespace with builtins stripped or whitelisted, preventing direct import of `os`, `subprocess`, or open file reads.

## ATT\&CK Complementarity

No ATT&CK equivalent. ATT&CK T1059.006 (Python) models scripting for lateral movement, not sandbox-escape puzzle craft.

## Tools

- python
- pyjail cheat references

## References

- Add challenge write-up link
