# CTFTTOU-026 — mssqlclient.py

> **Tool ID:** `CTFTTOU-026`  
> **Related techniques/counters:** CTFTTE-FPN-015, CTFTCTE-FPN-015

## Description

Impacket interactive MSSQL client. Once authenticated as a database administrator it drives T-SQL directly: inspect privileges, enable `xp_cmdshell` with `sp_configure`, and execute operating-system commands from the SQL shell.

## URL

<https://github.com/fortra/impacket/blob/master/examples/mssqlclient.py>

## Related Techniques

CTFTTE-FPN-015, CTFTCTE-FPN-015
