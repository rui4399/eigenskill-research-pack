#!/usr/bin/env python3
from __future__ import annotations

"""Build AWQ/GPTQ-style PTQ proxy allocations from measured sensitivity JSON.

This is not an official AWQ or GPTQ implementation. It creates executable
related-family proxy baselines using the repository's measured module-level
loss sensitivity:

- GPTQ-style proxy: protect modules by a loss/Hessian-like sensitivity score.
- AWQ-style proxy: protect modules by activation-saliency-inspired role and
  shape weighting combined with measured sensitivity.
"""

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(number):
        return default
    return number


def positive_sensitivity(record: dict[str, Any]) -> float:
    for key in ("positive_delta_nll", "sensitivity", "normalized_output_mse", "delta_nll"):
        value = finite_float(record.get(key), 0.0)
        if key == "delta_nll":
            value = max(value, 0.0)
        if value > 0.0:
            return value
    return 0.0


def module_cost(record: dict[str, Any]) -> float:
    return max(
        finite_float(record.get("cost"), 0.0)
        or finite_float(record.get("param_count"), 0.0)
        or finite_float(record.get("weight_params"), 0.0),
        1.0,
    )


def role_from_module(name: str) -> str:
    tail = name.rsplit(".", 1)[-1]
    return tail or "unknown"


def shape_imbalance(record: dict[str, Any]) -> float:
    shape = record.get("shape", [])
    if not isinstance(shape, list) or len(shape) < 2:
        return 1.0
    dims = [max(finite_float(dim, 1.0), 1.0) for dim in shape[:2]]
    return max(dims) / max(min(dims), 1.0)


def role_saliency(role: str) -> float:
    if role in {"k_proj", "v_proj"}:
        return 1.30
    if role in {"q_proj", "o_proj"}:
        return 1.18
    if role in {"gate_proj", "up_proj"}:
        return 1.10
    if role == "down_proj":
        return 1.00
    if role == "lm_head":
        return 0.80
    return 0.90


def bit_hist(alloc: list[int]) -> dict[str, int]:
    hist: dict[str, int] = {}
    for bits in alloc:
        hist[str(bits)] = hist.get(str(bits), 0) + 1
    return hist


def budgeted_select(groups: list[dict[str, Any]], scores: list[float], budget_avg_bits: float, base_bits: int, high_bits: int) -> list[int]:
    total_cost = sum(float(group["cost"]) for group in groups)
    budget = budget_avg_bits * total_cost
    base_memory = base_bits * total_cost
    remaining = max(budget - base_memory, 0.0)
    alloc = [base_bits for _ in groups]
    selected: set[int] = set()
    ordered = sorted(range(len(groups)), key=lambda idx: (scores[idx], groups[idx]["sensitivity"]), reverse=True)
    for idx in ordered:
        if scores[idx] <= 0.0:
            continue
        extra = (high_bits - base_bits) * float(groups[idx]["cost"])
        if extra <= remaining + 1.0e-9:
            alloc[idx] = high_bits
            selected.add(idx)
            remaining -= extra
    for idx in sorted(range(len(groups)), key=lambda i: float(groups[i]["cost"])):
        if idx in selected:
            continue
        extra = (high_bits - base_bits) * float(groups[idx]["cost"])
        if extra <= remaining + 1.0e-9 and scores[idx] > 0.0:
            alloc[idx] = high_bits
            remaining -= extra
    return alloc


def normalize_scores(scores: list[float]) -> list[float]:
    best = max(scores) if scores else 0.0
    if best <= 0.0:
        return [0.0 for _ in scores]
    return [score / best for score in scores]


def enrich(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, group in enumerate(groups):
        name = str(group.get("module") or group.get("name") or f"group_{index}")
        role = role_from_module(name)
        sensitivity = positive_sensitivity(group)
        cost = module_cost(group)
        imbalance = shape_imbalance(group)
        rows.append(
            {
                "index": int(group.get("index", index)),
                "module": name,
                "role": role,
                "shape": group.get("shape", []),
                "cost": cost,
                "sensitivity": sensitivity,
                "score_per_cost": sensitivity / cost,
                "shape_imbalance": imbalance,
            }
        )
    return rows


def method_scores(rows: list[dict[str, Any]]) -> dict[str, list[float]]:
    gptq_raw = [
        float(row["sensitivity"]) * math.log2(float(row["cost"]) + 2.0) / max(float(row["cost"]), 1.0)
        for row in rows
    ]
    awq_raw = [
        float(row["sensitivity"])
        * role_saliency(str(row["role"]))
        * (1.0 + 0.08 * math.log2(max(float(row["shape_imbalance"]), 1.0)))
        / math.sqrt(max(float(row["cost"]), 1.0))
        for row in rows
    ]
    return {
        "gptq_loss_hessian_proxy": normalize_scores(gptq_raw),
        "awq_activation_saliency_proxy": normalize_scores(awq_raw),
    }


def summarize_method(
    name: str,
    rows: list[dict[str, Any]],
    scores: list[float],
    alloc: list[int],
    target_avg_bits: float,
    base_bits: int,
) -> dict[str, Any]:
    total_cost = sum(float(row["cost"]) for row in rows)
    memory = sum(float(row["cost"]) * bits for row, bits in zip(rows, alloc))
    total_sens = sum(float(row["sensitivity"]) for row in rows)
    protected_sens = sum(float(row["sensitivity"]) for row, bits in zip(rows, alloc) if bits > base_bits)
    selected = [
        {
            "module": row["module"],
            "role": row["role"],
            "score": scores[idx],
            "sensitivity": row["sensitivity"],
            "bits": alloc[idx],
        }
        for idx, row in enumerate(rows)
        if alloc[idx] > base_bits
    ]
    selected.sort(key=lambda row: (float(row["score"]), float(row["sensitivity"])), reverse=True)
    return {
        "name": name,
        "groups": len(rows),
        "target_avg_bits": target_avg_bits,
        "avg_bits": memory / max(total_cost, 1.0e-12),
        "budget_satisfied": memory <= target_avg_bits * total_cost + 1.0e-6,
        "bit_hist": bit_hist(alloc),
        "protected_count": len(selected),
        "positive_sensitivity_total": total_sens,
        "positive_sensitivity_protected": protected_sens,
        "positive_sensitivity_protected_ratio": protected_sens / max(total_sens, 1.0e-12),
        "top_protected_modules": selected[:12],
    }


def package_summary(audit: dict[str, Any]) -> list[dict[str, Any]]:
    packages = []
    for item in audit.get("packages", []) or []:
        if not isinstance(item, dict):
            continue
        if str(item.get("name")) in {"optimum", "auto_gptq", "gptqmodel", "awq"}:
            packages.append(
                {
                    "name": item.get("name"),
                    "available": bool(item.get("available")),
                    "version": item.get("version", ""),
                }
            )
    return packages


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    payload = load_json(args.input)
    groups = payload.get("groups", []) or payload.get("records", [])
    if not isinstance(groups, list) or not groups:
        raise SystemExit(f"no groups/records found in {args.input}")
    rows = enrich(groups)
    scores_by_method = method_scores(rows)
    allocations = {
        method: budgeted_select(rows, scores, args.target_avg_bits, args.base_bits, args.high_bits)
        for method, scores in scores_by_method.items()
    }
    summaries = [
        summarize_method(method, rows, scores_by_method[method], alloc, args.target_avg_bits, args.base_bits)
        for method, alloc in allocations.items()
    ]
    audit = load_json(args.environment_audit) if args.environment_audit and args.environment_audit.exists() else {}
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "method": "awq_gptq_style_ptq_baseline_proxy",
        "source": str(args.input),
        "model": payload.get("model"),
        "probe_bits": payload.get("probe_bits"),
        "group_size": payload.get("group_size"),
        "base_bits": args.base_bits,
        "high_bits": args.high_bits,
        "target_avg_bits": args.target_avg_bits,
        "record_count": len(rows),
        "environment_packages": package_summary(audit),
        "records": rows,
        "allocations": allocations,
        "summaries": summaries,
        "claim_boundary": (
            "Valid claim: executable AWQ/GPTQ-style proxy baselines exist over measured module sensitivity records. "
            "Invalid claim: this is an official AWQ/GPTQ quantizer run, a CUDA PTQ implementation, or a SOTA comparison."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# AWQ/GPTQ-Style PTQ Baseline Proxy",
        "",
        f"Date: `{result['date']}`",
        f"Method: `{result['method']}`",
        f"Source: `{result['source']}`",
        f"Records: `{result['record_count']}`",
        "",
        "## Package Audit Snapshot",
        "",
        "| package | available | version |",
        "|---|---:|---|",
    ]
    for item in result["environment_packages"]:
        lines.append(f"| `{item['name']}` | {item['available']} | `{item['version']}` |")
    lines.extend(
        [
            "",
            "## Proxy Methods",
            "",
            "| method | avg bits | budget | protected | protected sensitivity | bit hist |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for item in result["summaries"]:
        lines.append(
            f"| `{item['name']}` | {item['avg_bits']:.6f} | {str(item['budget_satisfied']).lower()} | "
            f"{item['protected_count']} | {item['positive_sensitivity_protected_ratio']:.6f} | `{item['bit_hist']}` |"
        )
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build AWQ/GPTQ-style proxy baselines from sensitivity JSON.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--environment-audit", type=Path, default=Path("outputs/baseline_environment_audit.json"))
    parser.add_argument("--base-bits", type=int, default=4)
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--target-avg-bits", type=float, default=4.5)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    result = build_result(args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "record_count": result["record_count"],
                "summaries": [
                    {
                        "name": item["name"],
                        "avg_bits": item["avg_bits"],
                        "protected_ratio": item["positive_sensitivity_protected_ratio"],
                    }
                    for item in result["summaries"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
