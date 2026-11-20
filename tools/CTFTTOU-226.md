# CTFTTOU-226 — ScoutSuite

> **Tool ID:** `CTFTTOU-226`  
> **Related techniques/counters:** (referenced by FOM entries)

## Description

Multi-cloud security auditing tool. Pure Python and slow (API-crawl bound) — under CTF
time pressure prefer [CTFTTOU-221 cloudfox](CTFTTOU-221.md) (Go, prebuilt binary).
Install on this box into the shared venv, not pipx:
`~/.venvs/ctfcloud/bin/pip install scoutsuite` (the local PyPI mirror may lack it).

## URL

<https://github.com/nccgroup/ScoutSuite>

## Related Techniques

(referenced by FOM entries)

## Skills

- [CTFTSKL-019 ctf-cloud-aws](../skills/CTFTSKL-019.md) — broad read-only posture dump
