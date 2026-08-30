# CTFTCTE-OSI-006 — Mine git history, objects and reflog

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-006`](../techniques/CTFTTE-OSI-006.md) — Git-repository archaeology

---

## Offensive Recovery (CTF practitioner / solver)

Mine the repository: git log, reflog, dangling objects, and search every blob.

## Forensic / Blue-Team Perspective (DFIR analyst)

Git archaeology recovers deleted content deterministically from object storage.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1596 | Search Open Technical Databases | Repository mining for secrets. |

## Tools

- git
- gitgrabber
- trufflehog

## References

- <https://github.com/trufflesecurity/trufflehog>

