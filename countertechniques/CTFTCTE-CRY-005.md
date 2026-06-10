# CTFTCTE-CRY-005 — Forge data via length extension

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-005`](../techniques/CTFTTE-CRY-005.md) — Hash length-extension exposure

---

## Offensive Recovery (CTF practitioner / solver)

Use a length-extension tool with the known digest and length to forge a valid extended message.

## Forensic / Blue-Team Perspective (DFIR analyst)

The vulnerability report attributes forgery to the insecure secret-prefix MAC construction.

## Tools

- hashpump
- hash_extender

## References

- https://github.com/iagox86/hash_extender
- Add challenge write-up link