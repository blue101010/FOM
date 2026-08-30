# CTFTTE-OSI-008 — ASN / IP-range / subdomain recon

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-008`](../countertechniques/CTFTCTE-OSI-008.md) — Map ASN, ranges, subdomains (bbot, assetfinder)

---

## How the challenge author hides

The flag lives on infrastructure hidden among an ASN/IP range or a forgotten subdomain.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1596.001 | DNS/Passive DNS | DNS/asset enumeration. |

## Tools

- bbot
- assetfinder
- amass
- dnsx

## References

- https://github.com/blacklanternsecurity/bbot
- Add challenge write-up link
