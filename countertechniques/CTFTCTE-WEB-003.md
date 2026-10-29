# CTFTCTE-WEB-003 — Forge or downgrade a JSON Web Token

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-003`](../techniques/CTFTTE-WEB-003.md) — JWT misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Strip/replace the algorithm, crack the secret, or perform RS256->HS256 confusion to forge a token.

Treat the forged token as a **canary**, not as a one-off: mint one token per
hypothesis (unverified algorithm, empty signature, substituted key, expired
claim) and replay it against every endpoint that reads the token, not only the
one that issued it. A verification path and an unverified path frequently coexist
in one application, and the second is found by replaying the same canary across
the recorded surface. Keep the cookie jar of each attempt separate, otherwise a
refreshed legitimate session masks the forged one.

## Forensic / Blue-Team Perspective (DFIR analyst)

Token validation logs reveal accepted tokens with unexpected alg/signature.
The complementary signal is a token whose claims changed for an identity that did
not re-authenticate, and a single client presenting several token variants inside
a short window — the shape of a canary sweep rather than of normal use.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1606 | Forge Web Credentials | JWT misconfiguration echoes web credential forgery. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — replays each forged variant across the surface with a separate cookie jar per variant, and diffs the answers
- jwt_tool
- hashcat
- CyberChef

## References

- <https://github.com/ticarpi/jwt_tool>
- Add challenge write-up link