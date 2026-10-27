# CTFTTE-CLD-010 — Secret store reachable by a workload identity

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-010`](../countertechniques/CTFTCTE-CLD-010.md) — Enumerate secret stores the held identity can read

---

## How the challenge author hides

The objective is a value inside a managed secret store — a vault secret, a certificate, a key, a
parameter — and the identity the player already holds carries a **data-plane grant** to it. Nothing
has to be broken: the flag is behind a read that the configuration intends to be routine, and the
work is to find which store, which object and which version the identity actually reaches.

Design variants, in increasing subtlety:

- **Grant without discovery.** The identity can read the store but holds no listing permission, so
  object names must be guessed from the narrative, from a leaked template, or from conventional names.
- **Dual authorisation models.** The store accepts both a role-assignment model and a legacy
  per-object access-policy model; the identity is granted through the one the player does not think
  to check, so an empty role assignment list is not evidence of denial.
- **Version history.** The current value is a decoy or blank while a previous version still holds the
  answer; only reading the version list exposes it.
- **Soft-deleted object.** The object was deleted and remains recoverable while purge protection keeps
  it restorable — the store answers "gone" to a naive read and "still here" to a recovery-aware one.
- **Object kind mismatch.** The answer sits in a certificate or a key, while the player searches
  secrets only.
- **Store reached from a workload.** The grant belongs to the workload's identity, not the human one,
  so the token must first come from the instance metadata or the workload's own credential chain.

Boundary: when the identity reaches the store through an over-broad administrative role over the whole
subscription, the pair is the over-permissive-role one; when the material is a bearer credential
embedded in a URL, it belongs to the signed-URL pair. Here the grant is narrow, deliberate and
data-plane.

## Indicators

- a vault-style hostname in the prompt, a leaked template, a configuration file or an environment dump
- identity-based connection material: a connection string with no key, an endpoint plus "use managed
  identity", a `SecretUri`/`KeyUri` reference instead of a literal value
- role names that only make sense on a data plane (read a secret, read a certificate, read a key)
- a workload environment exposing an identity endpoint or an identity client identifier
- the story says the secret "is managed" or "is rotated", implying versions or a recovery window
- a deployment template showing an access policy or a role assignment beside the store

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1555 | Credentials from Password Stores | The store is the credential repository; the recovery is an authorised read, not an exploit. |
| T1552.001 | Unsecured Credentials: Credentials In Files | Leaked templates, connection strings and environment dumps are the usual discovery artefacts. |
| T1078.004 | Valid Accounts: Cloud Accounts | The read is performed by a legitimate workload identity. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — data-plane reads and `az rest` calls against the store's API
- [Microsoft Graph API / Graph CLI](../tools/CTFTTOU-431.md) ([CTFTTOU-431](../tools/CTFTTOU-431.md)) — resolving the identity, its grants and its group memberships
- [MicroBurst](../tools/CTFTTOU-433.md) ([CTFTTOU-433](../tools/CTFTTOU-433.md)) — enumerating the surrounding subscription for stores and secrets
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline sweep for store hostnames, identity endpoints and secret-bearing configuration
- a raw HTTP client, when the data-plane API version or the response shape matters

## References

- <https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide>
- <https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy>
- <https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview>
- <https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview>
