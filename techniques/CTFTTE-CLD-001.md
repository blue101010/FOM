# CTFTTE-CLD-001 — Misconfigured object-storage exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-001`](../countertechniques/CTFTCTE-CLD-001.md) — Enumerate and list public buckets

---

## How the challenge author hides

The flag object sits in a world-readable or weakly-named bucket the author assumes is private.
The weakness is in the access policy, not in the data: an ACL or bucket policy grants read to a
principal set that includes anonymous callers, or the object itself is public while the bucket is
not. Nothing in the traffic resembles an attack — an unauthenticated request returns the flag.

Design variants, in increasing subtlety:

- **Listable bucket.** Anonymous callers may list the bucket, so object names are handed over and
  the flag object downloads directly.
- **Readable objects, denied listing.** The list operation is refused while individual objects are
  served: the exposure is complete, only the index is missing.
- **Guessable name.** The prompt or a leaked artefact supplies a keyword instead of a name, and the
  bucket name is that keyword plus a short, predictable qualifier.
- **Versioned storage.** A deleted object survives as a non-current version that stays readable.
- **Storage as a carrier.** The exposed objects hold a further artefact (source tree, repository,
  configuration) whose history or companion files contain credentials, so the bucket is the entry
  point to a second weakness rather than the flag itself.

Boundary: when the grant is scoped to *any authenticated principal of the provider*, the exposure is
credential-gated and no longer anonymous — that belongs to the over-permissive-access pairs.

## Indicators

- the narrative asserts privacy or asks to verify permissions ("I think it is private", "check the
  access rights")
- a storage endpoint appears literally: provider hostname in the prompt, a leaked script, a
  commented-out URL in served HTML or JS, or an object-storage URI scheme
- object names follow conventions worth trying: flag-like files, archives, dotfiles, source trees
- response signatures: a listing document returned with success; a refused listing that still serves
  object bodies; a redirect that encodes a region mismatch; a provider error code for a missing bucket

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1530 | Data from Cloud Storage Object | Access to an object in misconfigured storage; ATT&CK models the access, not the anonymous-enumeration craft. |
| T1619 | Cloud Storage Object Discovery | The solve is discovery first: name enumeration, then listing. |

## Tools

- [s3_public_probe.py](../tools/CTFTTOU-415.md) ([CTFTTOU-415](../tools/CTFTTOU-415.md)) — anonymous probe: region discovery, listing, versioned listing, name permutations
- provider CLI in anonymous / unsigned mode
- multi-cloud bucket-name enumerators
- a generic HTTP client, when raw provider responses are clearer than a wrapper

## References

- <https://github.com/mzet-/ctf-writeups/blob/master/flaws.cloud/flaws.cloud.md>
- <https://blog.welcomethrill.house/2020/11/2020-hth-ctf-cloud-challenges.html>