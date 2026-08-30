# CTFTCTE-REV-005 — Solve the check with an SMT/symbolic engine

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-005`](../techniques/CTFTTE-REV-005.md) — Constraint-gated flag check

---

## Offensive Recovery (CTF practitioner / solver)

Model the constraints and solve for the satisfying input that is the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Extracting the constraint set proves how the flag was derived rather than stored.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1480 | Execution Guardrails | Constraint-gated flag checks echo execution guardrails. |

## Tools

- z3
- angr
- Ghidra

## References

- <https://github.com/Z3Prover/z3>
- Add challenge write-up link