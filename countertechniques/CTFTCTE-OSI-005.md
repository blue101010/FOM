# CTFTCTE-OSI-005 — Mine public repositories and records

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-005`](../techniques/CTFTTE-OSI-005.md) — Public-record / repo leak pivot

---

## Offensive Recovery (CTF practitioner / solver)

Search code history, pastes and documents for the leaked token or hint.

## Forensic / Blue-Team Perspective (DFIR analyst)

Commit history and timestamps document when and where the secret was exposed.

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