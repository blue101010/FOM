# CTFTCTE-FOR-022 — Recover deleted files via /proc handles, journal, carving

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-022`](../techniques/CTFTTE-FOR-022.md) — Deleted-file / open-handle recovery

---

## Offensive Recovery (CTF practitioner / solver)

Recover via /proc/<pid>/fd open handles, extundelete, journal replay, or raw carving.

## Forensic / Blue-Team Perspective (DFIR analyst)

Deleted-file recovery is standard DFIR; open handles and journal remnants outlive directory entries.

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

- <https://github.com/sleuthkit/sleuthkit>

