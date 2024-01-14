# Repair p_info header on UPX

Some C code to repair corrupt p_info header on UPX! packed malware. It fixes two variants found that are pretty common. There are many other variants that have UPX headers either stripped, or null bytes injected to change offsets that this code does not work on.

# Details
- ID: FOMCTE001.002
- Sub-technique of: [FOMCTE001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.md)
- Tactic: [Modify legitimate signature of a file](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md)


# Sources 
- [akamai-security-research (2024, January 13). UPX Fixer. Retrieved January 13, 2024.](https://github.com/akamai/akamai-security-research/tree/main/UPX)
