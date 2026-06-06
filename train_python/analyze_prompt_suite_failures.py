#!/usr/bin/env python3
from __future__ import annotations

"""Cross-run prompt-suite failure analysis.

This utility compares multiple `eval_fused_qkv_prompt_suite.py` JSON outputs
and reports which prompts remain fragile across precision-guard candidates.
It is intentionally diagnostic: it does not rerun the model.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from eval_esmp_module_reconstruction import repo_root, resolve_path


def parse_run_spec(text: str) -> tuple[str, Path]:
    if "=" not in text:
        raise ValueError(f"expected label=path, got: {text}")
    label, path_text = text.split("=", 1)
    label = label.strip()
    path_text = path_text.strip()
    if not label or not path_text:
        raise ValueError(f"expected non-empty label=path, got: {text}")
    return label, Path(path_text)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def short_text(text: str, max_chars: int = 72) -> str:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3] + "..."


def yes_no(value: bool) -> str:
    return "Y" if value else "N"


def build_report(runs: list[dict[str, Any]]) -> dict[str, Any]:
    prompt_ids = sorted({int(row["id"]) for run in runs for row in run["rows"]})
    prompts: list[dict[str, Any]] = []
    for prompt_id in prompt_ids:
        per_run = []
        prompt_text = ""
        for run in runs:
            row = run["rows_by_id"].get(prompt_id)
            if row is None:
                continue
            prompt_text = str(row["prompt"])
            cmp = row["comparison"]
            per_run.append(
                {
                    "label": run["label"],
                    "exact_match": bool(cmp["exact_match"]),
                    "common_prefix_ratio": float(cmp["common_prefix_ratio"]),
                    "char_edit_similarity": float(cmp["char_edit_similarity"]),
                    "baseline_text": row["baseline"]["generated_text"],
                    "fused_text": row["fused"]["generated_text"],
                }
            )
        exact_count = sum(1 for item in per_run if item["exact_match"])
        best_prefix = max(per_run, key=lambda item: item["common_prefix_ratio"]) if per_run else None
        best_edit = max(per_run, key=lambda item: item["char_edit_similarity"]) if per_run else None
        prompts.append(
            {
                "id": prompt_id,
                "prompt": prompt_text,
                "exact_count": exact_count,
                "run_count": len(per_run),
                "exact_rate": exact_count / len(per_run) if per_run else 0.0,
                "best_prefix": best_prefix,
                "best_edit": best_edit,
                "runs": per_run,
            }
        )
    prompts.sort(key=lambda item: (item["exact_count"], item["best_prefix"]["common_prefix_ratio"] if item["best_prefix"] else 0.0))
    return {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "runs": [
            {
                "label": run["label"],
                "path": run["path"],
                "exact_matches": int(run["aggregate"]["exact_matches"]),
                "prompts": int(run["aggregate"]["prompts"]),
                "mean_prefix": float(run["aggregate"]["mean_common_prefix_ratio"]),
                "mean_edit": float(run["aggregate"]["mean_char_edit_similarity"]),
                "mean_speed": float(run["aggregate"]["mean_speedup_fused_vs_baseline"]),
            }
            for run in runs
        ],
        "prompts": prompts,
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Prompt-Suite Failure Analysis",
        "",
        f"Date: `{report['date']}`",
        "",
        "## Run Summary",
        "",
        "| run | exact | mean edit | mean prefix | speed |",
        "|---|---:|---:|---:|---:|",
    ]
    for run in report["runs"]:
        lines.append(
            f"| `{run['label']}` | {run['exact_matches']} / {run['prompts']} | "
            f"{run['mean_edit']:.4f} | {run['mean_prefix']:.4f} | {run['mean_speed']:.4f}x |"
        )
    labels = [run["label"] for run in report["runs"]]
    lines.extend(
        [
            "",
            "## Prompt Matrix",
            "",
            "| id | prompt | " + " | ".join(f"`{label}`" for label in labels) + " | best prefix | best edit |",
            "|---:|---|" + "|".join("---:" for _ in labels) + "|---|---|",
        ]
    )
    for prompt in report["prompts"]:
        by_label = {row["label"]: row for row in prompt["runs"]}
        exact_cells = [yes_no(bool(by_label[label]["exact_match"])) if label in by_label else "-" for label in labels]
        best_prefix = prompt["best_prefix"]
        best_edit = prompt["best_edit"]
        lines.append(
            f"| {prompt['id']} | {short_text(prompt['prompt'])} | "
            + " | ".join(exact_cells)
            + f" | `{best_prefix['label']}` {best_prefix['common_prefix_ratio']:.4f} | "
            + f"`{best_edit['label']}` {best_edit['char_edit_similarity']:.4f} |"
        )
    lines.extend(["", "## Hardest Prompts", ""])
    hardest = [prompt for prompt in report["prompts"] if prompt["exact_count"] == 0]
    if not hardest:
        min_exact = min((prompt["exact_count"] for prompt in report["prompts"]), default=0)
        hardest = [prompt for prompt in report["prompts"] if prompt["exact_count"] == min_exact]
    for prompt in hardest:
        lines.append(f"### Prompt {prompt['id']}")
        lines.append("")
        lines.append(prompt["prompt"])
        lines.append("")
        for row in sorted(prompt["runs"], key=lambda item: (-int(item["exact_match"]), -item["common_prefix_ratio"], item["label"])):
            lines.append(
                f"- `{row['label']}` exact={yes_no(row['exact_match'])}, "
                f"prefix={row['common_prefix_ratio']:.4f}, edit={row['char_edit_similarity']:.4f}; "
                f"fused: {short_text(row['fused_text'], 120)}"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare prompt-suite failures across multiple runs.")
    parser.add_argument("--run", action="append", required=True, help="Run spec in label=path form.")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = repo_root()
    runs: list[dict[str, Any]] = []
    for spec in args.run:
        label, path = parse_run_spec(spec)
        resolved = resolve_path(str(path), root)
        data = load_json(resolved)
        rows_by_id = {int(row["id"]): row for row in data["rows"]}
        runs.append(
            {
                "label": label,
                "path": str(resolved),
                "aggregate": data["aggregate"],
                "rows": data["rows"],
                "rows_by_id": rows_by_id,
            }
        )
    report = build_report(runs)
    out_json = resolve_path(args.out_json, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(out_md, report)
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
