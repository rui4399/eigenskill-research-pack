#!/usr/bin/env python3
from __future__ import annotations

"""Build public benchmark fixture files through Hugging Face streaming.

The default command still creates tiny smoke files. Larger runs can reuse the
same builder with a different file tag and claim boundary. These fixtures are
not benchmark leaderboards; they are reproducibility inputs for guarded task
evaluation.
"""

import argparse
import json
from datetime import datetime, timezone
from itertools import islice
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlencode
from urllib.request import urlopen


DATASETS = {
    "gsm8k": {
        "dataset": "openai/gsm8k",
        "config": "main",
        "split": "test",
        "task_format": "gsm8k",
        "file": "gsm8k_test_smoke.jsonl",
    },
    "mmlu_abstract_algebra": {
        "dataset": "cais/mmlu",
        "config": "abstract_algebra",
        "split": "test",
        "task_format": "mmlu",
        "file": "mmlu_abstract_algebra_test_smoke.jsonl",
    },
}

DEFAULT_CLAIM_BOUNDARY = "Tiny public benchmark smoke fixtures; not leaderboard-scale evaluation."


def take_records(rows: Iterable[dict[str, Any]], count: int) -> list[dict[str, Any]]:
    if count < 0:
        raise ValueError("count must be non-negative")
    return [dict(row) for row in islice(rows, count)]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def artifact_file(base_file: str, file_tag: str) -> str:
    tag = file_tag.strip().replace(" ", "_")
    if not tag or tag == "smoke":
        return base_file
    if base_file.endswith("_smoke.jsonl"):
        return f"{base_file[:-len('_smoke.jsonl')]}_{tag}.jsonl"
    if base_file.endswith(".jsonl"):
        return f"{base_file[:-len('.jsonl')]}_{tag}.jsonl"
    return f"{base_file}_{tag}"


def load_dataset_server_records(dataset: str, config: str | None, split: str, count: int) -> list[dict[str, Any]]:
    params = {
        "dataset": dataset,
        "split": split,
        "offset": 0,
        "length": count,
    }
    if config:
        params["config"] = config
    url = f"https://datasets-server.huggingface.co/rows?{urlencode(params)}"
    with urlopen(url, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    rows = payload.get("rows", [])
    return [dict(item["row"]) for item in rows[:count]]


def load_streamed_records(dataset: str, config: str | None, split: str, count: int, source: str = "auto") -> list[dict[str, Any]]:
    if source not in {"auto", "datasets", "datasets-server"}:
        raise ValueError(f"unsupported source: {source}")
    if source in {"auto", "datasets"}:
        try:
            return load_hf_datasets_records(dataset, config, split, count)
        except ImportError:
            if source == "datasets":
                raise
    return load_dataset_server_records(dataset, config, split, count)


def load_hf_datasets_records(dataset: str, config: str | None, split: str, count: int) -> list[dict[str, Any]]:
    from datasets import load_dataset

    stream = load_dataset(dataset, config, split=split, streaming=True) if config else load_dataset(dataset, split=split, streaming=True)
    return take_records(stream, count)


def build_suite(
    out_dir: Path,
    counts: dict[str, int],
    *,
    file_tag: str = "smoke",
    claim_boundary: str = DEFAULT_CLAIM_BOUNDARY,
    title: str = "Public Task Smoke Manifest",
    source: str = "auto",
) -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    for key, spec in DATASETS.items():
        count = int(counts.get(key, 0))
        if count <= 0:
            continue
        rows = load_streamed_records(str(spec["dataset"]), spec.get("config"), str(spec["split"]), count, source=source)
        out_path = out_dir / artifact_file(str(spec["file"]), file_tag)
        write_jsonl(out_path, rows)
        artifacts.append(
            {
                "id": key,
                "dataset": spec["dataset"],
                "config": spec.get("config"),
                "split": spec["split"],
                "task_format": spec["task_format"],
                "source": source,
                "path": out_path.as_posix(),
                "rows": len(rows),
                "columns": sorted(rows[0].keys()) if rows else [],
            }
        )
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "title": title,
        "file_tag": file_tag,
        "source": source,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "claim_boundary": claim_boundary,
    }


def write_markdown(path: Path, manifest: dict[str, Any]) -> None:
    lines = [
        f"# {manifest.get('title', 'Public Task Smoke Manifest')}",
        "",
        f"Date: `{manifest['date']}`",
        f"Artifacts: `{manifest['artifact_count']}`",
        "",
        "## Files",
        "",
        "| id | dataset | config | split | task format | rows | path |",
        "|---|---|---|---|---|---:|---|",
    ]
    for item in manifest["artifacts"]:
        lines.append(
            f"| `{item['id']}` | `{item['dataset']}` | `{item.get('config')}` | `{item['split']}` | "
            f"`{item['task_format']}` | {item['rows']} | `{item['path']}` |"
        )
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            f"- {manifest['claim_boundary']}",
            "- Use these files to verify public-schema task ingestion before running larger benchmark slices.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build tiny public benchmark smoke JSONL files.")
    parser.add_argument("--out-dir", type=Path, default=Path("data_eval/public_task_smoke_v1"))
    parser.add_argument("--gsm8k-count", type=int, default=4)
    parser.add_argument("--mmlu-count", type=int, default=4)
    parser.add_argument("--file-tag", default="smoke")
    parser.add_argument("--title", default="Public Task Smoke Manifest")
    parser.add_argument("--claim-boundary", default=DEFAULT_CLAIM_BOUNDARY)
    parser.add_argument("--source", choices=["auto", "datasets", "datasets-server"], default="auto")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/public_task_smoke_manifest_2026_06_06.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/PUBLIC_TASK_SMOKE_MANIFEST_2026_06_06.md"))
    args = parser.parse_args()

    manifest = build_suite(
        args.out_dir,
        {
            "gsm8k": args.gsm8k_count,
            "mmlu_abstract_algebra": args.mmlu_count,
        },
        file_tag=args.file_tag,
        claim_boundary=args.claim_boundary,
        title=args.title,
        source=args.source,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, manifest)
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "out_md": str(args.out_md),
                "artifact_count": manifest["artifact_count"],
                "rows": {item["id"]: item["rows"] for item in manifest["artifacts"]},
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
