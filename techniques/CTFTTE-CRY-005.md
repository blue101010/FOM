# CTFTTE-CRY-005 — Hash length-extension exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-005`](../countertechniques/CTFTCTE-CRY-005.md) — Forge data via length extension

---

## How the challenge author hides

A MAC built as H(secret || message) with a Merkle-Damgard hash lets an attacker append data.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; hash length-extension forgery craft. |

## Tools

- hashpump
- hash_extender

## References

- <https://github.com/iagox86/hash_extender>
- Add challenge write-up link