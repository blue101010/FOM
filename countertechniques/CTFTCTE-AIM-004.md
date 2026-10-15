# CTFTCTE-AIM-004 — Safely inspect serialized model files

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-004`](../techniques/CTFTTE-AIM-004.md) — Malicious / opaque serialized model

---

## Offensive Recovery (CTF practitioner / solver)

Statically inspect the serialized opcodes without executing them to recover content.

## Forensic / Blue-Team Perspective (DFIR analyst)

Opcode-level inspection documents embedded payloads without triggering them.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Malicious serialized models echo public-app exploitation on ML serving endpoints. |

## Tools

- [fickling](../tools/CTFTTOU-045.md)
- [python](../tools/CTFTTOU-050.md) [pickletools](../tools/CTFTTOU-046.md)

## References

- <https://github.com/trailofbits/fickling>
- Add challenge write-up link