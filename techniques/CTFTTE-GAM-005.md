# CTFTTE-GAM-005 — Protocol sequence replay / race

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-005`](../countertechniques/CTFTCTE-GAM-005.md) — Record, replay, or race the server sequence precisely

---

## How the challenge author hides

The server validates a precise sequence or timing of game-protocol actions; the flag is only released when a specific state-machine path is triggered under strict timing constraints.

## ATT\&CK Complementarity

No ATT&CK equivalent. ATT&CK does not model game-protocol state-machine puzzle craft.

## Tools

- wireshark / tshark
- pwntools
- python threading

## References

- Add challenge write-up link
