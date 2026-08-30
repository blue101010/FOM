# CTFTCTE-CRY-004 — Assess nonce reuse and its cryptographic consequence

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-004`](../techniques/CTFTTE-CRY-004.md) — Nonce reuse in cryptographic operations

---

## Offensive Recovery (CTF practitioner / solver)

Identify the repeated nonce condition in the declared challenge data and validate
the resulting cryptographic weakness with reproducible evidence.

## Forensic / Blue-Team Perspective (DFIR analyst)

Nonce reuse is documented as the root cause; generator-state prediction is
tracked separately by CTFTCTE-CRY-007.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Nonce-reuse consequences are cryptanalytic craft ATT&CK omits. |

## Tools

- SageMath
- Python cryptographic reference implementations

## References

- Add challenge write-up link