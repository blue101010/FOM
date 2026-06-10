# CTFTTE-CLD-003 — Instance metadata service exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-003`](../countertechniques/CTFTCTE-CLD-003.md) — Retrieve credentials via SSRF to IMDS

---

## How the challenge author hides

An SSRF-able app sits beside the metadata endpoint holding role credentials.

## ATT\&CK Complementarity

Complements T1552.005 (Cloud Instance Metadata API) with the SSRF retrieval recipe.

## Tools

- curl
- Burp Suite
- awscli

## References

- Add challenge write-up link