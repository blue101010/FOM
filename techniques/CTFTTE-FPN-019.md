# CTFTTE-FPN-019 — Interactive-shell history and protected credential stores

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-019`](../countertechniques/CTFTCTE-FPN-019.md) — Harvest shell histories and decrypt protected stores

---

## How the challenge author hides

The next credentials are not exposed by any service: they sit in the
administrator's PowerShell readline history and inside DPAPI-protected scheduled
task blobs. The author expects credential archaeology on the first host instead
of network exploitation for the next hop.

## Evidence expected

- The administrator's console history file contains a typed domain password.
- A DPAPI dump decrypts masterkeys and recovers a task-scheduler credential blob.
- The recovered account unlocks a new attack path in the graph.

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
