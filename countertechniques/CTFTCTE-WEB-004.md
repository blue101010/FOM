# CTFTCTE-WEB-004 — Extract data via blind injection

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-004`](../techniques/CTFTTE-WEB-004.md) — Blind / WAF-evaded SQL injection

---

## Offensive Recovery (CTF practitioner / solver)

Use boolean/time-based inference with WAF-evasion encodings to extract the value.

## Forensic / Blue-Team Perspective (DFIR analyst)

Many near-identical timed/parametric requests in logs indicate blind extraction.

## Tools

- sqlmap
- Burp Suite

## References

- Add challenge write-up link