# CTFTCTE-ICS-009 — Map device names to MAC addresses and rename the target

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-009`](../techniques/CTFTTE-ICS-009.md) — Field-device identity takeover through MAC-addressed naming

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the MAC-to-name bindings of the field devices, fetch the vendor
rename utility from its store, transfer it to the controller that shares the
field network, and rename the target device. The process state follows the
identity change.

## Forensic / Blue-Team Perspective (DFIR analyst)

An unauthenticated naming protocol is by-design exposure: any station on the
segment can rename a device. Log naming changes, restrict the protocol to a
management segment, and treat identity changes on field devices as incidents.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0855 | Unauthorized Command Message | The rename command alters the device identity. |

## Tools

- [PLCnext Store](../tools/CTFTTOU-060.md)
- [openssh client](../tools/CTFTTOU-058.md)

## References

- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
