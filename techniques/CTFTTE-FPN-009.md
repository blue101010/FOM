# CTFTTE-FPN-009 — Redis/NoSQL service misconfiguration chain

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-009`](../countertechniques/CTFTCTE-FPN-009.md) — Enumerate Redis/Mongo/MySQL, dump or RCE

---

## How the challenge author hides

An internal DB service is misconfigured (no auth, weak credentials); the flag is in the data or reachable via RCE.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Database data extraction. |

## Tools

- redis-cli
- mongosh
- mysql
- crackmapexec

## References

- <https://redis.io/docs/latest/commands/>
- Add challenge write-up link
