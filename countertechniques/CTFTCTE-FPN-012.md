# CTFTCTE-FPN-012 — Validate PKINIT trust and extract PAC material

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-012`](../techniques/CTFTTE-FPN-012.md) — Certificate-derived Kerberos authentication chain

---

## Offensive Recovery (CTF practitioner / solver)

Load the PFX with its export password and request a TGT for the backdoored
account. Keep the AS-REP encryption key printed by the exchange, then extract
the NT hash from the PAC of the ticket and switch to hash-based tooling.

## Forensic / Blue-Team Perspective (DFIR analyst)

Correlate certificate-based TGT requests (event 4768 with certificate
information) against the certificate-to-account binding. Flag machine accounts
that request tickets through PKINIT for the first time and audit every PFX
export.

## Preconditions

- A valid PFX plus its export password is in hand.
- The domain controller accepts PKINIT for the target account.

## Indicators

- PKINIT AS exchange returns an AS-REP encryption key.
- A ccache ticket for the account loads into subsequent tooling.
- NTLM-style access works with the recovered NT hash only.

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
