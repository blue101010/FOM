# CTFTTOU-025 — Enter-PSSession / New-PSSession

> **Tool ID:** `CTFTTOU-025`  
> **Related techniques/counters:** CTFTTE-FPN-014, CTFTCTE-FPN-014

## Description

PowerShell remoting cmdlets. With `-ConfigurationName` they select a constrained (JEA) session configuration; the entered session is where a vulnerable module parameter is injected. `Get-PSSession` and transcript configuration are the corresponding audit surface.

## URL

<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession>

## Related Techniques

CTFTTE-FPN-014, CTFTCTE-FPN-014
