# CTFTCTE-IOT-008 — Assemble the emulated board boot

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-008`](../techniques/CTFTTE-IOT-008.md) — Full-board boot gate (kernel + device tree + disk image)

---

## Offensive Recovery (CTF practitioner / solver)

1. Inventory the artifacts before booting anything: image format (`qemu-img info`), any
   kernel image, any `.dtb` file, and the boot partition contents (boot config, command
   line, dtb names) which identify the board family.
2. Pick the machine type to match the board the image was built for, and the CPU the
   kernel supports. For ARM evaluation boards, a kernel built for the emulator's machine
   is usually required — the device's own kernel often lacks the emulator's peripherals.
3. Clear the container friction first: convert to the format the emulator wants and resize
   to a power-of-two size when it refuses the image.
4. Boot with kernel, DTB and a `root=` pointing at the emulated disk device name — the
   device name changes with the bus (`/dev/sda2` for a disk on an emulated SCSI/SD
   controller, `/dev/mmcblk0p2` on real hardware). Watch the serial console.
5. When the kernel panics on root mount, read the partition list it prints and correct
   `root=`; the panic output is the diagnosis.
6. When no kernel is supplied, extract one from the image's boot partition or use a
   community kernel built for the emulator machine.
7. When the boot hangs silently, decompile the DTB with `dtc` and check the console/UART
   and disk nodes against the machine type.

## Forensic / Blue-Team Perspective (DFIR analyst)

Booting a seized image mutates it: work on a converted copy, snapshot the state, and record
the exact emulator invocation so the session is reproducible. Full-system emulation of a
device is standard lab practice for observing runtime behaviour that offline inspection
cannot reach, but every change made inside the emulated session must be reported as such.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1200 | Hardware Additions | The emulator replaces the physical device in the analysis loop; the pivot is the sandbox, not added hardware. |

## Tools

- [qemu](../tools/CTFTTOU-262.md)
- [qemu-img](../tools/CTFTTOU-444.md)
- [dtc](../tools/CTFTTOU-443.md)

## References

- <https://www.qemu.org/docs/master/system/invocation.html>
- <https://www.devicetree.org/specifications/>
