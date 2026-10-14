# CTFTTOU-019 — PKINITtools

> **Tool ID:** `CTFTTOU-019`  
> **Related techniques/counters:** CTFTTE-FPN-011, CTFTCTE-FPN-011

## Description

Dirkjan's toolkit for certificate-based Kerberos abuse. Provides `gettgtpkinit.py` (request a TGT from a PFX certificate) and `getnthash.py` (unPAC the NT hash from a TGT). Combined with a planted key credential they convert certificate material into NTLM-compatible access.

## URL

<https://github.com/dirkjanm/PKINITtools>

## Related Techniques

CTFTTE-FPN-011, CTFTCTE-FPN-011
