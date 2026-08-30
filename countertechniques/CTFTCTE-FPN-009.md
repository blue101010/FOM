# CTFTCTE-FPN-009 — Enumerate Redis/Mongo/MySQL, dump or RCE

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-009`](../techniques/CTFTTE-FPN-009.md) — Redis/NoSQL service misconfiguration chain

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the service, dump data or achieve code execution, and pivot to the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

DB access logs and audit trails record the enumeration and exfiltration.

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

