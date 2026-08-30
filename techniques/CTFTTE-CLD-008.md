# CTFTTE-CLD-008 — Azure management-plane misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-008`](../countertechniques/CTFTCTE-CLD-008.md) — Enumerate Azure AD/VM/storage from credentials

---

## How the challenge author hides

Leaked Azure credentials unlock management-plane access where the flag sits (AD users, VMs, storage).

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
- Add challenge write-up link
