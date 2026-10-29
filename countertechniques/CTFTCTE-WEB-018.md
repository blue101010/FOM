# CTFTCTE-WEB-018 — Capture pre-load browser traffic and correlate interactions

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-018`](../techniques/CTFTTE-WEB-018.md) — Interaction-gated asset loading

---

## Offensive Recovery (CTF practitioner / solver)

Instrument the browser before `page.goto()`: subscribe to requests, responses, failures, WebSockets, console errors, DOM mutations and storage writes; drive the page by clicking, pressing keys and moving into scenes; correlate every interaction with the assets it triggers.

Keep a second, independent record at the proxy. In-process instrumentation dies
with the script, whereas proxied traffic stays addressable by request id after the
session ends — which is what makes the correlation re-readable, and what lets a
passive rule set run over the gated burst later. When an exchange must be examined
mid-flight, hold the queue rather than re-running the scenario: a paused intercept
is reversible, a lost click sequence is not.

## Forensic / Blue-Team Perspective (DFIR analyst)

Proxy or RUM logs that join user interactions with subsequent asset fetches show what surfaced only after engagement.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1564 | Hide Artifacts | Recovery is the browser-side interaction audit ATT&CK does not model. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — proxy-side recording of the interaction-gated burst, addressable by request id after the browser closes
- Playwright
- browser devtools
- mitmproxy

## References

- <https://playwright.dev/>
- Add challenge write-up link
