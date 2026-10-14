# CTFTTOU-034 — Get-PSReadlineOption

> **Tool ID:** `CTFTTOU-034`  
> **Related techniques/counters:** CTFTTE-FPN-019, CTFTCTE-FPN-019

## Description

PowerShell cmdlet that reveals where PSReadLine stores console history. `(Get-PSReadlineOption).HistorySavePath` points to `ConsoleHost_history.txt`, the file that may contain typed passwords from interactive administrator sessions.

## URL

<https://learn.microsoft.com/en-us/powershell/module/psreadline/get-psreadlineoption>

## Related Techniques

CTFTTE-FPN-019, CTFTCTE-FPN-019
