# CTFTCTE-FOR-032 — Isolate the outlier file by scalable comparison

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-032`](../techniques/CTFTTE-FOR-032.md) — Flag concealed in a haystack of near-identical files

---

## Offensive Recovery (CTF practitioner / solver)

1. Do not read files individually. Reduce the haystack by content hash:
   `find . -type f -exec sha256sum {} + | sort | uniq -c -w64 | sort -n` — the line with
   count `1` (or the smallest counts) is the outlier whose bytes differ from the crowd.
2. If every file is unique but shares a common template, diff against a baseline instead:
   pick any file as reference and `cmp`/`diff` the rest, keeping only the one with a
   non-trivial delta. For fixed-size records, hash a byte range rather than the whole file.
3. When the difference is a single changed region, `xxd` the outlier and the baseline and
   compare the dumps to read the injected bytes directly.
4. This is the scalable equivalent of the original C++ comparison loop: hashing is O(n) over
   the corpus and never holds more than one file in memory, so it finishes on archives of
   tens of thousands of files.

## Forensic / Blue-Team Perspective (DFIR analyst)

The same hash-and-group pass is how analysts find the one tampered file in a large
deployment (known-good baseline diffing, NSRL hash filtering). The outlier-by-frequency
heuristic generalises: group by hash, investigate the rare bucket.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Recovery defeats concealment-by-volume by collapsing near-duplicates to the unique file. |

## Tools

- [diffutils / coreutils comparison set](../tools/CTFTTOU-286.md)
- [xxd / hexdump](../tools/CTFTTOU-055.md)
- [strings](../tools/CTFTTOU-200.md)

## References

- <https://github.com/blue101010/writeups/tree/main/2024/LEVELEFFECTCDA2024/Forensics/haystackzip>
