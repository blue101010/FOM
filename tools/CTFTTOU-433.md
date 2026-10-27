# CTFTTOU-433 — MicroBurst

> **Tool ID:** `CTFTTOU-433`  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-010, CTFTCTE-CLD-010

## Description

A PowerShell collection of Azure enumeration routines, most of which answer a question the first-party
tooling makes awkward:

- **Storage discovery** — enumerate storage accounts and blobs from a keyword, from a subscription, or
  from an identity, which is the shortcut when a challenge leaks a partial name.
- **Sub-domain and host enumeration** for the provider's naming conventions, useful when the objective is
  an application hostname rather than a management-plane object.
- **Credential and secret hunting inside a subscription** — deployment history, automation accounts,
  runbook content, application settings, and the resource kinds that keep secrets in readable properties.
- **Key-vault and automation helpers** that turn a discovered store into a read attempt.

It is a *sweep* tool: read the list of functions it exposes (`Get-Command -Module MicroBurst`) and pick the
two that match the story, rather than running everything against a live tenant.

## URL

- <https://github.com/NetSPI/MicroBurst>

## Installation

```bash
git clone --depth 1 https://github.com/NetSPI/MicroBurst.git ~/TOOLS/MicroBurst
pwsh -NoProfile -Command "Import-Module ~/TOOLS/MicroBurst/MicroBurst.psm1; Get-Command -Module MicroBurst | Select-Object -ExpandProperty Name"
```

## Usage

```bash
pwsh -NoProfile -Command "Import-Module ~/TOOLS/MicroBurst/MicroBurst.psm1; Get-Command -Module MicroBurst"

# storage discovery from a keyword / from the current identity
pwsh -NoProfile -Command "Import-Module ~/TOOLS/MicroBurst/MicroBurst.psm1; Invoke-EnumerateAzureBlobs -Base KEYWORD"

# subscription-wide sweep for the resource kinds that keep secrets in readable properties
pwsh -NoProfile -Command "Import-Module ~/TOOLS/MicroBurst/MicroBurst.psm1; Get-AzurePasswords -Verbose"
```

Several functions write output files next to the module; run from a scratch directory. Some routines are
noisy against a real tenant — in a challenge, prefer the narrow function that matches the artefact over a
full sweep.

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-010, CTFTCTE-CLD-010

## References

- [MicroBurst repository](https://github.com/NetSPI/MicroBurst)
- [Azure Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)
- [Azure Key Vault overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
