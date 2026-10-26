# CTFTTOU-402 — ad_inventory.py

> **Tool ID:** `CTFTTOU-402`
> **Related techniques/counters:** CTFTTE-FPN-002, CTFTCTE-FPN-002

## Description

Workspace-authored read-only Active Directory orientation snapshot (Python, ldap3). Reports the domain, DCs, functional level, your effective group memberships, LDAP clock skew vs the DC, the DNS resolver and MachineAccountQuota — the facts that gate every later Kerberos/LDAP step. It performs only LDAP reads (RootDSE + your own token groups) and never writes to the directory.

## URL

Local (workspace): [ctf-skills-main/ctf-ad-attack-paths/scripts/ad_inventory.py](../../ctf-skills-main/ctf-ad-attack-paths/scripts/ad_inventory.py)

## Usage

```bash
python ad_inventory.py --dc-ip 10.10.10.10 -d corp.local -u user -p 'Password1' -o inv.json
```

## Skills

- [ctf-ad-attack-paths](../skills/CTFTSKL-004.md)

## Related Techniques

CTFTTE-FPN-002, CTFTCTE-FPN-002
