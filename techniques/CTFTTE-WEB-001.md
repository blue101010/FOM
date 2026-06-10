# CTFTTE-WEB-001 — Obscured endpoint / source-comment hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-001`](../countertechniques/CTFTCTE-WEB-001.md) — Content discovery and source review

---

## How the challenge author hides

The flag route is unlinked, hinted in comments, robots.txt, JS bundles or backup files.

## ATT\&CK Complementarity

Complements T1083/T1595 (discovery/recon) but is CTF content-discovery craft.

## Tools

- ffuf
- feroxbuster
- gobuster
- browser devtools

## References

- https://github.com/ffuf/ffuf
- Add challenge write-up link