# CTFTTE-WEB-024 — Race window in a state-changing flow

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-024`](../countertechniques/CTFTCTE-WEB-024.md) — Fire a synchronized request burst at the state change

---

## How the challenge author hides

The business rule is enforced across two distinct steps — the **check** (balance,
stock, coupon unused, name unique, vote not cast) and the **commit** — with no
lock bridging them. Every request inspected on its own is

correct, so ordinary play always satisfies the rule: the state is read, the
decision is taken, then the new state is written. The invariant only breaks when
two requests both observe the pre-state and both commit, so a player who works
sequentially never sees the flaw, and a player who works quickly still does not
see it unless the requests actually overlap.

The concealment is temporal, not structural: nothing is missing, nothing is
misnamed, and no authorization check is absent. The intended read is "this is a
normal shop/vote/registration endpoint".

Design variants, in increasing subtlety:

- **Single-use artefact.** A coupon, invitation or one-time token is meant to be
  consumed once; concurrent redemptions all pass the "still valid" check.
- **Bounded balance.** A transfer or withdrawal debits a balance that is
  validated, not reserved, so N concurrent debits each pass on the full amount.
- **Counting limit.** A quota ("one vote", "three attempts", "one entry per
  user") is compared before insertion, so the counter overshoots under overlap.
- **Uniqueness constraint.** A "unique" resource is checked in application code
  rather than by the store, so duplicates are created in the same window.
- **Multi-step workflow.** Only the last step is guarded; submitting the final
  step concurrently with the first skips an approval the story promises.
- **Read-modify-write on a shared field.** Two independent updates each preserve
  the documented invariant, but their combination does not.

Boundary: when a single request is simply missing an authorization check, the
pair is the function-level authorization one; when the payload differs but the
number of concurrent requests is irrelevant, the pair is the one about state the
server trusts from the client. Here the request is legitimate and correct and
only its **simultaneity** is illegitimate.

## Indicators

- narrative language about "only once", "single use", "one per account",
  "never below zero", "limited stock", "cannot be undone twice"
- a single endpoint that validates and mutates in one call, returning the new
  total, balance or counter in its response
- a token or nonce issued by an earlier response and echoed back later
- refusal text that says "already used" or "would exceed" rather than "denied",
  which shows the decision is a state comparison
- a store call sequence visible in errors (two statements named in a stack trace
  or debug page), or a visible commit delay
- a challenge that hands the player a request template and stresses throughput

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | The flaw is exercised through an ordinary application endpoint. |
| T1565.001 | Data Manipulation: Stored Data Manipulation | The winning burst leaves persisted state that a sequential player cannot reach. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — raw last-byte-synchronized bursts and parallel batches, with every attempt recorded by request id
- Turbo Intruder or an equivalent raw-socket driver, when the window must be hit on the wire rather than through a client library
- a proxy that preserves the exact byte framing of each attempt, so the burst is reproducible

## References

- <https://portswigger.net/web-security/race-conditions>
- <https://portswigger.net/research/smashing-the-state-machine>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/>
