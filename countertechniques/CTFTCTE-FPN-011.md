# CTFTCTE-FPN-011 — Detect and revoke key-credential backdoors

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-011`](../techniques/CTFTTE-FPN-011.md) — Alternate key-credential backdoor on a machine account

---

## Offensive Recovery (CTF practitioner / solver)

Confirm the write edge on the computer object, then attach a key credential to
it and request a TGT through PKINIT. Derive the NT hash from the PAC. If one
collection tool reports no interesting path, re-collect the graph with a second
collector and compare coverage before giving up.

## Forensic / Blue-Team Perspective (DFIR analyst)

Audit `msDS-KeyCredentialLink` modifications (directory change event 5136) and
correlate new DeviceID values with issued certificates. Enforce key trust
settings so only managed workflows can attach alternate credentials.

## Preconditions

- A domain account with write access to a computer object is already held.
- Machine Account Quota prevents the machine-creation fallback.

## Indicators

- GenericWrite edge on a computer object in the attack-path graph.
- A fresh `msDS-KeyCredentialLink` value with no corresponding admin action.
- PKINIT TGT requests from a machine account that rarely uses certificates.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1098 | Account Manipulation | Credential material added to an existing machine account. |
| T1558 | Steal or Forge Kerberos Tickets | The planted certificate yields a forged TGT. |

## Tools

- [pywhisker](../tools/CTFTTOU-018.md)
- [certipy](../tools/CTFTTOU-020.md) (shadow action)
- [PKINITtools](../tools/CTFTTOU-019.md)

## References

- <https://www.thehacker.recipes/ad/movement/kerberos/shadow-credentials>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
