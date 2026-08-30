# CTFTTE-CRY-010 — Certificate / PEM / ASN.1 field hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-010`](../countertechniques/CTFTCTE-CRY-010.md) — Parse certificates and extract hidden fields

---

## How the challenge author hides

The flag is stashed in certificate fields (subject, extensions, serial) or in the ASN.1 structure.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Credentials in Files | Certificates as secret carriers. |

## Tools

- openssl
- dumpasn1
- Python cryptography

## References

- <https://www.openssl.org/>
- Add challenge write-up link
