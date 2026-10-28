# CTFTTE-CLD-008 — Azure management-plane misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-008`](../countertechniques/CTFTCTE-CLD-008.md) — Enumerate Azure AD/VM/storage from credentials

---

## How the challenge author hides

The flag sits behind the **management plane** — the subscription's control API, the tenant directory, or
a resource whose data plane is only reachable after a control-plane action. The challenge hands over
something that authenticates (a service-principal secret, a user account, a certificate, an instance
metadata endpoint, a cached session) and the configuration intends that principal to be narrower than it
is: an over-broad role assignment, a directory role granted to a guest, a delegation that reaches another
subscription, or a control-plane action that executes code on a resource.

Design variants, in increasing subtlety:

- **Credential in an artefact.** Client identifier plus secret or certificate in a configuration, a
  pipeline variable, a bundle or a log; resolving the tenant and subscription identifiers is the first
  move, not the last.
- **Instance metadata reachable.** From a workload, or through a server-side request forgery, the metadata
  service mints a token for whatever resource the caller names — so the plane reached is chosen by the
  solver, not by the application.
- **Broad directory role.** The principal reads or modifies directory objects, which exposes further
  credentials, applications, service principals and group memberships.
- **Control plane as execution.** An action that runs a command or a script on a resource turns a
  read-looking grant into code execution on a host, with the output returned by the same API.
- **Cross-subscription reach.** A grant at a management-group or root scope, or a guest principal with
  directory-wide read, exposes subscriptions the narrative never mentions.
- **Plane as a doorway.** The credential is valid for the control plane, and the flag is in a resource's
  **data** plane (storage, vault, database, container registry) reached only after discovery, chaining
  into those pairs.

Boundary: with no credential at all the challenge is anonymous exposure; with a store-scoped key it is the
storage pair; with token material that must be re-audienced it is the session-material pair. Here the
material authenticates to a control API.

## Indicators

- a tenant or subscription identifier in the prompt, a leaked script or a deployment template
- a client identifier with a secret or certificate, or a workload identity endpoint in an environment dump
- directory or resource hostnames (`management.*`, `graph.*`, `login.*`, `vault.*`, `*.azurewebsites.net`)
- role names that read as administrative, or a template assigning a role at a wide scope
- a story about "we gave the app too many permissions" or "the guest account should not see this"
- an instance metadata address inside a request-forgery surface
- deployment templates, parameter files and pipeline definitions offered as artefacts

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Valid Accounts: Cloud Accounts | Management-plane access from valid cloud credentials. |
| T1098.003 | Account Manipulation: Additional Cloud Roles | Over-broad role and directory-role grants are what make the plane reachable. |
| T1552.001 | Unsecured Credentials: Credentials In Files | The credential normally arrives in a configuration, template or pipeline artefact. |
| T1651 | Cloud Administration Command | Control-plane actions that execute commands on a resource. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — control-plane enumeration, `az rest` for any API the CLI does not wrap
- [AzureHound](../tools/CTFTTOU-428.md) ([CTFTTOU-428](../tools/CTFTTOU-428.md)) — directory and resource grant collection into a graph
- [ROADtools](../tools/CTFTTOU-429.md) ([CTFTTOU-429](../tools/CTFTTOU-429.md)) — tenant reconnaissance and token work around the same directory
- [AADInternals](../tools/CTFTTOU-430.md) ([CTFTTOU-430](../tools/CTFTTOU-430.md)) — directory objects, tenant information and token inspection
- [Microsoft Graph API / Graph CLI](../tools/CTFTTOU-431.md) ([CTFTTOU-431](../tools/CTFTTOU-431.md)) — directory reads the resource-manager API does not expose
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline artefact sweep before any authenticated request
- [azure_entra_search.py](../tools/CTFTTOU-440.md) ([CTFTTOU-440](../tools/CTFTTOU-440.md)) — read-only directory sweep for a value or a property name, with page traversal and field-path attribution
- Az PowerShell modules, when the environment is Windows-shaped or a module-only cmdlet is needed

## References

- <https://learn.microsoft.com/en-us/cli/azure/>
- <https://learn.microsoft.com/en-us/azure/role-based-access-control/overview>
- <https://learn.microsoft.com/en-us/graph/api/overview>
- <https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token>
