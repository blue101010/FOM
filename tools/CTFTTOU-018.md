# CTFTTOU-018 — pywhisker

> **Tool ID:** `CTFTTOU-018`  
> **Related techniques/counters:** CTFTTE-FPN-011, CTFTCTE-FPN-011

## Description

Python implementation of the shadow-credentials attack: generates a certificate and a key credential, writes it to the target account's `msDS-KeyCredentialLink` attribute, and saves the resulting PFX plus its export password. Works over LDAP without changing the account password.

## URL

<https://github.com/ShutdownRepo/pywhisker>

## Related Techniques

CTFTTE-FPN-011, CTFTCTE-FPN-011
