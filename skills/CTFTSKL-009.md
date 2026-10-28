# CTFTSKL-009 — ctf-cloud-azure

> **Skill ID:** `CTFTSKL-009`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003, CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011

## Description

Decision workflow for authorized Azure / Entra ID challenges. Given an Azure artefact — a token or
refresh token, a service-principal secret or certificate, an `az` profile, a signed blob URL or connection
string, a key-vault name, an App Service or Functions host, an instance-metadata endpoint, a Bicep/ARM
template or a pipeline definition — establish the acting identity, enumerate what it can actually read, and
name the single grant that reaches the flag: a re-audienced token, an over-broad role assignment, a
management-plane action, a vault grant, a signed-URL scope, or a data plane that needs a second
authorisation.

It complements `ctf-cloud-kubernetes` (cluster-first challenges) by covering the directory/management-plane
side, and it turns four loose ideas into executable steps: token audience work, the two key-vault
authorisation models, the control-plane-versus-data-plane split, and the platform leaks of App Service.

## Skill file

- [ctf-skills-main/ctf-cloud-azure/SKILL.md](../../ctf-skills-main/ctf-cloud-azure/SKILL.md) — canonical
- References: [entra-identity.md](../../ctf-skills-main/ctf-cloud-azure/references/entra-identity.md),
  [arm-and-rbac.md](../../ctf-skills-main/ctf-cloud-azure/references/arm-and-rbac.md),
  [storage-and-keyvault.md](../../ctf-skills-main/ctf-cloud-azure/references/storage-and-keyvault.md),
  [app-service-and-functions.md](../../ctf-skills-main/ctf-cloud-azure/references/app-service-and-functions.md)
- Script: [azure_ctf_inventory.py](../../ctf-skills-main/ctf-cloud-azure/scripts/azure_ctf_inventory.py)
  (`selftest` = 32 offline checks, no network)
- Script: [azure_entra_search.py](../../ctf-skills-main/ctf-cloud-azure/scripts/azure_entra_search.py)
  (directory-wide value/property-name search, paging, `--offline` replay, `--sqlite` dump search,
  `selftest` = 26 offline checks)

## When to load

```yaml
artifact_type: credential | token | signed-url | template | hostname | environment-dump
runtime: azure | entra
evidence:
  - a token, refresh token, token cache, client id with secret or certificate, or an az login profile
  - azure hostnames: *.blob.core.windows.net, *.vault.azure.net, *.azurewebsites.net,
    *.scm.azurewebsites.net, *.documents.azure.com, *.azurecr.io, *.database.windows.net, graph.microsoft.com
  - an instance metadata endpoint (169.254.169.254, IDENTITY_ENDPOINT / MSI_ENDPOINT)
  - a signed URL (sig=, sv=, se=, sp=, sr=, srt=) or a connection string with AccountKey=
  - an ARM/Bicep template, a parameter file, a deployment history or a pipeline definition
  - a story about "too many permissions", a guest account, a misconfigured vault or a public database
```

## FOM pairs

- [CTFTTE-CLD-001](../techniques/CTFTTE-CLD-001.md) / [CTFTCTE-CLD-001](../countertechniques/CTFTCTE-CLD-001.md) — object-storage exposure (anonymous)
- [CTFTTE-CLD-002](../techniques/CTFTTE-CLD-002.md) / [CTFTCTE-CLD-002](../countertechniques/CTFTCTE-CLD-002.md) — over-permissive role
- [CTFTTE-CLD-003](../techniques/CTFTTE-CLD-003.md) / [CTFTCTE-CLD-003](../countertechniques/CTFTCTE-CLD-003.md) — instance metadata (IMDS) exposure
- [CTFTTE-CLD-005](../techniques/CTFTTE-CLD-005.md) / [CTFTCTE-CLD-005](../countertechniques/CTFTCTE-CLD-005.md) — container image / registry leak
- [CTFTTE-CLD-007](../techniques/CTFTTE-CLD-007.md) / [CTFTCTE-CLD-007](../countertechniques/CTFTCTE-CLD-007.md) — document/key-value store misconfiguration
- [CTFTTE-CLD-008](../techniques/CTFTTE-CLD-008.md) / [CTFTCTE-CLD-008](../countertechniques/CTFTCTE-CLD-008.md) — management-plane misconfiguration
- [CTFTTE-CLD-009](../techniques/CTFTTE-CLD-009.md) / [CTFTCTE-CLD-009](../countertechniques/CTFTCTE-CLD-009.md) — delegated session material exposed
- [CTFTTE-CLD-010](../techniques/CTFTTE-CLD-010.md) / [CTFTCTE-CLD-010](../countertechniques/CTFTCTE-CLD-010.md) — secret store reachable by a workload identity
- [CTFTTE-CLD-011](../techniques/CTFTTE-CLD-011.md) / [CTFTCTE-CLD-011](../countertechniques/CTFTCTE-CLD-011.md) — bearer credential embedded in a storage URL

## Tools

- [CTFTTOU-427](../tools/CTFTTOU-427.md) — Azure CLI (`az`, `az rest`)
- [CTFTTOU-428](../tools/CTFTTOU-428.md) — AzureHound / BloodHound
- [CTFTTOU-429](../tools/CTFTTOU-429.md) — ROADtools (roadrecon / roadtx)
- [CTFTTOU-430](../tools/CTFTTOU-430.md) — AADInternals
- [CTFTTOU-431](../tools/CTFTTOU-431.md) — Microsoft Graph API and Graph CLI
- [CTFTTOU-432](../tools/CTFTTOU-432.md) — AzCopy and `az storage` (data plane)
- [CTFTTOU-433](../tools/CTFTTOU-433.md) — MicroBurst
- [CTFTTOU-434](../tools/CTFTTOU-434.md) — GraphRunner
- [CTFTTOU-435](../tools/CTFTTOU-435.md) — Monkey365
- [CTFTTOU-436](../tools/CTFTTOU-436.md) — ScoutSuite and Prowler
- [CTFTTOU-437](../tools/CTFTTOU-437.md) — o365spray / MSOLSpray
- [CTFTTOU-438](../tools/CTFTTOU-438.md) — TokenTacticsV2
- [CTFTTOU-439](../tools/CTFTTOU-439.md) — azure_ctf_inventory.py (bundled, offline)
- [CTFTTOU-440](../tools/CTFTTOU-440.md) — azure_entra_search.py (bundled, read-only directory sweep)

## Related skills

- [ctf-cloud-kubernetes](CTFTSKL-006.md) — when the foothold becomes a cluster or the path crosses a workload identity
- [ctf-cloud-public-bucket](CTFTSKL-008.md) — when the storage exposure needs no credential at all
- [ctf-ad-attack-paths](CTFTSKL-004.md) — when the directory is hybrid (sync, domain-joined hosts, Kerberos)

## Notes

Added 2026-10-27 to close the Azure gap: CLD-008 was a three-line entry with no executable workflow, and no
skill covered the token/audience half of the domain. New pairs CLD-009 (delegated session material),
CLD-010 (secret store reachable by an identity) and CLD-011 (bearer credential in a storage URL) fill
boundaries the existing eight entries explicitly left open. CLD-007 and CLD-008 were rewritten to carry
variants, indicators and DFIR markers. All new pairs remain `taxonomy_only`: no attested CTF event record yet.

Kali already ships `az` (azure-cli, apt) and `pwsh`; everything else installs via apt, pipx or
`~/.venvs/ctfazure` — never a bare `pip install` (PEP 668).

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003,
CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-008, CTFTCTE-CLD-008,
CTFTTE-CLD-009, CTFTCTE-CLD-009, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011
