# CTFTCTE-ICS-003 — Dissect industrial protocol captures

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-003`](../techniques/CTFTTE-ICS-003.md) — Proprietary-protocol capture concealment

---

## Offensive Recovery (CTF practitioner / solver)

Apply protocol dissectors to decode fields and extract the payload.

## Forensic / Blue-Team Perspective (DFIR analyst)

Dissection documents the protocol semantics carrying the hidden data.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0842 | Network Sniffing | ICS ATT&CK: industrial protocol captures. |

## Tools

- wireshark (ICS dissectors)
- tshark

## References

- Add challenge write-up link