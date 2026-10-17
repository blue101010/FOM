# CTFTTOU-284 — block explorers (Etherscan-style)

> **Tool ID:** `CTFTTOU-284`  
> **Related techniques/counters:** CTFTTE-BLK-004, CTFTCTE-BLK-004

## Description

Web UIs that index an EVM chain and expose its history without a local node: transaction
lists, input calldata (raw + decoded), event logs, internal calls and contract source
verification. Etherscan is the public-chain reference; CTF chains usually ship a
Blockscout instance for the same purpose. Use them for the read-only archaeology step —
browsing historical logs and calldata by address or topic — before scripting anything
with web3.py or cast.

## URL

<https://etherscan.io/> — self-hosted: <https://github.com/blockscout/blockscout>

## Related Techniques

CTFTTE-BLK-004, CTFTCTE-BLK-004
