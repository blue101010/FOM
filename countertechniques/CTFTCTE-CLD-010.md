# CTFTCTE-CLD-010 — Enumerate secret stores the held identity can read

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-010`](../techniques/CTFTTE-CLD-010.md) — Secret store reachable by a workload identity

---

## Offensive Recovery (CTF practitioner / solver)

Treat the identity as the discovery tool: ask the control plane which stores exist, ask the store's
own data plane which objects the identity may read, and reconcile the two answers — they are granted
through different models and disagree often.

1. **Establish which identity you are, from which plane.** A human session, a workload identity and an
   instance-metadata credential reach different stores; resolve the object identifier and the token
   audience before enumerating.
2. **List stores at the control plane.** Enumerate the scope you can see for store resources and their
   recovery settings; note the ones whose name matches the narrative even if the grant looks absent.
3. **Check both authorisation models.** A data-plane grant may come from a role assignment or from a
   legacy per-object policy. An empty role-assignment list is not a denial — look for the policy form,
   and look for grants inherited through a group or a parent scope.
4. **Walk object kinds, not just one.** Ask for secrets, then keys, then certificates; an empty answer in
   one kind is routinely filled by another.
5. **Read versions and recovery state.** Request the object, then its version list; if it reports
   deleted, request the recoverable form. A decoy current value with a live earlier version is a common
   design.
6. **Fall back to the conventional names.** When listing is denied, request the names a story would
   use (flag-like, environment-scoped, purpose-scoped) instead of brute-forcing a dictionary.
7. **Record the grant, not just the value.** The evidence is the store, the object, the version and the
   authorisation path that allowed the read.

Signatures to expect: a store that exists but refuses listing while answering a direct read; a role
assignment visible only at a parent scope; a version list with more entries than the current value
implies; a recovery endpoint that succeeds where the plain read failed; a per-object policy that grants
exactly the read the story needs.

## Forensic / Blue-Team Perspective (DFIR analyst)

The store's data-plane diagnostic or audit stream records every object read with the caller identity,
the object and the version; the control-plane audit log records the grant that made it possible, often
long before, at a different scope. The pair of the two is what distinguishes a legitimate deployment
read from a challenge-style one — a read performed by a workload identity outside its deployment
window, or by a principal whose grant was created by a template change, is the anomaly. Check the
recovery and version endpoints as well: a recover or version-list call is a strong tell. Remediation is
a grant review plus rotation of every object the identity could read, and removal of stale per-object
policies.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1555 | Credentials from Password Stores | Reading the store is the recovery action; the authorisation path is what makes it a finding. |
| T1078.004 | Valid Accounts: Cloud Accounts | A workload identity performs the read. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — control-plane listing plus data-plane read and `az rest` for shapes the CLI hides
- [Microsoft Graph API / Graph CLI](../tools/CTFTTOU-431.md) ([CTFTTOU-431](../tools/CTFTTOU-431.md)) — resolving identity, groups and inherited grants
- [MicroBurst](../tools/CTFTTOU-433.md) ([CTFTTOU-433](../tools/CTFTTOU-433.md)) — subscription-wide sweep for stores and secret-bearing configuration
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline artefact sweep before touching the tenant
- a raw HTTP client, for data-plane API versions and response shapes

## References

- <https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide>
- <https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy>
- <https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview>
- <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log>
