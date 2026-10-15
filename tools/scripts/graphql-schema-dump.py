#!/usr/bin/env python3
"""Dump a GraphQL schema via introspection and highlight sensitive fields.

Companion tool for CTFTTE-WEB-023 / CTFTCTE-WEB-023 (GraphQL introspection
disclosure / field-level authorization gap). Standard library only - no pip
install, safe on Kali (PEP 668).

Usage:
  graphql-schema-dump.py --url http://target/api/graphql
  graphql-schema-dump.py --url http://target/api/graphql --json schema.json
  graphql-schema-dump.py --selftest        # local mock server, no network

What it does:
  1. POSTs the __schema introspection query to the endpoint.
  2. Prints every type with its fields, one type per block.
  3. Highlights fields whose name matches the sensitive-word list
     (password, secret, hidden, token, admin, flag, key, private).
  4. Detects a disabled-introspection response and suggests fallbacks.

Never contacts anything except --url.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request

INTROSPECTION_QUERY = """
query IntrospectionQuery {
  __schema {
    types {
      name
      kind
      fields {
        name
        type { name kind ofType { name } }
      }
    }
  }
}
"""

SENSITIVE_RE = re.compile(
    r"password|secret|hidden|token|admin|flag|key|private", re.I
)


def post_query(url: str, query: str, timeout: float = 15.0) -> dict:
    body = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8", errors="replace"))
    if "errors" in payload and not payload.get("data"):
        msgs = "; ".join(e.get("message", "")[:120] for e in payload["errors"])
        raise RuntimeError(f"GraphQL errors: {msgs}")
    return payload


def render(payload: dict) -> str:
    lines: list[str] = []
    types = payload["data"]["__schema"]["types"]
    interesting = 0
    for t in types:
        fields = t.get("fields") or []
        if not fields:
            continue
        lines.append(f"== {t['name']} ({t['kind']})")
        for f in fields:
            ftype = (f["type"] or {}).get("name") or (
                ((f["type"] or {}).get("ofType") or {}).get("name") or "?"
            )
            mark = "  <-- SENSITIVE" if SENSITIVE_RE.search(f["name"]) else ""
            if mark:
                interesting += 1
            lines.append(f"  {f['name']}: {ftype}{mark}")
        lines.append("")
    lines.append(f"{interesting} sensitive-looking field(s) highlighted")
    lines.append("next: query the object by id, over-fetch the highlighted fields")
    return "\n".join(lines)


def _selftest(post_query, render) -> int:
    """Mock introspection server on localhost; asserts the highlight logic."""
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    schema = {
        "data": {
            "__schema": {
                "types": [
                    {"name": "PostType", "kind": "OBJECT", "fields": [
                        {"name": "id", "type": {"name": "Int", "kind": "SCALAR", "ofType": None}},
                        {"name": "title", "type": {"name": "String", "kind": "SCALAR", "ofType": None}},
                        {"name": "postPassword", "type": {"name": "String", "kind": "SCALAR", "ofType": None}},
                        {"name": "isHidden", "type": {"name": "Boolean", "kind": "SCALAR", "ofType": None}},
                    ]},
                    {"name": "Query", "kind": "OBJECT", "fields": [
                        {"name": "posts", "type": {"name": None, "kind": "LIST", "ofType": {"name": "PostType"}}},
                        {"name": "post", "type": {"name": "PostType", "kind": "OBJECT", "ofType": None}},
                    ]},
                ]
            }
        }
    }

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            body = json.dumps(schema).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        url = f"http://127.0.0.1:{server.server_port}/api/graphql"
        payload = post_query(url, INTROSPECTION_QUERY)
        out = render(payload)
        ok = "postPassword" in out and "SENSITIVE" in out and "isHidden" in out
        print(out)
        print("SELFTEST:", "PASS" if ok else "FAIL")
        return 0 if ok else 1
    finally:
        server.shutdown()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--url", help="GraphQL endpoint (e.g. http://target/api/graphql)")
    ap.add_argument("--json", metavar="FILE", help="save raw introspection response")
    ap.add_argument("--selftest", action="store_true",
                    help="run against a local mock server (no network)")
    args = ap.parse_args()

    if args.selftest:
        return _selftest(post_query, render)

    if not args.url:
        ap.error("provide --url or --selftest")

    try:
        payload = post_query(args.url, INTROSPECTION_QUERY)
    except RuntimeError as exc:
        print(f"introspection failed: {exc}", file=sys.stderr)
        print("fallbacks: field-name wordlists, client-bundle clue mining, "
              "error-message suggestions", file=sys.stderr)
        return 2
    except Exception as exc:  # network errors, non-JSON bodies
        print(f"request failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
        print(f"raw response saved: {args.json}")
    print(render(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
