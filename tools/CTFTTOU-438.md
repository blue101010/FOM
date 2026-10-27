# CTFTTOU-438 — TokenTacticsV2

> **Tool ID:** `CTFTTOU-438`  
> **Related techniques/counters:** CTFTTE-CLD-009, CTFTCTE-CLD-009

## Description

A PowerShell toolkit dedicated to token manipulation on the Microsoft identity platform: request tokens
for a chosen resource, refresh an existing refresh token, parse what a token authorises, and hand the
result to the next tool.

It is narrower than a full directory toolkit and that is its advantage in a challenge: when the artefact is
a refresh token and the flag is behind a different audience, this is the shortest path from "wrong token"
to "token for the plane in the story", without pulling in a whole collection framework.

## URL

- <https://github.com/f-bader/TokenTacticsV2>

## Installation

```bash
git clone --depth 1 https://github.com/f-bader/TokenTacticsV2.git ~/TOOLS/TokenTacticsV2
pwsh -NoProfile -Command "Import-Module ~/TOOLS/TokenTacticsV2/TokenTacticsV2.psd1; Get-Command -Module TokenTacticsV2"
```

## Usage

```bash
pwsh -NoProfile -Command "Import-Module ~/TOOLS/TokenTacticsV2/TokenTacticsV2.psd1; Get-Command -Module TokenTacticsV2"

# refresh a token for another resource / client
#   Invoke-RefreshToAzureCoreManagementToken   – resource-manager audience
#   Invoke-RefreshToMicrosoftGraphToken        – directory audience
#   Invoke-RefreshToSubstrateToken             – first-party surface
#   Get-JWTDetails                             – decode and print the claims
```

The command set is per-resource/per-client and grows with the toolkit; list the module's exported commands
before assuming a name. Every request is a sign-in event, and a token request outside the challenge's
intended flow is exactly the pattern a defender's detection looks for — keep it to what the story needs.

## Related Techniques

CTFTTE-CLD-009, CTFTCTE-CLD-009

## References

- [TokenTacticsV2 repository](https://github.com/f-bader/TokenTacticsV2)
- [Microsoft identity platform refresh tokens](https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens)
- [Access tokens and their claims](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
