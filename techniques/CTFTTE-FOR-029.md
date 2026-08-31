# CTFTTE-FOR-029 — Registry-hive persistence artifact concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-029`](../countertechniques/CTFTCTE-FOR-029.md) — Extract and analyse registry hives from a forensic image

---

## How the challenge author hides

The flag or the decisive indicator is a persistence entry inside a Windows registry hive, and the
hive is delivered inside a forensic container (AD1, E01, raw) rather than as a loose file. The
author counts on two barriers: the container format, which ordinary tools will not open, and the
value itself, whose payload is encoded — typically a `Run` key holding a base64 PowerShell stager.
The surrounding hive is legitimate, so nothing looks out of place until the value is decoded.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1547.001 | Registry Run Keys / Startup Folder | ATT&CK models the persistence; CTFT models recovering it from an offline hive. |
| T1027.010 | Command Obfuscation | Encoded stager stored in the value data. |
| T1562.001 | Impair Defenses | Stagers that disable AMSI/ETW once decoded. |

## Tools

- FTK Imager
- Registry Explorer
- hivex / python-registry

## References

**Sources**

- (1) [Registry hive file format](https://learn.microsoft.com/windows/win32/sysinfo/registry-hives)

**Writeups**

- Add challenge write-up link
