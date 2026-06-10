# JAL — Jail / Sandbox Escape

> **Tactic ID:** `CTFT-TA-JAL`  
> **HTB mapping:** HTB: Misc (Jail)  
> **Techniques:** 5

## Description

Challenges where the author constructs a restricted execution environment — a language-level sandbox, a limited shell, or an OS/kernel isolation boundary — to prevent direct flag access. Solvers must find a path out of the confinement.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-JAL-001](../techniques/CTFTTE-JAL-001.md) | Python jail (pyjail) confinement | [CTFTCTE-JAL-001](../countertechniques/CTFTCTE-JAL-001.md) | Escape the Python sandbox | No ATT&CK equivalent. |
| [CTFTTE-JAL-002](../techniques/CTFTTE-JAL-002.md) | Restricted-shell confinement | [CTFTCTE-JAL-002](../countertechniques/CTFTCTE-JAL-002.md) | Escape the restricted shell | Complements T1059 with CTF restricted-shell-escape detail. |
| [CTFTTE-JAL-003](../techniques/CTFTTE-JAL-003.md) | Docker / container escape | [CTFTCTE-JAL-003](../countertechniques/CTFTCTE-JAL-003.md) | Break out of the container to the host | Complements T1611 (Escape to Host) with CTF-specific misconfiguration paths. |
| [CTFTTE-JAL-004](../techniques/CTFTTE-JAL-004.md) | JavaScript browser-sandbox jail | [CTFTCTE-JAL-004](../countertechniques/CTFTCTE-JAL-004.md) | Traverse the prototype chain to escape | No ATT&CK equivalent. |
| [CTFTTE-JAL-005](../techniques/CTFTTE-JAL-005.md) | Seccomp / AppArmor policy confinement | [CTFTCTE-JAL-005](../countertechniques/CTFTCTE-JAL-005.md) | Identify allowed syscalls and pivot around the filter | Complements T1055 with CTF syscall-filter-bypass detail. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
