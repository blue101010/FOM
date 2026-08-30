# CTFTTE-WEB-013 — CSRF-gated state change

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-013`](../countertechniques/CTFTCTE-WEB-013.md) — Forge cross-site requests

---

## How the challenge author hides

The flag is released only after a state change that requires a forged cross-site request from the victim session.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1606 | Forge Web Credentials | Cross-site forgery of web interactions. |

## Tools

- Burp Suite
- browser

## References

- https://owasp.org/www-community/attacks/csrf
- Add challenge write-up link
