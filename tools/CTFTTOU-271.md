# CTFTTOU-271 — graphql-schema-dump.py

> **Tool ID:** `CTFTTOU-271`  
> **Related techniques/counters:** CTFTTE-WEB-023, CTFTCTE-WEB-023

## Description

CTFT-authored introspection dumper (Python, standard library only — no pip install, safe
on Kali under PEP 668). POSTs the `__schema` query to a GraphQL endpoint, prints every
type with its fields, highlights sensitive-looking field names (password, secret, hidden,
token, admin, flag, key, private) and suggests the over-fetch step. Detects disabled
introspection and prints fallbacks. `--selftest` runs against a built-in mock server.

## URL

[scripts/graphql-schema-dump.py](scripts/graphql-schema-dump.py) (local CTFT tool)

## Related Techniques

CTFTTE-WEB-023, CTFTCTE-WEB-023
