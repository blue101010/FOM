# CTFTCTE-FOR-008 — Recover legitimate header signature of an OpenEXR image file

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-008`](../techniques/CTFTTE-FOR-008.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Fix the legitimate magic header for an EXR file (1) with [FOMTOU001 - hexed.it](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU001.md)

|Hex Signature | ASCII Signature | File Extension | File Description      |
|--------------|-----------------|----------------| ----------------------|
|76 2F 31 01   |                 | EXR            | [OpenEXR](https://openexr.com/en/latest) bitmap image format |

## Forensic / Blue-Team Perspective (DFIR analyst)

_See sources and writeups for forensic analysis context._

## Tools

| Useful tools|
| ------------------------------------------------------------ |
| [FOMTOU001 - hexed.it](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU001.md)  |
| [FOMTOU002 - imhex](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU002.md) |

Recover the legitimate "magic number" header signature of the OpenEXR bitmap image format with hexadecimals tools.

## References

**Writeups**

- (1) [garykessler.net. (2024, January 13). GCK'S FILE SIGNATURES TABLE. Retrieved January 13, 2024.](https://www.garykessler.net/library/file_sigs.html)
- (2) [Asis CTF 2023 - Challenge White and Black with EXR](https://github.com/blue101010/writeups/blob/main/2023/AsisCTF/SOLVED/white_and_blank/analysis/white_and_blank.md)
