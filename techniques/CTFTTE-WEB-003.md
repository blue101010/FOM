# CTFTTE-WEB-003 — JWT misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-003`](../countertechniques/CTFTCTE-WEB-003.md) — Forge or downgrade a JSON Web Token

---

## How the challenge author hides

The flag sits behind auth using a JWT with alg=none, a weak HMAC secret, or key confusion.

## ATT\&CK Complementarity

No direct ATT&CK technique.

## Tools

- jwt_tool
- hashcat
- CyberChef

## References

- https://github.com/ticarpi/jwt_tool
- Add challenge write-up link