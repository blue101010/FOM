# CTFTTE-REV-002 — Packing / runtime self-modification

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-002`](../countertechniques/CTFTCTE-REV-002.md) — Unpack and dump the real code

---

## How the challenge author hides

Code is packed (UPX/custom) or decrypts itself at runtime so static strings/logic are hidden.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027.002 | Software Packing | Packing / runtime self-modification. |

## Tools

- upx
- x64dbg+Scylla
- Ghidra
- volatility3

## References

- Add challenge write-up link