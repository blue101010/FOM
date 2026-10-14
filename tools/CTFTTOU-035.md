# CTFTTOU-035 — ldapdomaindump

> **Tool ID:** `CTFTTOU-035`  
> **Related techniques/counters:** CTFTTE-FPN-020, CTFTCTE-FPN-020

## Description

Active Directory information dumper: binds to LDAP and serializes users, groups, computers, trusts and policies into JSON and HTML reports. The JSON export is where a flag embedded in an object property is recovered with a case-insensitive search.

## URL

<https://github.com/dirkjanm/ldapdomaindump>

## Related Techniques

CTFTTE-FPN-020, CTFTCTE-FPN-020
