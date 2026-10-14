# CTFTTE-FPN-020 — Flag payload embedded in directory object properties

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-020`](../countertechniques/CTFTCTE-FPN-020.md) — Dump directory attributes and search hidden payloads

---

## How the challenge author hides

The final flag is not a file on any host: it is stored in a property of a
directory object, reachable only by dumping the whole domain and searching the
serialized attributes. Host compromise alone returns nothing; directory-level
exfiltration is the required final stage.

## Evidence expected

- No flag file exists on the last compromised domain controller.
- A full directory dump serializes every object attribute.
- A case-insensitive search of the dump reveals the flag string.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1087.002 | Account Discovery: Domain Account | Domain objects are enumerated and dumped. |
| T1213 | Data from Information Repositories | The payload is extracted from directory attributes. |

## Tools

- [ldapdomaindump](../tools/CTFTTOU-035.md)
- [grep](../tools/CTFTTOU-036.md)
- [jq](../tools/CTFTTOU-037.md)

## References

- <https://github.com/dirkjanm/ldapdomaindump>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
