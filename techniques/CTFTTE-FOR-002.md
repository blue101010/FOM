# CTFTTE-FOR-002 — Slack-space and unallocated-area concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-002`](../countertechniques/CTFTCTE-FOR-002.md) — Carve hidden files from slack/unallocated space

---

## How the challenge author hides

Flag data is written into file slack, unallocated clusters, or between partitions where directory entries do not point.

## ATT\&CK Complementarity

No ATT&CK equivalent; this is media-forensics carving craft.

## Tools

- foremost
- scalpel
- binwalk
- photorec
- dd

## References

- https://github.com/ReFirmLabs/binwalk
- Add challenge write-up link