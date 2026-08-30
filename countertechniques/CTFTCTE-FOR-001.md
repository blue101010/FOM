# CTFTCTE-FOR-001 — Recover the legitimate file signature

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-001`](../techniques/CTFTTE-FOR-001.md) — Magic-byte / file-signature tampering

---

## Offensive Recovery (CTF practitioner / solver)

Compare bytes against a signature table, identify the true type from structure/footers, and patch the header with a hex editor or python.

## Forensic / Blue-Team Perspective (DFIR analyst)

During carving, signature-based recovery reconstructs files whose extension or header was altered; corroborate with internal structure, not just the leading bytes.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | ATT&CK omits the byte-level magic-header recovery detail. |

## Tools

- xxd / hexedit
- file
- binwalk
- python struct

## References

- <https://www.garykessler.net/library/file_sigs.html>
- Add challenge write-up link