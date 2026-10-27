# CTFTTOU-431 — Microsoft Graph API and Graph CLI

> **Tool ID:** `CTFTTOU-431`  
> **Related techniques/counters:** CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009, CTFTTE-CLD-010, CTFTCTE-CLD-010

## Description

The tenant directory's REST surface, and the endpoint most Azure challenge flags actually live behind:
users, groups, applications, service principals, directory roles, role assignments, conditional-access
policies, and the sign-in objects that describe how an identity authenticated.

Two access paths, both worth knowing:

- **`az rest`** — any authenticated request, with `--resource https://graph.microsoft.com` selecting the
  audience. Present wherever the CLI is, needs no extra install, and shows the raw JSON.
- **A Graph CLI** (`mgc`) — generated commands per endpoint, quicker for browsing the surface, slower to
  install.

The endpoint list itself is a reconnaissance artefact: `v1.0/organization` identifies the tenant,
`v1.0/me` identifies the caller, `v1.0/directoryRoles` and `v1.0/roleManagement/directory/roleAssignments`
describe privilege, `v1.0/applications` and `v1.0/servicePrincipals` expose credentials and consent.

## URL

- <https://learn.microsoft.com/en-us/graph/api/overview>
- <https://github.com/microsoftgraph/msgraph-cli>

## Installation

`az rest` needs nothing beyond the CLI. The optional Graph CLI:

```bash
pipx install msgraph-cli          # PEP 668-safe on Kali
mgc --version
```

## Usage

```bash
G=https://graph.microsoft.com/v1.0

az rest --method get --url "$G/organization" -o json
az rest --method get --url "$G/me" -o json
az rest --method get --url "$G/users?\$select=userPrincipalName,id,displayName" -o json
az rest --method get --url "$G/groups?\$select=displayName,id" -o json
az rest --method get --url "$G/applications?\$select=appId,displayName" -o json
az rest --method get --url "$G/servicePrincipals?\$select=appId,displayName" -o json
az rest --method get --url "$G/directoryRoles" -o json
az rest --method get --url "$G/roleManagement/directory/roleAssignments" -o json
az rest --method get --url "$G/identity/conditionalAccess/policies" -o json
```

Pitfalls: a `401` means the token's audience is the resource manager rather than Graph — mint a Graph
token instead of retrying; a `403` is a missing scope or role, and the error body names which; `$select`
and `$filter` must be URL-quoted for the shell; paging is real (`@odata.nextLink`) and a truncated listing
is a common dead end.

## Related Techniques

CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009, CTFTTE-CLD-010, CTFTCTE-CLD-010

## References

- [Microsoft Graph REST API v1.0](https://learn.microsoft.com/en-us/graph/api/overview)
- [Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [az rest](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-rest)
