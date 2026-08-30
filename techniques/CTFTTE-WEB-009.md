# CTFTTE-WEB-009 — Web configuration secret exposure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-009`](../countertechniques/CTFTCTE-WEB-009.md) — Classify a configuration secret exposure

---

## How the challenge author hides

A supplied deployment configuration embeds a credential, connection reference,
or privileged service setting that is not intended to be exposed with the Web
application. The secret is represented only as a redacted challenge artifact.

## ATT\&CK Complementarity

This is a configuration-hygiene failure represented in a challenge artifact; it
does not describe credential use against an external system.

## Evidence expected

- A configuration artifact contains a redacted secret-bearing field.
- The field is linked to an application, service role, and remediation owner.

## References

- <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>
