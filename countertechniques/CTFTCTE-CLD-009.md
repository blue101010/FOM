# CTFTCTE-CLD-009 — Redeem and replay delegated cloud tokens

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-009`](../techniques/CTFTTE-CLD-009.md) — Delegated sign-in session material exposed

---

## Offensive Recovery (CTF practitioner / solver)

The artefact must be transformed before it opens anything. Read it, renew it, re-audience it, then
prove access with the least-privileged read that still demonstrates the claim.

1. **Decode before trusting.** Split the material: a three-part base64url blob is a token (read the
   algorithm, key identifier, then the claims); a JSON document is a cache or a credential file; a
   bare opaque string is a renewal credential. Record tenant, client, object, user and **audience** —
   the audience is the whole puzzle.
2. **Fix the tenant and the client.** Both appear in the claims; a tenant identifier in the prompt may
   be a domain rather than a GUID, so resolve it through the identity provider's metadata document
   before any request.
3. **Renew.** Exchange a refresh token at the token endpoint for the resource you actually need,
   asking for the resource's default scope. An expired access token is not a dead credential when a
   renewal credential accompanies it.
4. **Re-audience.** One session can usually mint tokens for several first-party resources. Walk the
   candidate resources from the story (management plane, graph directory, storage data plane, vault
   data plane, the challenge's own service) rather than guessing scopes blindly.
5. **Complete the flow when a code is supplied.** Redeem the code exactly as delivered — the code is
   single-use and short-lived, so capture the response verbatim, including the renewal credential.
6. **Import session material when that is the form given.** Cookie or primary-refresh-token material
   has to be placed where a client expects it before the endpoint accepts it; do the import in a
   throwaway profile and keep the artefact untouched.
7. **Prove the claim narrowly.** One read that only the target identity can perform — the directory
   object of the signed-in principal, the subscription list, the object named in the story — is
   evidence; a full dump is not.

Signatures to expect: a token response with a renewal credential despite no password; a claim set
whose audience names the plane the story implied; a refusal that changes with the audience rather than
with the identity; a code redemption that reports the grant type the client is allowed; an assertion
exchange that fails only because the federation subject does not match.

## Forensic / Blue-Team Perspective (DFIR analyst)

Identity-provider sign-in logs separate the interactive sign-in from the token issuance that followed
it: a suspicious pattern is a non-interactive grant (refresh, device code, assertion exchange) with no
matching interactive sign-in from the same device, or an interactive sign-in from an address that never
appears again while the renewal continues. Correlate token issuance with the resource's data-plane
access logs — the token is the join key. Device-code grants show as an authentication whose initiator
is not the user's own client. Remediation: revoke the renewal credentials, not just the access token;
invalidate sessions, review federation objects, and check for re-issued tokens after the revocation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1528 | Steal Application Access Token | Recovery starts by reading material that was never meant to be a credential. |
| T1550.001 | Use Alternate Authentication Material: Application Access Token | The re-audienced token is replayed against a plane the original client never asked for. |
| T1539 | Steal Web Session Cookie | Imported session material is the same class of artefact. |

## Tools

- [ROADtools](../tools/CTFTTOU-429.md) ([CTFTTOU-429](../tools/CTFTTOU-429.md)) — token reuse, re-audiencing, device-code and primary-refresh-token workflows
- [TokenTacticsV2](../tools/CTFTTOU-438.md) ([CTFTTOU-438](../tools/CTFTTOU-438.md)) — request and replay helpers for the identity platform
- [AADInternals](../tools/CTFTTOU-430.md) ([CTFTTOU-430](../tools/CTFTTOU-430.md)) — directory queries once a delegated token works
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline token and artefact decoding before any request
- a JWT inspection utility, for reading claims without a client

## References

- <https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow>
- <https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code>
- <https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens>
- <https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins>
