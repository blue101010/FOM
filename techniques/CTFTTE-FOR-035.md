# CTFTTE-FOR-035 — Virtual-disk container labyrinth

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-035`](../countertechniques/CTFTCTE-FOR-035.md) — Convert, decrypt and map virtual-disk containers

---

## How the challenge author hides

The evidence is a full-disk image wrapped in one or more virtualization containers: an
appliance archive (a tar holding a `.ovf` descriptor, `.mf` manifest and `.vmdk` member),
a qcow2 image encrypted with the legacy qcow2 AES format, a raw dump whose partition table
carries garbage or misleading entries, or the same disk shipped in several formats where
only one is current. The concealment is format friction: each layer needs a different
converter, the encrypted qcow2 refuses every filesystem tool until it is decrypted with its
password, and partition offsets must be mapped before any carving or mounting applies.
Distinct from CTFTTE-FOR-020 (a LUKS volume inside a filesystem) and CTFTTE-FOR-021
(LVM fragment reassembly): here the outermost obstacle is the virtualization container
itself, not a volume manager or an encrypted filesystem.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1006 | Direct Volume Access | The recovery reads the disk through its container instead of through the operating system that owns it. |

## Tools

- [qemu-img](../tools/CTFTTOU-444.md)
- [losetup / kpartx](../tools/CTFTTOU-445.md)
- [binwalk](../tools/CTFTTOU-126.md)

## Indicators

- `file` reports an appliance archive as a POSIX tar, with `.ovf`/`.mf`/`.vmdk` members inside
- `qemu-img info` or `file` reports a qcow2 image as AES-encrypted (v2/v3 legacy format)
- an emulator rejects the image (`Invalid SD card size`, unrecognized format) or the partition table parses to absurd sizes while the filesystems are intact at their offsets
- several images of the same disk in different formats, with no statement of which one is authoritative

## References

- <https://www.qemu.org/docs/master/interop/qemu-img.html>
- <https://gitlab.com/qemu-project/qemu/-/blob/master/docs/interop/qcow2.txt>
- <https://www.dmtf.org/standards/ovf>
