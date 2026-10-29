# CTFTCTE-WEB-025 — Rewrite or extend the trust-bearing client fields

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-025`](../techniques/CTFTTE-WEB-025.md) — Server-trusted client-computed state

---

## Offensive Recovery (CTF practitioner / solver)

The question is never "can I change this value" but "which value does the server
derive and which does it accept". Enumerate the accepted surface before editing
anything.

1. **Inventory the trust-bearing fields.** Read the rendered form, the inline
   script and one response object, and list every value that decides privilege,
   price, ownership, quantity or status. Mark each as `derived server-side`,
   `echoed back`, or unknown.
2. **Send the baseline unchanged.** Keep the exact request, so that every later
   variant differs by one field and the diff is attributable.
3. **Test the invisible ones first.** Disabled, `readonly` and hidden inputs are
   the cheapest edit: the field name is already correct and the only question is
   whether the server re-reads it.
4. **Test the unlisted ones next.** Add properties the interface never sends —
   the flag, the related object, the status, the tenant. A property that appears
   in a response object but not in the request is a candidate the binder already
   knows.
5. **Reshape what is rejected.** If a value is refused, resend it as a structure
   (array, nested object, duplicate parameter) or in another representation;
   coercion frequently decides where validation did not.
6. **Recompute what is checked.** When a total, hash or signature guards the
   edit, calculate the correct value for the new intent instead of removing the
   check — the check then validates your forgery.
7. **Judge by effect, not by status.** Evidence is a changed price on the invoice,
   a badge granted, a redirect into the privileged area, or a resource owned by
   another identity. Diff the two responses to confirm the field, not the status
   code, did the work.
8. **Escalate only if it is the same mechanic.** If the field carries no privilege
   and the function itself is above your role, switch to the function-level
   authorization pair.

Signatures to expect: the same status with a different body; a validated field
whose validation error disappears when the encoding changes; a response echoing
your injected property back; a redirect that lands somewhere the interface never
offers.

## Forensic / Blue-Team Perspective (DFIR analyst)

The signature is a request that carries a property the client never sends: an
unknown field in a bound object, a status flag set without the transition that
normally precedes it, a price or total that does not match the catalogue. Server
logs are only useful if the accepted field is logged, which is why the control is
an explicit allow-list at the binder — the weakness is architectural (binding
everything the wire carries) rather than a bad input check. On the detection
side, reconciliation between the order record and the catalogue, and between the
status field and its audit trail, is what surfaces the write.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1565.001 | Data Manipulation: Stored Data Manipulation | A client-asserted value is persisted as authoritative. |
| T1190 | Exploit Public-Facing Application | The field is edited on an ordinary endpoint. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — edit one recorded request per hypothesis, with a persistent cookie jar and a response diff per variant
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — diffing request and response shapes to find writable-but-hidden properties
- an authorization-bypass harness (Autorize-style), when the rewritten field must be judged against a second role

## References

- <https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html>
- <https://owasp.org/API-Security/editions/2023/en/0xa6-broken-object-property-level-authorization/>
- <https://cwe.mitre.org/data/definitions/915.html>
