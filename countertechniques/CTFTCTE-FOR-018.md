# CTFTCTE-FOR-018 — Analyze orphaned MFT records and raw attributes

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-018`](../techniques/CTFTTE-FOR-018.md) — MFT record and attribute tampering

---

## Offensive Recovery (CTF practitioner / solver)

Inspect the supplied NTFS image at record and attribute level, correlate
unlinked records with allocation evidence, and recover only artifacts supported
by the image.

## Forensic / Blue-Team Perspective (DFIR analyst)

Compare directory reachability with raw MFT records, sequence values and
attribute consistency. An orphaned record is evidence for review, not by itself
proof of a recovered file's content or provenance.

## Preconditions

- A read-only NTFS image or a documented MFT extract is available.
- The analyst has a declared artifact scope and preserves the source image.

## Indicators

- A file reference points to a missing or inconsistent record.
- A record is unlinked while retaining coherent attributes.
- Allocation metadata conflicts with directory metadata.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564.001 | Hidden Files and Directories | MFT-level tampering extends hidden-file craft below ATT&CK granularity. |

## Tools

- MFTECmd / analyzeMFT
- The Sleuth Kit
- [CTFTTOU-005](../tools/CTFTTOU-005.md)

## References

- <https://learn.microsoft.com/windows/win32/devnotes/master-file-table>
- <https://www.sleuthkit.org/>