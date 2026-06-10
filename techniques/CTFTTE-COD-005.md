# CTFTTE-COD-005 — Symbolic-execution / SMT-solver puzzle

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Paired counter-technique:** [`CTFTCTE-COD-005`](../countertechniques/CTFTCTE-COD-005.md) — Extract constraints and solve with Z3 / angr

---

## How the challenge author hides

The correct flag input is the unique solution to a system of mathematical or Boolean constraints embedded in the binary's verification routine; no amount of manual guessing will reach it.

## ATT\&CK Complementarity

No ATT&CK equivalent. ATT&CK does not model constraint-satisfaction puzzle craft.

## Tools

- z3-solver
- angr
- miasm

## References

- https://github.com/angr/angr
- https://github.com/Z3Prover/z3
- Add challenge write-up link
