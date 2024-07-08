# FOMCTE001 - Recover legitimate signature of a file

## Tactics

[FOM tactics](https://github.com/blue101010/FOM/blob/main/tactics/tactics.md)

| FOM related tactics  |
| --------------------------------------- |
| [FOMTA001 - Binary hexadecimal format modifications](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md)    |

## Sub-techniques related

| FOM related  Sub-techniques IDs and names                   |
| ------------------------------------------------------------ |
| [FOMTE001.001 - Modify legitimate header signature of a file via python script](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMTE001.001.md)         |

## Counter-techniques related

| FOM related  Sub-Counter-techniques IDs and names|
| ------------------------------------------------------------ |
| [FOMCTE001.001 - Recover OpenEXR magic signature](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.001.md)         |

## Details

Recover legitimate signature of a file, often called magic headers.
Magic headers, also known as file signatures, are specific byte sequences located at the beginning of a file that help identify the file type.
These headers are used by operating systems and applications to determine how to process or open a file.

## Writeups and Sources

- (1) [Joep van Steen. (2021, Mars 23). Some thoughts on signature based file recovery. Retrieved January 14, 2024.](https://www.disktuna.com/some-thoughts-on-signature-based-file-recovery/)
- (2) [GCK'S FILE SIGNATURES TABLE](https://www.garykessler.net/library/file_sigs.html)
- (3) [2024 - LEVELEFFECTCDA2024 - Forensics - Magic repairman](https://github.com/blue101010/writeups/blob/main/2024/LEVELEFFECTCDA2024/Forensics/Magic_repairman/README.md)
