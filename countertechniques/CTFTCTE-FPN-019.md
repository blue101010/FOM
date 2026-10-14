# CTFTCTE-FPN-019 — Harvest shell histories and decrypt protected stores

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-019`](../techniques/CTFTTE-FPN-019.md) — Interactive-shell history and protected credential stores

---

## Offensive Recovery (CTF practitioner / solver)

Read the console history file of the administrator profile for typed
credentials, then dump DPAPI masterkeys and credential blobs with local
administrative rights. Search the decrypted material for domain accounts and
their passwords to fuel the next hop.

## Forensic / Blue-Team Perspective (DFIR analyst)

History files and DPAPI blobs are high-value DFIR artifacts too: collect them
read-only and review what each protected blob stored. Audit process access to
DPAPI and alert on bulk masterkey decryption during interactive hours.

## Preconditions

- Local administrator access on a host used interactively.
- The profile's history and protected stores have not been purged.

## Indicators

- A console history file contains command lines with passwords.
- Bulk DPAPI masterkey decryption precedes credential reuse.
- A task-scheduler credential blob yields a domain account.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Unsecured Credentials: Credentials In Files | The console history file stores a plaintext password. |
| T1555.004 | Credentials from Password Stores: Windows Credential Manager | DPAPI blobs are decrypted to expose stored secrets. |

## Tools

- [evil-winrm](../tools/CTFTTOU-024.md)
- [Get-PSReadlineOption](../tools/CTFTTOU-034.md)
- [netexec](../tools/CTFTTOU-016.md) (dpapi module)

## References

- <https://www.thehacker.recipes/ad/movement/credentials/dpapi-protected-secrets>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
