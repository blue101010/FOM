# CTFTCTE-STE-005 — Decode invisible-character payloads

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-005`](../techniques/CTFTTE-STE-005.md) — Zero-width / whitespace text steganography

---

## Offensive Recovery (CTF practitioner / solver)

Normalize/inspect code points and map zero-width sequences back to bits/characters.

## Forensic / Blue-Team Perspective (DFIR analyst)

Unicode code-point inspection reveals non-printing characters that should not appear in plain prose.

## Tools

- CyberChef
- python unicodedata
- stegcloak-style decoders

## References

- https://gchq.github.io/CyberChef/
- Add challenge write-up link