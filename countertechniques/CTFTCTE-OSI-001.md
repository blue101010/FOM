# CTFTCTE-OSI-001 — Correlate leaked metadata

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-001`](../techniques/CTFTTE-OSI-001.md) — Metadata-dispersed identity/location

---

## Offensive Recovery (CTF practitioner / solver)

Extract metadata (GPS/author/timestamps) and pivot to the real identity/location.

## Forensic / Blue-Team Perspective (DFIR analyst)

Aggregating metadata across artifacts reconstructs the subject's footprint.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1589 | Gather Victim Identity Information | Metadata correlation echoes identity gathering. |

## Tools

- exiftool
- reverse geocoding
- maps

## References

- https://exiftool.org/
- Add challenge write-up link