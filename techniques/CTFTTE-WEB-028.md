# CTFTTE-WEB-028 — Function-level authorization gap on a privileged endpoint

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-028`](../countertechniques/CTFTCTE-WEB-028.md) — Sweep privileged endpoints across session tokens

---

## How the challenge author hides

The privileged **function** exists, works, and is not gated for the identity the
player holds. What is gated is its **discovery**: the privileged screen is
withheld from the interface, so the player sees a reduced application and
concludes the function is unavailable, while the route behind it answers anyone
who asks.

Authorization is enforced per object (that is the IDOR pair) but not per function:
the endpoint never compares the caller's role with the operation's requirement,
and often the only difference between the permitted and the forbidden path is
which HTML page links to it.

Design variants, in increasing subtlety:

- **Unlinked route.** `/admin`, `/internal`, an operations console or a debug menu
  answers a low-privilege session; only the navigation link is missing.
- **Verb equivalence.** The guarded verb is checked and a sibling is not —
  `POST` refused, `PUT`/`PATCH`/`DELETE` accepted.
- **Path-shape equivalence.** A canonical path is guarded and an equivalent one
  is not: trailing slash, case, encoded segment, path-parameter suffix, or an
  older API prefix that still routes.
- **Namespace sibling.** The desktop API is guarded and the mobile or partner
  namespace, or a parallel query on the same GraphQL endpoint, is not.
- **Anonymous path.** The reduced interface invites re-login, but the action also
  succeeds with the session removed — the server treats the request as
  authenticated by construction.
- **UI-only role.** The interface hides controls above the caller's role, and the
  corresponding calls are the only place the role would have been checked.

Boundary: when the caller asserts the role or the flag itself, the pair is the
server-trusts-client-state one; when the function is legitimately available and
the object is another subject's, the pair is the IDOR one; when the route is
merely unknown and the response is uniform, the pair is the obscured-endpoint or
soft-404 one. Here the function is above the caller's privilege and nothing but
the interface noticed.

## Indicators

- a role, tenant or plan concept in the interface with fewer visible controls
  than the application obviously contains
- HTML routes answering `403` while a JSON sibling answers `200` for the same
  identity
- a sitemap, route manifest, JavaScript bundle, OpenAPI document or changelog
  listing operations the interface never links
- an administrative vocabulary in responses: audit rows, user listings, feature
  switches, impersonation
- two identities (or one identity and none) producing different lengths rather
  than different statuses for the same request
- an error message that names the calling role as a decision input

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | An ordinary, legitimately obtained session reaches a function above its role. |
| T1190 | Exploit Public-Facing Application | The gap is exercised through an ordinary route. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — one request definition swept across several session token jars, anonymous included, with status and length per variant
- an authorization-bypass harness (Autorize-style) driven from the same captured traffic
- the sitemap of the instrument, as the route inventory the UI withheld

## References

- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema>
- <https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/>
- <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
