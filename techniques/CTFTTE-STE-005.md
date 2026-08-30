# CTFTTE-STE-005 — Zero-width / whitespace text steganography

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-005`](../countertechniques/CTFTCTE-STE-005.md) — Decode invisible-character payloads

---

## How the challenge author hides

Zero-width or whitespace characters encode bits inside otherwise normal text.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Zero-width / whitespace text steganography. |

## Tools

- CyberChef
- python unicodedata
- stegcloak-style decoders

## References

- https://gchq.github.io/CyberChef/
- Add challenge write-up link