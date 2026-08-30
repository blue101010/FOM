# PWN — Binary Exploitation

> **Tactic ID:** `CTFT-TA-PWN`  
> **HTB mapping:** HTB: Pwn  
> **Techniques:** 8

## Description

Hiding flags behind memory-corruption gates and constrained runtime puzzles.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-PWN-001](../techniques/CTFTTE-PWN-001.md) | Hidden win-function backdoor | [CTFTCTE-PWN-001](../countertechniques/CTFTCTE-PWN-001.md) | Redirect execution to the win function | No ATT&CK equivalent |
| [CTFTTE-PWN-002](../techniques/CTFTTE-PWN-002.md) | Format-string information hiding | [CTFTCTE-PWN-002](../countertechniques/CTFTCTE-PWN-002.md) | Leak and overwrite via format string | No ATT&CK equivalent. |
| [CTFTTE-PWN-003](../techniques/CTFTTE-PWN-003.md) | Heap-grooming puzzle | [CTFTCTE-PWN-003](../countertechniques/CTFTCTE-PWN-003.md) | Groom the heap to corrupt allocator metadata | No ATT&CK equivalent. |
| [CTFTTE-PWN-004](../techniques/CTFTTE-PWN-004.md) | Stripped/static gadget search | [CTFTCTE-PWN-004](../countertechniques/CTFTCTE-PWN-004.md) | Build a ROP chain from available gadgets | No ATT&CK equivalent. |
| [CTFTTE-PWN-005](../techniques/CTFTTE-PWN-005.md) | seccomp-restricted shell puzzle | [CTFTCTE-PWN-005](../countertechniques/CTFTCTE-PWN-005.md) | Open-Read-Write the flag under seccomp | No ATT&CK equivalent. |
| [CTFTTE-PWN-006](../techniques/CTFTTE-PWN-006.md) | Stack canary / PIE / ASLR hardening puzzle | [CTFTCTE-PWN-006](../countertechniques/CTFTCTE-PWN-006.md) | Leak canary/PIE base, ret2libc | T1068 |
| [CTFTTE-PWN-007](../techniques/CTFTTE-PWN-007.md) | Kernel/mseal-guarded memory puzzle | [CTFTCTE-PWN-007](../countertechniques/CTFTCTE-PWN-007.md) | Exploit kernel-module or mseal protections | T1068 |
| [CTFTTE-PWN-008](../techniques/CTFTTE-PWN-008.md) | Shellcode craft & encoding constraints | [CTFTCTE-PWN-008](../countertechniques/CTFTCTE-PWN-008.md) | Generate/encode shellcode (alphanumeric, null-free) | T1055 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
