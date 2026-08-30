# CTFTTE-WEB-001 — Obscured endpoint / source-comment hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-001`](../countertechniques/CTFTCTE-WEB-001.md) — Content discovery and source review

---

## How the challenge author hides

The flag route is unlinked, hinted in comments, robots.txt, JS bundles or backup files.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Credentials in Files | Source-comment/endpoint hiding is CTF craft; credential discovery is the closest ATT&CK echo. |

## Tools

- ffuf
- feroxbuster
- gobuster
- browser devtools

## References

- https://github.com/ffuf/ffuf
- Add challenge write-up link