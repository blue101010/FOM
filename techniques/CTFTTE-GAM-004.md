# CTFTTE-GAM-004 — Game binary win-condition bypass

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-004`](../countertechniques/CTFTCTE-GAM-004.md) — Patch the jump / comparison to force a win state

---

## How the challenge author hides

The win condition is hardcoded in the game binary (e.g. score must reach an astronomically high value) and is unreachable through legitimate play, requiring binary patching to bypass the comparison.

## ATT\&CK Complementarity

Complements T1027 (Obfuscated Files / Information) with CTF binary-patching detail (NOP-ing comparisons, flipping jump conditions).

## Tools

- ghidra / ida
- binary patching scripts
- pwntools

## References

- Add challenge write-up link
