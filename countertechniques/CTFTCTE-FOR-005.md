# CTFTCTE-FOR-005 — Recover secrets from a memory image

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-005`](../techniques/CTFTTE-FOR-005.md) — Memory-resident artifact concealment

---

## Offensive Recovery (CTF practitioner / solver)

Profile the dump, list processes, scan for strings/patterns, and dump the owning process's address space.

## Forensic / Blue-Team Perspective (DFIR analyst)

Volatility plugins reconstruct process lists, network state, command history and injected regions to locate transient secrets.

## Tools

- volatility3
- strings
- yara
- bulk_extractor

## References

- https://github.com/volatilityfoundation/volatility3
- Add challenge write-up link