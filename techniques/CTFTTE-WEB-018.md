# CTFTTE-WEB-018 — Interaction-gated asset loading

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-018`](../countertechniques/CTFTCTE-WEB-018.md) — Capture pre-load browser traffic and correlate interactions

---

## How the challenge author hides

The page itself is public and linked, but the key modules, JSON configuration or data files load only after an explicit interaction — keypress, click, hover or movement into a scene — so link crawlers, `curl` and asset extractors never see them. The challenge surface sits behind the interaction, not behind the route.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | Deferred, interaction-conditional loading echoes artifact hiding; ATT&CK omits the browser-side trigger detail. |

## Tools

- Playwright
- browser devtools
- Katana

## References

- <https://playwright.dev/>
- <https://github.com/projectdiscovery/katana>
- Add challenge write-up link
