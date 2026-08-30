# CTFTCTE-CRY-013 — Transcode nonstandard alphabets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-013`](../techniques/CTFTTE-CRY-013.md) — Nonstandard-alphabet substitution (braille, cetacean)

---

## Offensive Recovery (CTF practitioner / solver)

Identify the alphabet, transcode to plaintext, and decode.

## Forensic / Blue-Team Perspective (DFIR analyst)

Unusual encodings are catalogued as data-obfuscation families; transcoding is deterministic.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1140 | Deobfuscate/Decode Files or Information | Encoding-layer deobfuscation. |

## Tools

- CyberChef
- dcode.fr
- Python

## References

- <https://www.dcode.fr/>

