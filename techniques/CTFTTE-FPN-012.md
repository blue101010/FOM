# CTFTTE-FPN-012 — Certificate-derived Kerberos authentication chain

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-012`](../countertechniques/CTFTCTE-FPN-012.md) — Validate PKINIT trust and extract PAC material

---

## How the challenge author hides

The planted or stolen certificate is useless to ordinary password-based tooling.
The solver must chain PKINIT authentication (pass the certificate) into a TGT,
then extract the account's NT hash from the PAC of the ticket (unPAC the hash)
before standard Kerberos and NTLM moves unlock the next hop.

## Evidence expected

- A PFX certificate and its export password are recovered from a previous stage.
- The PKINIT exchange logs an AS-REP encryption key for the account.
- The derived NT hash opens delegation or ticket-forging moves on the domain.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1558 | Steal or Forge Kerberos Tickets | TGT obtained through certificate-based PKINIT. |
| T1649 | Steal or Forge Authentication Certificates | The PFX is the credential that drives the chain. |

## Tools

- [gettgtpkinit.py](../tools/CTFTTOU-021.md)
- [getnthash.py](../tools/CTFTTOU-022.md)
- KRB5CCNAME-aware tooling

## References

- <https://www.thehacker.recipes/ad/movement/kerberos/pass-the-certificate>
- <https://www.thehacker.recipes/ad/movement/kerberos/unpac-the-hash>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
