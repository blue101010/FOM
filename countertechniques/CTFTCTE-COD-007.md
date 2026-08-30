# CTFTCTE-COD-007 — Solve constraint grids programmatically

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Counters technique:** [`CTFTTE-COD-007`](../techniques/CTFTTE-COD-007.md) — Grid/logic-constraint puzzle (Sudoku)

---

## Offensive Recovery (CTF practitioner / solver)

Model the constraints (backtracking/SAT) and solve the grid to extract the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Constraint puzzles are pure computation; solvers double as verifiers.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; constraint-satisfaction craft. |

## Tools

- Python
- z3

## References

- <https://github.com/Z3Prover/z3>
