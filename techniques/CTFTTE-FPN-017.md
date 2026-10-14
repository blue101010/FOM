# CTFTTE-FPN-017 — Coerced domain controller authentication toward a delegated host

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-017`](../countertechniques/CTFTCTE-FPN-017.md) — Constrain delegation trust and detect coerced authentication

---

## How the challenge author hides

A compromised server is configured with unconstrained delegation: any ticket
sent to it is cached locally. The author expects the solver to monitor incoming
authentication on that server while coercing the domain controller to connect,
capturing the DC machine ticket. A case-sensitivity detail in the coercion
hostname is the hidden obstacle.

## Evidence expected

- The controlled server has unconstrained delegation set on its account.
- The domain controller is reachable from the server.
- A coerced connection from the DC lands while a ticket monitor is listening.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1558 | Steal or Forge Kerberos Tickets | The coerced DC machine TGT is captured and reused. |
| T1187 | Forced Authentication | Printer-bug coercion forces the DC to authenticate. |

## Tools

- [Rubeus](../tools/CTFTTOU-030.md) (monitor mode)
- [printerbug.py](../tools/CTFTTOU-031.md)
- [getST.py](../tools/CTFTTOU-032.md)

## References

- <https://www.thehacker.recipes/ad/movement/kerberos/delegations/unconstrained>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
