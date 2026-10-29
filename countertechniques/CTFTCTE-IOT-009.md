# CTFTCTE-IOT-009 — Mount the rootfs offline and reset or crack the credential

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-009`](../techniques/CTFTTE-IOT-009.md) — Offline credential reset on a mounted rootfs

---

## Offensive Recovery (CTF practitioner / solver)

1. Map the image's partitions without booting it: `losetup -fP` on a raw image, or
   `kpartx -av` on a device-mapper node, then identify each partition with `file -s`.
2. Mount the rootfs partition read-write on a copy of the image and locate the credential
   store (`/etc/shadow` for Linux). Keep a backup of the file before touching it.
3. Choose the path the objective wants:
   - the objective is *access* — blank the hash field (everything between the first and
     second colon) for the target account, or replace it with a hash of a known password;
   - the objective is *the plaintext itself* — copy the hash out and crack it offline
     (CTFTCTE-CRY-012); a known external format of the plaintext collapses the mask.
4. Unmount cleanly, boot the image, and log in with the reset or cracked credential.
5. If the objective is a runtime artifact (banner, login script), capture it from the
   booted session rather than hunting for it in the files.

## Forensic / Blue-Team Perspective (DFIR analyst)

Editing a credential store is evidence tampering on the original: always operate on a
copy, hash before and after, and document the change. In DFIR the same offline mount yields
the password hashes for auditing without any reset — the reset path exists only when the
analysis goal is to observe the device's authenticated behaviour.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1003 | OS Credential Dumping | The credential store is read from the mounted image, no device execution needed. |
| T1078 | Valid Accounts | The reset prepares a valid account; the login is its use. |

## Tools

- [losetup / kpartx](../tools/CTFTTOU-445.md)
- [qemu-img](../tools/CTFTTOU-444.md)
- [hashcat](../tools/CTFTTOU-011.md)

## References

- <https://man7.org/linux/man-pages/man8/losetup.8.html>
- <https://man7.org/linux/man-pages/man5/shadow.5.html>
