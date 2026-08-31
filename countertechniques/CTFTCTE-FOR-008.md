# CTFTCTE-FOR-008 — Recover legitimate header signature of an OpenEXR image file

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-008`](../techniques/CTFTTE-FOR-008.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Fix the legitimate magic header for an EXR file (1) with `FOMTOU001` (FOM) -> [CTFTTOU-001](../tools/CTFTTOU-001.md) - hexed.it

|Hex Signature | ASCII Signature | File Extension | File Description      |
|--------------|-----------------|----------------| ----------------------|
|76 2F 31 01   |                 | EXR            | [OpenEXR](https://openexr.com/en/latest) bitmap image format |

## Forensic / Blue-Team Perspective (DFIR analyst)

_See sources and writeups for forensic analysis context._

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | ATT&CK omits the byte-level header-recovery detail. |

## Tools

| Useful tools|
| ------------------------------------------------------------ |
| `FOMTOU001` (FOM) -> [CTFTTOU-001](../tools/CTFTTOU-001.md) - hexed.it  |
| `FOMTOU002` (FOM) -> [CTFTTOU-002](../tools/CTFTTOU-002.md) - imhex |

Recover the legitimate "magic number" header signature of the OpenEXR bitmap image format with hexadecimals tools.

## References

**Writeups**

- (1) [garykessler.net. (2024, January 13). GCK'S FILE SIGNATURES TABLE. Retrieved January 13, 2024.](https://www.garykessler.net/library/file_sigs.html)
- (2) [Asis CTF 2023 - Challenge White and Black with EXR](https://github.com/blue101010/writeups/blob/main/2023/AsisCTF/SOLVED/white_and_blank/analysis/white_and_blank.md)
