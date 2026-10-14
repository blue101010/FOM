# CTFTTOU-031 — printerbug.py

> **Tool ID:** `CTFTTOU-031`  
> **Related techniques/counters:** CTFTTE-FPN-017, CTFTCTE-FPN-017

## Description

MS-RPRN coercion trigger from krbrelayx. Forces a remote host (typically the domain controller) to authenticate back to a chosen machine by abusing the print spooler RPC interface. Hostname casing matters: the writeup notes the target must be spelled in lowercase for the coercion to fire.

## URL

<https://github.com/dirkjanm/krbrelayx/blob/master/printerbug.py>

## Related Techniques

CTFTTE-FPN-017, CTFTCTE-FPN-017
