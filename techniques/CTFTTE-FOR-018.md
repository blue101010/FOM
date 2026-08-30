# CTFTTE-FOR-018 — MFT record and attribute tampering

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-018`](../countertechniques/CTFTCTE-FOR-018.md) — Analyze orphaned MFT records and raw attributes

---

## How the challenge author hides

The challenge modifies, unlinks, or partially corrupts NTFS Master File Table
records so that the expected file is absent from normal directory traversal
while residual record, attribute, or allocation evidence remains in the image.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564.001 | Hidden Files and Directories | MFT-level tampering extends hidden-file craft below ATT&CK granularity. |

## Tools

- MFTECmd / analyzeMFT
- The Sleuth Kit
- [CTFTTOU-005](../tools/CTFTTOU-005.md)

## References

- https://learn.microsoft.com/windows/win32/devnotes/master-file-table
- https://www.sleuthkit.org/