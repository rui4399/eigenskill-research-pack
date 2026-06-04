#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_allocation(path: str, method: str) -> tuple[list[dict], list[int], dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["groups"], [int(x) for x in data["allocations"][method]], data


def load_ppl(path: str) -> dict[str, float]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {item["name"]: float(item["metrics"]["ppl"]) for item in data["results"]}


def bit_hist(bits: list[int]) -> dict[str, int]:
    hist: dict[str, int] = {}
    for bit in bits:
        hist[str(bit)] = hist.get(str(bit), 0) + 1
    return hist


def selected_modules(groups: list[dict], bits: list[int], high_bits: int) -> set[str]:
    return {group["module"] for group, bit in zip(groups, bits) if bit == high_bits}


def changed_modules(groups: list[dict], a_bits: list[int], b_bits: list[int], limit: int) -> list[dict]:
    rows = []
    for group, a_bit, b_bit in zip(groups, a_bits, b_bits):
        if a_bit == b_bit:
            continue
        rows.append(
            {
                "module": group["module"],
                "from_bits": a_bit,
                "to_bits": b_bit,
                "param_count": int(group.get("param_count", group.get("weight_params", 0))),
                "positive_delta_nll": float(group.get("positive_delta_nll", 0.0)),
                "sensitivity_rank": int(group.get("sensitivity_rank", 0)),
            }
        )
    rows.sort(key=lambda item: (item["from_bits"], -item["positive_delta_nll"], item["module"]))
    return rows[:limit]


def markdown_report(result: dict) -> str:
    lines = [
        "# Allocation Stability Report",
        "",
        f"Left allocation: `{result['left_path']}`",
        f"Right allocation: `{result['right_path']}`",
        "",
        "## Summary",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| modules | {result['module_count']} |",
        f"| left high-bit modules | {result['left_high_count']} |",
        f"| right high-bit modules | {result['right_high_count']} |",
        f"| overlap high-bit modules | {result['overlap_count']} |",
        f"| Jaccard | {result['jaccard']:.4f} |",
        f"| unchanged bit decisions | {result['unchanged_count']} |",
        f"| changed bit decisions | {result['changed_count']} |",
        "",
        "## PPL",
        "",
        "| split | fp16 | uniform int4 | left allocation | right allocation | right vs left |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for split in result["ppl"]:
        lines.append(
            f"| {split['name']} | {split['fp16']:.4f} | {split['uniform_int4']:.4f} | "
            f"{split['left']:.4f} | {split['right']:.4f} | {split['right_minus_left']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Changed Modules",
            "",
            "| module | from | to | params | positive delta NLL | rank |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["changed_modules"]:
        lines.append(
            f"| `{item['module']}` | {item['from_bits']} | {item['to_bits']} | "
            f"{item['param_count']} | {item['positive_delta_nll']:.6f} | {item['sensitivity_rank']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The comparison measures whether the selected 8-bit module set is stable when",
            "the calibration probe changes. PPL is reported separately because a lower",
            "Jaccard does not necessarily mean worse downstream quality.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--left-method", default="loss_sensitive_4to8")
    parser.add_argument("--right", required=True)
    parser.add_argument("--right-method", default="loss_sensitive_4to8")
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--left-wikitext-ppl", default="")
    parser.add_argument("--right-wikitext-ppl", default="")
    parser.add_argument("--left-c4-ppl", default="")
    parser.add_argument("--right-c4-ppl", default="")
    parser.add_argument("--changed-limit", type=int, default=30)
    parser.add_argument("--out-json", default="outputs/allocation_stability_summary.json")
    parser.add_argument("--out-md", default="outputs/allocation_stability_report.md")
    args = parser.parse_args()

    left_groups, left_bits, _left_data = load_allocation(args.left, args.left_method)
    right_groups, right_bits, _right_data = load_allocation(args.right, args.right_method)
    if len(left_groups) != len(right_groups):
        raise SystemExit("allocation group counts differ")
    left_modules = [group["module"] for group in left_groups]
    right_modules = [group["module"] for group in right_groups]
    if left_modules != right_modules:
        raise SystemExit("allocation module order differs")

    left_selected = selected_modules(left_groups, left_bits, args.high_bits)
    right_selected = selected_modules(right_groups, right_bits, args.high_bits)
    overlap = left_selected & right_selected
    union = left_selected | right_selected
    unchanged = sum(1 for a_bit, b_bit in zip(left_bits, right_bits) if a_bit == b_bit)

    ppl_rows = []
    if args.left_wikitext_ppl and args.right_wikitext_ppl:
        left_w = load_ppl(args.left_wikitext_ppl)
        right_w = load_ppl(args.right_wikitext_ppl)
        ppl_rows.append(
            {
                "name": "WikiText2-128",
                "fp16": right_w["fp16"],
                "uniform_int4": right_w["uniform_int4"],
                "left": left_w.get("loss_sensitive_4to8", left_w.get("loss_sensitive_4to8_limit8")),
                "right": right_w.get("loss_sensitive_4to8_limit8", right_w.get("loss_sensitive_4to8")),
            }
        )
    if args.left_c4_ppl and args.right_c4_ppl:
        left_c = load_ppl(args.left_c4_ppl)
        right_c = load_ppl(args.right_c4_ppl)
        ppl_rows.append(
            {
                "name": "C4-64",
                "fp16": right_c["fp16"],
                "uniform_int4": right_c["uniform_int4"],
                "left": left_c.get("loss_sensitive_4to8", left_c.get("loss_sensitive_4to8_limit8")),
                "right": right_c.get("loss_sensitive_4to8_limit8", right_c.get("loss_sensitive_4to8")),
            }
        )
    for row in ppl_rows:
        row["right_minus_left"] = row["right"] - row["left"]

    result = {
        "left_path": args.left,
        "right_path": args.right,
        "left_bit_hist": bit_hist(left_bits),
        "right_bit_hist": bit_hist(right_bits),
        "module_count": len(left_groups),
        "left_high_count": len(left_selected),
        "right_high_count": len(right_selected),
        "overlap_count": len(overlap),
        "union_count": len(union),
        "jaccard": len(overlap) / max(len(union), 1),
        "unchanged_count": unchanged,
        "changed_count": len(left_bits) - unchanged,
        "ppl": ppl_rows,
        "changed_modules": changed_modules(left_groups, left_bits, right_bits, args.changed_limit),
    }

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "jaccard": result["jaccard"]}, indent=2))


if __name__ == "__main__":
    main()
