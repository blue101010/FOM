# CTFTTE-REV-005 — Constraint-gated flag check

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-005`](../countertechniques/CTFTCTE-REV-005.md) — Solve the check with an SMT/symbolic engine

---

## How the challenge author hides

The binary validates input against arithmetic/bitwise constraints rather than comparing to a stored flag.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1480 | Execution Guardrails | Constraint-gated flag checks echo execution guardrails. |

## Tools

- z3
- angr
- Ghidra

## References

- https://github.com/Z3Prover/z3
- Add challenge write-up link