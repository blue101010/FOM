# CTFTTMOU-003 — MDB-MCP (GDB/LLDB)

> **MCP ID:** `CTFTTMOU-003`  
> **Related tool:** [`CTFTTOU-163`](../tools/CTFTTOU-163.md) — gdb (also [`CTFTTOU-291`](../tools/CTFTTOU-291.md) — lldb)  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-002, CTFTCTE-PWN-002, CTFTTE-PWN-003, CTFTCTE-PWN-003, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-007, CTFTCTE-PWN-007, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012, CTFTTE-REV-001, CTFTCTE-REV-001

## Description

MCP server (stdio, Python) that gives AI agents a real debugger: it drives GDB through
GDB/MI and LLDB through its Python API, one session per binary. Five MCP tools:

- `debugger_status` — which debuggers work (and why not), open sessions.
- `debugger_start` — start a `gdb`/`lldb` session, optionally loading a program + args.
- `debugger_command` — any native command (`break main`, `run < in.bin`, `bt`,
  `x/16gx $rsp`, `register read`); resuming commands wait up to `timeout` (≤ 600 s).
- `debugger_interrupt` — Ctrl-C a running target.
- `debugger_terminate` — kill the target and close the session.

GDB loads `~/.gdbinit`, and `MDB_GDB_PATH` selects another gdb: pointing it at the
pwndbg launcher (`gdb-pwndbg`) exposes pwndbg commands (`checksec`, `telescope`,
`vmmap`, `cyclic`) over MCP. Installed in Kali WSL from a reviewed, pinned commit
(`5d03b25`, v0.2.0) into `~/.venvs/mdbmcp`; registered as `mdb` (vanilla gdb + lldb)
and `mdb-pwndbg` in `.mcp.json`, `.vscode/mcp.json`, `.codex/config.toml`.

## Start / Stop / Check

MDB-MCP is a stdio MCP server: the MCP client launches it on demand through WSL.

```sh
# Check prerequisites (Kali WSL): debuggers, matching python3-lldb, server version
gdb --version | head -1; lldb --version; dpkg -l python3-lldb | tail -1
~/.venvs/mdbmcp/bin/mdb-mcp --version
# Install / upgrade from the reviewed clone (never uvx from a moving git ref)
git -C ~/TOOLS/MDB-MCP log --oneline -1
uv venv ~/.venvs/mdbmcp && uv pip install --python ~/.venvs/mdbmcp/bin/python ~/TOOLS/MDB-MCP

# Start: the client runs, from Windows
#   wsl.exe -d kali-linux -e /home/fhp/.venvs/mdbmcp/bin/mdb-mcp
#   wsl.exe -d kali-linux -e env MDB_GDB_PATH=/home/fhp/.local/bin/gdb-pwndbg /home/fhp/.venvs/mdbmcp/bin/mdb-mcp
claude mcp add mdb -- wsl.exe -d kali-linux -e /home/fhp/.venvs/mdbmcp/bin/mdb-mcp

# Check: tools/list exposes the five debugger_* tools; debugger_status shows
#   gdb: available - GNU gdb ... / lldb: available - lldb version ...
# Smoke test: make -C ~/TOOLS/MDB-MCP/examples, then debugger_start
#   {debugger: "gdb", program: "/home/fhp/TOOLS/MDB-MCP/examples/crash"} -> run
#   -> SIGSEGV in main () at crash.c:24 (same with lldb)

# Stop: debugger_terminate each session; the server exits with the client
claude mcp remove mdb
```

Agents without MCP-client support drive the stdio protocol directly: spawn the command
above, send `initialize` → `notifications/initialized` → `tools/call` over
newline-delimited JSON. From Git Bash, set `MSYS_NO_PATHCONV=1` or `/home/...` arguments
to `wsl.exe` are rewritten to `C:/Program Files/Git/home/...`.

## Notes

- `ptrace_scope=1` in Kali: debug programs the session launches; attaching fails.
- The target cannot read the keyboard: feed input with `run < file` / `process launch -i file`.
- gdb `shell`/`python` and lldb `script`/`platform shell` run commands as the user, and
  the debugged binary runs for real: keep approval on `debugger_command`, Kali only.

## URL

<https://github.com/smadi0x86/MDB-MCP>

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-002, CTFTCTE-PWN-002, CTFTTE-PWN-003, CTFTCTE-PWN-003, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-007, CTFTCTE-PWN-007, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012, CTFTTE-REV-001, CTFTCTE-REV-001
