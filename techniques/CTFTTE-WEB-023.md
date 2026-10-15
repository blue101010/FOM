# CTFTTE-WEB-023 — GraphQL introspection disclosure / field-level authorization gap

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-023`](../countertechniques/CTFTCTE-WEB-023.md) — Introspect the schema and over-fetch hidden fields

---

## How the challenge author hides

The flag lives in a sensitive field of a hidden GraphQL object (e.g. `postPassword` on a
post with `isHidden: true`). The list query the UI uses filters hidden objects out, so the
application looks complete and innocent — but the GraphQL endpoint accepts `__schema`
introspection, which discloses every type and field name, and the single-object query does
not re-apply the list-level filter. Introspection turns authorization-by-obscurity into an
open book: the schema names the secret, and a direct query by id reads it. The player is
steered toward classic web-vuln hunting while the actual path is schema disclosure plus a
field-level authorization gap.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | An introspectable GraphQL API exposes its own attack surface; field-level authz gaps are exploited through ordinary queries. |

## Tools

- [graphql-schema-dump.py](../tools/scripts/graphql-schema-dump.py) ([CTFTTOU-271](../tools/CTFTTOU-271.md))
- inql ([CTFTTOU-272](../tools/CTFTTOU-272.md))
- jq ([CTFTTOU-037](../tools/CTFTTOU-037.md))

## References

- <https://github.com/jameskaois/ctf-writeups/blob/main/vsl-ctf-2026/mrgraph/README.md> (VSL CTF 2026 "mrGraph")
- <https://graphql.org/learn/introspection/> (introspection semantics)
- <https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html> (OWASP: disable introspection in production)
