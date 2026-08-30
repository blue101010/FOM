# CTFTCTE-STE-001 — Extract least-significant-bit payloads

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-001`](../techniques/CTFTTE-STE-001.md) — LSB image steganography

---

## Offensive Recovery (CTF practitioner / solver)

Run LSB extractors across channels/bit-planes; visual bit-plane inspection reveals embedded structure.

## Forensic / Blue-Team Perspective (DFIR analyst)

Bit-plane and chi-square analysis flags non-natural LSB distributions characteristic of embedding.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | CTFT details LSB extraction mechanics ATT&CK omits. |

## Tools

- zsteg
- stegsolve
- stegoVeritas
- stegseek

## References

- https://github.com/zed-0xff/zsteg
- Add challenge write-up link