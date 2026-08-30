# CTFTCTE-BLK-003 — Decompile EVM bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-003`](../techniques/CTFTTE-BLK-003.md) — Unverified-bytecode logic hiding

---

## Offensive Recovery (CTF practitioner / solver)

Decompile the deployed bytecode to recover the function logic and the flag condition.

## Forensic / Blue-Team Perspective (DFIR analyst)

A decompilation report makes the on-chain logic auditable despite missing source.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1140 | Deobfuscate/Decode Files or Information | EVM decompilation echoes deobfuscation. |

## Tools

- heimdall-rs
- panoramix
- evm disassemblers

## References

- Add challenge write-up link