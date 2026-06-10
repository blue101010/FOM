# CTFTCTE-FOR-004 — Enumerate and extract Alternate Data Streams

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-004`](../techniques/CTFTTE-FOR-004.md) — NTFS Alternate Data Stream hiding

---

## Offensive Recovery (CTF practitioner / solver)

List streams (dir /r, Get-Item -Stream) and read the named stream directly.

## Forensic / Blue-Team Perspective (DFIR analyst)

Enumerate $DATA attributes per MFT record; non-default named streams are immediate indicators of concealment.

## Tools

- dir /r
- PowerShell Get-Item -Stream
- streams.exe
- TSK icat

## References

- Add challenge write-up link