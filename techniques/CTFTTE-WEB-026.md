# CTFTTE-WEB-026 — Signal buried in a high-volume response corpus

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-026`](../countertechniques/CTFTCTE-WEB-026.md) — Sweep every captured response with passive detection rules and triage the findings

---

## How the challenge author hides

Nothing is protected and nothing is misrouted: every exchange the player can
capture is a legitimate response to a legitimate request. The concealment is
**volume and monotony** — the answer sits where human review cannot reach at
review speed, and the interface is designed so that nobody scrolls there.

The player is expected to map "interesting" traffic (the login, the API, the
admin panel) and to ignore the long tail: the assets, the repeated list pages,
the headers, the fields rendered nowhere. The target signal is in that tail.

Design variants, in increasing subtlety:

- **Position past the truncation point.** The value lives deep inside a large
  body, after the byte count any comfortable reader cuts at.
- **Header-only carriage.** The signal travels in a custom header, in `ETag`, a
  timing header, a cookie comment, a `103` early hint, or a trailer chunk that
  no browser tab ever shows.
- **Statistical needle.** Hundreds of near-identical responses, one of which
  differs by a token, a length or a single character — invisible by inspection,
  obvious by comparison.
- **Fragment per response.** One piece per exchange; the artefact is the ordered
  concatenation, not any single page.
- **Encoded value inside a rendered field.** A base64, hex, escaped or JWT-shaped
  string inside a JSON property the page never draws.
- **Comment or asset payload.** The value is inside a static asset, a source
  comment, an inline script or a `data:` blob loaded by an otherwise ordinary page.

Boundary: choosing **which** path to ask for is the obscured-endpoint pair;
judging whether another user's object is reachable is the IDOR pair; deciding
whether a hidden object exists behind a filtered list is the introspection pair.
Here the access is already granted and the only obstacle is where to look.

## Indicators

- a prompt that says, or implies, "somewhere in the traffic", "keep an eye on the
  responses", or hands over a capture rather than a URL
- an endpoint family returning the same shape hundreds of times (feeds, lists,
  search pages, sitemaps)
- a response noticeably larger than the interface uses, or a page whose rendered
  content ends well before its body does
- an uncommon or challenge-specific response header next to conventional ones
- truncation marks in what you were given (`…`, `[cut]`, a byte-count column)
- an assertion in the narrative about what "the app does not show"

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The signal is present but not legible at the granularity a human reviews. |
| T1213 | Data from Information Repositories | Recovery reads what an ordinary bulk retrieval already returned. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — records every exchange, addresses it by request id, and reports rule hits as first-class findings
- [Caido workflow catalogue](../tools/CTFTTOU-442.md) ([CTFTTOU-442](../tools/CTFTTOU-442.md)) — the passive rule set that provides the per-response checks
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — flatten and compare the decoded bodies once a hit is located
- a recursive text searcher over the exported capture, as the last-resort second pass

## References

- <https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>
- <https://www.rfc-editor.org/rfc/rfc9110#section-6.1> (field semantics: what a client is allowed to ignore)
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/>
