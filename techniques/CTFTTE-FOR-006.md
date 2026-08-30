# CTFTTE-FOR-006 — PCAP payload obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-006`](../countertechniques/CTFTCTE-FOR-006.md) — Reassemble and decode hidden network payloads

---

## How the challenge author hides

Flag is split across packets, tunnelled in odd fields (ICMP data, DNS labels), or encoded before transmission.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573 | Encrypted Channel | PCAP payload obfuscation echoes encrypted-channel traffic; ATT&CK omits reassembly craft. |

## Tools

- wireshark
- tshark
- scapy
- NetworkMiner
- tcpflow

## References

- Add challenge write-up link