# CTFTTOU-439 — azure_ctf_inventory.py

> **Tool ID:** `CTFTTOU-439`  
> **Related techniques/counters:** CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011

## Description

The bundled offline triage script of the `ctf-cloud-azure` skill. It answers the questions that must be
settled **before** any authenticated request, and it never touches the network:

- **`jwt`** — decode a token without verification: header (algorithm, key identifier), claims (tenant,
  object, client, user, scopes, roles, groups, expiry) and a classification of what the token *is*
  (access, identity or renewal material) plus which plane its audience names.
- **`sas`** — decode a signed storage URL: account, service, resource type, decoded operation letters,
  validity window, and whether the grant exceeds read-only.
- **`artifacts`** — sweep local files (prompts, bundles, configuration, environment dumps, logs) for the
  identifiers a challenge hides in them: tenant and client identifiers, store and vault hostnames,
  application-service hosts, instance-metadata endpoints, connection strings, account keys, signed-URL
  parameters and token-shaped strings — grouped, with a suggested next step per hit.
- **`imds`** — print (never execute) the instance-metadata requests that mint a token for a named resource,
  ready to paste into the surface that reaches the endpoint.

Capability sheet, not a value sheet: nothing here is specific to one challenge, and the script is meant to
be re-run on every artefact set.

## URL

- <https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens>

Canonical path in this repository:

```text
ctf-skills-main/ctf-cloud-azure/scripts/azure_ctf_inventory.py
```

## Installation

Standard library only — no installation, no virtual environment:

```bash
python3 ctf-skills-main/ctf-cloud-azure/scripts/azure_ctf_inventory.py --help
python3 ctf-skills-main/ctf-cloud-azure/scripts/azure_ctf_inventory.py selftest
```

## Usage

```bash
# what is this token, and which plane does it open?
python3 .../azure_ctf_inventory.py jwt --token "$(cat token.jwt)"
python3 .../azure_ctf_inventory.py jwt --file ~/.azure/accessTokens.json

# what does this signed URL actually grant?
python3 .../azure_ctf_inventory.py sas --url "https://acct.blob.core.windows.net/c/f?sv=...&sig=..."

# what did the artefact set give me?
python3 .../azure_ctf_inventory.py artifacts --path ./challenge ./notes.md --json

# requests to paste into the surface that can reach the metadata service
python3 .../azure_ctf_inventory.py imds --resource https://management.azure.com/
```

`selftest` builds its own token and signature fixtures and asserts every parser offline, so the script can
be trusted before it is pointed at a real artefact.

## Related Techniques

CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009,
CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011

## References

- [Microsoft identity platform access tokens](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
- [Shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [Azure Instance Metadata Service](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service)
