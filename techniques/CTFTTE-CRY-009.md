# CTFTTE-CRY-009 — Stream-cipher keystream reuse (Salsa20)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-009`](../countertechniques/CTFTCTE-CRY-009.md) — Exploit keystream reuse to recover plaintext

---

## How the challenge author hides

Two messages are encrypted under the same Salsa20 key/nonce; the XOR of ciphertexts leaks plaintext.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Nonce-reuse cryptanalysis. |

## Tools

- CyberChef
- Python
- cribdrag

## References

- https://github.com/SpiderLabs/cribdrag
- Add challenge write-up link
