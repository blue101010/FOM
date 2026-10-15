# CTFTTE-IOT-001 — Vendor firmware image with hardcoded secrets

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-001`](../countertechniques/CTFTCTE-IOT-001.md) — Unpack the firmware image and grep the rootfs for secrets

---

## How the challenge author hides

The flag is a hardcoded secret inside a device firmware image: a credential, key or flag
string baked into the vendor squashfs, a config blob, or an embedded database. The image is
handed over as an opaque blob (or fetched off the device); the concealment is the packaging
itself — multiple filesystems, offsets and compression layers — plus the assumption the
player will not carve the rootfs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.001 | Valid Accounts: Default Accounts | Embedded firmware routinely bakes default accounts and keys into the rootfs. |

## Tools

- [binwalk](../tools/CTFTTOU-126.md)
- binwalk -e / unsquashfs, strings

## References

- <https://github.com/ReFirmLabs/binwalk>
- Add challenge write-up link
