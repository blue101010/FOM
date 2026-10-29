# CTFTCTE-WEB-012 — Craft XSS payloads (stored/reflected/DOM)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-012`](../techniques/CTFTTE-WEB-012.md) — XSS-driven flag exfiltration

---

## Offensive Recovery (CTF practitioner / solver)

Craft stored/reflected/DOM payloads that read the flag and exfiltrate it.

Two instrument-side habits shorten this materially. First, **find the sink before
writing the payload**: a passive rule that reports any query value echoed verbatim
into the response turns sink discovery into a ranked list, and a reflection is the
cheapest evidence that a context is injectable. Second, **host the payload from the
instrument**: when the exfiltration has to reach a page you control, serve it from
the recording proxy's own file host so the callback lands in the same history as
the request that triggered it, instead of in an origin you cannot read afterwards.

## Forensic / Blue-Team Perspective (DFIR analyst)

XSS artifacts live in page source, logs and browser history; CSP reports corroborate.
Reflected payloads leave the value in the access log of the victim page and in the
`Referer` of the callback; stored payloads leave the write in the create/update
audit trail, which is the only place the author identity survives.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.007 | JavaScript | Browser-executed script craft; ATT&CK omits XSS mechanics. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — reflection canaries as passive rules, and a hosted file as the exfiltration endpoint inside the same recorded history
- [Caido workflow catalogue](../tools/CTFTTOU-442.md) ([CTFTTOU-442](../tools/CTFTTOU-442.md)) — reflection and cookie-hygiene rules that locate the injectable context
- Burp Suite
- browser devtools
- [XSStrike](../tools/CTFTTOU-317.md)

## References

- <https://portswigger.net/web-security/cross-site-scripting>
- Add challenge write-up link
