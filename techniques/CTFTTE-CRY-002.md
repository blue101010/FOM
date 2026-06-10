# CTFTTE-CRY-002 — Classical cipher layering

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-002`](../countertechniques/CTFTCTE-CRY-002.md) — Break layered classical ciphers

---

## How the challenge author hides

The flag is wrapped in stacked classical ciphers (ROT/Caesar, Vigenere, substitution) to resist a single pass.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- CyberChef
- quipqiup
- dcode helpers

## References

- https://gchq.github.io/CyberChef/
- Add challenge write-up link