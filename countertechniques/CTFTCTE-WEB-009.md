# CTFTCTE-WEB-009 — Classify a configuration secret exposure

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-009`](../techniques/CTFTTE-WEB-009.md) — Web configuration secret exposure

---

## Offensive Recovery (CTF practitioner / solver)

Classify the exposure from the supplied redacted artifact, link it to the
declared service boundary, and report it as a candidate path condition rather
than using or reproducing the secret.

Do not review markup by hand when the corpus is larger than one page. Sweep every
captured response with a passive rule set whose rules carry stable names —
credential shapes, token shapes, key prefixes, configuration keys inside a
rendered document — and read the result as a ranked list of findings, each tied
to the request it came from. The class of the secret then decides the next step:
a configuration key is a boundary statement, a live token is a path condition.

## Forensic / Blue-Team Perspective (DFIR analyst)

Record the configuration source, affected service, secret class and rotation
requirement. The remediation is removal from the artifact and credential
rotation through the approved secret store.

## Preconditions

- The challenge provides a redacted configuration artifact.
- The result is stored as evidence without retaining a secret value.

## Indicators

- A configuration key denotes credentials, connection data, or an access token.
- The field is reachable from a Web deployment artifact.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Configuration secret exposure echoes unsecured credentials. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — passive secret-shape rules over every proxied response, findings tied to a request id
- [Caido workflow catalogue](../tools/CTFTTOU-442.md) ([CTFTTOU-442](../tools/CTFTTOU-442.md)) — the rule set that supplies the secret and token detectors
- [Nikto](../tools/CTFTTOU-315.md)

## References

- <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>
