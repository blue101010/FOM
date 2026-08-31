# CTFTTE-FOR-017 — Conceal text data strings in ELF binary

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-017`](../countertechniques/CTFTCTE-FOR-017.md)  

---

## How the challenge author hides

Conceal text data strings in ELF binary.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Strings concealed in ELF binaries echo obfuscated payloads. |

## Tools

| Related tools |
| --------------------------------------- |
| `FOMTA008` (FOM) -> [CTFT-TA-FOR](../tactics/CTFT-TA-FOR.md) - Conceal data in binary format   |

## References

## Tactics

[CTFT correlation matrix](../CORRELATION.md)

| FOM related tactics  |
| --------------------------------------- |
| `FOMTA008` (FOM) -> [CTFT-TA-FOR](../tactics/CTFT-TA-FOR.md) - Conceal data in binary format   |

## Techniques And Counter-Techniques

| Related Techniques IDs and names  | Counter-Techniques names and descriptions  |
| -----------------------------------|  -----------------------------------------|
| `FOMTE013` (FOM, superseded) |  `FOMCTE011` (FOM) -> [CTFTCTE-FOR-017](../countertechniques/CTFTCTE-FOR-017.md) - Recover text data strings from ELF binary                                        |

**Writeups**

- (1) [LEVELEFFECTCDA2024 snek challenge](https://github.com/blue101010/writeups/tree/main/2024/LEVELEFFECTCDA2024/Forensics/snek)
