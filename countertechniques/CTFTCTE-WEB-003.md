# CTFTCTE-WEB-003 — Forge or downgrade a JSON Web Token

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-003`](../techniques/CTFTTE-WEB-003.md) — JWT misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Strip/replace the algorithm, crack the secret, or perform RS256->HS256 confusion to forge a token.

## Forensic / Blue-Team Perspective (DFIR analyst)

Token validation logs reveal accepted tokens with unexpected alg/signature.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1606 | Forge Web Credentials | JWT misconfiguration echoes web credential forgery. |

## Tools

- jwt_tool
- hashcat
- CyberChef

## References

- https://github.com/ticarpi/jwt_tool
- Add challenge write-up link