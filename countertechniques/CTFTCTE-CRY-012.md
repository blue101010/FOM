# CTFTCTE-CRY-012 — Crack hashes under masks/rules

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-012`](../techniques/CTFTTE-CRY-012.md) — Hash-cracking maze with constraints

---

## Offensive Recovery (CTF practitioner / solver)

Identify the hash type, build masks/rules, crack with hashcat/john, and verify.

## Forensic / Blue-Team Perspective (DFIR analyst)

Hash recovery is standard evidence processing; salt and algorithm identification come first.

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

