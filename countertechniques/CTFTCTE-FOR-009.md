# CTFTCTE-FOR-009 — Repair a corrupted image magic signature

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-009`](../techniques/CTFTTE-FOR-009.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Read the first bytes with a hex editor and compare them against the signature table for the
extension claimed by the file name. When the magic is corrupted rather than merely wrong, the
rest of the container is usually intact: rewrite the expected signature in place and re-open
the file. For PNG also check the IHDR chunk and the trailing IEND; for JPEG the SOI/EOI
markers. If several candidate types fit, carve the file and let the structural parser decide.

## Forensic / Blue-Team Perspective (DFIR analyst)

A single-field header edit leaves the rest of the container consistent, which is itself the
detection signal: a file whose magic disagrees with its internal structure was altered
deliberately. Record the original bytes before repairing — the corrupted value can carry
authorship information.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | ATT&CK omits the byte-level magic-header repair detail. |

## Tools

- xxd / hexdump
- file
- binwalk

## References

**Sources**

- (1) [File Signatures table](https://www.garykessler.net/library/file_sigs.html)

**Writeups**

- Add challenge write-up link
