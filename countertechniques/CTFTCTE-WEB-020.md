# CTFTCTE-WEB-020 — Fingerprint HTTP responses against a baseline

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-020`](../techniques/CTFTTE-WEB-020.md) — Uniform soft-404 / deceptive HTTP responses

---

## Offensive Recovery (CTF practitioner / solver)

Record per URL: initial and final URL, redirect chain, status, content-type, size, normalized body hash, title, server, timings, and the test origin (browser vs CLI client). Compare against a random route and a random hostname; classify as unique content, redirect, soft 404, uniform refusal, standard edge response, CORS-only false negative, or timeout.

## Forensic / Blue-Team Perspective (DFIR analyst)

Edge and origin logs distinguish real 404s from soft 404s; uniform error pages are a hardening finding for WAF misconfiguration.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1036 | Masquerading | Baseline comparison is the detection of the masquerade. |

## Tools

- curl
- httpx
- ffuf (auto-calibration baseline)
- Playwright

## References

- <https://github.com/ffuf/ffuf>
- Add challenge write-up link
