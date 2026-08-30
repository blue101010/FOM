# CTFTCTE-NET-006 — Decode TTL/ICMP/padding channels

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-006`](../techniques/CTFTTE-NET-006.md) — TTL / protocol-field covert channel

---

## Offensive Recovery (CTF practitioner / solver)

Extract per-packet fields with tshark/scapy, map TTL deltas to characters, and reassemble the message.

## Forensic / Blue-Team Perspective (DFIR analyst)

Covert-channel detection looks for unnatural field distributions; the same extraction logic serves both solver and analyst.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1095 | Non-Application Layer Protocol | Field-level covert channels; ATT&CK omits the decoding detail. |

## Tools

- tshark
- scapy
- Wireshark

## References

- <https://scapy.net/>

