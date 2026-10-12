# CTFTCTE-GAM-007 — Inventory per-page assets and enumerate interactions

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-007`](../techniques/CTFTTE-GAM-007.md) — Interactive object hidden in a page scene

---

## Offensive Recovery (CTF practitioner / solver)

Build a per-page asset graph (links, scripts, stylesheets, inline JSON, modules) and score each asset by rarity, page-uniqueness, size/entropy anomaly, thematic naming and post-interaction loading — not by expected vocabulary. Enumerate interactable elements and drive them: keys, clicks, hover, movement into scenes.

## Forensic / Blue-Team Perspective (DFIR analyst)

Event analytics document which interactions are reachable; engagement telemetry shows which surface was actually exercised.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | Recovery enumerates interactions instead of URLs. |

## Tools

- browser devtools
- Playwright
- Katana

## References

- <https://playwright.dev/>
- Add challenge write-up link
