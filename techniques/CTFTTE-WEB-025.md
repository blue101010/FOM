# CTFTTE-WEB-025 — Server-trusted client-computed state

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-025`](../countertechniques/CTFTCTE-WEB-025.md) — Rewrite or extend the trust-bearing client fields

---

## How the challenge author hides

A value that decides privilege, price or eligibility is computed in the browser
and then **persisted from the request verbatim**. The server validates shape,
format and sometimes range, but never recomputes the value or re-derives it from
the session, so the effective identity, price or status of a request is whatever
the client asserts.

The concealment is that the field is invisible rather than absent: the rendered
form shows a label, a disabled or hidden input, or nothing at all, while the
model behind it happily binds any property the request carries — including ones
the interface never sends.

Design variants, in increasing subtlety:

- **Hidden or disabled field.** Price, owner, role, quantity or discount travels
  as a hidden input or a read-only value the browser paints.
- **Over-posting.** The UI sends three properties; the object binds all of them,
  so adding a fourth (an administrative flag, a related object, a status) is
  accepted.
- **Type and structure reshaping.** The same field is sent as an array, a nested
  object or a second value, and the framework's coercion decides the outcome —
  a scalar comparison against a list, a last-value-wins duplicate, a `[]`
  suffix that reaches the model unchanged.
- **Client-computed aggregate.** A total, hash, checksum or eligibility flag is
  calculated in JavaScript and trusted, so recomputing it correctly for a
  different intent defeats the rule.
- **Status flag written directly.** `paid`, `verified`, `approved`, `unlocked`
  is a writable property rather than a consequence of an action.
- **Trusted routing header.** The origin honours a header that names the internal
  route or scheme, letting a request addressed at one function reach another
  (the boundary with host-header discovery is that no hidden vhost is involved
  here — the route is known and the claim is elevated).

Boundary: when the role value is genuine and only the endpoint fails to check
it, the pair is the function-level authorization one; when the object is another
user's but the field carries no privilege claim, the pair is the IDOR one. Here
the client asserts a state the server should own.

## Indicators

- any security-relevant value present in a request body but absent from the
  rendered form, or rendered `disabled` / `readonly` / `hidden`
- client-side script computing a total, price, discount, hash or eligibility
  decision immediately before submission
- a response object carrying more properties than the request sent, revealing
  writable fields the UI never exposes
- API documentation or a schema listing fields the interface omits
- a 403 on the HTML page beside a 200 on the JSON endpoint for the same action
- an "unexpected field" that changes a list, a badge or a redirect target

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1565.001 | Data Manipulation: Stored Data Manipulation | The rewritten field is persisted as if the server had derived it. |
| T1190 | Exploit Public-Facing Application | The accepted field is reached through an ordinary application endpoint. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — edit one recorded request, add a property, replay both variants and diff the outcomes
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — compare request and response object shapes to spot writable fields
- an authorization-bypass harness (Autorize-style, two sessions), when the rewritten field must be judged per role

## References

- <https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html>
- <https://owasp.org/API-Security/editions/2023/en/0xa6-broken-object-property-level-authorization/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/>
