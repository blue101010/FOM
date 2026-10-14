# CTFTTOU-032 — getST.py

> **Tool ID:** `CTFTTOU-032`  
> **Related techniques/counters:** CTFTTE-FPN-017, CTFTCTE-FPN-017

## Description

Impacket S4U2Self/S4U2Proxy service-ticket requester. With the captured DC machine TGT (or a delegated account's hash) it requests a `CIFS/DC` service ticket as Administrator — the ticket that unlocks remote registry, SMB access and hash dumping on the domain controller.

## URL

<https://github.com/fortra/impacket/blob/master/examples/getST.py>

## Related Techniques

CTFTTE-FPN-017, CTFTCTE-FPN-017
