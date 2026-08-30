# CTFTCTE-NET-001 — Systematic port/service enumeration

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-001`](../techniques/CTFTTE-NET-001.md) — Port/service discovery maze

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate TCP/UDP ports with nmap/rustscan/masscan, fingerprint versions, then focus on the anomalous service.

## Forensic / Blue-Team Perspective (DFIR analyst)

Scan discipline matters: logged scan footprints and scope limits are respected, and service banners are correlated with netflow.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1046 | Network Service Discovery | CTFT adds the scan-tuning detail ATT&CK omits. |

## Tools

- nmap
- rustscan
- masscan
- netcat

## References

- <https://nmap.org/book/>

