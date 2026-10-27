# CTFTCTE-CLD-001 — Enumerate and list public buckets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-001`](../techniques/CTFTTE-CLD-001.md) — Misconfigured object-storage exposure

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate bucket names and list/download objects anonymously.

1. **Normalise the identity.** Object-store name alone, DNS name, or the bucket segment inside a URL
   path — drop the scheme, the storage URI prefix and any region suffix. When only a keyword is
   given, expand it with the qualifiers authors actually use (visibility, environment, role, year)
   before reaching for a dictionary.
2. **Resolve region and endpoint before judging permissions.** An unsigned HEAD on the bucket root
   usually advertises the region in a response header even when the body is refused, and a redirect
   is a wrong-region answer rather than a denial. Retrying against the regional endpoint is the most
   commonly wasted hour in this technique.
3. **List anonymously.** Issue the list-objects call unsigned, with pagination, and no request
   signing of any kind.
4. **When the listing is refused, change the endpoint, not the target.** Two fallbacks carry most of
   the weight: the versioned listing (it also names deleted objects and their version identifiers)
   and a direct object read on guessed keys, since a read-only grant often coexists with a denied
   list.
5. **Treat every object as an artefact.** Download the set, match the expected answer format, then
   follow what each object *is*: an archive, a source tree or a repository can hold credentials in
   its history or companion files, which pivots the challenge to the over-permissive-access pair —
   only with explicit authorization.

Signatures to expect: success on the listing; a refused listing with object bodies still served; a
redirect that encodes a region mismatch; a provider error code for a missing bucket; a disabled or
suspended storage account; a blanket refusal (private, or a grant scoped to authenticated callers).

## Forensic / Blue-Team Perspective (DFIR analyst)

Storage access logs document anonymous reads of the exposed objects. In provider access logs the
requester field records the absence of an authenticated identity for an unauthenticated object or
listing request that nevertheless returns success — that combination is the exposure signature,
whereas the same request from an authenticated principal carries a credential-derived requester.
Provider audit trails (data events for object reads and listings) and CDN logs cover the layers the
access log does not. Remediation is a policy fix, not a credential rotation: remove the public grant
from the bucket policy and from the object ACLs, enable the provider's public-access block, and audit
versions and replicas for as long as the object was public.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1530 | Data from Cloud Storage Object | Recovery reads the exposed object anonymously; the anonymous requester is the DFIR marker. |
| T1619 | Cloud Storage Object Discovery | Bucket-name enumeration and listing precede the read. |

## Tools

- [s3_public_probe.py](../tools/CTFTTOU-415.md) ([CTFTTOU-415](../tools/CTFTTOU-415.md)) — region discovery, anonymous listing, versioned listing, name permutations, download and pattern match
- provider CLI in anonymous / unsigned mode
- multi-cloud bucket-name enumerators
- a version-control client, for repository artefacts recovered from the exposed objects

## References

- <https://github.com/mzet-/ctf-writeups/blob/master/flaws.cloud/flaws.cloud.md>
- <https://blog.welcomethrill.house/2020/11/2020-hth-ctf-cloud-challenges.html>