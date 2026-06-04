#!/usr/bin/env python3
from __future__ import annotations

"""Summarize consensus mixed-precision budget curves from fake-quant PPL runs."""

import argparse
import csv
import json
from pathlib import Path


def parse_input(text: str) -> tuple[str, str]:
    if "=" not in text:
        path = Path(text)
        return path.stem, text
    label, path = text.split("=", 1)
    return label.strip(), path.strip()


def load_rows(label: str, path: str) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    fp16 = next(item for item in data["results"] if item["name"] == "fp16")
    uniform = next(item for item in data["results"] if item["name"] == "uniform_int4")
    fp16_ppl = float(fp16["metrics"]["ppl"])
    uniform_ppl = float(uniform["metrics"]["ppl"])
    rows = []
    for item in data["results"]:
        metrics = item["metrics"]
        summary = item.get("allocation_summary") or {}
        quant_meta = item.get("quant_meta", {})
        ppl = float(metrics["ppl"])
        if item["name"] == "fp16":
            avg_bits = 16.0
        elif item["name"] == "uniform_int4":
            avg_bits = 4.0
        else:
            avg_bits = float(summary.get("avg_bits", 0.0))
        uniform_gap = max(uniform_ppl - fp16_ppl, 1.0e-12)
        rows.append(
            {
                "dataset": label,
                "model": data.get("model", ""),
                "prompt_count": int(data.get("prompt_count", 0)),
                "config": item["name"],
                "avg_bits": avg_bits,
                "ppl": ppl,
                "delta_nll_vs_fp16": float(item.get("delta_nll_vs_fp16", 0.0)),
                "ppl_improvement_vs_uniform": uniform_ppl - ppl,
                "uniform_gap_closed_ratio": (uniform_ppl - ppl) / uniform_gap,
                "bit_hist": json.dumps(quant_meta.get("bit_hist", {}), sort_keys=True),
            }
        )
    return rows


def markdown(rows: list[dict]) -> str:
    lines = [
        "# Consensus Budget Curve",
        "",
        "This table evaluates the same cross-dataset consensus allocator at multiple",
        "average-bit budgets. It is a short-slice PyTorch fake-quant diagnostic,",
        "not a packed runtime or hardware result.",
        "",
        "| dataset | model | config | avg bits | PPL | PPL gain vs uniform INT4 | uniform gap closed | bit hist |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['dataset']} | `{row['model']}` | `{row['config']}` | "
            f"{row['avg_bits']:.4f} | {row['ppl']:.4f} | "
            f"{row['ppl_improvement_vs_uniform']:.4f} | {row['uniform_gap_closed_ratio']:.4f} | "
            f"`{row['bit_hist']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A useful allocation curve should improve as more high-precision budget is",
            "released. Non-monotonic points should be treated as calibration noise or",
            "module-interaction evidence rather than hidden as failed runs.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, help="label=summary.json; can be repeated")
    parser.add_argument("--out-json", default="outputs/consensus_budget_curve_summary.json")
    parser.add_argument("--out-csv", default="outputs/consensus_budget_curve_summary.csv")
    parser.add_argument("--out-md", default="outputs/consensus_budget_curve_report.md")
    args = parser.parse_args()

    rows: list[dict] = []
    for text in args.input:
        label, path = parse_input(text)
        rows.extend(load_rows(label, path))

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
    out_md.write_text(markdown(rows), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
