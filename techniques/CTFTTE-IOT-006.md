# CTFTTE-IOT-006 — Embedded-binary exploitation behind device emulation (MIPS/ARM)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-006`](../countertechniques/CTFTCTE-IOT-006.md) — Emulate the service and exploit the embedded binary

---

## How the challenge author hides

The vulnerable service is an embedded binary — a MIPS or ARM build of a device daemon
(lighttpd CGI, a custom TCP service) — shipped either as a loose binary or inside the
firmware image. The player must first make it run (qemu-user with the right endianness,
libs and page size), then exploit a classic memory-corruption bug on an unfamiliar
architecture. The concealment is the emulation barrier plus the architecture: gadgets,
calling conventions and exploit primitives all differ from x86.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1210 | Exploitation of Remote Services | Device daemons exposed on the LAN are the remote-exploitation surface of IoT. |

## Tools

- [qemu](../tools/CTFTTOU-262.md)
- [ghidra](../tools/CTFTTOU-073.md)
- [pwntools](../tools/CTFTTOU-053.md)

## References

- <https://www.qemu.org/docs/master/user/main.html> (qemu-user)
- Add challenge write-up link
