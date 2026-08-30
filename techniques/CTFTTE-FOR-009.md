# CTFTTE-FOR-009 — Corrupt Image file magic signature

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-009`](../countertechniques/CTFTCTE-FOR-009.md)  

---

## How the challenge author hides

Modify or Corrupt legitimate magic headers of an image file.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | ATT&CK omits the byte-level magic-header repair detail. |

## Tools

_See references._

## References

## Tactics

[FOM tactics](https://github.com/blue101010/FOM/blob/main/tactics/tactics.md)

| FOM related tactics  |
| --------------------------------------- |
| [FOMTA001](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md) - Binary hexadecimal format modifications   |

## Fom Related Sub-Techniques (St)

| FOM Sub-techniques ID and description  |
| --------------------------------------- |
| [FOMTE001.001 - Modify legitimate header signature of a file via python script ](https://github.com/blue101010/FOM/blob/main/techniques/FOMTE001.001.md)   |

## Fom Counter-Techniques (Ct)

| FOM Counter-Techniques ID and description  |
| --------------------------------------- |
| [FOMCTE001 - Recover legitimate signature of a file](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.md)   |

**Sources**

- (1) [Jason (jxb5151). (2021, January 28). findapihash.py. Retrieved August 22, 2022.](https://github.com/MITRECND/malchive/blob/main/malchive/utilities/findapihash.py)

**Writeups**

- (1) xxx
