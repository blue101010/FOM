# CTFTTE-ICS-009 — Field-device identity takeover through MAC-addressed naming

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-009`](../countertechniques/CTFTCTE-ICS-009.md) — Map device names to MAC addresses and rename the target

---

## How the challenge author hides

The wind turbines are managed through an Ethernet protocol that binds device
names to MAC addresses. Stopping a turbine means renaming its identity, and the
renaming command ships in a vendor store package that must be fetched,
transferred onto the controller and pointed at the right MAC address.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0855 | Unauthorized Command Message | The rename command alters the device identity. |

## Tools

- [PLCnext Store](../tools/CTFTTOU-060.md)
- [openssh client](../tools/CTFTTOU-058.md)

## References

- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
