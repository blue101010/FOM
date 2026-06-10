# CTFTCTE-FOR-006 — Reassemble and decode hidden network payloads

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-006`](../techniques/CTFTTE-FOR-006.md) — PCAP payload obfuscation

---

## Offensive Recovery (CTF practitioner / solver)

Follow streams, filter by protocol, export objects, then decode the reassembled payload.

## Forensic / Blue-Team Perspective (DFIR analyst)

Reconstruct sessions and extract transferred objects; covert channels show up as anomalous field usage or unusual protocol volume.

## Tools

- wireshark
- tshark
- scapy
- NetworkMiner
- tcpflow

## References

- Add challenge write-up link