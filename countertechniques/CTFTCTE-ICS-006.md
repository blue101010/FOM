# CTFTCTE-ICS-006 — Read the device label and vendor documentation for default credentials

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-006`](../techniques/CTFTTE-ICS-006.md) — Physical controller-label default credentials

---

## Offensive Recovery (CTF practitioner / solver)

Identify the exact model from the label, the HMI banner or the service
fingerprints, then read its vendor documentation for the default account
policy. Check every physical surface of the challenge — device photos, printed
labels, handouts — for the password and MAC address. Expect the same credential
to unlock both the web-based manager and SSH, and reuse it on every exposed
service.

## Forensic / Blue-Team Perspective (DFIR analyst)

Default credentials printed on the device label are a configuration-audit
finding: the label is visible to anyone with physical access, and a credential
shared between the web manager and SSH widens the blast radius of one
compromised service.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0859 | Valid Accounts | Default credentials recovered from the device label. |

## Tools

- [openssh client](../tools/CTFTTOU-058.md)

## References

- <https://www.phoenixcontact.com/en-ca/products/controller-axc-f-2152-2404267>
- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
