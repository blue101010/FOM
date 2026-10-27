# CTFTTOU-412 — smbclient.py (Impacket)

> **Tool ID:** `CTFTTOU-412`  
> **Related techniques/counters:** CTFTTE-NET-003, CTFTCTE-NET-003, CTFTTE-NET-009, CTFTCTE-NET-009

## Description

Impacket's pure-Python SMB client. Unlike Samba's `smbclient` ([CTFTTOU-112](CTFTTOU-112.md)), `smbclient.py` speaks SMB directly from Python and is built for authenticated access during offensive engagements: password, NTLM pass-the-hash (`-hashes`), and Kerberos (`-k`, with `KRB5CCNAME`). It drives SMB enumeration (share listing, directory browsing, file download/upload) and pairs naturally with the rest of the Impacket suite (`secretsdump.py`, `psexec.py`, `getTGT.py`).

## URL

- **Impacket**: <https://github.com/fortra/impacket>

## Installation

**Kali WSL (PEP 668 — use a venv, never bare pip):**
```bash
python3 -m venv ~/.venvs/impacket
~/.venvs/impacket/bin/pip install impacket
# scripts land in ~/.venvs/impacket/bin/ (smbclient.py, secretsdump.py, ...)
~/.venvs/impacket/bin/smbclient.py -h
```
Kali also ships `impacket-smbclient` via apt.

## Usage

```bash
# Password auth
smbclient.py 'DOMAIN/user:Password123@10.10.10.10'

# Pass-the-hash (LM:NT or :NT)
smbclient.py -hashes :aad3b435b51404eeaad3b435b51404ee 'DOMAIN/user@10.10.10.10'

# Kerberos (ticket in KRB5CCNAME)
smbclient.py -k -no-pass 'DOMAIN/user@host.domain.local'

# Null / guest baseline
smbclient.py ''@10.10.10.10
```

Interactive commands: `shares`, `use <share>`, `ls`, `cd <dir>`, `get <file>`, `put <file>`, `mkdir`, `cat`.

## Related Techniques

CTFTTE-NET-003, CTFTCTE-NET-003, CTFTTE-NET-009, CTFTCTE-NET-009

## References

- [Impacket GitHub](https://github.com/fortra/impacket)
- [Impacket examples](https://github.com/fortra/impacket/tree/master/examples)
- [HackTricks — SMB pentesting](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)
