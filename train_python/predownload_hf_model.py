#!/usr/bin/env python3
from __future__ import annotations

"""Pre-download a Hugging Face model and record cache/download evidence.

This helper exists because stronger-model experiments can fail before any PPL
metric is produced. It records the cache state before and after
snapshot_download so failed downloads are auditable instead of being confused
with model results.
"""

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

try:
    from huggingface_hub import snapshot_download
except ModuleNotFoundError:
    snapshot_download = None


def repo_cache_dir(cache_root: Path, repo_id: str) -> Path:
    return cache_root / ("models--" + repo_id.replace("/", "--"))


def default_cache_root() -> Path:
    hf_home = os.environ.get("HF_HOME")
    if hf_home:
        return Path(hf_home) / "hub"
    return Path.home() / ".cache" / "huggingface" / "hub"


def dir_size(path: Path) -> int:
    if not path.exists():
        return 0
    total = 0
    for item in path.rglob("*"):
        if item.is_file():
            try:
                total += item.stat().st_size
            except OSError:
                pass
    return total


def cache_audit(cache_root: Path, repo_id: str) -> dict[str, Any]:
    root = repo_cache_dir(cache_root, repo_id)
    files = []
    incomplete = []
    if root.exists():
        for item in root.rglob("*"):
            if not item.is_file():
                continue
            try:
                stat = item.stat()
            except OSError:
                continue
            rel = str(item.relative_to(root)).replace("\\", "/")
            row = {
                "path": rel,
                "bytes": stat.st_size,
                "mtime": stat.st_mtime,
            }
            files.append(row)
            if rel.endswith(".incomplete"):
                incomplete.append(row)
    files.sort(key=lambda row: row["bytes"], reverse=True)
    incomplete.sort(key=lambda row: row["bytes"], reverse=True)
    return {
        "cache_root": str(cache_root),
        "repo_cache_dir": str(root),
        "exists": root.exists(),
        "total_bytes": dir_size(root),
        "file_count": len(files),
        "incomplete_count": len(incomplete),
        "largest_files": files[:10],
        "incomplete_files": incomplete[:10],
    }


def parse_patterns(text: str) -> list[str] | None:
    if not text:
        return None
    values = [item.strip() for item in text.split(",") if item.strip()]
    return values or None


def markdown_report(result: dict[str, Any]) -> str:
    after = result["after"]
    lines = [
        "# Hugging Face Model Predownload Report",
        "",
        f"Model: `{result['model']}`",
        f"Started: `{result['started_at']}`",
        f"Elapsed seconds: `{result['elapsed_sec']:.2f}`",
        f"Status: `{result['status']}`",
        f"Cache root: `{after['cache_root']}`",
        "",
        "## Cache State",
        "",
        "| metric | before | after |",
        "|---|---:|---:|",
        f"| total bytes | {result['before']['total_bytes']} | {after['total_bytes']} |",
        f"| file count | {result['before']['file_count']} | {after['file_count']} |",
        f"| incomplete files | {result['before']['incomplete_count']} | {after['incomplete_count']} |",
        "",
        "## Largest After Files",
        "",
        "| bytes | path |",
        "|---:|---|",
    ]
    for item in after["largest_files"]:
        lines.append(f"| {item['bytes']} | `{item['path']}` |")
    if after["incomplete_files"]:
        lines.extend(["", "## Incomplete Files", "", "| bytes | path |", "|---:|---|"])
        for item in after["incomplete_files"]:
            lines.append(f"| {item['bytes']} | `{item['path']}` |")
    if result.get("error"):
        lines.extend(["", "## Error", "", "```text", str(result["error"]), "```"])
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A `success` status means `snapshot_download` completed and the cache",
            "audit found no `.incomplete` blobs for this repo. It does not mean any",
            "quantization or PPL evaluation has run. A `failed` or",
            "`incomplete_cache` status is a download/cache blocker and must not be",
            "reported as a model-quality result.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--revision", default="")
    parser.add_argument("--cache-dir", default="")
    parser.add_argument("--allow-patterns", default="", help="comma-separated patterns passed to snapshot_download")
    parser.add_argument("--ignore-patterns", default="", help="comma-separated patterns passed to snapshot_download")
    parser.add_argument("--max-workers", type=int, default=4)
    parser.add_argument("--etag-timeout", type=float, default=30.0)
    parser.add_argument("--token-env", default="HF_TOKEN")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--out-json", default="outputs/hf_model_predownload_summary.json")
    parser.add_argument("--out-md", default="outputs/hf_model_predownload_report.md")
    args = parser.parse_args()

    if snapshot_download is None:
        raise SystemExit("This script requires huggingface_hub in the active Python environment.")

    cache_root = Path(args.cache_dir) if args.cache_dir else default_cache_root()
    started = time.strftime("%Y-%m-%d %H:%M:%S")
    before = cache_audit(cache_root, args.model)
    token_value = os.environ.get(args.token_env)
    token_arg: bool | str | None = token_value if token_value else None
    result: dict[str, Any] = {
        "model": args.model,
        "revision": args.revision or None,
        "started_at": started,
        "cache_dir_arg": str(cache_root),
        "allow_patterns": parse_patterns(args.allow_patterns),
        "ignore_patterns": parse_patterns(args.ignore_patterns),
        "max_workers": args.max_workers,
        "etag_timeout": args.etag_timeout,
        "token_env": args.token_env,
        "token_present": bool(token_value),
        "local_files_only": args.local_files_only,
        "dry_run": args.dry_run,
        "before": before,
    }
    t0 = time.time()
    try:
        path = snapshot_download(
            repo_id=args.model,
            revision=args.revision or None,
            cache_dir=cache_root,
            allow_patterns=parse_patterns(args.allow_patterns),
            ignore_patterns=parse_patterns(args.ignore_patterns),
            max_workers=args.max_workers,
            etag_timeout=args.etag_timeout,
            token=token_arg,
            local_files_only=args.local_files_only,
            dry_run=args.dry_run,
        )
        result["status"] = "success"
        result["snapshot_path"] = str(path)
    except Exception as exc:  # noqa: BLE001 - error text is the audit payload.
        result["status"] = "failed"
        result["error"] = f"{type(exc).__name__}: {exc}"
    result["elapsed_sec"] = time.time() - t0
    result["after"] = cache_audit(cache_root, args.model)
    if result["status"] == "success" and result["after"]["incomplete_count"] > 0:
        result["status"] = "incomplete_cache"
        result["error"] = (
            f"snapshot_download returned a path, but cache audit found "
            f"{result['after']['incomplete_count']} incomplete blob(s)."
        )

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "status": result["status"], "after_bytes": result["after"]["total_bytes"], "incomplete": result["after"]["incomplete_count"]}, ensure_ascii=False, indent=2))
    if result["status"] != "success":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
