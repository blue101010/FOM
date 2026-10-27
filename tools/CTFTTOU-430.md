# CTFTTOU-430 — AADInternals

> **Tool ID:** `CTFTTOU-430`  
> **Related techniques/counters:** CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## Description

A PowerShell toolkit for the Microsoft cloud directory. Large surface, but four families carry most
challenge value:

- **Tenant and login information.** Resolve a domain to a tenant, read the identity provider's metadata,
  and answer "which tenant is this?" from a domain name alone.
- **User-object queries.** Enumerate users, groups and applications with the permissions the recovered
  identity actually holds, including the outsider-style queries that do not need a token at all.
- **Token work.** Inspect, decode and request tokens for other audiences, and examine what a given token
  authorises.
- **Configuration review.** Read the tenant's own settings and find the ones a challenge describes as
  misconfigured.

PowerShell is present on Kali (`pwsh`), so the module runs natively in the same environment as the rest of
the tooling.

## URL

- <https://github.com/Gerenios/AADInternals>

## Installation

```bash
pwsh -NoProfile -Command "Install-Module AADInternals -Scope CurrentUser -Force"
pwsh -NoProfile -Command "Import-Module AADInternals; Get-Command -Module AADInternals | Measure-Object"
```

If the gallery is unreachable from the challenge network, clone the repository and import the module file
directly from the checkout.

## Usage

```bash
pwsh -NoProfile -Command "Import-Module AADInternals; Get-AADIntLoginInformation -UserName user@tenant.tld"
pwsh -NoProfile -Command "Import-Module AADInternals; Get-AADIntTenantID -Domain tenant.tld"
pwsh -NoProfile -Command "Import-Module AADInternals; Get-AADIntAccessTokenForMSGraph -SaveToCache"
pwsh -NoProfile -Command "Import-Module AADInternals; Get-AADIntUsers | Select UserPrincipalName,ObjectId"
pwsh -NoProfile -Command "Import-Module AADInternals; ConvertTo-AADIntJWT -Token \$(Get-Content token.jwt)"
```

Cmdlet names are stable but their `-Verbose` output is the fastest way to see the underlying request —
useful when the challenge's tenant behaves differently from the public cloud. The module caches tokens in
the current user profile; use a throwaway profile per challenge.

Pitfalls: on Linux/macOS PowerShell the module loads but prints
`Add-Type: Cannot find path '…/System.Web.Extensions.dll'` — that assembly is Windows-only, so the cmdlets
that depend on it fail there. Run those from Windows PowerShell instead
(`powershell.exe -NoProfile -Command "Import-Module AADInternals; …"`), and keep `pwsh` on Linux for the
token/tenant cmdlets that do work. A redacted tenant is not a broken module: check the error class before
abandoning a cmdlet.

## Related Techniques

CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## References

- [AADInternals repository](https://github.com/Gerenios/AADInternals)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [OpenID Connect metadata document](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc)
