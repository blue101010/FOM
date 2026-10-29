# CTFTTE-WEB-027 — Representation differential across body formats

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-027`](../countertechniques/CTFTCTE-WEB-027.md) — Re-encode the request body across representations and replay

---

## How the challenge author hides

The layer that **validates** and the layer that **binds** read the same request
differently. A filter inspects one representation — the JSON document, the
declared content type, the first occurrence of a parameter — while the
application resolves the value from another: the form encoding, the second
occurrence, the nested structure, the alternative parser selected by
`Content-Type`.

So one logical payload has two encodings, and only one of them is inspected. The
request looks refused in the shape a player naturally tries and succeeds in a
shape the interface never produces, which is why brute-forcing payload
vocabulary finds nothing.

Design variants, in increasing subtlety:

- **Content-type switch.** The same bytes are re-labelled (`application/json` →
  `application/x-www-form-urlencoded` → `multipart/form-data` → `text/xml`) and
  the framework instantiates a different binder than the one the filter guards.
- **Dual representation.** A JSON body travels next to query parameters or a
  second body; parser precedence, not the filter, decides which value wins.
- **Scalar-versus-structure.** The same field is sent as a scalar and as an
  array or nested object; coercion turns a rejected value into an accepted one.
- **Repeated parameter.** Duplicate occurrences resolve last-wins or first-wins,
  so a validated first value and a used second value coexist.
- **Value encoding.** Percent, double-percent, overlong or otherwise non-canonical
  encoding of the same character reaches the sink in a form the filter did not
  normalise.
- **Container smuggling.** Multipart boundary games, a filename in
  `Content-Disposition`, duplicate `Content-Type` headers.
- **Stored-then-reserved type.** A value stored through one representation is
  later served under another (JSON text rendered as HTML), so validation happened
  on a shape that no longer describes the output.

Boundary: when a single representation is merely obfuscated, the pair is the
WAF-evaded injection one; when the disagreement is about where the request **ends**
on the wire, the pair is the desync one. Here both parsers agree on the boundary
and disagree on the content.

## Indicators

- documentation or an OpenAPI fragment admitting several request content types
  for one operation
- a 4xx whose message names only one format ("invalid JSON"), while the same
  value in another format is not mentioned
- a framework known to bind form fields and JSON bodies through different paths
- duplicate parameters surviving to the application, or arrays where the UI sends
  a scalar
- a filter response that echoes or rejects the **serialised** form of the value
- a debug header or error page naming the parser that handled the request

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The payload exists in more than one representation; only one is inspected. |
| T1190 | Exploit Public-Facing Application | The differential is exercised against an ordinary endpoint. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — converts a captured body between JSON, form, XML and multipart, then replays it with the matching content type
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — rebuilds the payload in the alternative representation for a targeted replay
- a raw HTTP client, when the differential needs duplicate parameters or headers a convenience client would merge

## References

- <https://portswigger.net/web-security/logic-flaws>
- <https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html>
- <https://www.rfc-editor.org/rfc/rfc9110#section-8.3> (content negotiation and media type handling)
