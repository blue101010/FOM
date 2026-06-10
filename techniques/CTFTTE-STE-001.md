# CTFTTE-STE-001 — LSB image steganography

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-001`](../countertechniques/CTFTCTE-STE-001.md) — Extract least-significant-bit payloads

---

## How the challenge author hides

Bits of the secret are written into the least-significant bits of pixel channels, leaving the image visually unchanged.

## ATT\&CK Complementarity

No ATT&CK equivalent; pure steganalysis.

## Tools

- zsteg
- stegsolve
- stegoVeritas
- stegseek

## References

- https://github.com/zed-0xff/zsteg
- Add challenge write-up link