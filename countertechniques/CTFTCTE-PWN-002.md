# CTFTCTE-PWN-002 — Leak and overwrite via format string

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-002`](../techniques/CTFTTE-PWN-002.md) — Format-string information hiding

---

## Offensive Recovery (CTF practitioner / solver)

Use %p/%s to leak, then %n-style writes to redirect execution or overwrite the GOT.

## Forensic / Blue-Team Perspective (DFIR analyst)

The vulnerability report attributes the leak/overwrite to unsanitized format arguments.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Format-string leak/write mechanics are omitted by ATT&CK. |

## Tools

- pwntools
- GDB+pwndbg

## References

- Add challenge write-up link