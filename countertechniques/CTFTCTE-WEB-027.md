# CTFTCTE-WEB-027 — Re-encode the request body across representations and replay

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-027`](../techniques/CTFTTE-WEB-027.md) — Representation differential across body formats

---

## Offensive Recovery (CTF practitioner / solver)

If validation and binding read the request differently, the recovery is a
**matrix**: one payload, every representation, and a comparison of what each one
produced. Do not hunt for a better payload until the matrix is exhausted.

1. **Keep the successful baseline.** The captured request that the application
   accepts is the control; every variant must be judged against it and against
   the refusal the filter produced.
2. **Convert before you invent.** Rewrite the same logical body into the sibling
   representations the framework accepts — form-encoded, multipart, XML, and the
   JSON document — and let each carry the **same** value. The content type must
   travel with the body, since it is the switch that selects the parser.
3. **Vary the container, not only the value.** A field accepted as a string may
   be refused as an array and vice versa; a nested object may reach a property
   the flat form did not.
4. **Duplicate deliberately.** Send the value twice — in two body formats, in body
   and query, or as two occurrences of the parameter — and use the resulting
   behaviour to learn which parser wins. Parser precedence is the vulnerability,
   so measuring it is the exploit.
5. **Test the value encoding separately.** Once the container is settled,
   normalise and denormalise the characters: percent, double-percent, overlong,
   escaped. A sink that decodes twice is reachable only from this axis.
6. **Send malformed framing on purpose.** A boundary that ends early, a filename
   in a disposition header, a duplicate content type — these decide which part of
   the body the binder even looks at.
7. **Confirm which layer answered.** A refusal naming one syntax, a debug header
   or an error page identifies the parser that read the request; that name is the
   evidence that two layers exist.
8. **Re-check the output representation.** When the value is stored and served
   later, replay the read path too: validation on the input shape says nothing
   about the shape the output is rendered in.

Signatures to expect: identical bytes refused under one content type and accepted
under another; a validation error that mentions a syntax the request did not use;
the last duplicate winning when the first was the one validated; success only
when the value is encoded twice.

## Forensic / Blue-Team Perspective (DFIR analyst)

The control gap is architectural: inspection and binding are two components with
two grammars, and the request is only safe if the second is at least as strict as
the first. Logs show it as a content type the endpoint does not document, a body
carrying two representations of one field, or repeated parameters surviving to
the application. Detection is on the shape of the request rather than on the
payload, and the durable fix is canonicalisation — parse once, bind from the
single parsed structure, reject ambiguity.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The same value arrives in a representation the inspection layer does not read. |
| T1190 | Exploit Public-Facing Application | Variants are replayed against an ordinary endpoint. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — converts a captured body between JSON, form, XML and multipart, and returns the matching content type for the replay
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — rebuilding the alternative representation from the original payload
- a raw HTTP client, for duplicate parameters and duplicate headers a convenience client would merge

## References

- <https://portswigger.net/web-security/logic-flaws>
- <https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html>
- <https://cwe.mitre.org/data/definitions/436.html>
