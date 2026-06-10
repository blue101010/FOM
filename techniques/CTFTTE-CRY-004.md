# CTFTTE-CRY-004 — Predictable PRNG / nonce reuse

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-004`](../countertechniques/CTFTCTE-CRY-004.md) — Reconstruct keys from broken randomness

---

## How the challenge author hides

A weak/seeded PRNG (LCG, time-seeded) or a reused ECDSA/CTR nonce undermines the scheme.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- SageMath
- z3
- python ecdsa

## References

- Add challenge write-up link