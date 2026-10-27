# CTFTTE-NET-009 — Credential-gated SMB share (hash / Kerberos)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-009`](../countertechniques/CTFTCTE-NET-009.md) — Authenticate to SMB and enumerate with smbclient.py (Impacket)

---

## How the challenge author hides

The flag lives in an SMB share that refuses anonymous access: listing and reading require valid credentials, a captured NTLM hash (pass-the-hash), or a Kerberos ticket. Unlike a plain enumeration barrier, the obstacle is authentication — the share, path, or file is only reachable once the solver proves an identity recovered earlier in the chain (dumped hash, reused password, forged/obtained ticket).

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
