# CTFTCTE-OSI-009 — Gate historical OSINT behind current-surface checks

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-009`](../techniques/CTFTTE-OSI-009.md) — Historical-infrastructure lure

---

## Offensive Recovery (CTF practitioner / solver)

Finish the first-party inventory (routes, assets, interactions) before touching historical leads. Before any action on an old target, require current attribution: reachability on indicative ports, then a targeted scan with reasons, and a full scan only with a specific question it will answer. Timebox passive sources and treat every absence as ambiguous, never as confirmation.

## Forensic / Blue-Team Perspective (DFIR analyst)

Historical records and current certificates or DNS are correlated explicitly; dead infrastructure is documented as out of scope, not as evidence.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; discipline against distraction. |

## Tools

- dig
- Subfinder
- Nmap (targeted, `--reason`)

## References

- <https://github.com/projectdiscovery/subfinder>
- Add challenge write-up link
