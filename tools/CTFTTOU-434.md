# CTFTTOU-434 — GraphRunner

> **Tool ID:** `CTFTTOU-434`  
> **Related techniques/counters:** CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## Description

A PowerShell toolkit organised around the Graph endpoint rather than the resource manager: token
acquisition and inspection, then enumeration and action routines that map onto the directory's own objects,
plus a search facility that queries the tenant for the terms the story uses.

Where the resource-manager tools answer "which subscriptions and resources", this answers "which directory
objects and relationships" — including the objects that carry credentials (applications, service
principals, and the mail and file surfaces a delegated identity can reach). The token routines are the
entry point: they let a recovered token or refresh token be re-audienced before any enumeration.

## URL

- <https://github.com/dafthack/GraphRunner>

## Installation

```bash
git clone --depth 1 https://github.com/dafthack/GraphRunner.git ~/TOOLS/GraphRunner
pwsh -NoProfile -Command "Set-Location ~/TOOLS/GraphRunner; Import-Module ./GraphRunner.ps1; Get-Help Invoke-GraphRunner -Detailed"
```

The toolkit expects a module of Graph request helpers in the same directory — import the module the
repository's README names first, then the main script.

## Usage

```bash
pwsh -NoProfile -Command "Set-Location ~/TOOLS/GraphRunner; Import-Module ./GraphRunner.ps1; Get-Command -Module GraphRunner"

# token handling first, enumeration second
#   Get-GraphTokens        – acquire/refresh tokens for the directories you can reach
#   Invoke-GraphRecon      – enumerate users, groups, applications, service principals
#   Invoke-SearchMailbox   – search the mail surface when the flag is a message
```

Run `Get-Help <command> -Full` for the parameter set of the installed version: the routine names have been
stable, the parameters less so.

## Related Techniques

CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## References

- [GraphRunner repository](https://github.com/dafthack/GraphRunner)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft identity platform refresh tokens](https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens)
