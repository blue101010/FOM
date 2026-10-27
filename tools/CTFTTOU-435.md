# CTFTTOU-435 — Monkey365

> **Tool ID:** `CTFTTOU-435`  
> **Related techniques/counters:** CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## Description

A read-only assessment tool for Microsoft cloud tenants that runs a large set of configuration checks and
reports findings as structured output. In a challenge it is a **misconfiguration index**: instead of
guessing which setting the author weakened, run the checks and read the list of conditions the tenant
itself reports as risky, then verify the one that matches the story.

Its value is breadth, not depth: it will tell you that a mailbox rule, a consent grant, a role assignment
or an authentication policy is non-default — the flag itself still comes from following that finding by
hand. Findings are exported as HTML, JSON and CSV, so the JSON is what a script should consume.

## URL

- <https://github.com/silverhack/monkey365>

## Installation

```bash
git clone --depth 1 https://github.com/silverhack/monkey365.git ~/TOOLS/monkey365
pwsh -NoProfile -Command "Import-Module ~/TOOLS/monkey365/monkey365.psd1; Get-Command -Module monkey365"
# or, when the gallery is reachable:
pwsh -NoProfile -Command "Install-Module monkey365 -Scope CurrentUser -Force"
```

## Usage

```bash
# full instance against the current session, exporting every format
pwsh -NoProfile -Command "Import-Module ~/TOOLS/monkey365/monkey365.psd1; Invoke-Monkey365 -Instance ALL -ExportTo JSON,HTML -OutDir ./m365"

# single instance, when the story points at one surface
pwsh -NoProfile -Command "Import-Module ~/TOOLS/monkey365/monkey365.psd1; Invoke-Monkey365 -Instance ExchangeOnline -ExportTo JSON"
```

The `-Instance` values select the surface (the directory, exchange, the collaboration suite, the resource
manager). A full run is loud and slow: in a timed challenge, start from the instance the narrative implies
and widen only if it comes back empty.

## Related Techniques

CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## References

- [Monkey365 repository](https://github.com/silverhack/monkey365)
- [Microsoft Entra security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults)
- [Azure role-based access control](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
