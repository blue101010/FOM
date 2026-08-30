# CTFTTE-CLD-003 — Instance metadata service exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-003`](../countertechniques/CTFTCTE-CLD-003.md) — Retrieve credentials via SSRF to IMDS

---

## How the challenge author hides

An SSRF-able app sits beside the metadata endpoint holding role credentials.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.005 | Cloud Instance Metadata API | IMDS credential retrieval. |

## Tools

- curl
- Burp Suite
- awscli

## References

- Add challenge write-up link