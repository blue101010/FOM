# CTFTTE-CLD-007 — Cloud NoSQL-store misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-007`](../countertechniques/CTFTCTE-CLD-007.md) — Enumerate and query exposed cloud databases

---

## How the challenge author hides

A document or key-value store holds the flag and the misconfiguration is in the **data plane**, not in
an object bucket: an endpoint that answers without authentication, a key that acts as the store's
administrative principal, or a grant broad enough that enumerating databases and collections is itself
the solve. Nothing resembles an injection — the store simply answers a request it should have refused.

Design variants, in increasing subtlety:

- **Open endpoint.** The data-plane endpoint accepts unauthenticated reads — sometimes only for metadata
  (database and collection names) and not for the documents themselves.
- **Administrative key in an artefact.** A connection string or account key in a configuration, a bundle
  or a log grants the store's primary principal; the request must then be **signed** with that key rather
  than sent as a bearer token, and the signature recipe is the whole obstacle.
- **Narrow but sufficient grant.** The identity may read one container only, so listing fails while a
  guessed document identifier succeeds.
- **Query surface over a plain read.** The store's query language is reachable through a portal or a
  proxy, so the answer requires building the right query instead of reading a known identifier.
- **Compatibility layer.** The store is reachable through a protocol emulation (a document API, a
  Mongo-compatible endpoint), and the flag is found with a client for that protocol rather than the
  provider's own.
- **Snapshot or change feed.** An export, backup or change feed in a second service retains records the
  live store has already purged.

Boundary: object storage rather than a database API belongs to the object-storage pair; a store reached
with a leaked session token rather than a store credential belongs to the session-material pair.

## Indicators

- a data-plane hostname for a document or key-value service in the prompt, a configuration or a bundle
- a connection string carrying a primary-key field, or an administrative key named as such
- an endpoint answering a metadata request with database and collection names
- identifiers shaped like partitions, collections or containers rather than filenames
- a story about "the database is public" or "the reporting service has no auth"
- a second service holding snapshots, exports or a change feed of the same data

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Cloud data-store enumeration and query is the recovery path. |
| T1552.001 | Unsecured Credentials: Credentials In Files | The primary key usually arrives through a configuration or a bundle. |

## Tools

- [Azure CLI](../tools/CTFTTOU-427.md) ([CTFTTOU-427](../tools/CTFTTOU-427.md)) — control-plane listing of the store and `az rest` for its data-plane API
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline sweep for store endpoints and keys
- a raw HTTP client, when the request must be signed by hand
- provider data-plane CLIs and SDKs (document store, key-value store, Mongo-compatible clients)
- a generic NoSQL request tool, when the query language itself is the obstacle

## References

- <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
- <https://learn.microsoft.com/en-us/rest/api/cosmos-db/>
- <https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/security-how-to-connect>
- <https://learn.microsoft.com/en-us/azure/cosmos-db/emulator>
