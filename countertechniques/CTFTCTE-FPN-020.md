# CTFTCTE-FPN-020 — Dump directory attributes and search hidden payloads

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-020`](../techniques/CTFTTE-FPN-020.md) — Flag payload embedded in directory object properties

---

## Offensive Recovery (CTF practitioner / solver)

After domain compromise, dump the directory into serialized artifacts and search
every field case-insensitively for the flag format. When no flag file exists on
any host, treat directory attributes as the payload location.

## Forensic / Blue-Team Perspective (DFIR analyst)

The same dump technique surfaces injected payloads during incident response.
Audit large directory reads (event 4662) and watch for wholesale attribute
exfiltration that has no operational justification.

## Preconditions

- Directory access with enumeration rights.
- A dump tool that serializes every object attribute.

## Indicators

- Hosts are clean while the flag format exists in directory data.
- A bulk directory read returns all attributes at once.

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
