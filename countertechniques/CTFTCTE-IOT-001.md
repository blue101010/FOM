# CTFTCTE-IOT-001 — Unpack the firmware image and grep the rootfs for secrets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-001`](../techniques/CTFTTE-IOT-001.md) — Vendor firmware image with hardcoded secrets

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify the image type and embedded filesystems: `binwalk <image>`, note offsets and
   compression (gzip/lzma/xz/squashfs/cramfs).
2. Extract recursively (`binwalk -e`, then `unsquashfs` on the carved rootfs) until a real
   filesystem tree appears.
3. Grep the tree for secrets: credentials, private keys, URLs, `flag{`-like strings and
   shadow/passwd entries; check `/etc`, init scripts and bundled config databases.
4. Validate against the device: recovered credentials should log into the admin interface
   or unlock the next stage.

## Forensic / Blue-Team Perspective (DFIR analyst)

Hardcoded secrets in shipped firmware are a supply-chain finding: inventory every released
image, extract the rootfs the same way an attacker would, and alert on default accounts and
embedded keys. CWE-798 (Use of Hard-coded Credentials) is the standard anchor.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.001 | Valid Accounts: Default Accounts | Embedded firmware routinely bakes default accounts and keys into the rootfs. |

## Tools

- [binwalk](../tools/CTFTTOU-126.md)
- unsquashfs / strings

## References

- <https://github.com/ReFirmLabs/binwalk>
- Add challenge write-up link
