# CTFTCTE-NET-002 — Detect DNS tunneling and beaconing in PCAPs

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-002`](../techniques/CTFTTE-NET-002.md) — DNS covert channel / tunnel

---

## Offensive Recovery (CTF practitioner / solver)

Parse DNS queries with tshark/zeek, decode label entropy, and reassemble the tunneled payload.

## Forensic / Blue-Team Perspective (DFIR analyst)

DNS tunnel detection compares query entropy, label length and cadence against a baseline; C2-style beaconing leaves the same signature.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071.004 | DNS | DNS tunneling; CTFT adds the decoding recipe. |

## Tools

- tshark
- zeek
- dnscat2
- pcap-bloodhound

## References

- <https://github.com/iagox86/dnscat2>

