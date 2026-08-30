# CTFTCTE-WEB-016 — Inject Mongo/NoSQL queries

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-016`](../techniques/CTFTTE-WEB-016.md) — NoSQL injection

---

## Offensive Recovery (CTF practitioner / solver)

Inject NoSQL operators ($gt/$ne/$where) to bypass auth/filters and dump the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

NoSQL payloads ($ operators) appear in application logs; unusual query shapes are the tell.

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
