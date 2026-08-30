# CTFTTE-CRY-008 — Block-cipher mode / AES implementation weakness

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-008`](../countertechniques/CTFTCTE-CRY-008.md) — Attack AES modes (padding oracle, IV flaws)

---

## How the challenge author hides

AES is used with a weak mode (ECB patterns, predictable IV, padding oracle); the flag ciphertext is given.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Misused symmetric crypto; ATT&CK omits the attack detail. |

## Tools

- CyberChef
- pycryptodome
- padbuster

## References

- <https://github.com/AonCyberLabs/PadBuster>
- Add challenge write-up link
