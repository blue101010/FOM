# CTFTTE-WEB-016 — NoSQL injection

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-016`](../countertechniques/CTFTCTE-WEB-016.md) — Inject Mongo/NoSQL queries

---

## How the challenge author hides

The flag query is gated by a NoSQL (Mongo) filter; operator injection bypasses it.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Injection on public apps. |

## Tools

- Burp Suite
- mongosh
- NoSQLMap

## References

- https://github.com/codingo/NoSQLMap
- Add challenge write-up link
