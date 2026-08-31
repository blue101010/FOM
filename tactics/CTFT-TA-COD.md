# COD — Coding / Programming Puzzle

> **Domain ID:** `CTFT-TA-COD`  
> **HTB mapping:** HTB: Coding  
> **Techniques:** 7

## Description

Challenges where the flag is gated behind a programming or algorithmic problem: an esoteric language, a time-bounded algorithm, a scripted marathon of protocol rounds, a polyglot/code-golf constraint, or a constraint-satisfaction puzzle solvable with symbolic execution.

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
| [CTFTTE-COD-001](../techniques/CTFTTE-COD-001.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-COD-001](../countertechniques/CTFTCTE-COD-001.md) | Interpret or transpile the encoding | T1140 |
| [CTFTTE-COD-002](../techniques/CTFTTE-COD-002.md) | Algorithm optimisation challenge | [CTFTCTE-COD-002](../countertechniques/CTFTCTE-COD-002.md) | Implement an efficient algorithm to satisfy the server | — |
| [CTFTTE-COD-003](../techniques/CTFTTE-COD-003.md) | Scripted protocol / automation marathon | [CTFTCTE-COD-003](../countertechniques/CTFTCTE-COD-003.md) | Write a pwntools script to complete all rounds | T1071 |
| [CTFTTE-COD-004](../techniques/CTFTTE-COD-004.md) | Code-golf / polyglot code puzzle | [CTFTCTE-COD-004](../countertechniques/CTFTCTE-COD-004.md) | Craft a minimal polyglot that satisfies every parser | T1027 |
| [CTFTTE-COD-005](../techniques/CTFTTE-COD-005.md) | Symbolic-execution / SMT-solver puzzle | [CTFTCTE-COD-005](../countertechniques/CTFTCTE-COD-005.md) | Extract constraints and solve with Z3 / angr | — |
| [CTFTTE-COD-006](../techniques/CTFTTE-COD-006.md) | Combinatorial enumeration puzzle | [CTFTCTE-COD-006](../countertechniques/CTFTCTE-COD-006.md) | Generate permutations/combinations efficiently | — |
| [CTFTTE-COD-007](../techniques/CTFTTE-COD-007.md) | Grid/logic-constraint puzzle (Sudoku) | [CTFTCTE-COD-007](../countertechniques/CTFTCTE-COD-007.md) | Solve constraint grids programmatically | — |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
