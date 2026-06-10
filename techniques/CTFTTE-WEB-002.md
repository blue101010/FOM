# CTFTTE-WEB-002 — IDOR / predictable object obscurity

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-002`](../countertechniques/CTFTCTE-WEB-002.md) — Enumerate insecure direct object references

---

## How the challenge author hides

The flag belongs to another object/user reachable by guessing an ID the UI never exposes.

## ATT\&CK Complementarity

No direct ATT&CK technique; web authorization-flaw craft.

## Tools

- Burp Suite
- python requests

## References

- Add challenge write-up link