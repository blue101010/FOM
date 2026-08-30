# CTFTTE-WEB-004 — Blind / WAF-evaded SQL injection

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-004`](../countertechniques/CTFTCTE-WEB-004.md) — Extract data via blind injection

---

## How the challenge author hides

The flag is in the database, reachable only through a filtered, blind injection point.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | ATT&CK has no SQLi technique; public-application exploitation is the closest echo. |

## Tools

- sqlmap
- Burp Suite

## References

- Add challenge write-up link