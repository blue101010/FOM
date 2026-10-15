# CTFTTE-ICS-006 — Physical controller-label default credentials

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-006`](../countertechniques/CTFTCTE-ICS-006.md) — Read the device label and vendor documentation for default credentials

---

## How the challenge author hides

The controller is the entry point of the whole track, but its credentials are
never handed out: the default password is printed on the device label, next to
the MAC address, and the same password unlocks both the web-based manager and
SSH. A physical view of the controller — a photo, a label on the table of the
SCADA village, the vendor datasheet for the exact model — is part of the
intended reconnaissance.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0859 | Valid Accounts | Default credentials recovered from the device label. |

## Tools

- [openssh client](../tools/CTFTTOU-058.md)

## References

- <https://www.phoenixcontact.com/en-ca/products/controller-axc-f-2152-2404267>
- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
