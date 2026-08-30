# CTFTTE-WEB-014 — WebSocket message hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-014`](../countertechniques/CTFTCTE-WEB-014.md) — Intercept and decode WebSocket traffic

---

## How the challenge author hides

The flag travels over a WebSocket channel; plain HTTP tools miss it.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071.001 | Web Protocols | Hidden channels over web protocols. |

## Tools

- Burp Suite
- Chrome devtools
- websocat

## References

- https://github.com/vi/websocat
- Add challenge write-up link
