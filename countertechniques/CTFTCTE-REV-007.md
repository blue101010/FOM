# CTFTCTE-REV-007 — Decompile Python bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-007`](../techniques/CTFTTE-REV-007.md) — Python bytecode (.pyc/.pyo) concealment

---

## Offensive Recovery (CTF practitioner / solver)

Disassemble (dis/pycdc), decompile (uncompyle6/decompyle3), and recover the logic.

## Forensic / Blue-Team Perspective (DFIR analyst)

Bytecode analysis works without running the interpreter; marshal headers reveal the Python version.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Compiled-only distribution hides logic. |

## Tools

- pycdc
- uncompyle6
- decompyle3
- dis

## References

- <https://github.com/zrax/pycdc>

