# CTFTTE-JAL-004 — JavaScript browser-sandbox jail

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-004`](../countertechniques/CTFTCTE-JAL-004.md) — Traverse the prototype chain to escape

---

## How the challenge author hides

A sandboxed JavaScript eval context strips or proxies `window`, `Function`, `eval`, and dangerous globals, requiring prototype-chain or constructor traversal to reach native execution.

## ATT\&CK Complementarity

No ATT&CK equivalent. ATT&CK does not model JS sandbox-escape puzzle craft.

## Tools

- browser DevTools
- js-sandbox cheat references

## References

- Add challenge write-up link
