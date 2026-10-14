# CTFTCTE-FPN-018 — Map adjacent namespaces and test credential reuse

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-018`](../techniques/CTFTTE-FPN-018.md) — Cross-domain credential reuse after hidden-namespace discovery

---

## Offensive Recovery (CTF practitioner / solver)

Read hosts entries and DNS zone records on a compromised host to find adjacent
namespaces, enumerate their network records, and replay every harvested
credential against the new domain. Re-run the graph collection on the second
domain before planning the next stage.

## Forensic / Blue-Team Perspective (DFIR analyst)

Cross-domain logons with a mismatched account domain signal credential reuse.
Audit hosts file modifications on domain controllers and treat shared
credentials across security boundaries as an immediate remediation item.

## Preconditions

- Administrative access to a host that references the hidden namespace.
- Credentials harvested from the first domain are available for replay.

## Indicators

- A hosts entry or zone record names a second domain controller.
- The same account authenticates on both domains with one password.
- Network records outside the declared scope appear in zone data.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | Reused credentials grant cross-domain access. |
| T1482 | Domain Trust Discovery | The second namespace and its records must be mapped. |

## Tools

- [netexec](../tools/CTFTTOU-016.md) (get-network module)
- [nmap](../tools/CTFTTOU-033.md)
- [BloodHound / SharpHound](../tools/CTFTTOU-017.md) collectors

## References

- <https://www.thehacker.recipes/ad/recon/domain>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
