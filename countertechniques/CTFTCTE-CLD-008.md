# CTFTCTE-CLD-008 — Enumerate Azure AD/VM/storage from credentials

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-008`](../techniques/CTFTTE-CLD-008.md) — Azure management-plane misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Use the credentials against the management plane: enumerate AD, VMs and storage accounts, and extract the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Azure AD sign-in logs and activity logs document every management-plane call.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Cloud Accounts | Management-plane access from valid cloud credentials. |

## Tools

- azure-cli
- Az PowerShell
- AADInternals

## References

- <https://learn.microsoft.com/en-us/cli/azure/>

