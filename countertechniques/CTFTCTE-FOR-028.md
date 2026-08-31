# CTFTCTE-FOR-028 — Reconstruct the timeline from Windows event logs

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-028`](../techniques/CTFTTE-FOR-028.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Do not read channels one by one. Normalise the whole `Logs/` tree into a single time-ordered table
(`EvtxECmd` to CSV, or `python-evtx` to JSON), then pivot: filter on the window the challenge
frames, then on providers that should be quiet. Records that matter are usually the ones whose
channel does not match their content — a scripting engine event in an application channel, a
service install outside a maintenance window. Gaps matter as much as records: a channel that stops
and resumes marks a clearing.

## Forensic / Blue-Team Perspective (DFIR analyst)

Event IDs alone are a weak pivot; correlate channel, provider, record identifier and the sequence
numbers, which expose deletions that timestamps do not. Preserve the raw `.evtx` before any
conversion: parsers silently drop malformed records that are themselves evidence.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070.001 | Clear Windows Event Logs | Recovery of cleared or hidden records. |
| T1562.002 | Disable Windows Event Logging | Detecting suppressed providers. |

## Tools

- EvtxECmd
- python-evtx
- Chainsaw
- Timeline Explorer

## References

**Sources**

- (1) [Windows event log reference](https://learn.microsoft.com/windows/win32/eventlog/event-logging)

**Writeups**

- Add challenge write-up link
