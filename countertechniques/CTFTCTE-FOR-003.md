# CTFTCTE-FOR-003 — Detect and reconstruct true timestamps

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-003`](../techniques/CTFTTE-FOR-003.md) — Timestomping (MACB manipulation)

---

## Offensive Recovery (CTF practitioner / solver)

On NTFS, compare $STANDARD_INFORMATION vs $FILE_NAME timestamps; mismatches reveal manipulation and often the real ordering.

## Forensic / Blue-Team Perspective (DFIR analyst)

Cross-reference MFT, $LogFile/$UsnJrnl, registry and event logs; timestamps that disagree across sources expose the stomped value.

## Tools

- MFTECmd
- analyzeMFT
- fls/mactime (TSK)
- istat

## References

- https://github.com/sleuthkit/sleuthkit
- Add challenge write-up link