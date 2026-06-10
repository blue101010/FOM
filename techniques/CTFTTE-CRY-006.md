# CTFTTE-CRY-006 — Nested encoding obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-006`](../countertechniques/CTFTCTE-CRY-006.md) — Unwrap chained encodings

---

## How the challenge author hides

The flag is buried under stacked encodings (base64/base85/base32/hex/url) to look like ciphertext.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- CyberChef (Magic)
- python base64/codecs

## References

- https://gchq.github.io/CyberChef/
- Add challenge write-up link