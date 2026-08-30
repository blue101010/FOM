# CTFTTE-WEB-005 — Server-side template injection

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-005`](../countertechniques/CTFTCTE-WEB-005.md) — Exploit template evaluation

---

## How the challenge author hides

User input is rendered by a server template engine, letting the author gate the flag behind it.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | SSTI echoes public-application exploitation. |

## Tools

- tplmap
- Burp Suite

## References

- Add challenge write-up link