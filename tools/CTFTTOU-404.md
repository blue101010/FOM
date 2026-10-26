# CTFTTOU-404 — ticket_check.sh

> **Tool ID:** `CTFTTOU-404`
> **Related techniques/counters:** CTFTTE-FPN-012, CTFTCTE-FPN-012

## Description

Workspace-authored read-only Kerberos ccache inspector (bash + klist). Shows the cache in use, its principal, the tickets it holds (TGT/service, SPN, validity) and flags expiry/skew — the usual cause of a failing Kerberos step. It never requests, renews, converts or deletes a ticket.

## URL

Local (workspace): [ctf-skills-main/ctf-ad-attack-paths/scripts/ticket_check.sh](../../ctf-skills-main/ctf-ad-attack-paths/scripts/ticket_check.sh)

## Usage

```bash
export KRB5CCNAME=/tmp/user.ccache; bash ticket_check.sh
```

## Skills

- [ctf-ad-attack-paths](../skills/CTFTSKL-004.md)

## Related Techniques

CTFTTE-FPN-012, CTFTCTE-FPN-012
