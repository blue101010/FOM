# CTFTCTE-FOR-021 — Reassemble LVM logical volumes and mount

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-021`](../techniques/CTFTTE-FOR-021.md) — LVM fragment/concat volume labyrinth

---

## Offensive Recovery (CTF practitioner / solver)

Scan PVs/LVs, assemble the volume group, and mount the logical volume to read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Volume reassembly mirrors RAID/LVM reconstruction: metadata blocks (PV headers) are the map.

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

- <https://man7.org/linux/man-pages/man8/lvm.8.html>

