# CTFTTOU-093 — bbot

> **Tool ID:** `CTFTTOU-093`  
> **Related techniques/counters:** CTFTCTE-OSI-008, CTFTTE-OSI-008

## Description

Recursive OSINT and attack-surface framework. `bbot` chains modules — name discovery (certificate
transparency, passive DNS, archive), resolution, HTTP probing, artefact extraction — and emits every
result as an **event** (`DNS_NAME`, `IP_ADDRESS`, `HTTP_RESPONSE`, `URL`, `STORAGE_BUCKET`, …), so one
scan walks from a seed domain to the forgotten subdomain that actually hosts the target.

For a CTF it is the chain automator (seed → names → hosts → URLs → artefacts), not the tool you reach
for when a single `dig` answers the question.

## URL

<https://github.com/blacklanternsecurity/bbot>

## Install / verify

```bash
bbot --version        # 3.0.2 at validation time, installed at ~/.local/bin/bbot
```

## Usage

```bash
# 0. offline discovery of what this build offers
bbot -lp              # presets (wayback, web, web-heavy, webbrute, waf-bypass, ...)
bbot -lf              # module flags (web, web-heavy, slow, invasive, portscan, download, ...)
bbot -l               # modules;  -lmo  module options;  -mh <module>  module help

# 1. non-intrusive web surface, the default entry point
bbot -t target.com -f web --json -o out/

# 2. same, explicitly excluding intrusive modules
bbot -t target.com -f web -ef invasive --json -o out/

# 3. archived URLs only (no active probing of the target)
bbot -t target.com -p wayback --json -o out/

# 4. explicit minimal module set
bbot -t target.com -m sslcert,robots,securitytxt --no-deps --json -o out/

# 5. rehearse: print the module pipeline, send nothing
bbot -t target.com -f web --dry-run
```

| Flag | Effect |
|---|---|
| `-t TARGET` / `-s SEED` | seed targets (domain, IP, range, URL); `-s` for in-scope relations only |
| `-f FLAG` | select modules by flag (`web` is documented **non-intrusive**) |
| `-ef FLAG` / `-rf FLAG` | exclude / require modules by flag (`-ef invasive`, `-rf passive`) |
| `-p PRESET` | run a preset (`wayback`, `web`, `web-heavy`, `webbrute*`, `waf-bypass`, …) |
| `-m MODULE` / `-em MODULE` | explicit module selection / exclusion |
| `-o DIR` + `--json` | output directory, one JSON event per line (NDJSON) |
| `--dry-run` | print the pipeline without sending traffic |
| `--no-deps` / `--install-all-deps` | skip / pre-install module dependencies |
| `-n NAME` | scan name (output subdirectory) |

## Notes

- **First run has side effects**: it creates `~/.config/bbot/bbot.yml` and `secrets.yml`, and it may
  try to install module dependencies. On a fresh box use `--no-deps`, or pre-install with
  `--install-all-deps`, so a scan does not become a toolchain build.
- **Flag discipline is the CTF-relevant part**: `-f web` is non-intrusive, `-ef invasive` removes
  destructive modules, and the `webbrute*`/`portscan` families are loud by design. When the challenge
  says "be gentle", restrict to a flag set and prove it with `--dry-run`.
- Output is NDJSON: `jq -r 'select(.type=="DNS_NAME") | .data' out/*.ndjson` is how you read it, and
  `STORAGE_BUCKET` / `URL_UNVERIFIED` events are the usual pivot points toward other FOM pairs.
- Presets are dependency graphs, not single modules: `-lp` shows the module count and the flags each
  preset pulls in — check that count before running one on infrastructure you do not own.
- Siblings, for when one answer is enough: `assetfinder`/`amass` (names), `dnsx` (resolution),
  `crt.sh` (certificate transparency).

## Related Techniques

CTFTCTE-OSI-008, CTFTTE-OSI-008
