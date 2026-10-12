# CTFTTE-WEB-020 — Uniform soft-404 / deceptive HTTP responses

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-020`](../countertechniques/CTFTCTE-WEB-020.md) — Fingerprint HTTP responses against a baseline

---

## How the challenge author hides

Every missing path returns an identical body (same bytes, same length), so diff-less discovery cannot distinguish a real route from a soft 404. Redirect chains between bare domain and `www` create browser CORS false negatives, and standard edge responses (RFC 8164 endpoints, generic provider pages) look like findings. The real route drowns in uniform noise.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1036 | Masquerading | A uniform error page masquerades as "no route exists"; edge-standard replies masquerade as challenge content. |

## Tools

- curl
- httpx
- ffuf (auto-calibration baseline)

## References

- <https://github.com/ffuf/ffuf>
- Add challenge write-up link
