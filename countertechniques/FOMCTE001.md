# Recover legitimate signature of a file
Some C code to repair corrupt p_info header on UPX! packed malware. It fixes two variants found that are pretty common. There are many other variants that have UPX headers either stripped, or null bytes injected to change offsets that this code does not work on

# Details
- ID: FOMCTE001
- Sub-techniques: [FOMCTE001.001](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.001.md),[FOMCTE001.002](https://github.com/blue101010/FOM/blob/main/countertechniques/FOMCTE001.002.md),
- Tactic: [Binary hexadecimal format modifications ](https://github.com/blue101010/FOM/blob/main/tactics/FOMTA001.md),
- Platforms: Linux, Windows, macOS

# Procedure examples

| ID                                                  | Name       | Description |
| --------------------------------------------------- | ---------- | ----------- |
| [C0001](https://attack.mitre.org/campaigns/C00-XXX) | xxxxxxxTBC | TBC         |



# Sources 
- [Joep van Steen. (2021, Mars 23). Some thoughts on signature based file recovery. Retrieved January 14, 2024.](https://www.disktuna.com/some-thoughts-on-signature-based-file-recovery/)
