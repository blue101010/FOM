# CTFTTOU-021 — gettgtpkinit.py

> **Tool ID:** `CTFTTOU-021`  
> **Related techniques/counters:** CTFTTE-FPN-012, CTFTCTE-FPN-012

## Description

PKINIT client from PKINITtools: loads a PFX certificate and its export password, requests a TGT from the domain controller, writes the credential cache, and prints the AS-REP encryption key — the value needed later to recover the NT hash from the PAC.

## URL

<https://github.com/dirkjanm/PKINITtools/blob/master/gettgtpkinit.py>

## Related Techniques

CTFTTE-FPN-012, CTFTCTE-FPN-012
