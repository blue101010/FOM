# CTFTCTE-STE-007 — Detect and extract technical steganography

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-007`](../techniques/CTFTTE-STE-007.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Technical steganography hides the payload in the carrier's physical or format-level structure
rather than in its meaning. Enumerate the containers the format allows: appended data after
EOF, unused header fields, palette or colour-table entries, chunk padding, and metadata
segments. Compare the file against a clean file produced by the same encoder — the diff
isolates the carrier.

## Forensic / Blue-Team Perspective (DFIR analyst)

Format-level concealment survives copying but rarely survives re-encoding. If the artifact
passed through a transcoder, the payload may already be gone: preserve the original bitstream
before any conversion.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Technical steganography. |

## Tools

- binwalk
- exiftool
- stegoveritas
- xxd

## References

**Sources**

- (1) [Steganography — Wikipedia](https://en.wikipedia.org/wiki/Steganography)

**Writeups**

- Add challenge write-up link
