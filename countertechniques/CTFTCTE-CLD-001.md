# CTFTCTE-CLD-001 — Enumerate and list public buckets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-001`](../techniques/CTFTTE-CLD-001.md) — Misconfigured object-storage exposure

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate bucket names and list/download objects anonymously.

## Forensic / Blue-Team Perspective (DFIR analyst)

Storage access logs document anonymous reads of the exposed objects.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1530 | Data from Cloud Storage Object | Misconfigured object storage. |

## Tools

- awscli
- s3scanner
- gcsbucketbrute

## References

- Add challenge write-up link