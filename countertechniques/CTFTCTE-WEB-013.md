# CTFTCTE-WEB-013 — Forge cross-site requests

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-013`](../techniques/CTFTTE-WEB-013.md) — CSRF-gated state change

---

## Offensive Recovery (CTF practitioner / solver)

Forge the cross-site request (form auto-submit) to trigger the state change and capture the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

CSRF attempts are visible as cross-origin referer mismatches and suspicious requests in logs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1606 | Forge Web Credentials | Cross-site forgery of web interactions. |

## Tools

- Burp Suite
- browser

## References

- <https://owasp.org/www-community/attacks/csrf>
- Add challenge write-up link
