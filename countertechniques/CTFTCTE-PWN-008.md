# CTFTCTE-PWN-008 — Generate/encode shellcode (alphanumeric, null-free)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-008`](../techniques/CTFTTE-PWN-008.md) — Shellcode craft & encoding constraints

---

## Offensive Recovery (CTF practitioner / solver)

Generate or encode shellcode (msfvenom, custom encoders) and deliver it through the constrained path.

## Forensic / Blue-Team Perspective (DFIR analyst)

Encoded shellcode shows the same encoder fingerprints in memory dumps as in exploit artifacts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1055 | Process Injection | Shellcode delivery mirrors injection payloads. |

## Tools

- msfvenom
- pwntools shellcraft
- nasm

## References

- <https://github.com/Gallopsled/pwntools>

