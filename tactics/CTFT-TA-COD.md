# COD — Coding / Programming Puzzle

> **Tactic ID:** `CTFT-TA-COD`  
> **HTB mapping:** HTB: Coding  
> **Techniques:** 5

## Description

Challenges where the flag is gated behind a programming or algorithmic problem: an esoteric language, a time-bounded algorithm, a scripted marathon of protocol rounds, a polyglot/code-golf constraint, or a constraint-satisfaction puzzle solvable with symbolic execution.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-COD-001](../techniques/CTFTTE-COD-001.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-COD-001](../countertechniques/CTFTCTE-COD-001.md) | Interpret or transpile the encoding | No ATT&CK equivalent. |
| [CTFTTE-COD-002](../techniques/CTFTTE-COD-002.md) | Algorithm optimisation challenge | [CTFTCTE-COD-002](../countertechniques/CTFTCTE-COD-002.md) | Implement an efficient algorithm to satisfy the server | No ATT&CK equivalent. |
| [CTFTTE-COD-003](../techniques/CTFTTE-COD-003.md) | Scripted protocol / automation marathon | [CTFTCTE-COD-003](../countertechniques/CTFTCTE-COD-003.md) | Write a pwntools script to complete all rounds | No ATT&CK equivalent. |
| [CTFTTE-COD-004](../techniques/CTFTTE-COD-004.md) | Code-golf / polyglot code puzzle | [CTFTCTE-COD-004](../countertechniques/CTFTCTE-COD-004.md) | Craft a minimal polyglot that satisfies every parser | No ATT&CK equivalent. |
| [CTFTTE-COD-005](../techniques/CTFTTE-COD-005.md) | Symbolic-execution / SMT-solver puzzle | [CTFTCTE-COD-005](../countertechniques/CTFTCTE-COD-005.md) | Extract constraints and solve with Z3 / angr | No ATT&CK equivalent. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
