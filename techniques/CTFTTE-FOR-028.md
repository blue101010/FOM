# CTFTTE-FOR-028 — Windows event-log evidence concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-028`](../countertechniques/CTFTCTE-FOR-028.md) — Reconstruct the timeline from Windows event logs

---

## How the challenge author hides

The answer lives in the Windows event logs and nowhere else: the author supplies a full `Logs/`
tree of `.evtx` channels and hides the decisive record among tens of thousands of routine ones.
Concealment is by volume and by channel choice — the interesting event sits in an operational or
application channel rather than Security, its provider is unremarkable, and neighbouring records
are legitimate. Variants clear a channel, disable a provider, or roll the log so the record
survives only in a companion channel.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070.001 | Clear Windows Event Logs | ATT&CK covers clearing; CTFT covers the recovery and channel-correlation craft. |
| T1562.002 | Disable Windows Event Logging | Provider suppression as a concealment choice. |

## Tools

- Event Viewer
- EvtxECmd / Timeline Explorer
- python-evtx
- Chainsaw

## References

**Sources**

- (1) [Windows event log reference](https://learn.microsoft.com/windows/win32/eventlog/event-logging)

**Writeups**

- Add challenge write-up link
