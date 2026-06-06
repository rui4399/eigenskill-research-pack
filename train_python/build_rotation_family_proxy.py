#!/usr/bin/env python3
from __future__ import annotations

"""Build a QuaRot/SpinQuant-style rotation-family proxy from sensitivity JSON.

This script is deliberately a proxy. It does not implement the official
QuaRot/SpinQuant transforms. Instead, it makes the comparison family executable
by selecting modules whose measured quantization-loss sensitivity and role make
them plausible rotation/outlier-mitigation targets, then records a conservative
projected sensitivity reduction under a fixed rotation budget.
"""

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any


ATTN_ROLES = {"q_proj", "k_proj", "v_proj", "o_proj"}
MLP_ROLES = {"gate_proj", "up_proj", "down_proj"}


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


def role_from_module(name: str) -> str:
    tail = name.rsplit(".", 1)[-1]
    if tail:
        return tail
    return "unknown"


def layer_from_record(record: dict[str, Any]) -> int:
    value = record.get("layer")
    if isinstance(value, int):
        return value
    name = str(record.get("module") or record.get("name") or "")
    parts = name.split(".")
    for idx, part in enumerate(parts[:-1]):
        if part == "layers":
            try:
                return int(parts[idx + 1])
            except (ValueError, IndexError):
                return -1
    return -1


def shape_imbalance(record: dict[str, Any]) -> float:
    shape = record.get("shape", [])
    if not isinstance(shape, list) or len(shape) < 2:
        return 1.0
    dims = [max(finite_float(dim, 1.0), 1.0) for dim in shape[:2]]
    return max(dims) / max(min(dims), 1.0)


def robust_stats(values: list[float]) -> dict[str, float]:
    clean = sorted(value for value in values if math.isfinite(value))
    if not clean:
        return {"median": 0.0, "mad": 1.0, "max": 0.0}
    med = median(clean)
    deviations = sorted(abs(value - med) for value in clean)
    mad = median(deviations) if deviations else 0.0
    return {"median": float(med), "mad": float(max(mad, 1.0e-12)), "max": float(clean[-1])}


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


def role_weight(role: str) -> float:
    if role in {"q_proj", "k_proj", "v_proj"}:
        return 1.25
    if role == "o_proj":
        return 1.10
    if role in {"gate_proj", "up_proj"}:
        return 1.05
    if role == "down_proj":
        return 0.95
    return 0.80


def choose_policy(role: str, priority_percentile: float, imbalance: float) -> tuple[str, float]:
    if role in {"q_proj", "k_proj", "v_proj"} and priority_percentile >= 0.80:
        return "spinquant_learned_rotation_proxy", 0.22
    if role in ATTN_ROLES and priority_percentile >= 0.55:
        return "quarot_static_hadamard_proxy", 0.16
    if role in MLP_ROLES and (priority_percentile >= 0.72 or imbalance >= 1.75):
        return "spinquant_learned_rotation_proxy", 0.18
    return "none", 0.0


def enrich_records(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sensitivities = [positive_sensitivity(group) for group in groups]
    stats = robust_stats(sensitivities)
    max_sens = max(stats["max"], 1.0e-12)
    enriched: list[dict[str, Any]] = []
    for index, group in enumerate(groups):
        name = str(group.get("module") or group.get("name") or f"group_{index}")
        role = role_from_module(name)
        sensitivity = positive_sensitivity(group)
        cost = module_cost(group)
        imbalance = shape_imbalance(group)
        robust_z = max((sensitivity - stats["median"]) / stats["mad"], 0.0)
        normalized = sensitivity / max_sens
        priority = (
            math.log1p(robust_z)
            + 0.70 * normalized
            + 0.25 * role_weight(role)
            + 0.05 * math.log2(max(imbalance, 1.0))
        )
        enriched.append(
            {
                "index": int(group.get("index", index)),
                "module": name,
                "layer": layer_from_record(group),
                "role": role,
                "shape": group.get("shape", []),
                "cost": cost,
                "sensitivity": sensitivity,
                "score_per_cost": sensitivity / cost,
                "shape_imbalance": imbalance,
                "rotation_priority": priority,
            }
        )
    return enriched


def assign_rotation(records: list[dict[str, Any]], budget_fraction: float) -> list[dict[str, Any]]:
    total_cost = sum(float(record["cost"]) for record in records)
    budget_cost = max(total_cost * budget_fraction, 0.0)
    ordered = sorted(records, key=lambda row: (row["rotation_priority"], row["sensitivity"]), reverse=True)
    ranks = {id(row): rank for rank, row in enumerate(ordered)}
    rotated_cost = 0.0
    result: list[dict[str, Any]] = []
    for row in records:
        rank = ranks[id(row)]
        priority_percentile = 1.0 - rank / max(len(records) - 1, 1)
        policy, reduction = choose_policy(str(row["role"]), priority_percentile, float(row["shape_imbalance"]))
        can_rotate = policy != "none" and rotated_cost + float(row["cost"]) <= budget_cost + 1.0e-9
        applied_policy = policy if can_rotate else "none"
        applied_reduction = reduction if can_rotate else 0.0
        if can_rotate:
            rotated_cost += float(row["cost"])
        projected = float(row["sensitivity"]) * (1.0 - applied_reduction)
        out = dict(row)
        out.update(
            {
                "rotation_rank": rank + 1,
                "rotation_priority_percentile": priority_percentile,
                "rotation_policy": applied_policy,
                "projected_reduction_factor": applied_reduction,
                "projected_sensitivity_after_rotation": projected,
                "projected_sensitivity_reduction": float(row["sensitivity"]) - projected,
            }
        )
        result.append(out)
    return sorted(result, key=lambda row: int(row["index"]))


def summarize(source: Path, payload: dict[str, Any], records: list[dict[str, Any]], budget_fraction: float) -> dict[str, Any]:
    total_cost = sum(float(row["cost"]) for row in records)
    rotated = [row for row in records if row["rotation_policy"] != "none"]
    base_delta = sum(float(row["sensitivity"]) for row in records)
    projected_delta = sum(float(row["projected_sensitivity_after_rotation"]) for row in records)
    policy_hist: dict[str, int] = {}
    role_hist: dict[str, int] = {}
    for row in records:
        policy = str(row["rotation_policy"])
        policy_hist[policy] = policy_hist.get(policy, 0) + 1
        if policy != "none":
            role = str(row["role"])
            role_hist[role] = role_hist.get(role, 0) + 1
    top_rotated = sorted(
        rotated,
        key=lambda row: (float(row["projected_sensitivity_reduction"]), float(row["sensitivity"])),
        reverse=True,
    )[:12]
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "method": "quarot_spinquant_style_rotation_baseline_proxy",
        "source": str(source),
        "model": payload.get("model"),
        "prompt_count": payload.get("prompt_count"),
        "probe_bits": payload.get("probe_bits"),
        "group_size": payload.get("group_size"),
        "rotation_budget_fraction": budget_fraction,
        "record_count": len(records),
        "rotated_count": len(rotated),
        "rotated_cost_fraction": sum(float(row["cost"]) for row in rotated) / max(total_cost, 1.0e-12),
        "base_positive_sensitivity": base_delta,
        "projected_positive_sensitivity_after_rotation": projected_delta,
        "projected_sensitivity_reduction": base_delta - projected_delta,
        "projected_reduction_ratio": (base_delta - projected_delta) / max(base_delta, 1.0e-12),
        "mean_rotation_priority": mean(float(row["rotation_priority"]) for row in records) if records else 0.0,
        "policy_hist": policy_hist,
        "rotated_role_hist": role_hist,
        "top_rotated_modules": [
            {
                "module": row["module"],
                "role": row["role"],
                "policy": row["rotation_policy"],
                "sensitivity": row["sensitivity"],
                "projected_reduction": row["projected_sensitivity_reduction"],
            }
            for row in top_rotated
        ],
        "records": records,
        "claim_boundary": (
            "Valid claim: this is an executable QuaRot/SpinQuant-style rotation/outlier-mitigation proxy over "
            "measured module sensitivity records. Invalid claim: this is a faithful official QuaRot or SpinQuant "
            "implementation, an activation-rotation kernel, or a quality-retention proof."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Rotation Family Baseline Proxy",
        "",
        f"Date: `{result['date']}`",
        f"Method: `{result['method']}`",
        f"Source: `{result['source']}`",
        f"Model: `{result.get('model')}`",
        f"Records: `{result['record_count']}`",
        f"Rotated modules: `{result['rotated_count']}`",
        f"Rotated cost fraction: `{result['rotated_cost_fraction']:.6f}`",
        f"Projected sensitivity reduction: `{result['projected_reduction_ratio']:.6f}`",
        "",
        "## Policy Histogram",
        "",
        "| policy | count |",
        "|---|---:|",
    ]
    for policy, count in sorted(result["policy_hist"].items()):
        lines.append(f"| `{policy}` | {count} |")
    lines.extend(
        [
            "",
            "## Top Rotated Modules",
            "",
            "| module | role | policy | sensitivity | projected reduction |",
            "|---|---|---|---:|---:|",
        ]
    )
    for row in result["top_rotated_modules"]:
        lines.append(
            f"| `{row['module']}` | `{row['role']}` | `{row['policy']}` | "
            f"{float(row['sensitivity']):.8f} | {float(row['projected_reduction']):.8f} |"
        )
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build rotation-family baseline proxy from measured sensitivity JSON.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--rotation-budget-fraction", type=float, default=0.35)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    payload = load_json(args.input)
    groups = payload.get("groups", []) or payload.get("records", [])
    if not isinstance(groups, list) or not groups:
        raise SystemExit(f"no groups/records found in {args.input}")
    enriched = enrich_records(groups)
    records = assign_rotation(enriched, args.rotation_budget_fraction)
    result = summarize(args.input, payload, records, args.rotation_budget_fraction)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "record_count": result["record_count"],
                "rotated_count": result["rotated_count"],
                "rotated_cost_fraction": result["rotated_cost_fraction"],
                "projected_reduction_ratio": result["projected_reduction_ratio"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
