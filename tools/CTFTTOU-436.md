# CTFTTOU-436 — ScoutSuite and Prowler

> **Tool ID:** `CTFTTOU-436`  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## Description

Multi-cloud, read-only posture scanners. They enumerate what the held identity can see and grade it
against a rule set, which in a challenge answers two questions cheaply:

- **What exists?** The inventory section is a resource map (accounts, storage, identities, keys, compute)
  produced without writing anything — a fast way to find the one resource the story describes.
- **What is flagged?** Every rule that fires is a candidate misconfiguration; the flags are ranked, so the
  author's weakened setting usually appears near the top.

ScoutSuite focuses on a browsable report; Prowler focuses on per-check findings with machine-readable
output. Either is enough — prefer the one already installed, and treat the output as a lead list rather
than an answer. Both require the provider's own credentials/session to be configured first, and both are
only as read-only as their check set: confirm the rule you are about to run does not mutate.

## URL

- <https://github.com/nccgroup/ScoutSuite>
- <https://github.com/prowler-cloud/prowler>

## Installation

```bash
pipx install scoutsuite                    # PEP 668-safe on Kali
uv tool install prowler --python 3.12      # prowler pins numpy 2.2.x, which ships no cp314 wheel:
                                           # pipx/uv on Kali's Python 3.14 attempt a C++ build and fail
scout --help && prowler --version
```

Provider support in Prowler has changed across major versions: check `prowler <provider> --help` for the
installed build before scripting a run.

## Usage

```bash
# ScoutSuite against an existing CLI session
scout azure --cli --report-dir ./scoutsuite

# Prowler, scanning the current CLI context
prowler azure --az-cli-auth --output-formats json-ocsf

# narrow to one service when the story is specific
scout azure --cli --services storage --report-dir ./scoutsuite-storage
```

Pitfalls: a partial inventory usually means the identity lacks reader rights at a scope, not that the
resource is absent; the report embeds resource identifiers that later commands need verbatim; scanning a
large tenant can outlast a challenge timer, so scope by service or subscription.

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-008, CTFTCTE-CLD-008

## References

- [ScoutSuite repository](https://github.com/nccgroup/ScoutSuite)
- [Prowler repository](https://github.com/prowler-cloud/prowler)
- [Azure security benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/)
