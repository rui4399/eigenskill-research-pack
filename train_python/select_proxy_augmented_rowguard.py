#!/usr/bin/env python3
from __future__ import annotations

"""Augment multi-split rowguard selection with hidden/logit/KV drift proxies."""

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROXY_METRICS = [
    "final_hidden_rel_l2_mean",
    "last_logits_rel_l2_mean",
    "kv_mean_rel_l2_mean",
    "kv_max_rel_l2_mean",
]


def resolve_path(path: str, root: Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return root / p


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_proxy(spec: str, root: Path) -> tuple[str, dict[str, float]]:
    if "=" not in spec:
        raise ValueError(f"expected LABEL=PROXY_JSON, got {spec}")
    label, path_text = spec.split("=", 1)
    data = load_json(resolve_path(path_text.strip(), root))
    agg = data["aggregate"]
    return label.strip(), {
        "final_hidden_rel_l2_mean": float(agg["final_hidden_rel_l2"]["mean"]),
        "last_logits_rel_l2_mean": float(agg["last_logits_rel_l2"]["mean"]),
        "kv_mean_rel_l2_mean": float(agg["kv_mean_rel_l2"]["mean"]),
        "kv_max_rel_l2_mean": float(agg["kv_max_rel_l2"]["mean"]),
    }


def normalize(values: dict[str, float]) -> dict[str, float]:
    lo = min(values.values())
    hi = max(values.values())
    if hi <= lo:
        return {key: 0.0 for key in values}
    return {key: (value - lo) / (hi - lo) for key, value in values.items()}


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "label",
        "family",
        "selector_decision",
        "consensus_score",
        "proxy_penalty",
        "proxy_augmented_score",
        "min_exact_rate",
        "exact_span",
        *PROXY_METRICS,
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fieldnames})


def fmt(value: float) -> str:
    return f"{value:.4f}"


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    recs = result["recommendations"]
    lines = [
        "# Proxy-Augmented Rowguard Selector",
        "",
        f"Date: `{result['date']}`",
        f"Proxy weight: `{result['proxy_weight']}`",
        "",
        "The augmented score combines multi-split prompt robustness with normalized hidden/logit/KV drift. Lower proxy drift is better.",
        "",
        "## Recommendations",
        "",
    ]
    for key in ["best_overall", "best_rowguard", "stable_rowguard"]:
        rec = recs.get(key)
        if rec is None:
            lines.append(f"- `{key}`: none")
        else:
            lines.append(
                f"- `{key}`: `{rec['label']}`, augmented score `{fmt(float(rec['proxy_augmented_score']))}`, "
                f"proxy penalty `{fmt(float(rec['proxy_penalty']))}`, min exact `{fmt(float(rec['min_exact_rate']))}`"
            )

    lines.extend(
        [
            "",
            "## Ranking",
            "",
            "| rank | label | family | augmented | prompt score | proxy penalty | min exact | exact span | final hidden | logits | KV mean | KV max |",
            "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for idx, row in enumerate(rows, start=1):
        lines.append(
            f"| {idx} | {row['label']} | {row['family']} | "
            f"{fmt(float(row['proxy_augmented_score']))} | {fmt(float(row['consensus_score']))} | "
            f"{fmt(float(row['proxy_penalty']))} | {fmt(float(row['min_exact_rate']))} | "
            f"{fmt(float(row['exact_span']))} | {row['final_hidden_rel_l2_mean']:.6f} | "
            f"{row['last_logits_rel_l2_mean']:.6f} | {row['kv_mean_rel_l2_mean']:.6f} | "
            f"{row['kv_max_rel_l2_mean']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- This is a diagnostic selector, not final proof of quality.",
            "- Proxy drift strongly separates the stable baseline/full-V8 probes from the rowguard candidates in this slice.",
            "- Rowguards remain candidates for larger-suite testing only if their worst-split exact rate and proxy drift both improve.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Add hidden/logit/KV proxy drift to a multi-split selector.")
    parser.add_argument("--selector-json", required=True)
    parser.add_argument("--proxy", action="append", required=True, help="LABEL=PROXY_JSON")
    parser.add_argument("--proxy-weight", type=float, default=0.25)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    selector = load_json(resolve_path(args.selector_json, root))
    proxies = dict(parse_proxy(spec, root) for spec in args.proxy)
    rows = []
    for row in selector["rows"]:
        label = str(row["label"])
        if label not in proxies:
            continue
        rows.append({**row, **proxies[label]})
    if not rows:
        raise SystemExit("no selector rows had matching proxy inputs")

    normalized_by_metric: dict[str, dict[str, float]] = {}
    for metric in PROXY_METRICS:
        normalized_by_metric[metric] = normalize({row["label"]: float(row[metric]) for row in rows})
    proxy_weight = max(0.0, min(1.0, float(args.proxy_weight)))
    for row in rows:
        label = row["label"]
        row["proxy_penalty"] = float(sum(normalized_by_metric[metric][label] for metric in PROXY_METRICS) / len(PROXY_METRICS))
        row["proxy_augmented_score"] = float(
            (1.0 - proxy_weight) * float(row["consensus_score"]) + proxy_weight * (1.0 - row["proxy_penalty"])
        )

    rows.sort(
        key=lambda row: (
            row["proxy_augmented_score"],
            row["min_exact_rate"],
            -row["proxy_penalty"],
            row["mean_speedup"],
        ),
        reverse=True,
    )
    best_overall = rows[0]
    best_rowguard = next((row for row in rows if row.get("family") == "rowguard"), None)
    stable_rowguard = next(
        (
            row
            for row in rows
            if row.get("family") == "rowguard"
            and row.get("selector_decision") == "stable_reference"
            and float(row["proxy_penalty"]) <= 0.25
        ),
        None,
    )
    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "selector_json": str(resolve_path(args.selector_json, root)),
        "proxy_weight": proxy_weight,
        "recommendations": {
            "best_overall": best_overall,
            "best_rowguard": best_rowguard,
            "stable_rowguard": stable_rowguard,
        },
        "rows": rows,
    }
    out_json = resolve_path(args.out_json, root)
    out_csv = resolve_path(args.out_csv, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(out_csv, rows)
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "recommendations": result["recommendations"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
