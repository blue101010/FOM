# CTFTCTE-OSI-002 — Enumerate accounts across platforms

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-002`](../techniques/CTFTTE-OSI-002.md) — Cross-platform username pivot

---

## Offensive Recovery (CTF practitioner / solver)

Search a username across services and correlate profiles to find the flag-bearing one.

## Forensic / Blue-Team Perspective (DFIR analyst)

Profile correlation documents the linkage between disparate online identities.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1593 | Search Open Websites/Domains | Username pivoting echoes open-web searching. |

## Tools

- sherlock
- maigret

## References

- <https://github.com/sherlock-project/sherlock>
- Add challenge write-up link