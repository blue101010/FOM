# CTFTTOU-101 — trufflehog

> **Tool ID:** `CTFTTOU-101`  
> **Related techniques/counters:** CTFTCTE-OSI-005, CTFTCTE-OSI-006, CTFTTE-OSI-005, CTFTTE-OSI-006

## Description

Secret scanner (v3) that walks a source — git history, GitHub/GitLab organisations, a filesystem, S3,
Docker layers — matches content against hundreds of credential detectors, and optionally **verifies**
each hit against the provider's API. In OSINT it is the systematic form of "the secret was committed
and later removed": the working tree is clean, the history is not.

It is a *source* tool, not a *search-engine* tool: it reads what you point it at, so it complements
code search rather than replacing it.

## URL

<https://github.com/trufflesecurity/trufflehog>

## Install / verify

```bash
trufflehog --version          # a locally built binary prints "trufflehog dev"
```

## Usage

```bash
# never run it bare: with no argument it opens an interactive wizard
trufflehog git https://github.com/owner/repo.git --json | jq -r '.DetectorName + "\t" + .Raw'

# a repository shipped inside a challenge artefact (bundle, backup, disk image extract)
trufflehog filesystem ./extracted/ --json | jq .

# a whole organisation or a single repo through the host's API
trufflehog github --org=target-org --json | jq -r '[.DetectorName, .SourceMetadata.Data.Github.link] | @tsv'

# full history of a mirror when the upstream was force-pushed
git clone --mirror https://github.com/owner/repo.git repo.git
trufflehog git "file://$PWD/repo.git" --json | jq -r '.DetectorName'
```

Flags worth knowing (from `trufflehog git --help`):

| Flag | Effect |
|---|---|
| `-j`, `--json` | one JSON object per finding; pipe to `jq` |
| `--json-legacy` | pre-v3 layout, only for git/gitlab/github sources |
| `--no-verification` | do not call the provider — **mandatory offline**, and avoids touching a live credential |
| `--results=verified,unknown,unverified` | filter by verification state; the default prints everything it found |
| `--concurrency=N` | worker count when scanning a large history |
| `--github-actions`, `--sarif` | CI-shaped output, rarely useful for a CTF |

## Notes

- **The wizard trap**: a bare `trufflehog` drops into an interactive menu (scan wizard, secret
  permissions, docs). In a script or an agent session always give a source subcommand and a flag.
- **Verification leaves the box.** By default a hit may be checked against the real provider API: that
  is network egress and, on a live credential, an interaction with someone else's account. In a CTF —
  and always when the target is not yours to poke — run `--no-verification` and read `.Raw` /
  `.DetectorName` yourself.
- JSON fields emitted per finding: `DetectorName`, `DetectorType`, `Raw`, `RawV2`, `Redacted`,
  `SecretParts`, `Verified`, `SourceMetadata`, `ExtraData`. `Raw` is the secret you need; `Redacted` is
  what belongs in a report; `SourceMetadata` is what turns a finding into a timeline entry.
- **Provider-documented example credentials are allowlisted and never fire** — the well-known
  placeholder AWS keypair is ignored on purpose. If a test scan finds nothing, check that the sample is
  not an example value before assuming the scanner is broken.
- Findings change the exit code, so do not chain a scan into a `&&` pipeline that must keep running;
  capture the JSON first, then judge.
- Detectors overlap with `gitleaks` (separate sheet): trufflehog is broader and can verify, gitleaks is
  faster and rule-configurable. A CTF usually needs one, not both.

## Related Techniques

CTFTCTE-OSI-005, CTFTCTE-OSI-006, CTFTTE-OSI-005, CTFTTE-OSI-006
