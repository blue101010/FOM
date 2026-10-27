# CTFTTOU-428 — AzureHound

> **Tool ID:** `CTFTTOU-428`  
> **Related techniques/counters:** CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## Description

The Azure/Entra collector for the BloodHound graph model. Given a delegated or application identity it
walks the directory and the resource-manager scopes and emits principals, roles, assignments and trust
edges, which the BloodHound interface then renders as reachable paths.

What it is for in a challenge: turning a flat list of role assignments into a **path**. A directory dump
says "this group holds a role"; a graph says which principals can add themselves to that group, and
therefore which single edge the flag sits behind. It collects only — it does not exploit.

Two collection surfaces exist and are not interchangeable: the directory graph (users, groups,
applications, service principals, directory roles) and the resource model (subscriptions, resource
groups, resources, role assignments). A challenge that grants a management-group-scoped role only becomes
visible through the resource side.

## URL

- <https://github.com/SpecterOps/AzureHound>
- <https://bloodhound.specterops.io/>

## Installation

Release binaries, or a Go build:

```bash
# binary release, matching host architecture
curl -sL -o azurehound.zip https://github.com/SpecterOps/AzureHound/releases/latest/download/azurehound-linux-amd64.zip
unzip azurehound.zip && sudo install azurehound /usr/local/bin/ && azurehound --help

# or from source
go install github.com/specterops/azurehound/v2/cmd/azurehound@latest
```

The graph database (BloodHound) is a separate service, commonly run as a container. Record the collection
output even when no database is available: the JSON is the evidence.

## Usage

```bash
# token-based, when a token was recovered rather than a password
azurehound -j "$(cat token.json)" list --tenant TENANT_ID -o results.json

# credential-based (refresh token / username+password as the collector expects)
azurehound -r REFRESH_TOKEN list --tenant TENANT_ID -o results.json

# scope the collection when the identity is narrow
azurehound -j "$(cat token.json)" list subscriptions -o subs.json
```

Flag names changed between the standalone collector and the version folded into BloodHound, so confirm
with `azurehound --help` and `azurehound list --help` before scripting. Collection is read-only, but the
volume of requests is large enough to be visible in sign-in and audit logs — that is the DFIR signal too.

## Related Techniques

CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## References

- [AzureHound releases](https://github.com/SpecterOps/AzureHound/releases)
- [BloodHound documentation](https://bloodhound.specterops.io/)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
