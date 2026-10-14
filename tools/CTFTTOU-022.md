# CTFTTOU-022 — getnthash.py

> **Tool ID:** `CTFTTOU-022`  
> **Related techniques/counters:** CTFTTE-FPN-012, CTFTCTE-FPN-012

## Description

PAC hash extraction from PKINITtools. Given the AS-REP encryption key printed during a PKINIT exchange and a valid TGT, it requests a ticket to self and recovers the account's NT hash — converting certificate-based access into hash-based Kerberos and NTLM tooling.

## URL

<https://github.com/dirkjanm/PKINITtools/blob/master/getnthash.py>

## Related Techniques

CTFTTE-FPN-012, CTFTCTE-FPN-012
