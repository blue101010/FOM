# CTFTCTE-CRY-001 — Recover the RSA private key from weak parameters

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-001`](../techniques/CTFTTE-CRY-001.md) — Weak RSA parameter design

---

## Offensive Recovery (CTF practitioner / solver)

Identify the weakness class and apply the matching attack (Fermat, Wiener, common-modulus, Coppersmith).

## Forensic / Blue-Team Perspective (DFIR analyst)

Documenting the parameter weakness explains how plaintext was recoverable without the key custodian.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573 | Encrypted Channel | Weak RSA parameter design; ATT&CK omits cryptanalytic key recovery. |

## Tools

- RsaCtfTool
- SageMath
- python sympy

## References

- https://github.com/RsaCtfTool/RsaCtfTool
- Add challenge write-up link