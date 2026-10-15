# CTFTTE-ICS-007 — Engineering-tool process takeover

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-007`](../countertechniques/CTFTCTE-ICS-007.md) — Connect the vendor engineering tool and drive the process

---

## How the challenge author hides

The flag is gated by a physical process state — a train that must be stopped —
and no shell command or web click changes it. Only the vendor engineering tool
for the PLC family exposes the start/stop controls, and it runs on a single
platform, adding a setup obstacle to the takeover.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0843 | Program Download | The engineering tool downloads its control program to the PLC. |
| T0855 | Unauthorized Command Message | Process stop commands are issued through the tool. |

## Tools

- [PLCnext Engineer](../tools/CTFTTOU-059.md)

## References

- <https://www.phoenixcontact.com/en-ca/products/programming-plcnext-engineer-1046008>
- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
