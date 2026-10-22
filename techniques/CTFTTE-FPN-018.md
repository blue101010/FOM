# CTFTTE-FPN-018 — Cross-domain credential reuse after hidden-namespace discovery

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-018`](../countertechniques/CTFTCTE-FPN-018.md) — Map adjacent namespaces and test credential reuse

---

## How the challenge author hides

A second domain is never mentioned in the scope handout: it surfaces only in a
hosts entry on the first domain controller. The author reuses one account name
and password across both domains, so the solver must discover the hidden
namespace, map its network records, and replay the harvested credentials.

## Evidence expected

- A hosts entry or DNS zone record names a second domain controller.
- Domain network enumeration returns records outside the known scope.
- An already-harvested account authenticates on the second domain.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | Reused credentials grant cross-domain access. |
| T1482 | Domain Trust Discovery | The second namespace and its records must be mapped. |

## Tools

- [netexec](../tools/CTFTTOU-016.md) (get-network module)
- hosts file inspection
- [nmap](../tools/CTFTTOU-033.md)
- [BloodHound](../tools/CTFTTOU-294.md)
- [SharpHound](../tools/CTFTTOU-295.md) collectors

## References

- <https://www.thehacker.recipes/ad/recon/domain>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
