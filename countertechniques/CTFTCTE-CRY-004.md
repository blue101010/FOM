# CTFTCTE-CRY-004 — Reconstruct keys from broken randomness

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-004`](../techniques/CTFTTE-CRY-004.md) — Predictable PRNG / nonce reuse

---

## Offensive Recovery (CTF practitioner / solver)

Recover PRNG state from outputs, or recover the ECDSA private key from two signatures sharing a nonce.

## Forensic / Blue-Team Perspective (DFIR analyst)

Nonce reuse and predictable seeds are documented as the root cause enabling key recovery.

## Tools

- SageMath
- z3
- python ecdsa

## References

- Add challenge write-up link