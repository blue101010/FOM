# CTFTCTE-BLK-003 — Decompile EVM bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-003`](../techniques/CTFTTE-BLK-003.md) — Unverified-bytecode logic hiding

---

## Offensive Recovery (CTF practitioner / solver)

Decompile the deployed bytecode to recover the function logic and the flag condition.

## Forensic / Blue-Team Perspective (DFIR analyst)

A decompilation report makes the on-chain logic auditable despite missing source.

## Tools

- heimdall-rs
- panoramix
- evm disassemblers

## References

- Add challenge write-up link