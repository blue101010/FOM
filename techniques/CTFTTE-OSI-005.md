# CTFTTE-OSI-005 — Public-record / repo leak pivot

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-005`](../countertechniques/CTFTCTE-OSI-005.md) — Mine public repositories and records

---

## How the challenge author hides

The flag/secret was committed to a public repo, paste, or document and later assumed forgotten.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1596 | Search Open Technical Databases | Public-repo mining echoes open-technical-database searching. |

## Tools

- github search/dorking
- trufflehog
- gitleaks

## References

- https://github.com/trufflesecurity/trufflehog
- Add challenge write-up link