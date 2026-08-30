# CTFTTE-FOR-026 — Memory-image OS-artifact recovery

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-026`](../countertechniques/CTFTCTE-FOR-026.md) — Extract registry/services/process artifacts from memory images

---

## How the challenge author hides

The flag exists only in a Windows/Linux memory dump: registry hives, services, console history or process memory.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1003 | OS Credential Dumping | Memory extraction mirrors credential-dumping data sources. |

## Tools

- volatility3
- strings
- yara
- bulk_extractor

## References

- <https://github.com/volatilityfoundation/volatility3>
- Add challenge write-up link
