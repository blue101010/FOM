# CTFTCTE-CRY-008 — Attack AES modes (padding oracle, IV flaws)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-008`](../techniques/CTFTTE-CRY-008.md) — Block-cipher mode / AES implementation weakness

---

## Offensive Recovery (CTF practitioner / solver)

Attack the mode: padding oracle, IV reuse, or ECB block analysis to recover plaintext.

## Forensic / Blue-Team Perspective (DFIR analyst)

Weak-mode signatures (repeated blocks) identify misconfigured crypto in artifacts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Misused symmetric crypto; ATT&CK omits the attack detail. |

## Tools

- CyberChef
- pycryptodome
- padbuster

## References

- https://github.com/AonCyberLabs/PadBuster
- Add challenge write-up link
