# CTFTCTE-WEB-004 — Extract data via blind injection

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-004`](../techniques/CTFTTE-WEB-004.md) — Blind / WAF-evaded SQL injection

---

## Offensive Recovery (CTF practitioner / solver)

Use boolean/time-based inference with WAF-evasion encodings to extract the value.

Automate against the **oracle**, not against the payload vocabulary: define the
signal that distinguishes true from false (status, body length, normalized body
hash, response time) and let each request answer a single bit. A WAF-evaded
payload that leaves the oracle unchanged is indistinguishable from a blocked one,
so record the delta of every attempt and discard the variants that produced none
— otherwise the search space grows while the information rate stays at zero.

## Forensic / Blue-Team Perspective (DFIR analyst)

Many near-identical timed/parametric requests in logs indicate blind extraction.
The tell is regularity under variation: one parameter changing across hundreds of
requests, a body length that alternates between two clusters, and a per-request
timing distribution that is bimodal rather than natural.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | ATT&CK has no SQLi technique; public-application exploitation is the closest echo. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — parallel delivery of one parameter across payloads, with the response diff as the oracle per attempt
- sqlmap
- Burp Suite

## References

- Add challenge write-up link