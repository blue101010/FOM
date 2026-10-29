# CTFTTE-WEB-029 — Desynchronized request framing between edge and origin

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-029`](../countertechniques/CTFTCTE-WEB-029.md) — Craft unnormalized raw request pairs and read the desync

---

## How the challenge author hides

Two HTTP implementations sit in the path — a front end that decides what to
inspect or route, and an origin that decides what to execute — and they disagree
about **where a request ends**. The edge reads a `Content-Length`, the origin
prefers a `Transfer-Encoding`, or both accept a chunked framing they parse
differently. The bytes at the end of one request are therefore read as the
beginning of the next, and the smuggled prefix is the player's request.

The hiding is in the plumbing, not the application: every request the player
sends through a normalising client is well-formed and inspected, the application
behaves as documented, and the flaw only appears when framing is left exactly as
crafted. The challenge presents an ordinary app and expects the player to notice
that a reverse proxy exists at all.

Design variants, in increasing subtlety:

- **Length versus chunked.** One side honours `Content-Length`, the other
  `Transfer-Encoding: chunked`.
- **Chunked versus chunked.** Both honour the header but parse chunk extensions,
  a leading zero in the size, or a trailer differently.
- **Duplicate length.** Two `Content-Length` values, or differing whitespace
  around the colon, resolved inconsistently.
- **Obs-fold and line termination.** A header continuation line, a bare LF, or a
  space before the colon that one parser normalises and the other rejects late.
- **Prefix injection through a value.** CRLF reached through a header or a
  parameter, so the "smuggled" request is the tail of a legitimate one.
- **Protocol downgrade.** An HTTP/2 edge that reassembles downgraded HTTP/1.1
  requests, where the framing the client sent no longer describes the bytes the
  origin parses.

Boundary: when two parsers disagree about the **content** of one request, the
pair is the representation-differential one; when a single request is misrouted
because its `Host` names another site, the pair is the host-header one. Here the
disagreement is about the boundary between requests, and one request produces two.

## Indicators

- a challenge narrative, a header, or a version banner placing a reverse proxy,
  load balancer, CDN or gateway in front of the origin
- front-end and origin technologies whose framing implementations differ, stated
  in headers or error pages
- an application that answers twice, or answers a request nobody sent
- a `400` immediately followed by a valid response on the same connection
- a debug or health route revealing the origin directly, which makes the
  comparison between "through the edge" and "straight to the origin" possible
- the target described as internal, administrative or off-limits, reachable only
  from the origin's own trust boundary

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | The desync is exercised against the public edge and lands on an ordinary origin route. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — sends raw bytes verbatim, so normalisation does not destroy the framing under test
- an interactive TCP client, for the timing and connection-reuse behaviour a proxy layer would smooth over
- a desync test harness that automates the length/chunked variant matrix

## References

- <https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn>
- <https://www.rfc-editor.org/rfc/rfc9112#section-6.3>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/15-Testing_for_HTTP_Request_Smuggling>
