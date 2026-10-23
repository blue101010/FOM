# CTFTTOU-317 — XSStrike

> **Tool ID:** `CTFTTOU-317`  
> **Related techniques/counters:** CTFTCTE-WEB-012, CTFTTE-WEB-012

## Description

Cross-site scripting detection suite: analyses the reflection context of each parameter,
generates context-aware payloads, fingerprints and attempts to bypass WAFs, fuzzes, and
crawls for reflected and DOM XSS candidates. It finds the injection point; delivering the
flag-exfiltration payload to the bot or admin is still manual.

## URL

<https://github.com/s0md3v/XSStrike>

## Related Techniques

CTFTCTE-WEB-012, CTFTTE-WEB-012
