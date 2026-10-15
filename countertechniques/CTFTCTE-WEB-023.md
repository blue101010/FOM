# CTFTCTE-WEB-023 — Introspect the schema and over-fetch hidden fields

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-023`](../techniques/CTFTTE-WEB-023.md) — GraphQL introspection disclosure / field-level authorization gap

---

## Offensive Recovery (CTF practitioner / solver)

1. **Find the GraphQL endpoint**: page source, `/graphql`, `/api/graphql`,
   `.graphql` files, or a framework hint (Apollo, GraphiQL landing page).
2. **Introspect**: POST the `__schema { types { name fields { name } } }` query; if
   introspection is disabled, fall back to wordlists of field names and error-message
   suggestions, or clue mining in client bundles.
3. **Triage the schema** for sensitive field names (`password`, `hidden`, `secret`,
   `token`, `admin`, `flag`) and for types the UI never renders —
   `graphql-schema-dump.py` automates the dump and the highlight.
4. **Compare resolvers**: query the list (which the UI filters) and the single-object
   query by id; enumerate ids the list does not return and over-fetch the sensitive
   fields on them.
5. **Validate**: the hidden object's sensitive field satisfies the flag format.

## Forensic / Blue-Team Perspective (DFIR analyst)

In production, open introspection and per-field authorization gaps are inventory leaks:
an unauthenticated actor can enumerate the entire data model and probe object ids.
Blue teams detect the pattern by alerting on `__schema`/`__type` queries from external
sources and on field selections that the presentation layer never uses.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | An introspectable GraphQL API exposes its own attack surface; field-level authz gaps are exploited through ordinary queries. |

## Tools

- [graphql-schema-dump.py](../tools/scripts/graphql-schema-dump.py) ([CTFTTOU-271](../tools/CTFTTOU-271.md))
- inql ([CTFTTOU-272](../tools/CTFTTOU-272.md))
- jq ([CTFTTOU-037](../tools/CTFTTOU-037.md))
- curl ([CTFTTOU-038](../tools/CTFTTOU-038.md))

## References

- <https://github.com/jameskaois/ctf-writeups/blob/main/vsl-ctf-2026/mrgraph/README.md>
- <https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html>
