# CTFTCTE-WEB-012 — Craft XSS payloads (stored/reflected/DOM)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-012`](../techniques/CTFTTE-WEB-012.md) — XSS-driven flag exfiltration

---

## Offensive Recovery (CTF practitioner / solver)

Craft stored/reflected/DOM payloads that read the flag and exfiltrate it.

## Forensic / Blue-Team Perspective (DFIR analyst)

XSS artifacts live in page source, logs and browser history; CSP reports corroborate.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.007 | JavaScript | Browser-executed script craft; ATT&CK omits XSS mechanics. |

## Tools

- Burp Suite
- browser devtools

## References

- <https://portswigger.net/web-security/cross-site-scripting>
- Add challenge write-up link
