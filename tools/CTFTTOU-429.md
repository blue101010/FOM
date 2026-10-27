# CTFTTOU-429 — ROADtools

> **Tool ID:** `CTFTTOU-429`  
> **Related techniques/counters:** CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## Description

A framework for the Microsoft identity platform (ROADrecon, ROADtx, roadlib). It is the tool of record
for the token half of an Azure challenge:

- **`roadrecon`** authenticates once and dumps the directory into a local database, then serves queries
  and a browser UI — useful when the challenge gives a working account and the flag is in an object
  relationship rather than a document.
- **`roadtx`** is the token instrument: request tokens for an arbitrary resource, redeem a device code,
  refresh an existing refresh token, inspect token contents, and exercise session material that a client
  would normally hold. This is the practical way to answer "the token's audience is wrong, mint me
  another".
- **`roadlib`** holds the shared authentication primitives, importable when a flow needs to be scripted.

In a challenge it converts "here is a token" into "here is a token for the plane that matters", and
"here is a tenant" into "here is what this identity can read".

## URL

- <https://github.com/dirkjanm/ROADtools>

## Installation

Python package set; install into a dedicated environment (Kali blocks system pip):

```bash
python3 -m venv ~/.venvs/ctfazure && source ~/.venvs/ctfazure/bin/activate
pip install roadrecon roadtx
roadrecon --help && roadtx --help
```

## Usage

```bash
# directory dump from a working identity, then query locally
roadrecon auth -u user@tenant.onmicrosoft.com -p 'password'
roadrecon gather
roadrecon gui                                  # browser UI over the local database

# token work: request, inspect, and re-audience a token
roadtx gettoken --help
roadtx describe -t "$(cat access_token.jwt)"
roadtx refresh -r "$(cat refresh_token.txt)" --resource https://management.azure.com

# device-code flow when only an interactive grant is possible
roadtx auth --device-code --client 04b07795-8ddb-461a-bbee-02f9e1bf7b46
```

Keep the token cache directory disposable per challenge; a stale cache produces confusing audience
errors. Every token operation is a sign-in event on the tenant side.

## Related Techniques

CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## References

- [ROADtools repository](https://github.com/dirkjanm/ROADtools)
- [Microsoft identity platform refresh tokens](https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens)
- [Device authorization grant](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
