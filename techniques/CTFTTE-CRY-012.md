# CTFTTE-CRY-012 — Hash-cracking maze with constraints

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-012`](../countertechniques/CTFTCTE-CRY-012.md) — Crack hashes under masks/rules

---

## How the challenge author hides

The flag is a hash whose preimage satisfies extra constraints (mask, salt, charset).

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1110 | Brute Force | Credential-hash brute force; CTFT adds mask/rule craft. |

## Tools

- hashcat
- john
- hashid

## References

- <https://hashcat.net/hashcat/>
- Add challenge write-up link
