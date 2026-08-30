# CTFTCTE-NET-007 — Run beaconing/exfil/credential detectors over PCAPs

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-007`](../techniques/CTFTTE-NET-007.md) — Packet-capture forensics maze

---

## Offensive Recovery (CTF practitioner / solver)

Profile the capture (endpoints, protocols, timing), run detectors (beaconing, DNS tunnel, credentials, exfiltration) and pivot on the anomalies.

## Forensic / Blue-Team Perspective (DFIR analyst)

PCAP analysis is core DFIR: detector output becomes an annotated timeline of what happened on the wire.

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

- <https://tshark.dev/>

