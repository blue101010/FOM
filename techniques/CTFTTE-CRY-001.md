# CTFTTE-CRY-001 — Weak RSA parameter design

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-001`](../countertechniques/CTFTCTE-CRY-001.md) — Recover the RSA private key from weak parameters

---

## How the challenge author hides

The author ships RSA with an exploitable weakness: tiny e, close primes, shared modulus, or partial key leakage.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573 | Encrypted Channel | Weak RSA parameter design; ATT&CK omits cryptanalytic key recovery. |

## Tools

- RsaCtfTool
- SageMath
- python sympy

## References

- <https://github.com/RsaCtfTool/RsaCtfTool>
- Add challenge write-up link