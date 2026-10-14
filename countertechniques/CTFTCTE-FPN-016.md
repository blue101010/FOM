# CTFTCTE-FPN-016 — Audit privileged tokens and unpack suspicious binaries

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-016`](../techniques/CTFTTE-FPN-016.md) — Packed token-impersonation binary evading endpoint defenses

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the current account's privileges; when SeImpersonatePrivilege is
present, deliver an impersonation binary to the target. If endpoint protection
blocks it, repackage the binary with a packer, serve it over HTTP, and execute
it to run commands as SYSTEM and plant a local account.

## Forensic / Blue-Team Perspective (DFIR analyst)

Watch process creation events for service accounts spawning shells as SYSTEM,
and inspect delivered binaries for packer signatures in the PE sections.
Token-impersonation success leaves logon events tied to impersonated identities.

## Preconditions

- The current service account holds SeImpersonatePrivilege.
- A file delivery channel to the victim host exists.

## Indicators

- `whoami -priv` reports SeImpersonatePrivilege on a service account.
- A packed PE executable arrives over HTTP and executes.
- Commands run under `NT AUTHORITY\SYSTEM` from the service process.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1134.001 | Access Token Manipulation: Token Impersonation/Theft | The privileged token is impersonated to escalate. |
| T1027 | Obfuscated Files or Information | Packing defeats static detection. |

## Tools

- [PetitPotato](../tools/CTFTTOU-028.md)
- [UPX](../tools/CTFTTOU-029.md)

## References

- <https://github.com/wh0amitz/PetitPotato>
- <https://upx.github.io/>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
