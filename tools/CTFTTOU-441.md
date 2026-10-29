# CTFTTOU-441 — Caido (caido-cli and caido-mcp-server)

> **Tool ID:** `CTFTTOU-441`  
> **Related techniques/counters:** CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003, CTFTTE-WEB-004, CTFTCTE-WEB-004, CTFTTE-WEB-007, CTFTCTE-WEB-007, CTFTTE-WEB-009, CTFTCTE-WEB-009, CTFTTE-WEB-012, CTFTCTE-WEB-012, CTFTTE-WEB-014, CTFTCTE-WEB-014, CTFTTE-WEB-018, CTFTCTE-WEB-018, CTFTTE-WEB-020, CTFTCTE-WEB-020, CTFTTE-WEB-022, CTFTCTE-WEB-022, CTFTTE-WEB-024, CTFTCTE-WEB-024, CTFTTE-WEB-025, CTFTCTE-WEB-025, CTFTTE-WEB-026, CTFTCTE-WEB-026, CTFTTE-WEB-027, CTFTCTE-WEB-027, CTFTTE-WEB-028, CTFTCTE-WEB-028, CTFTTE-WEB-029, CTFTCTE-WEB-029

## Description

A web proxy with two programmable surfaces over one local instance, which is exactly what a CTF needs:
the traffic is captured once and stays addressable, instead of living in a shell history.

- **`caido-cli`** — a terminal client: HTTPQL history queries, full request/response by id, structured and
  raw replay, parallel batches (token sweeps, parameter fuzzing, endpoint sweeps), encode/decode.
- **`caido-mcp-server`** — the same instance exposed as MCP (66 tools, 6 read-only resources) so an agent
  can list/search requests, replay with a persistent per-session cookie jar, diff two responses, drive an
  intercept queue, manage scopes/projects/findings/tamper rules, and export a curl PoC. Sensitive headers
  (`Authorization`, `Cookie`, `X-Api-Key`…) are redacted in tool output unless explicitly opted out.

The MCP half carries the capabilities a plain traffic client does not have, and each one is a distinct
test technique rather than a convenience:

| Surface | What it makes possible |
| --- | --- |
| `race_window_send` | requests released together on one connection (raw last-byte synchronisation, proxy bypassed) for state-change races |
| `batch_send`, with `sessionId` per request | token and endpoint sweeps where each identity has its own cookie jar, anonymous included |
| `convert_body` | one payload re-rendered as JSON, form, XML or multipart, with the matching content type |
| `send_request` / `raw`, no normalisation | framing kept byte-exact, for length-versus-chunked desynchronisation tests |
| intercept control, tamper rules | hold the queue instead of replaying, and rewrite a field by rule instead of by request |
| `run_workflow`, `toggle_workflow`, `list_plugins` | passive rules on every proxied response, active checks fired per endpoint |
| `list_findings`, `create_finding`, `delete_findings`, `export_findings` | findings as records tied to a request id, exported with the raw request embedded |
| `get_sitemap` | the routed-resource inventory an interface never links |
| `list_ws_streams`, `list_ws_messages` | frame-level listing for channels whose HTTP history shows only an upgrade |
| replay collections and sessions, `get_session_cookies` / `clear_session_cookies` | per-identity state that survives between attempts, plus an explicit anonymous row |
| `list_hosted_files` | a payload served from the instrument's own origin, inside the same recorded history |
| environments | variable substitution across hosts, so one request definition follows a chain |

Both read the **local instance token**, not a Cloud PAT: `caido-mcp-server login` stores it (0600,
~7 days, refreshable). The CLI consumes the stored login; the MCP server also accepts
`CAIDO_ACCESS_TOKEN`.

## URL

- <https://caido.io/>
- <https://github.com/c0tton-fluff/caido-mcp-server>

## Installation

Go 1.25+ — two binaries into `$(go env GOPATH)/bin`:

```bash
go install github.com/c0tton-fluff/caido-mcp-server/v4/cmd/caido-mcp-server@latest
go install github.com/c0tton-fluff/caido-mcp-server/v4/cmd/caido-cli@latest
caido-mcp-server --version && caido-cli --help

# authentication (device flow, stores ~/.caido-mcp/token.json)
export CAIDO_URL="http://127.0.0.1:8080"
caido-mcp-server login
```

Pre-built binaries and a one-liner installer exist upstream (`install.sh`, GitHub Releases) when no Go
toolchain is available.

## Usage

```bash
caido-cli status                                  # auth + instance version
caido-cli history -n 100
caido-cli history -f 'req.host.eq:"target"' -n 50
caido-cli request 42 -b 50000                     # full exchange; bodies cap at 2000 B by default
caido-cli send GET https://target/api/users/1
caido-cli raw 'GET / HTTP/1.1\r\nHost: target\r\n\r\n'
caido-cli batch sweep https://target/api/profile -t "owner=<tokA>,other=<tokB>,none="
caido-cli batch fuzz "https://target/api/search?q=t" -p q -v "t,1' OR 1=1--"
caido-cli encode base64 "hello" && caido-cli decode url "%3Cscript%3E"
```

The capabilities with no CLI equivalent, as MCP call shapes:

```jsonc
// race: several requests released together, one connection
{"method": "POST", "url": "https://target/api/redeem", "body": "code=X", "count": 20,
 "windowMs": 30}

// representation differential: convert then replay
{"body": "{\"role\":\"user\"}", "from": "json", "to": "form"}

// passive/active rule execution, and on-demand scanning
{"id": "<workflow-id>", "type": "active", "request_id": "204"}

// findings: create against a request, then export the set
{"requestId": "204", "title": "...", "reporter": "agent"}
{"reporter": "agent"}   // export filter → export{id downloadUri}
```

MCP registration (stdio):

```json
{"mcpServers": {"caido": {"command": "caido-mcp-server", "args": ["serve"],
  "env": {"CAIDO_URL": "http://127.0.0.1:8080"}}}}
```

Pitfalls: `caido URL required` means `CAIDO_URL` is unset **in that shell**; `Instance: FAIL` while
`Auth: OK` means the app is running but its instance is stopped; a `caido_…` Cloud PAT will never
authenticate against the local instance; a paused intercept makes the browser look broken; batches cap
at 50 requests and history listings at 100 per page. A body cut by `bodyLimit` is reported as
`truncated: true` (read that flag, not only `bodySize`), and a `-` status row in `caido-cli history` is
an entry with no response attached. An MCP tool answering `disabled by the user` is present in the
session but not approved in the client's tool picker — fall back to the CLI for that call rather than
retrying, and note the parameter names are not shared (`is_in_scope` takes `target`; `list_requests`
rejects `filter`/`limit`).

## Related Techniques

CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003,
CTFTTE-WEB-004, CTFTCTE-WEB-004, CTFTTE-WEB-007, CTFTCTE-WEB-007, CTFTTE-WEB-009, CTFTCTE-WEB-009,
CTFTTE-WEB-012, CTFTCTE-WEB-012, CTFTTE-WEB-014, CTFTCTE-WEB-014, CTFTTE-WEB-018, CTFTCTE-WEB-018,
CTFTTE-WEB-020, CTFTCTE-WEB-020, CTFTTE-WEB-022, CTFTCTE-WEB-022, CTFTTE-WEB-024, CTFTCTE-WEB-024,
CTFTTE-WEB-025, CTFTCTE-WEB-025, CTFTTE-WEB-026, CTFTCTE-WEB-026, CTFTTE-WEB-027, CTFTCTE-WEB-027,
CTFTTE-WEB-028, CTFTCTE-WEB-028, CTFTTE-WEB-029, CTFTCTE-WEB-029

## References

- [Caido documentation](https://docs.caido.io/)
- [Caido GraphQL API](https://docs.caido.io/app/concepts/graphql)
- [caido-mcp-server repository](https://github.com/c0tton-fluff/caido-mcp-server)
