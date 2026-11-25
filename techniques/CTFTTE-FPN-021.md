# CTFTTE-FPN-021 — Delegated managed service account linked to a privileged predecessor

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-021`](../countertechniques/CTFTCTE-FPN-021.md) — Enumerate OU create rights and mint a linked successor account

---

## How the challenge author hides

A low-privileged principal is delegated `CreateChild` on one organizational unit — a
routine help-desk or service-management grant, not a privileged one. On a domain whose
schema supports delegated Managed Service Accounts, that grant is enough: the principal
creates its own dMSA, writes a privileged account's name into
`msDS-ManagedAccountPrecededByLink`, and sets `msDS-DelegatedMSAState` to *Completed*.
No right over the target object is ever required, so ACL reviews of users, groups and
computers show nothing. The concealment is an OU permission plus two attribute values,
and the escalation completes when the KDC copies the predecessor's SIDs into the
successor's PAC.

## Evidence expected

- A controlled principal holds `CreateChild` (often implied by `GenericAll`,
  `WriteDacl` or `WriteOwner` on the OU) below an organizational unit.
- The domain exposes the dMSA schema — `msDS-DelegatedMSAState` /
  `msDS-ManagedAccountPrecededByLink` on `msDS-DelegatedManagedServiceAccount` objects.
- After the link is completed, a TGT for the new dMSA carries the predecessor's user and
  group SIDs, so the ticket authorizes actions the controlled principal never had.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1098 | Account Manipulation | A dMSA object is created inside a delegated OU and its successor link and migration state are written by a non-privileged principal. |
| T1078.002 | Valid Accounts: Domain Accounts | The successor's ticket impersonates the predecessor's identity and groups. |

## Tools

- [Get-BadSuccessorOUPermissions.ps1](../tools/CTFTTOU-449.md)
- [impacket](../tools/CTFTTOU-116.md) (`badsuccessor.py`, `getTGT.py`, `getST.py`, `secretsdump.py`)
- [netexec](../tools/CTFTTOU-016.md) (`-M badsuccessor`)
- [BloodHound](../tools/CTFTTOU-294.md) (OU control edges)

## References

- <https://github.com/akamai/BadSuccessor>
- <https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory>
- <https://github.com/logangoins/SharpSuccessor>
