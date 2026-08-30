# CTFTCTE-WEB-014 — Intercept and decode WebSocket traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-014`](../techniques/CTFTTE-WEB-014.md) — WebSocket message hiding

---

## Offensive Recovery (CTF practitioner / solver)

Intercept the WS upgrade and frames (Burp/Chrome), replay and decode the messages.

## Forensic / Blue-Team Perspective (DFIR analyst)

WebSocket sessions are full-duplex artifacts; frame capture requires the upgrade context.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071.001 | Web Protocols | Hidden channels over web protocols. |

## Tools

- Burp Suite
- Chrome devtools
- websocat

## References

- <https://github.com/vi/websocat>
- Add challenge write-up link
