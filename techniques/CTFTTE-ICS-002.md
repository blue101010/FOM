# CTFTTE-ICS-002 — S7comm PLC memory hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-002`](../countertechniques/CTFTCTE-ICS-002.md) — Read S7 data blocks

---

## How the challenge author hides

Data is concealed inside S7 PLC data blocks reachable over S7comm.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: S7 data-block reads. |

## Tools

- snap7
- python-snap7

## References

- Add challenge write-up link