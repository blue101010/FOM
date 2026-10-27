# CTFTTE-CLD-011 — Bearer credential embedded in a storage URL

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-011`](../countertechniques/CTFTCTE-CLD-011.md) — Validate and reuse the signed storage grant

---

## How the challenge author hides

The store itself is private, so the anonymous-exposure pair does not apply. Instead the grant travels
**inside a URL or an artefact as a bearer credential** — a signed query string, an account key in a
connection string, a delegation key. Whoever holds the string is the principal; no account, no login
and no policy edit is required. The author counts on the player discarding the credential as
"just a link" or assuming an expired signature means a dead end.

Design variants, in increasing subtlety:

- **Single-object signature.** The signature is scoped to one object and no container listing, so the
  object name has to come from the narrative rather than from enumeration.
- **Over-broad scope.** The signature covers container or account level and several operations,
  including write or delete, so the exposure exceeds what the story implies.
- **Expired signature with a live key.** The query string is stale, but the account key that produced
  it is also present in the artefact, and a fresh signature can be computed locally.
- **Delegation signature.** The signature was minted from an identity rather than a key, so
  re-signing requires a token for that identity — a chain into the session-material pair.
- **Connection string.** The key arrives as a configuration value with a service endpoint, so the
  player must recognise the format and pick the right client.
- **Signature in a carrier artefact.** The link sits in served HTML, a comment, a mobile bundle or a
  log line, and only source review surfaces it.

Boundary: when the request needs no credential at all the pair is anonymous object-storage exposure;
when the artefact is a full account identity with broader administrative reach, the pair is the
over-permissive-access one. Here the credential is narrow in reach but bearer in nature.

## Indicators

- a URL carrying signature and validity parameters (`sig=`, `se=`, `sp=`, `sv=`, `sr=`, delegation
  key identifiers) in the prompt, served markup, a bundle or a log excerpt
- a connection-string style value naming a storage endpoint together with a key field
- a link whose query string is far longer than the path, or that the story calls "a temporary link"
- an expiry parameter in the past next to a key or a token for the same account
- an object URL whose container is demonstrably private when requested without the query string

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Unsecured Credentials: Credentials In Files | The bearer credential leaks through a URL, a configuration or a bundle. |
| T1530 | Data from Cloud Storage Object | Recovery reads the object the signature authorises. |

## Tools

- [AzCopy and az storage](../tools/CTFTTOU-432.md) ([CTFTTOU-432](../tools/CTFTTOU-432.md)) — signed-URL data-plane operations, listing, transfer
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline parsing of signature parameters, permissions and expiry
- a raw HTTP client, to compare signed and unsigned responses against the same object
- an identity token helper, when the signature is a delegation signature and must be re-minted

## References

- <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>
- <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>
- <https://learn.microsoft.com/en-us/rest/api/storageservices/create-user-delegation-sas>
- <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string>
