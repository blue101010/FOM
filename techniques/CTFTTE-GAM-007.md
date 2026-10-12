# CTFTTE-GAM-007 — Interactive object hidden in a page scene

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-007`](../countertechniques/CTFTCTE-GAM-007.md) — Inventory per-page assets and enumerate interactions

---

## How the challenge author hides

A challenge machine or object is embedded in the decorative imagery of a linked page: the solver must move into the scene and press an interaction key (example a displayed `Press E`) to activate it. The DOM may expose easter-egg text, but the real surface is the interactive object and the assets it then loads. The route is public — the interaction is the gate.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | The artifact is hidden in visible scenery, recoverable only through interaction — a browser-specific concealment. |

## Tools

- browser devtools
- Playwright
- asset crawlers with per-page inventory

## References

- <https://playwright.dev/>
- Add challenge write-up link
