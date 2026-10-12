# CTFTTE-OSI-009 — Historical-infrastructure lure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-009`](../countertechniques/CTFTCTE-OSI-009.md) — Gate historical OSINT behind current-surface checks

---

## How the challenge author hides

Years of OSINT sediment accumulate around a challenge domain: old AWS addresses, broken DNS delegations, expired certificates, archived virtual hosts. Whether planted or simply abandoned, this historical surface absorbs active effort — port scans, passive collection, write-up archaeology — while the current first-party site holds the door. The lure is time itself, not a planted artifact.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; distraction via accumulated infrastructure history. |

## Tools

- dig
- Subfinder
- crt.sh

## References

- <https://github.com/projectdiscovery/subfinder>
- Add challenge write-up link
