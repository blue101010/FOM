# CTFTCTE-WEB-028 — Sweep privileged endpoints across session tokens

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-028`](../techniques/CTFTTE-WEB-028.md) — Function-level authorization gap on a privileged endpoint

---

## Offensive Recovery (CTF practitioner / solver)

The interface is the wrong evidence: it shows what *should* be reachable, not what
*is*. Turn every candidate route into one request definition and sweep it across
identity contexts.

1. **Build the route inventory from artefacts, not from the menu.** Take the
   sitemap of the recorded traffic, the routes in the JavaScript bundle, source
   maps, an OpenAPI or GraphQL document, `robots.txt`, well-known paths and error
   pages. Privileged function is usually named there and unlinked in the UI.
2. **Fix one request per function.** Same method, path, headers and body for
   every identity; the only variable is the credential. A sweep with two
   variables at once produces a result nobody can attribute.
3. **Define the identity set.** At minimum: the lowest privilege session you
   hold, the highest you hold, and **no session at all**. The anonymous row is not
   a formality — the UI's "please log in" prompt is exactly the message the
   server may not enforce.
4. **Sweep and classify by response shape.** Record status, length, content type
   and a normalized body hash per variant. Three outcomes matter: equal to the
   privileged identity (full gap), different from both (partial gap: a redacted
   but populated response), or uniformly refused (the function is actually
   gated).
5. **Vary the route shape before concluding a function is gated.** Verb siblings
   (`POST` guarded, `PUT`/`PATCH`/`DELETE` not), path aliases (trailing slash,
   case, encoded segment, version prefix), and namespace siblings (mobile or
   partner prefix, a parallel query) frequently route to the same handler.
6. **Widen one axis at a time.** When the response differs by length rather than
   status, decode both bodies and compare field by field: a field that appears
   only for the privileged identity is the gap.
7. **Record per function.** One finding per (function, identity) pair, with the
   request embedded, so the report shows the matrix and not a single lucky hit.
8. **Hand off when the mechanic changes.** If the escalation comes from a value
   *you* wrote, it is the client-state pair; if the same function is legitimately
   available and the object belongs to another subject, it is the IDOR pair.

Signatures to expect: `200` with a full body for the lesser identity; `403` on the
HTML path beside `200` on the JSON path; identical bodies for the privileged and
anonymous rows; a route that exists in the manifest and answers `401` on one verb
only.

## Forensic / Blue-Team Perspective (DFIR analyst)

Broken function-level authorization is invisible in payload inspection and
obvious in the authorization matrix, so the defensible control is a per-function
requirement declared with the route rather than checked in the handler. Logs
reveal it as an operation performed by an identity that never performed its
prerequisite — a user listing read by an account that never opened the console,
an administrative write from a session with no administrative predecessor. The
detection is therefore a join between the operation log and the identity's
historical capability surface, and the remediation is on the route table, not on
the request.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | A legitimately obtained lower-privilege session performs the operation. |
| T1190 | Exploit Public-Facing Application | The sweep targets ordinary routed functions. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — one request definition replayed across several session jars, anonymous included, with status, length and diff per variant
- an authorization-bypass harness (Autorize-style) driven from the same captured traffic
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — field-level comparison of the bodies returned per identity

## References

- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema>
- <https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/>
- <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
