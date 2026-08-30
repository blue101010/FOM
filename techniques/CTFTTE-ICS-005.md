# CTFTTE-ICS-005 — DNP3 / BACnet object enumeration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-005`](../countertechniques/CTFTCTE-ICS-005.md) — Enumerate protocol objects

---

## How the challenge author hides

The flag is an object/point value exposed by a DNP3 or BACnet device.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: DNP3/BACnet object enumeration. |

## Tools

- bacnet/dnp3 clients
- scapy

## References

- Add challenge write-up link