# CTFTTE-ICS-004 — HMI project-file secrets

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-004`](../countertechniques/CTFTCTE-ICS-004.md) — Parse HMI/SCADA project files

---

## How the challenge author hides

Credentials/flags are stored in an HMI or SCADA project/configuration file.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0843 | Program Download | ICS ATT&CK: HMI project-file secrets. |

## Tools

- archive/file parsers
- strings

## References

- Add challenge write-up link