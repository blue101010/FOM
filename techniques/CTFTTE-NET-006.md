# CTFTTE-NET-006 — TTL / protocol-field covert channel

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-006`](../countertechniques/CTFTCTE-NET-006.md) — Decode TTL/ICMP/padding channels

---

## How the challenge author hides

Each packet's TTL (or ICMP type / payload padding) encodes one character; the flag is spread across a capture's protocol fields.

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
- Add challenge write-up link
