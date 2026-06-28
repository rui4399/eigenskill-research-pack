#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path

from huggingface_hub import snapshot_download


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a Hugging Face snapshot into an explicit local directory.")
    parser.add_argument("--repo-id", required=True)
    parser.add_argument("--local-dir", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--revision", default="main")
    parser.add_argument("--max-workers", type=int, default=8)
    args = parser.parse_args()

    args.local_dir.mkdir(parents=True, exist_ok=True)
    args.cache_dir.mkdir(parents=True, exist_ok=True)

    print(f"repo_id={args.repo_id}", flush=True)
    print(f"revision={args.revision}", flush=True)
    print(f"local_dir={args.local_dir}", flush=True)
    print(f"cache_dir={args.cache_dir}", flush=True)
    print(f"HF_HOME={os.environ.get('HF_HOME', '')}", flush=True)
    print(f"HF_HUB_CACHE={os.environ.get('HF_HUB_CACHE', '')}", flush=True)
    print(f"TMPDIR={os.environ.get('TMPDIR', '')}", flush=True)

    path = snapshot_download(
        repo_id=args.repo_id,
        revision=args.revision,
        local_dir=str(args.local_dir),
        cache_dir=str(args.cache_dir),
        max_workers=args.max_workers,
        local_files_only=False,
    )
    print(f"snapshot_path={path}", flush=True)


if __name__ == "__main__":
    main()
