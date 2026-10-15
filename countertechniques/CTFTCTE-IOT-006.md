# CTFTCTE-IOT-006 — Emulate the service and exploit the embedded binary

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-006`](../techniques/CTFTTE-IOT-006.md) — Embedded-binary exploitation behind device emulation (MIPS/ARM)

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify the architecture and endianness (`file`, ELF header) and the interpreter/libc
   dependencies (MIPS/ARM musl or uClibc builds differ from glibc).
2. Emulate with qemu-user: `qemu-mips{,el} -L <rootfs> ./service` — pull the rootfs from
   the firmware image (IOT-001) when libs are missing.
3. Reverse the service in Ghidra (MIPS/ARM calling conventions: argument registers
   `$a0-$a3` / `r0-r3`, delay slots on MIPS); locate the bug exactly as on x86.
4. Build the exploit with pwntools on the target architecture: ROP via gadgets in the
   binary or libc; mind that `syscall` conventions and bad bytes differ.
5. Validate: the payload executes on the emulated service and yields the flag or a shell.

## Forensic / Blue-Team Perspective (DFIR analyst)

Emulation-first analysis is also how responders triage captured device malware and
vulnerable daemons safely: stand up the binary in qemu, fuzz the exposed parser, and
reproduce the crash before touching production devices.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1210 | Exploitation of Remote Services | Device daemons exposed on the LAN are the remote-exploitation surface of IoT. |

## Tools

- [qemu](../tools/CTFTTOU-262.md)
- [ghidra](../tools/CTFTTOU-073.md)
- [pwntools](../tools/CTFTTOU-053.md)

## References

- <https://www.qemu.org/docs/master/user/main.html>
- Add challenge write-up link
