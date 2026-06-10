# CTFTTE-FOR-004 — NTFS Alternate Data Stream hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-004`](../countertechniques/CTFTCTE-FOR-004.md) — Enumerate and extract Alternate Data Streams

---

## How the challenge author hides

Payload is stored in a named ADS (file.txt:secret) that is invisible to ordinary directory listings.

## ATT\&CK Complementarity

Complements T1564.004 (NTFS File Attributes); CTFT adds the extraction recipe and MFT-attribute view.

## Tools

- dir /r
- PowerShell Get-Item -Stream
- streams.exe
- TSK icat

## References

- Add challenge write-up link