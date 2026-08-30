# CTFTCTE-GAM-006 — Script a bot interaction to reach the win branch

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation  
> **Counters technique:** [`CTFTTE-GAM-006`](../techniques/CTFTTE-GAM-006.md) — Chatbot / choice-path bot puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Script the interaction (automate the choices) to reach the win branch and capture the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Bot transcripts are replayable evidence; choice sequences reproduce the path.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Scripted application-layer interaction. |

## Tools

- pwntools
- Python requests

## References

- <https://github.com/Gallopsled/pwntools>

