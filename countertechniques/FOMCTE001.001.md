# FOMCTE001.001 -  Recover legitimate header signature of an OpenEXR image file

Recover the legitimate "magic number" header signature of the OpenEXR bitmap image format with hexadecimals tools like:

- https://hexed.it/
- imhex  <https://github.com/WerWolv/ImHex> (provide templating colorization of formats)

The legitimate magic header for an EXR file is (1): 

|Hex Signature | ASCII Signature | File Extension | File Description
|--------------|-----------------|--------| ----------------------|
|76 2F 31 01   |                 | EXR    | [OpenEXR](https://openexr.com/en/latest) bitmap image format |


## Details

- ID: [FOMCTE001 - Recover legitimate signature of a file](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.001.md)
- Related Sub-techniques:
    - [FOMCTE001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.md)
- Related Tactics:
    - [FOMTA001 - Modify legitimate signature of a file](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md)

## Writeups and Sources

- (1) [garykessler.net. (2024, January 13). GCK'S FILE SIGNATURES TABLE. Retrieved January 13, 2024.](https://www.garykessler.net/library/file_sigs.html)
- (2) [Asis CTF 2023 - Challenge White and Black with EXR](https://github.com/blue101010/writeups/blob/main/2023/AsisCTF/SOLVED/white_and_blank/analysis/white_and_blank.md)
