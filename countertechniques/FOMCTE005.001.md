# [FOMCTE005.001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE005.001.md) - Repair p_info header on UPX

## Tactics

[FOM tactics](https://github.com/blue101010/FOM/blob/main/tactics/tactics.md)

| FOM related tactics  |
| --------------------------------------- |
| [ |


## Sub-techniques related

| FOM related  Sub-techniques IDs and names|
| ------------------------------------------------------------ |
|  xx   |

## Counter-techniques related


| Counter-techniques ID                                                     | Name       | Description |
| ------------------------------------------------------------ | ---------- | ----------- |
| [FOMCTE003.001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE003.001.md) | Repair p_info header on UPX| TBC         |


## Tools
TBD


## Details

Some C code to repair corrupt p_info header on UPX! packed malware. It fixes two variants found that are pretty common. There are many other variants that have UPX headers either stripped, or null bytes injected to change offsets that this code does not work on.


## Writeups and Sources

- (1) [akamai-security-research (2024, January 13). UPX Fixer. Retrieved January 13, 2024.](https://github.com/akamai/akamai-security-research/tree/main/UPX)
