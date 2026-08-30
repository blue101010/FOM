# CTFTCTE-WEB-001 — Content discovery and source review

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-001`](../techniques/CTFTTE-WEB-001.md) — Obscured endpoint / source-comment hiding

---

## Offensive Recovery (CTF practitioner / solver)

Brute force paths/parameters and review client source/maps for hidden references.

## Forensic / Blue-Team Perspective (DFIR analyst)

Access logs of the discovery sweep document how the hidden surface was found.

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