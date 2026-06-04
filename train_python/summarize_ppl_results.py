#!/usr/bin/env python3
from __future__ import annotations

"""Summarize fake-quant PPL JSON files into paper-friendly tables."""

import argparse
import csv
import json
from pathlib import Path


def parse_label(text: str) -> tuple[str, str]:
    if "=" in text:
        label, path = text.split("=", 1)
        return label.strip(), path.strip()
    path = Path(text)
    return path.stem, text


def load_result(label: str, path: str) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = []
    for item in data["results"]:
        metrics = item["metrics"]
        quant_meta = item.get("quant_meta", {})
        rows.append(
            {
                "dataset": label,
                "model": data.get("model", ""),
                "prompt_count": int(data.get("prompt_count", 0)),
                "max_length": int(data.get("max_length", 0)),
                "dtype": data.get("dtype", ""),
                "config": item["name"],
                "mode": item.get("mode", ""),
                "ppl": float(metrics["ppl"]),
                "mean_nll": float(metrics["mean_nll"]),
                "delta_nll_vs_fp16": float(item.get("delta_nll_vs_fp16", 0.0)),
                "ppl_ratio_vs_fp16": float(item.get("ppl_ratio_vs_fp16", 1.0)),
                "tokens": int(metrics.get("tokens", 0)),
                "bit_hist": json.dumps(quant_meta.get("bit_hist", {}), sort_keys=True),
                "allocation": item.get("allocation", ""),
                "method": item.get("method", ""),
            }
        )
    return rows


def markdown_table(rows: list[dict]) -> str:
    lines = [
        "# PPL Result Summary",
        "",
        "| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['dataset']} | `{row['model']}` | `{row['config']}` | "
            f"{row['ppl']:.4f} | {row['delta_nll_vs_fp16']:.6f} | "
            f"{row['ppl_ratio_vs_fp16']:.4f} | `{row['bit_hist']}` |"
        )
    lines.extend(
        [
            "",
            "## Scope",
            "",
            "These values come from the fake weight-quantization evaluator. They are",
            "quality diagnostics, not packed-runtime latency, memory, or energy results.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        action="append",
        required=True,
        help="dataset_label=path/to/summary.json; can be repeated",
    )
    parser.add_argument("--out-json", default="outputs/ppl_result_summary.json")
    parser.add_argument("--out-csv", default="outputs/ppl_result_summary.csv")
    parser.add_argument("--out-md", default="outputs/ppl_result_summary.md")
    args = parser.parse_args()

    rows: list[dict] = []
    for text in args.input:
        label, path = parse_label(text)
        rows.extend(load_result(label, path))

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_table(rows), encoding="utf-8")

    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "rows": len(rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
