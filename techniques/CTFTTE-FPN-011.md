# CTFTTE-FPN-011 — Alternate key-credential backdoor on a machine account

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-011`](../countertechniques/CTFTCTE-FPN-011.md) — Detect and revoke key-credential backdoors

---

## How the challenge author hides

A domain user is granted GenericWrite over a computer account, but the classic
exploitation path (create a fake machine then abuse delegation) is closed by a
zero Machine Account Quota. The intended move is to attach an alternate key
credential (`msDS-KeyCredentialLink`) to the computer object and authenticate
with the generated certificate, without ever changing the account's password.

## Evidence expected

- A write edge on a computer object appears in the collected attack-path graph.
- Machine Account Quota is zero, ruling out machine-account creation.
- The target computer object accepts an unconstrained key credential write.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1098 | Account Manipulation | Credential material added to an existing machine account. |
| T1558 | Steal or Forge Kerberos Tickets | The planted certificate yields a forged TGT. |

## Tools

- [pywhisker](../tools/CTFTTOU-018.md)
- [certipy](../tools/CTFTTOU-020.md) (shadow action)
- [PKINITtools](../tools/CTFTTOU-019.md)
- [BloodHound](../tools/CTFTTOU-294.md)
- [SharpHound](../tools/CTFTTOU-295.md)

## References

- <https://www.thehacker.recipes/ad/movement/kerberos/shadow-credentials>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
