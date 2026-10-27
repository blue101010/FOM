# CTFTTE-CLD-009 — Delegated sign-in session material exposed

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-009`](../countertechniques/CTFTCTE-CLD-009.md) — Redeem and replay delegated cloud tokens

---

## How the challenge author hides

What the challenge hands over is not a password but *session material*: a refresh token, a
device-code grant, a primary refresh token, a cached token file, a client secret, or an external
assertion. The article the player holds is opaque, often expired, and its **audience** — not the
login — decides which plane it opens. The author counts on the player either refusing to look inside
the artefact or treating "the token has expired" as the end of the path.

Design variants, in increasing subtlety:

- **Cached token store.** A profile directory, an SDK cache or a CI secret holds an access token whose
  audience names a management plane the narrative never mentions.
- **Renewal credential only.** Just the refresh token is supplied; one token request mints an access
  token for a resource of the solver's choosing, so the apparent absence of a usable token is the trick.
- **Device-code grant.** The prompt supplies a code to redeem, or a retrieval endpoint is reachable;
  completing the flow yields a delegated identity whose scopes exceed the story.
- **Client family crossing audiences.** The same refresh token reaches several first-party resources
  because the requesting client belongs to a family allowed to do so — the scope string, not the user,
  is the lever.
- **Session material needing import.** Cookie or primary-refresh-token material must be placed in a
  client's expected form before the token endpoint accepts it.
- **Federated assertion.** An external OIDC token is trusted by a workload identity federation object;
  only the exchange step separates the player from a cloud token.

Boundary: a user password belongs to the credential-access pairs; a correctly scoped token that merely
needs replaying against one API is an authentication challenge. The distinguishing feature here is that
the material must be **transformed** — renewed, re-audienced, imported or exchanged — before it opens
the target.

## Indicators

- the prompt states it delivers "a token", "a session", "a refresh token", a cache file or a base64url
  blob with two dots
- the delivered token's audience names a service unrelated to the story's resource
- an endpoint list pairs an identity provider with a resource host
- an expiry in the past sitting next to a renewal credential
- a client/application identifier in the prompt, the artefact or a leaked configuration
- scope strings (`offline_access`, `*.default`, `user_impersonation`) — read the scope before the user
- a sign-in log or a browser profile offered as an artefact

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1528 | Steal Application Access Token | The exposure is token material rather than a password; ATT&CK models the theft, not the audience pivot. |
| T1550.001 | Use Alternate Authentication Material: Application Access Token | Recovery replays a token that was minted for a different client or resource. |
| T1539 | Steal Web Session Cookie | Browser-session and primary-refresh-token variants sit in the same class. |

## Tools

- [ROADtools](../tools/CTFTTOU-429.md) ([CTFTTOU-429](../tools/CTFTTOU-429.md)) — token reuse, re-audiencing, device-code and primary-refresh-token handling
- [TokenTacticsV2](../tools/CTFTTOU-438.md) ([CTFTTOU-438](../tools/CTFTTOU-438.md)) — token request and replay helpers for the Microsoft identity platform
- [AADInternals](../tools/CTFTTOU-430.md) ([CTFTTOU-430](../tools/CTFTTOU-430.md)) — token, tenant and user-object queries around the same tenant
- [azure_ctf_inventory.py](../tools/CTFTTOU-439.md) ([CTFTTOU-439](../tools/CTFTTOU-439.md)) — offline decode of token files and artefact sweeps
- a JWT inspection utility, for structure and claim reading before any request
- a raw HTTP client, when the token endpoint response must be seen verbatim

## References

- <https://github.com/dirkjanm/ROADtools>
- <https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow>
- <https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code>
- <https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens>
- <https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token/>
