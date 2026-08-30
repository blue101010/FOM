# CTFTCTE-ICS-002 — Read S7 data blocks

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-002`](../techniques/CTFTTE-ICS-002.md) — S7comm PLC memory hiding

---

## Offensive Recovery (CTF practitioner / solver)

Use an S7 client to read the relevant data block and extract the value.

## Forensic / Blue-Team Perspective (DFIR analyst)

Data-block reads document the accessible memory regions of the device.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: S7 data-block reads. |

## Tools

- snap7
- python-snap7

## References

- Add challenge write-up link