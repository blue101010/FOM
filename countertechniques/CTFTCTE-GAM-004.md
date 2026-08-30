# CTFTCTE-GAM-004 — Patch the jump / comparison to force a win state

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-004`](../techniques/CTFTTE-GAM-004.md) — Game binary win-condition bypass

---

## Offensive Recovery (CTF practitioner / solver)

Decompile the game binary, locate the win-condition comparison (e.g. `cmp score, 0x7FFFFFFF`), and patch the conditional jump to an unconditional one — or NOP the comparison so the branch is always taken.

## Forensic / Blue-Team Perspective (DFIR analyst)

Binary patching to bypass integrity checks follows the same technique used to crack license checks; production software should use code signing and runtime integrity verification to detect patched executables.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1055 | Process Injection | Memory patching to force a win state. |

## Tools

- ghidra / ida
- binary patching scripts
- pwntools

## References

- Add challenge write-up link
