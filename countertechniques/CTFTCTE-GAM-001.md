# CTFTCTE-GAM-001 — Script a client to beat the protocol

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-001`](../techniques/CTFTTE-GAM-001.md) — Networked game / protocol automation

---

## Offensive Recovery (CTF practitioner / solver)

Reverse the game protocol (from traffic capture or source), implement a pwntools/socket script that parses server state and responds optimally for every round, and run until the server releases the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Scripted game clients are indistinguishable from legitimate fast players; in production, server-side behavioural analytics (response timing distribution, move entropy) detect bots.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Game-protocol automation. |

## Tools

- pwntools
- python sockets

## References

- <https://github.com/Gallopsled/pwntools>
- Add challenge write-up link
