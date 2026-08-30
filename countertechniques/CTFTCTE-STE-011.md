# CTFTCTE-STE-011 — Analyze bitplanes and palette-based LSB

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-011`](../techniques/CTFTTE-STE-011.md) — Palette / bitplane LSB tricks

---

## Offensive Recovery (CTF practitioner / solver)

Split bitplanes, analyze palette anomalies, and extract the hidden bits.

## Forensic / Blue-Team Perspective (DFIR analyst)

Bitplane/palette analysis is standard steganalysis; visual inspection of planes reveals structure.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Image-domain data hiding. |

## Tools

- zsteg
- ImageMagick
- Stegsolve

## References

- <https://github.com/zed-0xff/zsteg>
- Add challenge write-up link
