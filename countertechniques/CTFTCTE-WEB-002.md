# CTFTCTE-WEB-002 — Enumerate insecure direct object references

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-002`](../techniques/CTFTTE-WEB-002.md) — IDOR / predictable object obscurity

---

## Offensive Recovery (CTF practitioner / solver)

Iterate identifiers/parameters to access objects outside the intended scope.

Then widen the same instrument to identities: hold method, path and body fixed
and replay one request definition across every session you hold, plus the
anonymous case. Record status, length and a normalized body hash per variant.
The object axis finds another subject's data; the identity axis finds the same
function still served to a lesser role (the boundary with the function-level
authorization pair is that here the function itself was always legitimate).

## Forensic / Blue-Team Perspective (DFIR analyst)

Sequential access to non-owned IDs in logs is the signature of IDOR abuse.
Sequences that walk an ID space from one identity, or the same object fetched by
two identities, are the two shapes to query for: the first is enumeration, the
second is a missing ownership check on a populated response.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | IDOR abuse echoes unauthorized data access from repositories. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — one request swept across session token jars, with per-variant status, length and body diff
- Burp Suite
- python requests
- [wfuzz](../tools/CTFTTOU-314.md)

## References

- Add challenge write-up link