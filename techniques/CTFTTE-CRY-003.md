# CTFTTE-CRY-003 — Repeating-key XOR / ECB pattern

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-003`](../countertechniques/CTFTCTE-CRY-003.md) — Exploit key reuse and block-mode patterns

---

## How the challenge author hides

Data is XORed with a short repeating key, or encrypted in ECB so identical blocks leak structure.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | ECB/repeating-XOR structural leakage; ATT&CK omits the cryptanalysis detail. |

## Tools

- xortool
- CyberChef
- python pwntools

## References

- <https://github.com/hellman/xortool>
- Add challenge write-up link