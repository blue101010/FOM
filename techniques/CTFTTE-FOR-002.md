# CTFTTE-FOR-002 — Slack-space and unallocated-area concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-002`](../countertechniques/CTFTCTE-FOR-002.md) — Carve hidden files from slack/unallocated space

---

## How the challenge author hides

Flag data is written into file slack, unallocated clusters, or between partitions where directory entries do not point.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | Slack/unallocated-space carving is media-forensics craft; ATT&CK covers artifact hiding only generically. |

## Tools

- foremost
- scalpel
- binwalk
- photorec
- dd

## References

- https://github.com/ReFirmLabs/binwalk
- Add challenge write-up link