# CTFTCTE-WEB-005 — Exploit template evaluation

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-005`](../techniques/CTFTTE-WEB-005.md) — Server-side template injection

---

## Offensive Recovery (CTF practitioner / solver)

Fingerprint the engine, then escalate from expression evaluation to file read or RCE.

## Forensic / Blue-Team Perspective (DFIR analyst)

Template-syntax payloads in request logs identify the injection vector.

## Tools

- tplmap
- Burp Suite

## References

- Add challenge write-up link