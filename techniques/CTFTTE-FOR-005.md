# CTFTTE-FOR-005 — Memory-resident artifact concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-005`](../countertechniques/CTFTCTE-FOR-005.md) — Recover secrets from a memory image

---

## How the challenge author hides

The flag exists only in RAM (process heap, clipboard, decrypted blob) and never touches disk in plaintext.

## ATT\&CK Complementarity

No ATT&CK technique; this is volatile-memory DFIR.

## Tools

- volatility3
- strings
- yara
- bulk_extractor

## References

- https://github.com/volatilityfoundation/volatility3
- Add challenge write-up link