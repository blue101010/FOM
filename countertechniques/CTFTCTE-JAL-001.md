# CTFTCTE-JAL-001 — Escape the Python sandbox

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-001`](../techniques/CTFTTE-JAL-001.md) — Python jail (pyjail) confinement

---

## Offensive Recovery (CTF practitioner / solver)

Reach builtins or OS access via object traversal: walk `__class__.__mro__` and `__subclasses__()` to find `_io.FileIO` or `os`, then open and read the flag file. When `_` is blocked, use `getattr` or string indexing on `dir([])[0]`.

## Forensic / Blue-Team Perspective (DFIR analyst)

The escape chain documents incomplete sandboxing of the eval context; audit the restricted namespace for object hierarchy exposure and ensure `__builtins__` is fully replaced rather than filtered.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.006 | Python | Python sandbox escape; ATT&CK models Python scripting for other purposes. |

## Tools

- python
- pyjail cheat references

## References

- Add challenge write-up link
