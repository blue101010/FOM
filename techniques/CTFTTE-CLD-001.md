# CTFTTE-CLD-001 — Misconfigured object-storage exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-001`](../countertechniques/CTFTCTE-CLD-001.md) — Enumerate and list public buckets

---

## How the challenge author hides

The flag object sits in a world-readable or weakly-named bucket the author assumes is private.

## ATT\&CK Complementarity

Complements T1530 (Data from Cloud Storage) with CTF enumeration procedure.

## Tools

- awscli
- s3scanner
- gcsbucketbrute

## References

- Add challenge write-up link