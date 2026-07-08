#!/usr/bin/env python3
from __future__ import annotations

"""Build tiny public text prompt files for matched PPL probes.

The files created here are prompt slices, not benchmark leaderboards. They are
used to move official PTQ readiness probes from hand-written prompts toward
public WikiText2/C4 text slices without downloading large datasets.
"""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlencode
from urllib.request import urlopen


DATASETS = {
    "wikitext2": {
        "dataset": "Salesforce/wikitext",
        "config": "wikitext-2-raw-v1",
        "split": "test",
        "file": "wikitext2_test_ppl_prompts.txt",
    },
    "c4": {
        "dataset": "allenai/c4",
        "config": "en",
        "split": "validation",
        "file": "c4_validation_ppl_prompts.txt",
    },
}


Loader = Callable[[str, Optional[str], str, int, int], list[dict[str, Any]]]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_text_rows(rows: list[dict[str, Any]], *, min_chars: int, max_chars: int) -> list[str]:
    prompts: list[str] = []
    for row in rows:
        text = normalize_text(str(row.get("text") or ""))
        if len(text) < min_chars:
            continue
        prompts.append(text[:max_chars])
    return prompts


def load_dataset_server_records(dataset: str, config: str | None, split: str, count: int, offset: int) -> list[dict[str, Any]]:
    params: dict[str, Any] = {
        "dataset": dataset,
        "split": split,
        "offset": offset,
        "length": count,
    }
    if config:
        params["config"] = config
    url = f"https://datasets-server.huggingface.co/rows?{urlencode(params)}"
    with urlopen(url, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return [dict(item["row"]) for item in payload.get("rows", [])[:count]]


def write_prompt_file(path: Path, prompts: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(prompts) + "\n", encoding="utf-8")


def collect_prompts(
    *,
    dataset: str,
    config: str | None,
    split: str,
    requested: int,
    loader: Loader,
    min_chars: int,
    max_chars: int,
    offset: int,
    max_batches: int = 50,
) -> tuple[list[str], int]:
    prompts: list[str] = []
    batch_size = min(max(requested * 4, requested, 1), 100)
    rows_seen = 0
    next_offset = offset
    for _ in range(max_batches):
        rows = loader(dataset, config, split, batch_size, next_offset)
        rows_seen += len(rows)
        prompts.extend(clean_text_rows(rows, min_chars=min_chars, max_chars=max_chars))
        if len(prompts) >= requested or not rows:
            break
        next_offset += batch_size
    return prompts[:requested], rows_seen


def build_suite(
    *,
    out_dir: Path,
    counts: dict[str, int],
    source: str,
    loader: Loader = load_dataset_server_records,
    min_chars: int = 40,
    max_chars: int = 512,
    offset: int = 0,
    title: str = "Public PPL Prompt Manifest",
    claim_boundary: str = "Tiny public text slices for matched PPL probes; not leaderboard-scale evaluation.",
) -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    for key, spec in DATASETS.items():
        requested = int(counts.get(key, 0) or 0)
        if requested <= 0:
            continue
        prompts, rows_seen = collect_prompts(
            dataset=str(spec["dataset"]),
            config=spec.get("config"),
            split=str(spec["split"]),
            requested=requested,
            loader=loader,
            min_chars=min_chars,
            max_chars=max_chars,
            offset=offset,
        )
        out_path = out_dir / str(spec["file"])
        write_prompt_file(out_path, prompts)
        artifacts.append(
            {
                "id": key,
                "dataset": spec["dataset"],
                "config": spec.get("config"),
                "split": spec["split"],
                "source": source,
                "path": out_path.as_posix(),
                "requested_prompts": requested,
                "prompts": len(prompts),
                "rows_seen": rows_seen,
                "min_chars": min_chars,
                "max_chars": max_chars,
                "offset": offset,
            }
        )
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "title": title,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "claim_boundary": claim_boundary,
    }


def write_markdown(path: Path, manifest: dict[str, Any]) -> None:
    lines = [
        f"# {manifest['title']}",
        "",
        f"Date: `{manifest['date']}`",
        f"Artifacts: `{manifest['artifact_count']}`",
        "",
        "| id | dataset | config | split | prompts | path |",
        "|---|---|---|---|---:|---|",
    ]
    for item in manifest["artifacts"]:
        lines.append(
            f"| `{item['id']}` | `{item['dataset']}` | `{item.get('config')}` | "
            f"`{item['split']}` | {item['prompts']} | `{item['path']}` |"
        )
    lines.extend(["", "## Claim Boundary", "", f"- {manifest['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build tiny public PPL prompt slices.")
    parser.add_argument("--out-dir", type=Path, default=Path("data_eval/public_ppl_prompts_2026_06_07"))
    parser.add_argument("--wikitext2-count", type=int, default=8)
    parser.add_argument("--c4-count", type=int, default=8)
    parser.add_argument("--source", choices=["datasets-server"], default="datasets-server")
    parser.add_argument("--min-chars", type=int, default=40)
    parser.add_argument("--max-chars", type=int, default=512)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--manifest-title", default="Public PPL Prompt Manifest")
    parser.add_argument(
        "--claim-boundary",
        default="Tiny public text slices for matched PPL probes; not leaderboard-scale evaluation.",
    )
    parser.add_argument("--out-json", type=Path, default=Path("outputs/public_ppl_prompt_manifest_2026_06_07.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/PUBLIC_PPL_PROMPT_MANIFEST_2026_06_07.md"))
    args = parser.parse_args()

    manifest = build_suite(
        out_dir=args.out_dir,
        counts={"wikitext2": args.wikitext2_count, "c4": args.c4_count},
        source=args.source,
        min_chars=args.min_chars,
        max_chars=args.max_chars,
        offset=args.offset,
        title=args.manifest_title,
        claim_boundary=args.claim_boundary,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, manifest)
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "out_md": str(args.out_md),
                "artifacts": {item["id"]: item["prompts"] for item in manifest["artifacts"]},
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
