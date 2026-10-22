# CTFTCTE-FPN-013 — Lock down certificate template ACLs and enrollment

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-013`](../techniques/CTFTTE-FPN-013.md) — Certificate template reconfiguration for arbitrary enrollment

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate ADCS with a certificate-aware scanner and list templates whose ACLs
allow a controlled account to write. Reconfigure the target template, request a
certificate with the desired UPN, then authenticate with the certificate to
obtain a TGT or recover the account hash.

## Forensic / Blue-Team Perspective (DFIR analyst)

Monitor certificate template modifications and CA issuance for anomalies: a
template edit followed by an unusual subject enrollment is a strong signal.
Least privilege on template ACLs and manager approval remove the write surface.

## Preconditions

- A domain account holds write access to a certificate template.
- A certificate authority is reachable and issues from that template.

## Indicators

- Template ACL grants write to a non-administrative principal.
- Subject-supplied identity is enabled on a template that did not allow it.
- A privileged certificate is issued right after a template change.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1649 | Steal or Forge Authentication Certificates | Template abuse forges a privileged certificate. |
| T1098 | Account Manipulation | Template settings altered to allow unauthorized enrollment. |

## Tools

- [certipy](../tools/CTFTTOU-020.md)
- [BloodHound](../tools/CTFTTOU-294.md)
- [SharpHound](../tools/CTFTTOU-295.md)

## References

- <https://www.thehacker.recipes/ad/movement/adcs/access-controls#certificate-templates-esc4>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
