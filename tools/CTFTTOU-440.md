# CTFTTOU-440 — azure_entra_search.py

> **Tool ID:** `CTFTTOU-440`  
> **Related techniques/counters:** CTFTTE-CLD-008, CTFTCTE-CLD-008

## Description

Bundled read-only sweep of the tenant directory for a **value** or a **property name**. It exists because
directory objects store their interesting content in fields nobody thinks to read — `notes`, `description`,
`displayName`, credential `displayName`, permission scopes, branding strings — and because a flag hunt needs
*attribution*: which object, which JSON path.

Capabilities, all of them GET-only through the signed-in `az` session:

- **Leaf-level matching over every object**: walks nested objects and arrays, so a value inside
  `keyCredentials[0].displayName` is found without knowing the shape in advance.
- **Property-name matching** (`--keys`): finds *which field* carries the pattern — the fastest way to spot
  the one object whose schema differs from the rest.
- **Pagination** on `@odata.nextLink` with a hard page cap, so a large tenant cannot silently truncate the
  result.
- **Per-endpoint outcome**: an endpoint that refuses (`403`) is reported by name instead of aborting the run.
- **`--dry-run`**: prints the exact `az rest` commands and touches nothing.
- **`--offline FILE`**: replays saved pages, so the paging/matching logic is regression-tested without a
  tenant.
- **`--sqlite DB`**: searches a *collected* directory dump (SQLite, read-only) across every text column — the
  attribution-preserving replacement for `strings dump.db | grep`, since each hit names the table, the row and
  the column.
- **`--json-out`**: an evidence artefact listing every hit with its object id and path.

`selftest` = 26 offline checks. No network, no state change.

## URL

- <https://learn.microsoft.com/en-us/graph/api/overview>

Canonical path in this repository:

```text
ctf-skills-main/ctf-cloud-azure/scripts/azure_entra_search.py
```

## Installation

Standard library only, plus an authenticated `az` for live runs:

```bash
python3 ctf-skills-main/ctf-cloud-azure/scripts/azure_entra_search.py selftest
az login --use-device-code        # or any session the challenge hands over
```

## Usage

```bash
S=ctf-skills-main/ctf-cloud-azure/scripts/azure_entra_search.py

python3 $S endpoints                                  # 17 presets, defaults listed
python3 $S find --query 'flag{'                       # default endpoint set
python3 $S find -q 'ctf\{[a-z0-9_]+\}' --regex        # regex mode
python3 $S find -q notes --keys                       # which objects carry that field
python3 $S find -q flag --endpoint users groups -e applications-credentials
python3 $S find -q flag --dry-run                     # print the az commands only
python3 $S find -q flag --offline saved_pages.json    # replay a saved capture
python3 $S find -q flag --sqlite roadrecon.db         # search a collected dump instead of the tenant
python3 $S find -q flag --sqlite roadrecon.db --table Users Groups
python3 $S find -q flag --json-out entra_hits.json    # evidence artefact
```

Presets worth knowing: `applications-credentials` and `servicePrincipals-credentials` expand
`keyCredentials`/`passwordCredentials` (where challenge authors hide values), `directoryRoles` and
`roleAssignments` cover privilege, `conditionalAccessPolicies` and `oauth2PermissionGrants` cover the
consent surface, `deletedUsers` asks for a consistency-level header and reaches the recycle bin.

## Pitfalls

- A `403` on an endpoint means a missing directory permission for the *delegated* identity — it is reported,
  not fatal; rerun with fewer endpoints rather than concluding the tenant is empty.
- `--sqlite` opens the database with `mode=ro`: it cannot corrupt a collected dump, and it does not need the
  tenant at all once the dump exists.
- `$expand` on credentials can be refused even when the plain collection is readable.
- A truncated result usually means pagination was capped: raise `--max-pages`.
- Matching is case-insensitive by default and on **string representations**, so booleans and numbers match
  too; use `--regex` when a pattern must be precise.
- The report contains secrets. Redact values before pasting anything into a write-up; keep the object id and
  path as the evidence instead.

## Related Techniques

CTFTTE-CLD-008, CTFTCTE-CLD-008

## References

- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [Application object properties](https://learn.microsoft.com/en-us/graph/api/resources/application)
