# CTFTTOU-427 — Azure CLI

> **Tool ID:** `CTFTTOU-427`  
> **Related techniques/counters:** CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011

## Description

The provider's first-party command line, and the most reliable single instrument in an Azure challenge.
Two properties make it the backbone rather than one tool among many:

- **Every control-plane API is reachable.** `az rest` sends an arbitrary authenticated request with any
  method, URL, body and `--resource` audience, so an endpoint missing from the CLI surface is still one
  command away.
- **It reports who it is.** The caller-identity and account commands establish the acting principal before
  any enumeration, which is what makes later results attributable.

The command groups that matter in a challenge: `account` (identity and scopes), `group` and `resource`
(inventory), `role assignment` (the authorisation layer), `ad` and `rest` (directory and Graph),
`storage` and `keyvault` (data planes), `vm` and `vmss` (compute, run-command), `webapp` and `functionapp`
(application services), `acr` (registry), `aks` (cluster credentials). Data-plane plugins installed
separately (`az storage`, `az keyvault`) are the ones whose authorisation model differs from the control
plane — expect a second refusal there.

## URL

- <https://learn.microsoft.com/en-us/cli/azure/>
- <https://learn.microsoft.com/en-us/cli/azure/reference-index>

## Installation

Kali / Debian ships the CLI in the repository (also the `python3-azure-cli` packages):

```bash
sudo apt update && sudo apt install -y azure-cli
az version
```

Never `pip install azure-cli` system-wide on Kali (PEP 668). If a newer version is required, use the
official install script inside a dedicated environment or the vendor's package for the distribution.

## Usage

```bash
# identity and reachable scopes
az account show -o json
az account list --all -o table
az ad signed-in-user show -o json            # delegated principal, when permitted
az rest --method get --url https://graph.microsoft.com/v1.0/me -o json

# inventory and authorisation
az group list -o table
az resource list --output json
az role assignment list --all --include-inherited -o json
az ad app list --all -o table
az ad sp list --all -o table

# data planes (separate authorisation)
az storage container list --account-name ACCT --auth-mode login -o table
az keyvault secret show --vault-name VAULT --name NAME
az acr login -n REGISTRY

# any API, including preview versions the CLI does not wrap
az rest --method get --url "https://management.azure.com/subscriptions?api-version=2020-01-01"

# compute: read the instance view, or run a command (state changing – gate it)
az vm list -d -o table
az vm run-command invoke -g RG -n VM --command-id RunShellScript --scripts "id"
```

Challenges hand over fragments rather than a configured CLI: a client identifier with a secret, a
certificate, a cached profile directory, or a raw token. Log in with the least state you need and keep
the profile disposable:

```bash
az login --service-principal -u CLIENT_ID -p SECRET --tenant TENANT_ID
az login --identity                            # from a workload, or through a reachable endpoint
az login --use-device-code                     # when only an interactive flow is allowed
AZURE_ACCESS_TOKEN=... az account show --sdk-auth   # when only an access token is available
```

Pitfalls seen in practice: a token minted for one audience is rejected by another plane (`--resource` fixes
it); `az` caches the account in a profile directory, so a "wrong tenant" error usually means a stale profile
(`--tenant` or a fresh `AZURE_CONFIG_DIR`); a subscription hidden by policy still answers a direct
`az rest` on its scope; a data-plane refusal after a successful control-plane read means a missing
data-plane role, not a missing credential.

## Related Techniques

CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-010, CTFTCTE-CLD-010,
CTFTTE-CLD-011, CTFTCTE-CLD-011

## References

- [Azure CLI reference](https://learn.microsoft.com/en-us/cli/azure/reference-index)
- [az rest](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-rest)
- [Azure role-based access control](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
