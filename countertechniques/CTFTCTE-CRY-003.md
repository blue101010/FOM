# CTFTCTE-CRY-003 — Exploit key reuse and block-mode patterns

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-003`](../techniques/CTFTTE-CRY-003.md) — Repeating-key XOR / ECB pattern

---

## Offensive Recovery (CTF practitioner / solver)

Recover XOR key length via Hamming distance then solve per byte; for ECB, use block cut-and-paste.

## Forensic / Blue-Team Perspective (DFIR analyst)

Repeated ciphertext blocks are a tell-tale of ECB and of structural leakage in the design.

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