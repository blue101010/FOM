# CTFTTOU-028 — PetitPotato

> **Tool ID:** `CTFTTOU-028`  
> **Related techniques/counters:** CTFTTE-FPN-016, CTFTCTE-FPN-016

## Description

Token-impersonation privilege-escalation binary for accounts holding SeImpersonatePrivilege. Takes a program plus arguments and runs it as `NT AUTHORITY\SYSTEM`. When endpoint protection blocks the stock build, repackaging the binary with UPX is the writeup's documented bypass.

## URL

<https://github.com/wh0amitz/PetitPotato>

## Related Techniques

CTFTTE-FPN-016, CTFTCTE-FPN-016
