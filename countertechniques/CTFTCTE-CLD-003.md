# CTFTCTE-CLD-003 — Retrieve credentials via SSRF to IMDS

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-003`](../techniques/CTFTTE-CLD-003.md) — Instance metadata service exposure

---

## Offensive Recovery (CTF practitioner / solver)

Force a request to the metadata endpoint and harvest temporary credentials.

## Forensic / Blue-Team Perspective (DFIR analyst)

Metadata requests from an application context flag SSRF-to-IMDS abuse.

## Tools

- curl
- Burp Suite
- awscli

## References

- Add challenge write-up link