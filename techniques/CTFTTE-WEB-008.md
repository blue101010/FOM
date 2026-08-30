# CTFTTE-WEB-008 — Legacy short-name namespace disclosure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-008`](../countertechniques/CTFTCTE-WEB-008.md) — Reconcile a disclosed short-name namespace

---

## How the challenge author hides

An application exposes a legacy short-name namespace that discloses partial
resource names while direct browsing keeps the complete resources hidden. The
challenge distinguishes naming evidence from proof that a resource is present
or reachable.

## Evidence expected

- A supplied observation identifies a short-name alias.
- The complete candidate name is corroborated by challenge metadata or a
  permitted artifact.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | 8.3 short-name disclosure echoes filesystem discovery. |

## References

- <https://learn.microsoft.com/windows/win32/fileio/naming-a-file>
