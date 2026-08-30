# CTFTTE-OSI-001 — Metadata-dispersed identity/location

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-001`](../countertechniques/CTFTCTE-OSI-001.md) — Correlate leaked metadata

---

## How the challenge author hides

Identifying data is scattered across file metadata and post artifacts rather than stated outright.

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