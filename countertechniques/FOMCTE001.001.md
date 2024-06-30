# FOMCTE001.001 -  Recover legitimate header signature of an OpenEXR image file

## Tactics

[FOM tactics](https://github.com/blue101010/FOM/blob/main/tactics/tactics.md)

| FOM related tactics  |
| --------------------------------------- |
| [FOMTA001](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md) - Binary hexadecimal format modifications   |

## Sub-techniques related

| FOM related  Sub-techniquesIDs and names|
| ------------------------------------------------------------ |
| [FOMTE001.001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMTE001.001.md)         |

## Counter-techniques related

| FOM related  Sub-Counter-techniques IDs and names|
| ------------------------------------------------------------ |
| [FOMCTE001.001 - Recover OpenEXR magic signature](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.001.md)         |

## Tools

Recover the legitimate "magic number" header signature of the OpenEXR bitmap image format with hexadecimals tools like:

| Related tools|
| ------------------------------------------------------------ |
| [FOMTOU001](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU001.md) - hexed.it |
| **imhex**  <https://github.com/WerWolv/ImHex> (provide templating colorization of formats) |

## Details and procedures

Fix the legitimate magic header for an EXR file (1) with [FOMTOU001 - hexed.it](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU001.md)

|Hex Signature | ASCII Signature | File Extension | File Description      |
|--------------|-----------------|----------------| ----------------------|
|76 2F 31 01   |                 | EXR            | [OpenEXR](https://openexr.com/en/latest) bitmap image format |


## Writeups and Sources

- (1) [garykessler.net. (2024, January 13). GCK'S FILE SIGNATURES TABLE. Retrieved January 13, 2024.](https://www.garykessler.net/library/file_sigs.html)
- (2) [Asis CTF 2023 - Challenge White and Black with EXR](https://github.com/blue101010/writeups/blob/main/2023/AsisCTF/SOLVED/white_and_blank/analysis/white_and_blank.md)
