# CTFTTE-FOR-021 — LVM fragment/concat volume labyrinth

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-021`](../countertechniques/CTFTCTE-FOR-021.md) — Reassemble LVM logical volumes and mount

---

## How the challenge author hides

The flag sits in an LVM volume assembled from scattered physical volumes or fragmented extents; naive mounting fails.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | Volume-level concealment; ATT&CK covers artifact hiding only generically. |

## Tools

- pvscan
- vgscan
- lvdisplay
- mount

## References

- https://man7.org/linux/man-pages/man8/lvm.8.html
- Add challenge write-up link
