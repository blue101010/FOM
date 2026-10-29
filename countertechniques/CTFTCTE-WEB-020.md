# CTFTCTE-WEB-020 — Fingerprint HTTP responses against a baseline

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-020`](../techniques/CTFTTE-WEB-020.md) — Uniform soft-404 / deceptive HTTP responses

---

## Offensive Recovery (CTF practitioner / solver)

Record per URL: initial and final URL, redirect chain, status, content-type, size, normalized body hash, title, server, timings, and the test origin (browser vs CLI client). Compare against a random route and a random hostname; classify as unique content, redirect, soft 404, uniform refusal, standard edge response, CORS-only false negative, or timeout.

Take the baseline from the **same client** that produced the finding: a body that
looks unique through the browser is often a uniform interception page through a
replay client, and the reverse. Then let the instrument do the comparison — two
recorded responses diffed on status, length and normalized hash settle the
classification faster than reading both bodies, and the diff stays attached to
the request ids that produced it.

## Forensic / Blue-Team Perspective (DFIR analyst)

Edge and origin logs distinguish real 404s from soft 404s; uniform error pages are a hardening finding for WAF misconfiguration.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1036 | Masquerading | Baseline comparison is the detection of the masquerade. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — two recorded responses diffed on status, length and normalized hash, with the classification kept beside the request ids
- curl
- httpx
- ffuf (auto-calibration baseline)
- Playwright

## References

- <https://github.com/ffuf/ffuf>
- Add challenge write-up link
