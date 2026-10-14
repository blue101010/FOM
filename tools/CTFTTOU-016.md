# CTFTTOU-016 — netexec

> **Tool ID:** `CTFTTOU-016`  
> **Related techniques/counters:** CTFTTE-FPN-015, CTFTCTE-FPN-015, CTFTTE-FPN-018, CTFTCTE-FPN-018, CTFTTE-FPN-019, CTFTCTE-FPN-019

## Description

Multi-protocol network execution and enumeration tool (formerly crackmapexec). One binary covers SMB, LDAP, MSSQL, WinRM and RDP with modules such as `get-network`, `spider_plus`, `--sam`, `--lsa`, `--dpapi` and `-x` command execution over MSSQL. Note that its BloodHound collection is less thorough than a native SharpHound run.

## URL

<https://github.com/Pennyw0rth/NetExec>

## Related Techniques

CTFTTE-FPN-015, CTFTCTE-FPN-015, CTFTTE-FPN-018, CTFTCTE-FPN-018, CTFTTE-FPN-019, CTFTCTE-FPN-019
