# CTFTTE-FOR-022 — Deleted-file / open-handle recovery

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-022`](../countertechniques/CTFTCTE-FOR-022.md) — Recover deleted files via /proc handles, journal, carving

---

## How the challenge author hides

The flag file is deleted but still open by a process, or recoverable from journal/extent remnants.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070.004 | File Deletion | Deletion-based hiding; CTFT reverses it. |

## Tools

- ls -l /proc/*/fd
- extundelete
- debugfs
- foremost

## References

- https://github.com/sleuthkit/sleuthkit
- Add challenge write-up link
