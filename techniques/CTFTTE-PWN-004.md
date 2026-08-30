# CTFTTE-PWN-004 — Stripped/static gadget search

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-004`](../countertechniques/CTFTCTE-PWN-004.md) — Build a ROP chain from available gadgets

---

## How the challenge author hides

A stripped, statically linked binary forces a return-oriented chain instead of a simple call.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1211 | Exploitation for Defense Evasion | ROP-chain construction bypasses mitigations ATT&CK does not model. |

## Tools

- ROPgadget
- ropper
- pwntools

## References

- <https://github.com/JonathanSalwan/ROPgadget>
- Add challenge write-up link