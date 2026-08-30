# CTFTTE-WEB-012 — XSS-driven flag exfiltration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-012`](../countertechniques/CTFTCTE-WEB-012.md) — Craft XSS payloads (stored/reflected/DOM)

---

## How the challenge author hides

The flag is delivered to an admin/bot that visits attacker-controlled content; XSS triggers the read.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.007 | JavaScript | Browser-executed script craft; ATT&CK omits XSS mechanics. |

## Tools

- Burp Suite
- browser devtools

## References

- https://portswigger.net/web-security/cross-site-scripting
- Add challenge write-up link
