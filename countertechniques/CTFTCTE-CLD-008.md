# CTFTCTE-CLD-008 — Enumerate Azure AD/VM/storage from credentials

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-008`](../techniques/CTFTTE-CLD-008.md) — Azure management-plane misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Ask the plane what the identity can do before asking it for anything, and descend one scope at a time:
tenant → subscription → resource group → resource → data plane.

1. **Normalise the credential.** Separate what is present — client identifier with secret or certificate,
   user account, cached session file, metadata endpoint, raw token. Resolve the tenant (a domain name in
   the prompt is not a tenant identifier) and note the client identifier, because it decides which flows
   the endpoint accepts.
2. **Establish the identity from the plane itself.** One read of the signed-in principal, the token's own
   claims, or the caller-identity API answers *who* is acting. Do this before enumerating, so every later
   result is attributable.
3. **Enumerate the reachable scopes, not just the current one.** List every subscription and tenant the
   identity can see, then resource groups and resources within them. Delegation and management-group
   grants surface here and nowhere else.
4. **Read the authorisation layer, not only the inventory.** Role assignments and directory roles explain
   *why* a resource is reachable and point at the next hop: a principal with a role on another scope, an
   application holding a secret, a group whose membership can be read.
5. **Prefer the read that proves the claim.** Where the story says a resource is reachable, the evidence is
   the read that only an authorised principal can perform — not a dump of everything visible.
6. **Use control-plane execution only when the objective demands it, and gate it.** Actions that run a
   command on a resource change state; state the exact action and expected output before running it, and
   prefer a read-only alternative when the flag is data.
7. **Follow the plane into the data plane.** A resource's own API (storage, vault, database, registry,
   cluster) is a second authorisation check; the control-plane grant does not guarantee it.

Signatures to expect: a token whose audience names the plane you need; a subscription list longer than the
story implies; a role assignment at a parent scope explaining an otherwise surprising read; a resource
that answers on the control plane but refuses its data plane (a second grant is missing); an execution
action returning output instead of a status.

## Forensic / Blue-Team Perspective (DFIR analyst)

The control-plane audit log records every write and most reads with the caller's identity, the resource
and the operation, while the directory's sign-in log records how the identity authenticated — service
principal versus user, interactive versus non-interactive. Read together they separate a scheduled
deployment from an enumeration burst: the anomaly is a principal acting outside its deployment window, a
role assignment created just before the reads, or a resource first seen from an address that never touched
the subscription before. Control-plane execution actions (command run, extension install) are the highest
value entries because they are code execution. Remediation: revoke the credential, remove the excess role
assignment at its true scope, rotate anything the principal could read, and review delegation at
management-group level.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Valid Accounts: Cloud Accounts | Management-plane access from valid cloud credentials. |
| T1098.003 | Account Manipulation: Additional Cloud Roles | Role assignments are both the mechanism and the audit signal. |
| T1651 | Cloud Administration Command | Command execution through a control-plane action. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — caller identity, scope enumeration, role assignments, `az rest` for any endpoint
- [AzureHound](../tools/CTFTTOU-428.md) ([CTFTTOU-428](../tools/CTFTTOU-428.md)) — collect directory and resource grants into an attack graph
- [ROADtools](../tools/CTFTTOU-429.md) ([CTFTTOU-429](../tools/CTFTTOU-429.md)) — directory reconnaissance and token handling
- [AADInternals](../tools/CTFTTOU-430.md) ([CTFTTOU-430](../tools/CTFTTOU-430.md)) — tenant, user-object and token queries
- [Microsoft Graph API / Graph CLI](../tools/CTFTTOU-431.md) ([CTFTTOU-431](../tools/CTFTTOU-431.md)) — directory reads beyond the resource-manager API
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline artefact sweep and token decoding
- Az PowerShell modules, for Windows-shaped environments and module-only cmdlets

## References

- <https://learn.microsoft.com/en-us/cli/azure/>
- <https://learn.microsoft.com/en-us/azure/role-based-access-control/overview>
- <https://learn.microsoft.com/en-us/graph/api/overview>
- <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log>

