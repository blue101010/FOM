# CTFTTE-MOB-007 — Memory-only encryption keys

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-007`](../countertechniques/CTFTCTE-MOB-007.md) — Dump memory with Frida to extract keys

---

## How the challenge author hides

Encryption keys are never stored on disk; they are generated or loaded at runtime and exist only in process memory, making them invisible to static analysis.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Credentials in Files | Memory-only keys evade file-based analysis. |

## Tools

- Frida
- objection

## References

- <https://frida.re/>
- Add challenge write-up link
