# CTFTCTE-FPN-017 — Constrain delegation trust and detect coerced authentication

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-017`](../techniques/CTFTTE-FPN-017.md) — Coerced domain controller authentication toward a delegated host

---

## Offensive Recovery (CTF practitioner / solver)

Start a ticket monitor on the delegated host targeting the domain controller
machine account, then trigger the printer-bug coercion with the exact hostname
casing. Capture the DC machine ticket, request a service ticket with it, and
use the resulting access to dump the domain controller.

## Forensic / Blue-Team Perspective (DFIR analyst)

Unconstrained delegation should not exist: replace it with constrained
delegation or resource-based delegation. Monitor for spooler-coerced logons and
ticket monitoring on member servers, and protect DC machine accounts from
coercion sources.

## Preconditions

- A compromised server has unconstrained delegation.
- The domain controller is reachable and coerced-authentication-prone.

## Indicators

- `TrustedForDelegation` is set on a non-DC computer account.
- The DC authenticates to the delegated host without a user session.
- A ticket monitor is active while a coercion request fires.

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
