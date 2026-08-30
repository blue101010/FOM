# CTFTCTE-ICS-005 — Enumerate protocol objects

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-005`](../techniques/CTFTTE-ICS-005.md) — DNP3 / BACnet object enumeration

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate objects/points and read the value carrying the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Object enumeration documents the device's exposed data model.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: DNP3/BACnet object enumeration. |

## Tools

- bacnet/dnp3 clients
- scapy

## References

- Add challenge write-up link