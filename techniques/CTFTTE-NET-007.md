# CTFTTE-NET-007 — Packet-capture forensics maze

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-007`](../countertechniques/CTFTCTE-NET-007.md) — Run beaconing/exfil/credential detectors over PCAPs

---

## How the challenge author hides

The flag is split among many packets or buried in protocol noise; the capture mixes decoys and real artifacts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1040 | Network Sniffing | Captured-traffic analysis echoes network-sniffing sources. |

## Tools

- tshark
- Wireshark
- zeek
- pcap-bloodhound

## References

- https://tshark.dev/
- Add challenge write-up link
