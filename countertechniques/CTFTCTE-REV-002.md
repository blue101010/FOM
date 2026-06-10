# CTFTCTE-REV-002 — Unpack and dump the real code

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-002`](../techniques/CTFTTE-REV-002.md) — Packing / runtime self-modification

---

## Offensive Recovery (CTF practitioner / solver)

Run to the original entry point and dump the unpacked image, or statically reverse the stub.

## Forensic / Blue-Team Perspective (DFIR analyst)

Memory dumping recovers the true payload that on-disk static analysis could not see.

## Tools

- upx
- x64dbg+Scylla
- Ghidra
- volatility3

## References

- Add challenge write-up link