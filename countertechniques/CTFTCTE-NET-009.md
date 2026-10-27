# CTFTCTE-NET-009 — Authenticate to SMB and enumerate with smbclient.py (Impacket)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-009`](../techniques/CTFTTE-NET-009.md) — Credential-gated SMB share (hash / Kerberos)

---

## Offensive Recovery (CTF practitioner / solver)

Use Impacket's `smbclient.py` to authenticate with the recovered material, then enumerate and pull the flag:

```bash
# Password auth
smbclient.py 'DOMAIN/user:Password123@10.10.10.10'
# Pass-the-hash (NTLM) — no password needed
smbclient.py -hashes :<NTLM> 'DOMAIN/user@10.10.10.10'
# Kerberos ticket from the environment (KRB5CCNAME)
smbclient.py -k -no-pass 'DOMAIN/user@host.domain.local'
```

Inside the interactive prompt: `shares` (list shares), `use <share>`, `ls`, `cd`, `get <file>`. For a quick scripted sweep prefer `netexec smb <host> -u user -H <hash> --shares` or `smbmap`. Null/guest sessions (`smbclient.py ''@host`) are worth one baseline attempt before spending the recovered credential.

## Forensic / Blue-Team Perspective (DFIR analyst)

Authenticated SMB access leaves Windows Security events (4624 logon type 3, 4672, 5140/5145 share and file access) and NTLM/Kerberos authentication traces. Pass-the-hash shows NTLM logons without a matching interactive logon; Kerberos use leaves 4768/4769 ticket events. Auditing reconstructs which account touched which share and file, and when.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1021.002 | SMB/Windows Admin Shares | Authenticated share access mirrors admin-share usage. |
| T1550.002 | Use Alternate Authentication Material: Pass the Hash | NTLM-hash access echoes pass-the-hash. |
| T1078 | Valid Accounts | Reusing recovered credentials to reach the share. |

## Tools

- smbclient.py
- impacket
- netexec
- smbmap

## References

- <https://github.com/fortra/impacket>
- [HackTricks — 139,445 SMB/pentesting](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)
