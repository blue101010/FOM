# CTFTCTE-COD-005 — Extract constraints and solve with Z3 / angr

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Counters technique:** [`CTFTTE-COD-005`](../techniques/CTFTTE-COD-005.md) — Symbolic-execution / SMT-solver puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Decompile the binary to identify the constraint system (comparisons, XOR chains, arithmetic relationships), model them as Z3 bit-vector equations, and call `solver.check()` to obtain the satisfying flag input. For complex control flow, use angr's symbolic execution with `find`/`avoid` addresses.

## Forensic / Blue-Team Perspective (DFIR analyst)

Constraint-extraction is also used in defensive reverse engineering to automatically derive anti-tamper key conditions; angr-based path exploration assists malware analysis by reaching flagged code paths without manual tracing.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; constraint-satisfaction craft. |

## Tools

- z3-solver
- angr
- miasm

## References

- <https://github.com/angr/angr>
- <https://github.com/Z3Prover/z3>
- Add challenge write-up link
