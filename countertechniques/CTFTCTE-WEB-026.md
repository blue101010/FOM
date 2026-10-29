# CTFTCTE-WEB-026 — Sweep every captured response with passive detection rules and triage the findings

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-026`](../techniques/CTFTTE-WEB-026.md) — Signal buried in a high-volume response corpus

---

## Offensive Recovery (CTF practitioner / solver)

The answer is in the tail of the traffic, so the recovery is **coverage, then
triage** — one rule per signal class applied to every exchange, and a report you
can rank instead of a scroll you have to survive.

1. **Scope the target host first.** Rules that run on every response are only
   useful if the corpus is the challenge. An unscoped rule set spends its
   attention on fonts, analytics and CDN noise, and the real hit is one among
   hundreds.
2. **Generate the corpus deliberately.** Walk the whole surface through the
   recording instrument — every link, every list page, every asset the pages
   reference, the endpoints the bundle calls, the sitemap. Rules observe what was
   captured; a path never requested has nothing to scan. Prefer a browser walk
   over a hand-built request list, because the browser requests what the
   interface actually loads.
3. **Run the passive tier, not one clever rule.** Instantiate a set of small
   checks, each answering one question: does a flag-shaped token appear anywhere,
   does a credential shape appear, is an unusual header present, is a value
   reflected verbatim, is a hostname echoed, does the body differ from its
   siblings. Many cheap rules beat one expensive hypothesis, and each rule
   reports under its own name, which is what makes step 4 possible.
4. **Triage by reporter, then by count.** A reporter with exactly one hit among
   hundreds of exchanges is the interesting row; a reporter with a thousand hits
   is a badly scoped rule. Sort by reporter so that a single-rule result is never
   averaged away by a noisy one, and treat the dedupe key as the identity of a
   signal: duplicates mean re-observation, not new evidence.
5. **Follow the hit to the full exchange.** Each finding names the request it came
   from. Read that request and the **entire** response — past the byte count any
   comfortable listing shows — then decode the value in place: base64, hex,
   escaped JSON, a token's claim section.
6. **Handle the statistical variant by comparison.** When no rule fires, take one
   response from a look-alike family and diff it against its siblings; the
   needle is a length, a character or a token that only one member carries.
7. **Handle the fragment variant by ordering.** Several weak hits with the same
   reporter, scattered across the corpus, are usually one artefact in pieces:
   order them by time and concatenate before concluding anything.
8. **Record once, with the request embedded.** Export the finding set; the export
   carries the raw request, so the evidence is reproducible without re-deriving
   it, and the reporter name keeps your finding separable from rule-generated
   ones.

Signatures to expect: a single hit under a reporter that fired nowhere else; a
hit whose title names a header rather than a body; the same value resurfacing
under different encodings; a rule that fires hundreds of times and is therefore
noise; a hit that vanishes when the scope is widened, which means it belonged to
telemetry rather than to the challenge.

## Forensic / Blue-Team Perspective (DFIR analyst)

Passive inspection of every response is exactly what a data-loss-prevention or
egress-inspection control does; a challenge that hides a signal in volume mirrors
the defender's real problem, where the exfiltration is not concealed
cryptographically but placed inside ordinary traffic. The DFIR reading is that
per-request review does not scale and never did: detection depends on a rule
library with stable names, on deduplication so a repeated observation is counted
once, and on retention of the full body rather than a truncated preview. When an
incident is reconstructed, the finding record plus the embedded request is the
chain of custody — the reviewer's eye is not.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The signal is legible only at a granularity manual review does not reach. |
| T1213 | Data from Information Repositories | Recovery reads data a bulk retrieval already returned. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — capture, per-response rule execution, findings as first-class records tied to a request id, and an export that embeds the raw request
- [Caido workflow catalogue](../tools/CTFTTOU-442.md) ([CTFTTOU-442](../tools/CTFTTOU-442.md)) — the passive and on-demand rule set, organised by signal class
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — flattening and comparing the decoded bodies behind a hit
- a recursive text searcher over the exported corpus, as the second pass when no rule fired

## References

- <https://docs.caido.io/app/concepts/findings>
- <https://docs.caido.io/app/concepts/workflows>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/>
