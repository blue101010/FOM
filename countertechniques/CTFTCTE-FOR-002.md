# CTFTCTE-FOR-002 — Carve hidden files from slack/unallocated space

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-002`](../techniques/CTFTTE-FOR-002.md) — Slack-space and unallocated-area concealment

---

## Offensive Recovery (CTF practitioner / solver)

Run file-carving over the raw image to extract artifacts independent of the filesystem index.

## Forensic / Blue-Team Perspective (DFIR analyst)

Treat the image at the block level; carving + manual cluster inspection recovers data the filesystem no longer references.

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

- <https://github.com/ReFirmLabs/binwalk>
- Add challenge write-up link