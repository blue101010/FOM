# CTFTTE-STE-002 — Appended data / polyglot after EOF

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-002`](../countertechniques/CTFTCTE-STE-002.md) — Detect and split appended/embedded files

---

## How the challenge author hides

A second file (zip, flag.txt) is concatenated after a valid image's end-of-image marker, so viewers ignore it.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- binwalk
- foremost
- dd
- unzip

## References

- https://github.com/ReFirmLabs/binwalk
- Add challenge write-up link