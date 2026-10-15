# CTFTCTE-ICS-007 — Connect the vendor engineering tool and drive the process

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-007`](../techniques/CTFTTE-ICS-007.md) — Engineering-tool process takeover

---

## Offensive Recovery (CTF practitioner / solver)

Install the vendor engineering tool (a Windows VM when it is platform-locked),
create a project for the exact controller model and IP address, connect with
the credentials recovered during reconnaissance, and operate the exposed
process controls until the target state is reached.

## Forensic / Blue-Team Perspective (DFIR analyst)

Engineering-tool connections and program downloads are high-signal events: log
project access, downloaded programs and issued commands. Default credentials on
the engineering interface put every process control within an attacker's
reach.

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
