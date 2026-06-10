# CTFTTE-FOR-001 — Magic-byte / file-signature tampering

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-001`](../countertechniques/CTFTCTE-FOR-001.md) — Recover the legitimate file signature

---

## How the challenge author hides

The author corrupts or swaps the file's magic header (e.g. flips PNG 89504E47 to a bogus value) so type detection and viewers fail.

## ATT\&CK Complementarity

Closest ATT&CK context is T1027 (Obfuscated Files), but ATT&CK omits the byte-level magic-header recovery detail that defines this CTF technique.

## Tools

- xxd / hexedit
- file
- binwalk
- python struct

## References

- https://www.garykessler.net/library/file_sigs.html
- Add challenge write-up link