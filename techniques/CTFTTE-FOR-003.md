# CTFTTE-FOR-003 — Timestomping (MACB manipulation)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-003`](../countertechniques/CTFTCTE-FOR-003.md) — Detect and reconstruct true timestamps

---

## How the challenge author hides

Author rewrites file timestamps so the relevant artifact blends into a noisy timeline or appears older/newer than reality.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070.006 | Timestomp | CTFT details MACB timestomping mechanics ATT&CK describes only at technique level. |

## Tools

- MFTECmd
- analyzeMFT
- fls/mactime (TSK)
- istat

## References

- https://github.com/sleuthkit/sleuthkit
- Add challenge write-up link