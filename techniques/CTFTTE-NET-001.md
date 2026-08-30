# CTFTTE-NET-001 — Port/service discovery maze

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-001`](../countertechniques/CTFTCTE-NET-001.md) — Systematic port/service enumeration

---

## How the challenge author hides

The flag sits behind a service on an unusual port, or the challenge hides which port is real among decoys; versions and banners mislead.

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

- https://nmap.org/book/
- Add challenge write-up link
