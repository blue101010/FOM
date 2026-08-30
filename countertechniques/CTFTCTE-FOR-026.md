# CTFTCTE-FOR-026 — Extract registry/services/process artifacts from memory images

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-026`](../techniques/CTFTTE-FOR-026.md) — Memory-image OS-artifact recovery

---

## Offensive Recovery (CTF practitioner / solver)

Profile the image (volatility3), enumerate processes/registry, scan strings, and dump the owning structures.

## Forensic / Blue-Team Perspective (DFIR analyst)

Memory forensics reconstructs transient OS state; plugin selection depends on the OS profile.

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

