# CTFTCTE-WEB-002 — Enumerate insecure direct object references

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-002`](../techniques/CTFTTE-WEB-002.md) — IDOR / predictable object obscurity

---

## Offensive Recovery (CTF practitioner / solver)

Iterate identifiers/parameters to access objects outside the intended scope.

## Forensic / Blue-Team Perspective (DFIR analyst)

Sequential access to non-owned IDs in logs is the signature of IDOR abuse.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | IDOR abuse echoes unauthorized data access from repositories. |

## Tools

- Burp Suite
- python requests

## References

- Add challenge write-up link