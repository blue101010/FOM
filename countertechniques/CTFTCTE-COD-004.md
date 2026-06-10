# CTFTCTE-COD-004 — Craft a minimal polyglot that satisfies every parser

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Counters technique:** [`CTFTTE-COD-004`](../techniques/CTFTTE-COD-004.md) — Code-golf / polyglot code puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Study each parser's grammar and find overlapping syntax: begin with the most restrictive language and layer compatible constructs. Use comments, string literals, and no-op tokens to satisfy parsers that would otherwise reject the code.

## Forensic / Blue-Team Perspective (DFIR analyst)

Polyglot files exploit parser ambiguity; the same technique is used by attackers to craft files that appear benign to one tool but execute as another format, evading content-type-based security controls.

## Tools

- python / bash / perl
- online polyglot references
- xxd / hexdump

## References

- Add challenge write-up link
