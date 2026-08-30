# CTFTTE-ICS-003 — Proprietary-protocol capture concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-003`](../countertechniques/CTFTCTE-ICS-003.md) — Dissect industrial protocol captures

---

## How the challenge author hides

The flag rides a less-common industrial protocol inside a provided capture.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0842 | Network Sniffing | ICS ATT&CK: industrial protocol captures. |

## Tools

- wireshark (ICS dissectors)
- tshark

## References

- Add challenge write-up link