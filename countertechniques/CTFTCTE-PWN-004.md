# CTFTCTE-PWN-004 — Build a ROP chain from available gadgets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-004`](../techniques/CTFTTE-PWN-004.md) — Stripped/static gadget search

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate gadgets and assemble a ROP chain to call execve or print the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

The chain shows how existing code was repurposed despite NX/no convenient symbols.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1211 | Exploitation for Defense Evasion | ROP-chain construction bypasses mitigations ATT&CK does not model. |

## Tools

- ROPgadget
- ropper
- pwntools

## References

- https://github.com/JonathanSalwan/ROPgadget
- Add challenge write-up link