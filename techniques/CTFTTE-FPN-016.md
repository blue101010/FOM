# CTFTTE-FPN-016 — Packed token-impersonation binary evading endpoint defenses

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-016`](../countertechniques/CTFTCTE-FPN-016.md) — Audit privileged tokens and unpack suspicious binaries

---

## How the challenge author hides

The SQL service account holds SeImpersonatePrivilege, the classic potato-class
escalation, but endpoint protection is running and known binaries are blocked.
The solver must repackage the impersonation binary with a packer so it clears
static detection, deliver it over HTTP, and abuse the privileged token to reach
SYSTEM.

## Evidence expected

- `whoami -priv` lists SeImpersonatePrivilege for the current service account.
- Endpoint protection blocks the unpacked exploit binary but not the packed one.
- The packed binary executes commands as `NT AUTHORITY\SYSTEM`.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1134.001 | Access Token Manipulation: Token Impersonation/Theft | The privileged token is impersonated to escalate. |
| T1027 | Obfuscated Files or Information | Packing defeats static detection. |

## Tools

- [PetitPotato](../tools/CTFTTOU-028.md)
- [UPX](../tools/CTFTTOU-029.md)
- HTTP file delivery ([curl](../tools/CTFTTOU-038.md) / python server)

## References

- <https://github.com/wh0amitz/PetitPotato>
- <https://upx.github.io/>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
