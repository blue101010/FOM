# CTFTCTE-WEB-014 — Intercept and decode WebSocket traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-014`](../techniques/CTFTTE-WEB-014.md) — WebSocket message hiding

---

## Offensive Recovery (CTF practitioner / solver)

Intercept the WS upgrade and frames (Burp/Chrome), replay and decode the messages.

Work at two levels, because they fail differently. At the **stream** level the
question is which upgrade produced the channel: a WebSocket only exists in the
recorded history if the upgrade itself was proxied, so an endpoint that appears
to do nothing in HTTP may still own the channel that matters. At the **frame**
level the question is which message carried the payload: list the frames per
stream in order, decode each independently, and treat a frame that differs from
its neighbours as the candidate. Replay by mutating one frame on an established
socket rather than replaying the handshake — the session state the server built
during the upgrade is not reproducible from the first frame alone.

## Forensic / Blue-Team Perspective (DFIR analyst)

WebSocket sessions are full-duplex artifacts; frame capture requires the upgrade context.
Proxies that record only HTTP exchanges lose the frames, so an investigation that
sees the upgrade but no messages should treat the gap as a collection defect, not
as an absence of activity.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071.001 | Web Protocols | Hidden channels over web protocols. |

## Tools

- [Caido (caido-cli and caido-mcp-server)](../tools/CTFTTOU-441.md) ([CTFTTOU-441](../tools/CTFTTOU-441.md)) — stream and frame listing from recorded traffic, frames addressable individually
- Burp Suite
- Chrome devtools
- websocat

## References

- <https://github.com/vi/websocat>
- Add challenge write-up link
