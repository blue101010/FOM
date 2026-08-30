# CTFTCTE-CRY-007 — Assess and predict recoverable PRNG state

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-007`](../techniques/CTFTTE-CRY-007.md) — Deliberately predictable stateful pseudo-random generator

---

## Offensive Recovery (CTF practitioner / solver)

Classify the declared generator family, validate that observations are sufficient
for a state-recovery hypothesis, and compare predicted outputs only within the
challenge's authorized laboratory scope.

## Forensic / Blue-Team Perspective (DFIR analyst)

Record the generator family, seed exposure, output observations and validation
result. A prediction failure is evidence against the hypothesis, not a reason to
silently change the model.

## Preconditions

- The challenge exposes outputs and generator assumptions needed for evaluation.
- The candidate state and observations are retained as reproducible evidence.

## Indicators

- Outputs show a declared weak seed, small state, or deterministic sequence.
- Repeated challenge instances expose a consistent generator family.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573.001 | Symmetric Cryptography | Predictable PRNG state undermines stream cryptography; recovery is CTF-specific. |

## Tools

- SageMath
- Z3
- Python reference implementations

## References

- <https://csrc.nist.gov/pubs/sp/800/90/a/r1/final>
- <https://docs.python.org/3/library/random.html>