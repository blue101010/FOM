# CTFTTE-MOB-002 — Native-library logic hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-002`](../countertechniques/CTFTCTE-MOB-002.md) — Reverse the native .so

---

## How the challenge author hides

Sensitive logic is pushed into a compiled native library to evade Java-level inspection.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1406 | Obfuscated Files or Information (Mobile) | Native-library logic hiding. |

## Tools

- Ghidra
- IDA
- jadx

## References

- Add challenge write-up link