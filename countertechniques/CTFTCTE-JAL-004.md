# CTFTCTE-JAL-004 — Traverse the prototype chain to escape

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-004`](../techniques/CTFTTE-JAL-004.md) — JavaScript browser-sandbox jail

---

## Offensive Recovery (CTF practitioner / solver)

Walk the prototype chain via `({}).__proto__.__proto__.constructor` or access `Function` through array methods to reconstruct a callable that reaches the flag. Use `with` statements or template-literal tags when `eval` is blocked.

## Forensic / Blue-Team Perspective (DFIR analyst)

The escape demonstrates that proxy-based sandboxes must intercept every prototype-chain access point; a missing `Function` proxy or unguarded `constructor` property breaks containment.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.007 | JavaScript | JS sandbox-escape craft. |

## Tools

- browser DevTools
- js-sandbox cheat references

## References

- Add challenge write-up link
