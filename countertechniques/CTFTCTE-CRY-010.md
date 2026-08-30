# CTFTCTE-CRY-010 — Parse certificates and extract hidden fields

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-010`](../techniques/CTFTTE-CRY-010.md) — Certificate / PEM / ASN.1 field hiding

---

## Offensive Recovery (CTF practitioner / solver)

Parse with openssl x509 -text, decode DER/ASN.1, and inspect every field for the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Certificate inspection is routine; unusual extensions or serials are immediate artifacts.

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

