# CTFTTE-COD-005 — Symbolic-execution / SMT-solver puzzle

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Paired counter-technique:** [`CTFTCTE-COD-005`](../countertechniques/CTFTCTE-COD-005.md) — Extract constraints and solve with Z3 / angr

---

## How the challenge author hides

The correct flag input is the unique solution to a system of mathematical or Boolean constraints embedded in the binary's verification routine; no amount of manual guessing will reach it.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; constraint-satisfaction craft. |

## Tools

- z3-solver
- angr
- miasm

## References

- https://github.com/angr/angr
- https://github.com/Z3Prover/z3
- Add challenge write-up link
