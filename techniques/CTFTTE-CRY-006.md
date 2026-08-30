# CTFTTE-CRY-006 — Nested encoding obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-006`](../countertechniques/CTFTCTE-CRY-006.md) — Unwrap chained encodings

---

## How the challenge author hides

The flag is buried under stacked encodings (base64/base85/base32/hex/url) to look like ciphertext.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1140 | Deobfuscate/Decode Files or Information | Chained encodings echo deobfuscation/decoding. |

## Tools

- CyberChef (Magic)
- python base64/codecs

## References

- <https://gchq.github.io/CyberChef/>
- Add challenge write-up link