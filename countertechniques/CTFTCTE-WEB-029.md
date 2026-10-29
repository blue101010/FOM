# CTFTCTE-WEB-029 — Craft unnormalized raw request pairs and read the desync

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-029`](../techniques/CTFTTE-WEB-029.md) — Desynchronized request framing between edge and origin

---

## Offensive Recovery (CTF practitioner / solver)

Two implementations, one wire. The procedure is a differential test: send
deliberately ambiguous framing and read whether the **second** response belongs
to the request you sent or to one you did not.

1. **Confirm two hops exist.** Read the banners, error pages, `Via`, `Server` and
   timing behaviour; a direct origin and a proxied origin rarely answer
   identically. Keep a path straight to the origin if the challenge exposes one —
   it is the reference the desync is measured against.
2. **Establish the connection baseline.** One request, twice, on a **reused**
   connection. If the second response is not the expected one, framing is already
   ambiguous and the rest of the matrix narrows.
3. **Send bytes verbatim.** Use a client that does not normalise: no header
   reordering, no recomputed length, no merged duplicates. A convenience client
   rewrites exactly the field under test.
4. **Walk the framing matrix, one variable at a time.** `Content-Length` versus
   `Transfer-Encoding: chunked`, then chunked versus chunked with an odd chunk
   extension or a leading zero, then duplicate `Content-Length`, then an
   obs-folded header, then a bare line termination.
5. **Read the timing, not only the body.** A desync often shows first as a
   timeout on one variant and an immediate answer on another: the front end is
   waiting for bytes the origin has already consumed, or the reverse.
6. **Inject only a harmless prefix first.** Prove the smuggled request executes
   with a request that reveals itself — a route returning a distinguishable body —
   before attempting an action. Attribution before exploitation.
7. **Reuse the poisoned slot.** The smuggled prefix sits in front of the *next*
   request on that connection, which may be someone else's; on a shared
   challenge instance that also means the answer may arrive on a connection you
   did not open. Look for it.
8. **Stop at the first confirmed variant.** The failure mode of this technique is
   queue poisoning that breaks the instance for everyone, including your own
   later attempts; record the working variant and the reasoning, then leave the
   connection closed.

Signatures to expect: a `400` followed by a valid response on the same connection;
your second request answered by the response to the first; a timeout on exactly
one framing variant; a body containing a header line you never sent; success
against an internal route that no external path reaches.

## Forensic / Blue-Team Perspective (DFIR analyst)

Desync is a queue-integrity defect, so the evidence lives at the edge: requests
whose recorded length differs from the bytes received, responses delivered to a
connection that never asked for them, and one client's body appearing in another
client's response. Because the smuggled prefix is executed by the origin under
the origin's trust of the edge, application logs show a request that no edge log
records — the join between the two layers is the detection, and the mismatch is
the finding. Hardening is framing canonicalisation at the edge plus rejecting
ambiguous requests, not a request-body filter.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | The edge is exercised on its public interface and the origin executes the prefix. |
| T1557 | Adversary-in-the-Middle | The smuggled prefix rides in front of another party's request on a reused connection. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — raw byte sending and connection-reuse batches, with the exact bytes stored per attempt
- an interactive TCP client, for per-connection timing and manual framing
- a desync test harness, to walk the length/chunked matrix reproducibly

## References

- <https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn>
- <https://www.rfc-editor.org/rfc/rfc9112#section-6.3>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/15-Testing_for_HTTP_Request_Smuggling>
