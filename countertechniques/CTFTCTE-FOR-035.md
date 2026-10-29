# CTFTCTE-FOR-035 — Convert, decrypt and map virtual-disk containers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-035`](../techniques/CTFTTE-FOR-035.md) — Virtual-disk container labyrinth

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify every layer with `file` before choosing a tool: an appliance archive is a
   POSIX tar (`tar -xvf` yields the `.ovf` descriptor, `.mf` manifest and `.vmdk` member);
   a qcow2 reports its version and encryption; a raw dump reports its partition table.
2. Convert members to one working format with `qemu-img convert` (`-f vmdk -O qcow2`,
   or `-O raw` when the next tool wants raw). Converting copies the image, which also
   protects the original.
3. Detect legacy qcow2 AES encryption via `qemu-img info` / `file` ("AES-encrypted").
   Decrypt by converting to another format — the converter prompts for the image password
   and no separate key file exists for that format; the password is the only secret.
4. Inspect the partition table (`fdisk -l`, `sfdisk -d`) and trust the start-sector
   offsets over CHS values: garbage CHS entries with sane offsets mean the table was
   scrambled, not the filesystems.
5. Map the partitions (`losetup -fP`, `kpartx -av`) and mount each one; when several
   images of the same disk exist, compare content hashes to find the authoritative copy.

## Forensic / Blue-Team Perspective (DFIR analyst)

Containers are views over the same evidence: convert to raw for imaging tools and keep the
original container for chain of custody. The qcow2 AES format is deprecated legacy —
record the password's provenance and the conversion command, because the decrypted copy
is a derived artifact. Partition-table anomalies are findings in themselves (tampering
indicator), not obstacles to repair silently.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1006 | Direct Volume Access | Recovery reads the disk through its container, below the operating system. |

## Tools

- [qemu-img](../tools/CTFTTOU-444.md)
- [losetup / kpartx](../tools/CTFTTOU-445.md)
- [binwalk](../tools/CTFTTOU-126.md)

## References

- <https://www.qemu.org/docs/master/interop/qemu-img.html>
- <https://gitlab.com/qemu-project/qemu/-/blob/master/docs/interop/qcow2.txt>
