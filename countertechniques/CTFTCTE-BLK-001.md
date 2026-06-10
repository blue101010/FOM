# CTFTCTE-BLK-001 — Read contract storage slots directly

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-001`](../techniques/CTFTTE-BLK-001.md) — Private storage-variable concealment

---

## Offensive Recovery (CTF practitioner / solver)

Read the storage slot directly from the node since on-chain storage is public.

## Forensic / Blue-Team Perspective (DFIR analyst)

Slot reads demonstrate that on-chain confidentiality cannot rely on visibility modifiers.

## Tools

- web3.py
- cast (foundry)
- eth_getStorageAt

## References

- https://book.getfoundry.sh/
- Add challenge write-up link