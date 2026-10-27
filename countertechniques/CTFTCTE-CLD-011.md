# CTFTCTE-CLD-011 — Validate and reuse the signed storage grant

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-011`](../techniques/CTFTTE-CLD-011.md) — Bearer credential embedded in a storage URL

---

## Offensive Recovery (CTF practitioner / solver)

The credential is in the string. Parse what it authorises before issuing any request, then issue the
narrowest request that proves it.

1. **Separate the artefact from the credential.** Normalise the URL: the scheme, the host and the
   resource path identify the account, the service and the object; everything in the query string is
   the credential, and it is as sensitive as a password.
2. **Read the grant before using it.** Decode the signature's parameters: which service and resource
   type it covers, which operations it permits, its validity window, and whether it was minted from a
   key or from a delegated identity. The permitted operations decide the plan — a read-only signature
   that allows listing is a different challenge from a single-object read.
3. **Compare against an unsigned request.** Fetch the object without the query string. If it also
   succeeds, the pair is anonymous exposure, not this one; if it fails, the signature is doing the work
   and the two responses are your evidence.
4. **When the signature is expired, look for the key.** A connection string or a key field in the same
   artefact lets you compute a new signature locally; a delegated signature instead needs a token for
   the identity that minted it, which chains into the session-material pair.
5. **Reach upward only as far as the grant allows.** Signature scope — object, container, account —
   bounds enumeration. Do not assume container listing exists because the object read works.
6. **Capture the response headers as evidence.** The service's API version, request identifier and
   signature-scope echo are what prove which credential was used.

Signatures to expect: success with the query string and refusal without it; a refusal naming the
operation the signature omits; an expiry error alongside a still-valid key in the artefact; a
permission error that changes when the scope in the URL is widened rather than when the identity
changes.

## Forensic / Blue-Team Perspective (DFIR analyst)

Signed-URL access appears in storage logs as an authenticated request whose identity fields name the
key or delegation rather than a user — the requester is the signature, so attribution depends on the
key identifier and the delegation object. The distribution of operations is the signal: a signature
created for one object but used for listing, or a burst of reads from an address unrelated to the
signature's issuance context. Control-plane logs record key regeneration and delegation-key issuance,
which is where the credential was born. Remediation is rotation of the key or revocation of the
delegation key, plus a stored-access-policy review — the leaked URL alone cannot be recalled, so only
key rotation invalidates it.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Unsecured Credentials: Credentials In Files | The credential is discovered in a URL or a configuration artefact. |
| T1530 | Data from Cloud Storage Object | The signed grant is exercised against the object. |

## Tools

- [AzCopy and az storage](../tools/CTFTTOU-432.md) ([CTFTTOU-432](../tools/CTFTTOU-432.md)) — signed-URL listing and transfer, both service and delegation signatures
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline decode of signature scope, operations and validity
- a raw HTTP client, for the unsigned-versus-signed comparison and verbatim headers

## References

- <https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview>
- <https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas>
- <https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string>
- <https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-stored-access-policy>
