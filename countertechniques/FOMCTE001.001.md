# FOMCTE001.001 -  Recover legitimate header signature of an OpenEXR image file

## Tactics

[FOM tactics](https://github.com/blue101010/FOM/blob/main/tactics/tactics.md)

| FOM related tactics  |
| --------------------------------------- |
| [FOMTA001](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md) - Binary hexadecimal format modifications   |


- Related sub-Techniques:
    - N/A
- Related Counter-Techniques:
    - [FOMCTE001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.md)

## Details

Recover the legitimate "magic number" header signature of the OpenEXR bitmap image format with hexadecimals tools like:

- https://hexed.it/
- **imhex**  <https://github.com/WerWolv/ImHex> (provide templating colorization of formats)


Fix the legitimate magic header for an EXR file . Reference: (1)

|Hex Signature | ASCII Signature | File Extension | File Description
|--------------|-----------------|--------| ----------------------|
|76 2F 31 01   |                 | EXR    | [OpenEXR](https://openexr.com/en/latest) bitmap image format |


## Writeups and Sources

- (1) [garykessler.net. (2024, January 13). GCK'S FILE SIGNATURES TABLE. Retrieved January 13, 2024.](https://www.garykessler.net/library/file_sigs.html)
- (2) [Asis CTF 2023 - Challenge White and Black with EXR](https://github.com/blue101010/writeups/blob/main/2023/AsisCTF/SOLVED/white_and_blank/analysis/white_and_blank.md)
