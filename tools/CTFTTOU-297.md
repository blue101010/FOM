# CTFTTOU-297 — Enter-PSSession

> **Tool ID:** `CTFTTOU-297`  
> **Related techniques/counters:** CTFTTE-FPN-014, CTFTCTE-FPN-014

## Description

PowerShell cmdlet that starts an interactive remoting session; with `-ConfigurationName` it selects a constrained (JEA) session configuration. `Get-PSSession` and transcripts are the audit surface.

## URL

<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession>

## Related Techniques

CTFTTE-FPN-014, CTFTCTE-FPN-014
