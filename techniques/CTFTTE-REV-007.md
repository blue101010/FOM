# CTFTTE-REV-007 — Python bytecode (.pyc/.pyo) concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-007`](../countertechniques/CTFTCTE-REV-007.md) — Decompile Python bytecode

---

## How the challenge author hides

Only compiled .pyc/.pyo files ship; the flag logic is bytecode-only.

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
- Add challenge write-up link
