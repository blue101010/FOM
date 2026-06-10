# CTFTCTE-STE-001 — Extract least-significant-bit payloads

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-001`](../techniques/CTFTTE-STE-001.md) — LSB image steganography

---

## Offensive Recovery (CTF practitioner / solver)

Run LSB extractors across channels/bit-planes; visual bit-plane inspection reveals embedded structure.

## Forensic / Blue-Team Perspective (DFIR analyst)

Bit-plane and chi-square analysis flags non-natural LSB distributions characteristic of embedding.

## Tools

- zsteg
- stegsolve
- stegoVeritas
- stegseek

## References

- https://github.com/zed-0xff/zsteg
- Add challenge write-up link