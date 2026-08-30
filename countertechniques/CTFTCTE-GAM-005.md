# CTFTCTE-GAM-005 — Record, replay, or race the server sequence precisely

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-005`](../techniques/CTFTTE-GAM-005.md) — Protocol sequence replay / race

---

## Offensive Recovery (CTF practitioner / solver)

Capture a valid game session with Wireshark, identify the critical state-machine path, then replay the exact byte sequence (adjusted for any session tokens) with precise inter-packet timing using a Python socket script or pwntools.

## Forensic / Blue-Team Perspective (DFIR analyst)

Replay attacks on game protocols mirror real credential-replay attacks; production services mitigate this with per-session nonces, sequence counters, and time-bounded tokens embedded in every packet.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Protocol replay / race. |

## Tools

- wireshark / tshark
- pwntools
- python threading

## References

- Add challenge write-up link
