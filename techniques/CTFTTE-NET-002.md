# CTFTTE-NET-002 — DNS covert channel / tunnel

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-002`](../countertechniques/CTFTCTE-NET-002.md) — Detect DNS tunneling and beaconing in PCAPs

---

## How the challenge author hides

Flag data is moved through DNS queries (labels encode chunks) or hidden in beacon intervals inside a capture.

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
- Add challenge write-up link
