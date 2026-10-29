# CTFTTE-IOT-008 — Full-board boot gate (kernel + device tree + disk image)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-008`](../countertechniques/CTFTCTE-IOT-008.md) — Assemble the emulated board boot

---

## How the challenge author hides

The flag or the next stage exists only at runtime: it is printed by a boot script, a login
banner or a service that starts when the device's whole operating system boots. The artifact
is therefore a complete disk image (raw, qcow2, an SD-card dump) rather than a loose binary,
and for ARM boards the player also needs a kernel image and a flattened device tree blob
(`.dtb`) that the emulator can consume. The concealment is the assembly work, not a bug:
the machine type, CPU, kernel, DTB and `root=` boot argument must all match, and the emulator
adds its own friction — image sizes that must be a power of two, kernels that must be built
for the emulator's board rather than the real device, root devices that change name between
real hardware (`mmcblk0p2`) and the emulated bus (`sda2`). Distinct from CTFTTE-IOT-006,
where only a single service binary has to run under user-mode emulation, and from
CTFTTE-IOT-001, where the image is unpacked offline and never booted.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1200 | Hardware Additions | The emulator stands in for the physical device; ATT&CK has no technique for defensive full-system emulation, so the sandbox pivot is anchored to the closest hardware technique. |

## Tools

- [qemu](../tools/CTFTTOU-262.md)
- [qemu-img](../tools/CTFTTOU-444.md)
- [dtc](../tools/CTFTTOU-443.md)

## Indicators

- a whole-disk or SD image with a boot partition and a Linux rootfs, and no single interesting binary
- an ARM/MIPS board story where a kernel image and a `.dtb` file are handed over, referenced, or absent on purpose
- boot attempts fail with `could not load kernel`, `Couldn't open dtb file`, `Invalid SD card size` or `Unable to mount root fs` until the right machine/kernel/DTB combination is assembled
- the objective is described as something the device *shows* or *runs* at boot, not a file that exists in the image

## References

- <https://www.qemu.org/docs/master/system/invocation.html>
- <https://www.devicetree.org/specifications/>
- <https://github.com/dhruvvyas90/qemu-rpi-kernel>
