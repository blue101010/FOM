# CTFTCTE-WEB-022 — Enumerate and triage source maps

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-022`](../techniques/CTFTTE-WEB-022.md) — Public source-map bait

---

## Offensive Recovery (CTF practitioner / solver)

Request the referenced `.map` for every asset; recover the original sources; classify each as structural (styles, section names) or functional (logic, endpoints, data). Treat section vocabulary as hint material for the next inventory, never as proof of the payload.

## Forensic / Blue-Team Perspective (DFIR analyst)

Public source maps are a build-pipeline hardening finding: they disclose development structure to every visitor.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | The recovery reads exactly what was exposed, then decides how much it is worth. |

## Tools

- curl
- browser devtools
- webcrack
- [wget](../tools/CTFTTOU-318.md)

## References

- <https://github.com/j4k0xb/webcrack>
- Add challenge write-up link
