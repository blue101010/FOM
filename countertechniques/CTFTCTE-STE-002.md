# CTFTCTE-STE-002 — Detect and split appended/embedded files

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-002`](../techniques/CTFTTE-STE-002.md) — Appended data / polyglot after EOF

---

## Offensive Recovery (CTF practitioner / solver)

Scan for embedded signatures and carve the trailing file; unzip/extract it.

## Forensic / Blue-Team Perspective (DFIR analyst)

Entropy + signature scanning reveals additional file structures beyond the declared container length.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Polyglot / appended-data concealment. |

## Tools

- binwalk
- foremost
- dd
- unzip

## References

- https://github.com/ReFirmLabs/binwalk
- Add challenge write-up link