# CTFTTE-CRY-001 — Weak RSA parameter design

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-001`](../countertechniques/CTFTCTE-CRY-001.md) — Recover the RSA private key from weak parameters

---

## How the challenge author hides

The author ships RSA with an exploitable weakness: tiny e, close primes, shared modulus, or partial key leakage.

## ATT\&CK Complementarity

No ATT&CK equivalent; applied cryptanalysis.

## Tools

- RsaCtfTool
- SageMath
- python sympy

## References

- https://github.com/RsaCtfTool/RsaCtfTool
- Add challenge write-up link