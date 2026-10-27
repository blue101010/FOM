# CTFTCTE-CLD-007 — Enumerate and query exposed cloud databases

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-007`](../techniques/CTFTTE-CLD-007.md) — Cloud NoSQL-store misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Separate the two questions the store answers differently — *what exists* and *what may I read* — then
build the request the store actually accepts.

1. **Identify the API surface.** A document API, a key-value API and a Mongo-compatible endpoint answer
   different paths with different authentication. Read the endpoint's error body before trying payloads:
   a version or `api-version` complaint names the protocol you must speak.
2. **Establish the authentication model.** Either the request carries a bearer token for the store's own
   audience, or it is **signed** with the account key (a date, a version, a resource and a signature over
   a canonical string). The signed form fails with a signature error rather than an authorisation error —
   that difference tells you which model is in play.
3. **Enumerate metadata first.** Listing databases and collections is a separate permission from reading
   documents; a successful metadata listing maps the space even when document reads are refused.
4. **Read by identifier when listing is refused.** Use the identifiers the narrative supplies and the
   conventions a store's own tooling would produce (partition keys, container names, well-known record
   identifiers) instead of blind brute force.
5. **Query when the surface is a query language.** A portal or proxy that exposes queries wants a query,
   not a path: learn the shape from one benign response, then constrain the next request.
6. **Follow the data out of the store.** A snapshot, export or change feed in a second service may retain
   records the live store has purged — check the artefact trail before concluding the store is decoy.

Signatures to expect: metadata success with document reads refused; a signature-mismatch error naming the
canonical pieces the service expects; a document read succeeding on a guessed identifier; a partition
key error that reveals the schema; a version header echoed back with the accepted value.

## Forensic / Blue-Team Perspective (DFIR analyst)

These stores expose their own data-plane diagnostic stream (a request log with the caller's identity or
key identifier) separately from the provider's control-plane audit log, and the two must be read
together: the control plane shows how the credential or grant appeared, the data plane shows what was
read. Key-based callers appear without a user identity, so attribution runs through the key identifier
and its rotation history. A burst of metadata listings followed by targeted document reads is the
enumeration signature. Remediation is key rotation plus disabling local/key authentication where the
platform allows it, and removing public network access from the store.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Metadata listing and document reads are the recovery actions. |
| T1078.004 | Valid Accounts: Cloud Accounts | A store key or a workload identity is the caller. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — store discovery plus `az rest` for data-plane calls
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline extraction of store endpoints, keys and connection strings
- a raw HTTP client, for hand-signed requests and verbatim error bodies
- provider SDKs and Mongo-compatible clients, when the compatibility layer is the target

## References

- <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
- <https://learn.microsoft.com/en-us/rest/api/cosmos-db/>
- <https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/security-how-to-connect>
