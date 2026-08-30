# CTFTTE-PWN-008 — Shellcode craft & encoding constraints

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-008`](../countertechniques/CTFTCTE-PWN-008.md) — Generate/encode shellcode (alphanumeric, null-free)

---

## How the challenge author hides

The exploit must deliver shellcode under constraints: no nulls, alphanumeric only, or length limits.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1055 | Process Injection | Shellcode delivery mirrors injection payloads. |

## Tools

- msfvenom
- pwntools shellcraft
- nasm

## References

- https://github.com/Gallopsled/pwntools
- Add challenge write-up link
