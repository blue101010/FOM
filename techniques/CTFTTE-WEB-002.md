# CTFTTE-WEB-002 — IDOR / predictable object obscurity

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-002`](../countertechniques/CTFTCTE-WEB-002.md) — Enumerate insecure direct object references

---

## How the challenge author hides

The flag belongs to another object/user reachable by guessing an ID the UI never exposes.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | IDOR abuse echoes unauthorized data access from repositories. |

## Tools

- Burp Suite
- python requests

## References

- Add challenge write-up link