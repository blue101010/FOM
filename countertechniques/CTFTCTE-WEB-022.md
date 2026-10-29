# CTFTCTE-WEB-022 — Enumerate and triage source maps

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-022`](../techniques/CTFTTE-WEB-022.md) — Public source-map bait

---

## Offensive Recovery (CTF practitioner / solver)

Request the referenced `.map` for every asset; recover the original sources; classify each as structural (styles, section names) or functional (logic, endpoints, data). Treat section vocabulary as hint material for the next inventory, never as proof of the payload.

Do not walk the asset list by hand: derive it from the recorded sitemap, then run
a passive rule that reports source-map references and map-shaped paths, so the
mapping between assets and their maps is a table rather than a search. A map that
is referenced but returns a uniform refusal is the soft-404 case, not a missing
asset — classify it that way before spending time on it.

## Forensic / Blue-Team Perspective (DFIR analyst)

Public source maps are a build-pipeline hardening finding: they disclose development structure to every visitor.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | The recovery reads exactly what was exposed, then decides how much it is worth. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — sitemap as the asset inventory, plus a passive rule for map references
- curl
- browser devtools
- webcrack
- [wget](../tools/CTFTTOU-318.md)

## References

- <https://github.com/j4k0xb/webcrack>
- Add challenge write-up link
