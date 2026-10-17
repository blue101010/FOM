# CTFTTE-FOR-032 — Flag concealed in a haystack of near-identical files

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-032`](../countertechniques/CTFTCTE-FOR-032.md) — Isolate the outlier file by scalable comparison

---

## How the challenge author hides

The flag (or the one meaningful file) is buried inside a very large archive of thousands of
near-duplicate files — same size, same structure, mostly identical bytes — so that no single
file stands out and manual inspection is infeasible. The concealment is scale plus sameness:
grep for the flag format may miss an encoded fragment, and opening files one by one never
terminates. The intended solve is a comparison that is efficient at scale — hash every file
and keep the one whose content is unique, or diff against the common baseline — rather than
reading each file.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The meaningful data is hidden by surrounding it with a mass of near-identical decoy files. |

## Tools

- [diffutils / coreutils comparison set](../tools/CTFTTOU-286.md)
- [xxd / hexdump](../tools/CTFTTOU-055.md)

## References

- <https://github.com/blue101010/writeups/tree/main/2024/LEVELEFFECTCDA2024/Forensics/haystackzip> (Level Effect CDA 2024 "haystackzip")
