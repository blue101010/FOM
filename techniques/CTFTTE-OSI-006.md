# CTFTTE-OSI-006 — Git-repository archaeology

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-006`](../countertechniques/CTFTCTE-OSI-006.md) — Mine git history, objects and reflog

---

## How the challenge author hides

The flag (or a credential) is in git history: old commits, dangling objects, or reflog entries.

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
- Add challenge write-up link
