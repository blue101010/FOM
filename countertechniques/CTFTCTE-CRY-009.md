# CTFTCTE-CRY-009 — Exploit keystream reuse to recover plaintext

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-009`](../techniques/CTFTTE-CRY-009.md) — Stream-cipher keystream reuse (Salsa20)

---

## Offensive Recovery (CTF practitioner / solver)

XOR the ciphertexts, crib-drag the keystream, and recover both messages.

## Forensic / Blue-Team Perspective (DFIR analyst)

Keystream reuse is detectable from ciphertext similarity; key-management flaws surface in logs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Nonce-reuse cryptanalysis. |

## Tools

- CyberChef
- Python
- cribdrag

## References

- <https://github.com/SpiderLabs/cribdrag>

