# CTFTTE-BLK-003 — Unverified-bytecode logic hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-003`](../countertechniques/CTFTCTE-BLK-003.md) — Decompile EVM bytecode

---

## How the challenge author hides

No source is published; the author assumes raw bytecode is opaque.

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