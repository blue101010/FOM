# CTFTTE-FPN-013 — Certificate template reconfiguration for arbitrary enrollment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-013`](../countertechniques/CTFTCTE-FPN-013.md) — Lock down certificate template ACLs and enrollment

---

## How the challenge author hides

A domain user holds WriteDacl over a certificate template. The path is invisible
to basic user and share enumeration: it lives in ADCS template ACLs, and only a
graph-aware collection reveals it. The solver reconfigures the template
(ESC4), enrolls a certificate for an arbitrary identity, and authenticates
with it.

## Evidence expected

- A non-admin account holds write access on a certificate template object.
- The template permits subject-supplied identity after reconfiguration.
- Certificate-based authentication succeeds for a privileged identity.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1649 | Steal or Forge Authentication Certificates | Template abuse forges a privileged certificate. |
| T1098 | Account Manipulation | Template settings altered to allow unauthorized enrollment. |

## Tools

- [certipy](../tools/CTFTTOU-020.md)
- [BloodHound](../tools/CTFTTOU-294.md)
- [SharpHound](../tools/CTFTTOU-295.md)
- [openssl](../tools/CTFTTOU-023.md)

## References

- <https://www.thehacker.recipes/ad/movement/adcs/access-controls#certificate-templates-esc4>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
