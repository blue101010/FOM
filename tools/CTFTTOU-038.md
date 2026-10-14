# CTFTTOU-038 — curl

> **Tool ID:** `CTFTTOU-038`  
> **Related techniques/counters:** CTFTTE-FPN-016, CTFTCTE-FPN-016

## Description

HTTP client used for the file-transfer stage of an escalation: the victim fetches the packed binary from the attacker's temporary web server into a writable folder before execution. Any HTTP client or a python `http.server` fulfills the same role.

## URL

<https://curl.se/>

## Related Techniques

CTFTTE-FPN-016, CTFTCTE-FPN-016
