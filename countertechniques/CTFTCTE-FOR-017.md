# CTFTCTE-FOR-017 — Recover text data strings from ELF binary

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-017`](../techniques/CTFTTE-FOR-017.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Recover text data strings from ELF binary with tools like
- strings (linux)

## Forensic / Blue-Team Perspective (DFIR analyst)

_See sources and writeups for forensic analysis context._

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Strings concealed in ELF binaries echo obfuscated payloads. |

## Tools

| Related tools |
| --------------------------------------- |
| linux strings  |

## References

**Writeups**

- (1) [LEVELEFFECTCDA2024 snek challenge](https://github.com/blue101010/writeups/tree/main/2024/LEVELEFFECTCDA2024/Forensics/snek)
