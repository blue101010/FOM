# CTFTCTE-ICS-004 — Parse HMI/SCADA project files

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-004`](../techniques/CTFTTE-ICS-004.md) — HMI project-file secrets

---

## Offensive Recovery (CTF practitioner / solver)

Open/parse the project file structure to extract embedded values.

## Forensic / Blue-Team Perspective (DFIR analyst)

Project-file analysis documents secrets persisted by the engineering tool.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0843 | Program Download | ICS ATT&CK: HMI project-file secrets. |

## Tools

- archive/file parsers
- strings

## References

- Add challenge write-up link