# PWN — Binary Exploitation

> **Domain ID:** `CTFT-TA-PWN`  
> **HTB mapping:** HTB: Pwn  
> **Techniques:** 8

## Description

Hiding flags behind memory-corruption gates and constrained runtime puzzles.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-PWN-001](../techniques/CTFTTE-PWN-001.md) | Hidden win-function backdoor | [CTFTCTE-PWN-001](../countertechniques/CTFTCTE-PWN-001.md) | Redirect execution to the win function | T1068 |
| [CTFTTE-PWN-002](../techniques/CTFTTE-PWN-002.md) | Format-string information hiding | [CTFTCTE-PWN-002](../countertechniques/CTFTCTE-PWN-002.md) | Leak and overwrite via format string | T1068 |
| [CTFTTE-PWN-003](../techniques/CTFTTE-PWN-003.md) | Heap-grooming puzzle | [CTFTCTE-PWN-003](../countertechniques/CTFTCTE-PWN-003.md) | Groom the heap to corrupt allocator metadata | T1068 |
| [CTFTTE-PWN-004](../techniques/CTFTTE-PWN-004.md) | Stripped/static gadget search | [CTFTCTE-PWN-004](../countertechniques/CTFTCTE-PWN-004.md) | Build a ROP chain from available gadgets | T1211 |
| [CTFTTE-PWN-005](../techniques/CTFTTE-PWN-005.md) | seccomp-restricted shell puzzle | [CTFTCTE-PWN-005](../countertechniques/CTFTCTE-PWN-005.md) | Open-Read-Write the flag under seccomp | T1059 |
| [CTFTTE-PWN-006](../techniques/CTFTTE-PWN-006.md) | Stack canary / PIE / ASLR hardening puzzle | [CTFTCTE-PWN-006](../countertechniques/CTFTCTE-PWN-006.md) | Leak canary/PIE base, ret2libc | T1068 |
| [CTFTTE-PWN-007](../techniques/CTFTTE-PWN-007.md) | Kernel/mseal-guarded memory puzzle | [CTFTCTE-PWN-007](../countertechniques/CTFTCTE-PWN-007.md) | Exploit kernel-module or mseal protections | T1068 |
| [CTFTTE-PWN-008](../techniques/CTFTTE-PWN-008.md) | Shellcode craft & encoding constraints | [CTFTCTE-PWN-008](../countertechniques/CTFTCTE-PWN-008.md) | Generate/encode shellcode (alphanumeric, null-free) | T1055 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
