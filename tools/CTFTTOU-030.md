# CTFTTOU-030 — Rubeus

> **Tool ID:** `CTFTTOU-030`  
> **Related techniques/counters:** CTFTTE-FPN-017, CTFTCTE-FPN-017

## Description

Windows Kerberos abuse toolkit. `Rubeus.exe monitor` listens for incoming TGTs on a host with unconstrained delegation — the capture side of a printer-bug coercion — and prints or exports the tickets (base64 kirbi) for later reuse against the domain controller.

## Running on Linux (mono)

The release binary is a .NET Framework PE — on Kali run it as `mono Rubeus.exe ...` (or `wine`).
On a TTY, mono's console init reads the terminfo entry for `$TERM` and throws
`System.Exception: File must be smaller than 4K` whenever that file exceeds 4096 bytes — with
ncurses ≥ 6.5 that includes `xterm` and `xterm-256color`. Prefix the command with a small-entry
TERM instead: `TERM=tmux-256color mono Rubeus.exe ...` (`linux`, `screen`, `vt100`, `dumb` also
work). Piping stdout (`... | cat`) takes the non-TTY path and dodges the issue entirely.

## URL

<https://github.com/GhostPack/Rubeus>

## Related Techniques

CTFTTE-FPN-017, CTFTCTE-FPN-017
