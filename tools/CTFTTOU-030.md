# CTFTTOU-030 — Rubeus

> **Tool ID:** `CTFTTOU-030`  
> **Related techniques/counters:** CTFTTE-FPN-017, CTFTCTE-FPN-017

## Description

Windows Kerberos abuse toolkit. `Rubeus.exe monitor` listens for incoming TGTs on a host with unconstrained delegation — the capture side of a printer-bug coercion — and prints or exports the tickets (base64 kirbi) for later reuse against the domain controller.

## URL

<https://github.com/GhostPack/Rubeus>

## Related Techniques

CTFTTE-FPN-017, CTFTCTE-FPN-017
