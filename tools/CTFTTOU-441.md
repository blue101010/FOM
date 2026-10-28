# CTFTTOU-441 — Caido (caido-cli and caido-mcp-server)

> **Tool ID:** `CTFTTOU-441`  
> **Related techniques/counters:** CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003, CTFTTE-WEB-009, CTFTCTE-WEB-009

## Description

A web proxy with two programmable surfaces over one local instance, which is exactly what a CTF needs:
the traffic is captured once and stays addressable, instead of living in a shell history.

- **`caido-cli`** — a terminal client: HTTPQL history queries, full request/response by id, structured and
  raw replay, parallel batches (token sweeps, parameter fuzzing, endpoint sweeps), encode/decode.
- **`caido-mcp-server`** — the same instance exposed as MCP (67 tools, 6 read-only resources) so an agent
  can list/search requests, replay with a persistent per-session cookie jar, diff two responses, drive an
  intercept queue, manage scopes/projects/findings/tamper rules, and export a curl PoC. Sensitive headers
  (`Authorization`, `Cookie`, `X-Api-Key`…) are redacted in tool output unless explicitly opted out.

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
CTFTTE-WEB-009, CTFTCTE-WEB-009

## References

- [Caido documentation](https://docs.caido.io/)
- [Caido GraphQL API](https://docs.caido.io/app/concepts/graphql)
- [caido-mcp-server repository](https://github.com/c0tton-fluff/caido-mcp-server)
