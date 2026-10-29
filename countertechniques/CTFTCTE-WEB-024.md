# CTFTCTE-WEB-024 — Fire a synchronized request burst at the state change

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-024`](../techniques/CTFTTE-WEB-024.md) — Race window in a state-changing flow

---

## Offensive Recovery (CTF practitioner / solver)

The flaw is temporal, so the procedure is about **getting the requests to overlap
on the server**, not about crafting a better payload. Capture a request that is
known to succeed, then vary only its concurrency.

1. **Locate the check and the commit.** Replay the request once and read the
   response: if it returns the new balance, counter or total, the same endpoint
   both validates and mutates, and that is the target. Write down the pre-state.
2. **Prove the invariant sequentially.** Fire the same request twice, one after
   the other. The second must be refused. If it is accepted, this is not a race —
   it is a plain logic or authorization gap, and the pair is a different one.
3. **Choose the synchronization.** Prefer the mode that removes network jitter
   from the equation: a single connection carrying the requests back-to-back with
   the final byte of each released together. Fall back to N connections released
   at a shared instant, then to plain parallel delivery. Escalate only when the
   previous mode produced no divergence.
4. **Raise N.** Start at the smallest burst that could break the invariant (2 for
   a single-use artefact, the balance divisor for a bounded amount, one more than
   the quota for a counting limit). Double until the responses diverge or the
   server starts refusing on unrelated grounds — which is a different failure and
   must be told apart from success.
5. **Read the outcome, not the status code.** The interesting evidence is the
   set of final states: a second acceptance, a total that exceeds the bound, two
   resources where one was promised, a balance below zero. Capture the whole
   response set, not the last one.
6. **Confirm it is reproducible.** Repeat the exact burst; a one-off success is
   noise. Record the burst size, the synchronization mode and the request ids, so
   the finding is reproducible by someone else.
7. **Stabilize the window if it is narrow.** When the window is shorter than the
   payload, lengthen the server's own work rather than the client's timing: a
   larger body, an expensive sort or filter, a slow downstream call.

Signatures to expect: every request in the burst returning success; the
downstream state showing more consumption than the number of *distinct* requests
justifies; a refusal that switches from "already used" to a validation error once
one of the requests wins; balanced results when the burst is small and overshoot
once it is not.

## Forensic / Blue-Team Perspective (DFIR analyst)

A race abuse is only visible as a **burst**: several operations on one resource
inside the same clock tick, from one identity, often on one connection. Access
logs show identical timestamps at millisecond granularity across rows that
should be minutes apart; the store shows the invariant violated without any
individual request being malformed. Detection therefore lives in the rate and
the arrival pattern, not in the payload — a lock on the resource, a serializable
transaction or a per-account concurrency limit is the control, and the missing
one is what the logs reveal. Reconciliation against the business rule (coupons
consumed versus issued, balance movements versus withdrawals) is the audit that
finds what per-request logs cannot.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | The burst is delivered to an ordinary endpoint. |
| T1565.001 | Data Manipulation: Stored Data Manipulation | Concurrent commits leave persisted state outside the documented invariant. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — last-byte-synchronized bursts and parallel batches, each attempt stored with a request id
- Turbo Intruder or an equivalent raw driver, for gate-based synchronization on a single connection
- [jq](../tools/CTFTTOU-037.md) ([CTFTTOU-037](../tools/CTFTTOU-037.md)) — extracting the returned counter or balance from each response of the set

## References

- <https://portswigger.net/web-security/race-conditions>
- <https://portswigger.net/research/smashing-the-state-machine>
- <https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html> (concurrency controls, from the defensive side)
