# CTFTCTE-CRY-006 — Unwrap chained encodings

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-006`](../techniques/CTFTTE-CRY-006.md) — Nested encoding obfuscation

---

## Offensive Recovery (CTF practitioner / solver)

Detect each encoding by alphabet/padding and decode iteratively until plaintext appears.

## Forensic / Blue-Team Perspective (DFIR analyst)

An encoding chain is recoverable without a key and is distinguished from genuine encryption.

## Tools

- CyberChef (Magic)
- python base64/codecs

## References

- https://gchq.github.io/CyberChef/
- Add challenge write-up link