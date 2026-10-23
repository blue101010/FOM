# CTFTTOU-314 — wfuzz

> **Tool ID:** `CTFTTOU-314`  
> **Related techniques/counters:** CTFTCTE-WEB-001, CTFTCTE-WEB-002, CTFTCTE-WEB-011, CTFTCTE-WEB-017, CTFTTE-WEB-001, CTFTTE-WEB-002, CTFTTE-WEB-011, CTFTTE-WEB-017

## Description

Python web application fuzzer: the `FUZZ` keyword can be placed anywhere in the request (path,
parameters, headers, cookies, body), with multiple payload sets, encoders, and response filters
on code, lines, words or characters (`--hc`, `--hl`, `--hw`, `--hh`). Suited to parameter and
object-ID enumeration, traversal payload lists and Host-header fuzzing as well as content
discovery.

## URL

<https://github.com/xmendez/wfuzz>

## Related Techniques

CTFTCTE-WEB-001, CTFTCTE-WEB-002, CTFTCTE-WEB-011, CTFTCTE-WEB-017, CTFTTE-WEB-001, CTFTTE-WEB-002, CTFTTE-WEB-011, CTFTTE-WEB-017
