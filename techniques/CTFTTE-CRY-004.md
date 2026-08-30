# CTFTTE-CRY-004 — Nonce reuse in cryptographic operations

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-004`](../countertechniques/CTFTCTE-CRY-004.md) — Assess nonce reuse and its cryptographic consequence

---

## How the challenge author hides

A challenge repeats a nonce in a declared cryptographic operation, creating a
relationship between outputs that should have been independent.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- SageMath
- Python cryptographic reference implementations

## References

- Add challenge write-up link