# TODO — Suggested techniques & counter-techniques inferred


> Every suggestion below is a candidate **pair** (technique + counter-technique) following the
> same naming/ID rules as the existing corpus. Nothing here is added yet — this is the backlog.

## How to promote an entry (from CORRELATION.md)

1. Pick a category below — never `MSC`, never a new catch-all.
2. Create `techniques/CTFTTE-<CAT>-NNN.md` **and** `countertechniques/CTFTCTE-<CAT>-NNN.md`
   (same `NNN`), each with the `## Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).
3. Add the row to `tactics/CTFT-TA-<CAT>.md`.
4. Re-render and re-index:

```bash
python v2/render_taxonomy_docs.py --write
python v2/catalog_audit.py --write --write-index --write-catalog --check
```

## A–N. Promoted into the corpus (2026-08-30)

All backlog pairs below were created as real entries via `v2/create_todo_entries.py`,
and `CORRELATION.md` / `HIERARCHY.md` / `index.json` were re-rendered (161 pairs, 19 active tactics).

| Tactic | Created IDs |
| --- | --- |
| SDR | `CTFTTE`/`CTFTCTE-SDR-001` |
| HWR | `HWR-001`, `HWR-002` (tactic promoted from reserved to active) |
| NET | `NET-001..007` (new tactic `CTFT-TA-NET`) |
| FOR | `FOR-019..026` |
| REV | `REV-006..009` |
| PWN | `PWN-006..008` |
| CRY | `CRY-008..013` |
| STE | `STE-010`, `STE-011` |
| WEB | `WEB-010..017` |
| OSI | `OSI-006..008` |
| CLD | `CLD-006..008` |
| AIM | `AIM-006`, `AIM-007` |
| FPN | `FPN-008..010` |
| GAM | `GAM-006` |
| COD | `COD-006`, `COD-007` |
| JAL | `JAL-006` |

## O. Remaining / cross-cutting

- **`to_categorize/to_categorize.md`** still lists open items: base64-in-pcap (→ FOR/NET), VBA-macro
  strings in `.docm` (→ FOR-024-adjacent), rMQR (covered by FOR-012), corrupted-JPEG extra bytes
  before `0xd9` (→ FOR-019), strings-in-ELF (covered by FOR-017).
- Consider promoting tool notes (`network/pcap-bloodhound`, `stegano/*`, `database/enumredis.py`)
  into the v2 `tools.json` catalogue (TOOL-* entries) as the typed slice generalizes beyond Forensics.
- Wi-Fi (`wifi/`) can join `SDR` (RF domain) or stay in `NET` — decide before promoting NET-004;
  keep ATT&CK anchors per-entry, not per-tactic.
- `sdr_RF/` also documents Gqrx / pulseaudio-WSL tooling; fold it into `tools/` and `v2/tools.json`
  when SDR-001 is promoted.
