# CTFTTE-WEB-007 — Deployment metadata index disclosure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-007`](../countertechniques/CTFTCTE-WEB-007.md) — Analyze a disclosed deployment metadata index

---

## How the challenge author hides

A deployment metadata artifact reveals a directory tree, historical paths, or
resource names that are absent from the visible application navigation. The
challenge requires correlating this disclosure with a supplied application
inventory instead of treating every listed path as accessible.

## Evidence expected

- A supplied metadata artifact names a resource absent from the public index.
- The disclosed name is corroborated by the declared challenge inventory.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | Deployment-metadata disclosure echoes file/directory discovery. |

## References

- <https://owasp.org/www-project-web-security-testing-guide/>
