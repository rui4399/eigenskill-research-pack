#!/usr/bin/env python3
from __future__ import annotations

"""Build a paper-facing ledger from executable evidence gates."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CATEGORIES = {
    "quality": "quality",
    "prompt": "quality",
    "triton": "kernel",
    "selector": "runtime wiring",
    "selected": "selected-row",
    "cpp": "c++ runtime",
    "sidecar": "decode integration",
    "qkv": "qkv replacement",
    "chat": "task retention",
    "esmp": "artifact integrity",
    "package": "artifact integrity",
    "artifact": "artifact integrity",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_gate_spec(spec: str) -> tuple[str, Path]:
    if "=" not in spec:
        raise ValueError(f"gate spec must be LABEL=PATH: {spec}")
    label, raw_path = spec.split("=", 1)
    label = label.strip()
    if not label:
        raise ValueError(f"empty gate label in spec: {spec}")
    return label, Path(raw_path)


def finite_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def infer_category(label: str) -> str:
    lower = label.lower()
    for token, category in CATEGORIES.items():
        if token in lower:
            return category
    return "evidence"


def metric_parts(summary: dict[str, Any]) -> list[str]:
    parts: list[str] = []
    if "valid_configs" in summary:
        parts.append(f"configs {summary.get('valid_configs')}/{summary.get('total_configs')}")
    if "fp16_wins" in summary:
        parts.append(f"FP16 wins {summary.get('fp16_wins')}")
    if (value := finite_float(summary.get("best_fp16_speedup"))) is not None:
        parts.append(f"best FP16 {value:.4f}x")
    if "selector_call_count" in summary:
        parts.append(f"selector calls {summary.get('selector_call_count')}")
    if "ok_rows" in summary:
        parts.append(f"ok rows {summary.get('ok_rows')}")
    if "wins_vs_full" in summary:
        parts.append(f"wins/full {summary.get('wins_vs_full')}")
    if (value := finite_float(summary.get("median_selected_speedup_vs_full"))) is not None:
        parts.append(f"median selected {value:.4f}x")
    if "sidecar_call_count" in summary:
        parts.append(f"sidecar calls {summary.get('sidecar_call_count')}")
    if "replacement_count" in summary:
        parts.append(f"replacements {summary.get('replacement_count')}")
    if (value := finite_float(summary.get("tokens_per_second_ratio_vs_baseline"))) is not None:
        parts.append(f"tok/s ratio {value:.4f}x")
    if (value := finite_float(summary.get("ttft_ratio_vs_baseline"))) is not None:
        parts.append(f"TTFT ratio {value:.4f}x")
    if "exact_matches" in summary and "prompts" in summary:
        parts.append(f"exact {summary.get('exact_matches')}/{summary.get('prompts')}")
    if "regressions" in summary and "tasks" in summary:
        parts.append(f"regressions {summary.get('regressions')}")
    if "fused_passes" in summary and "tasks" in summary:
        parts.append(f"fused {summary.get('fused_passes')}/{summary.get('tasks')}")
    if "checked_module_count" in summary:
        parts.append(f"checked modules {summary.get('checked_module_count')}/{summary.get('requested_module_count')}")
    if "missing_file_count" in summary:
        parts.append(f"missing files {summary.get('missing_file_count')}")
    if "failed_module_count" in summary:
        parts.append(f"failed modules {summary.get('failed_module_count')}")
    if (value := finite_float(summary.get("mean_speedup_fused_vs_baseline"))) is not None:
        parts.append(f"mean speed {value:.4f}x")
    if (value := finite_float(summary.get("replacement_compression_vs_fp32"))) is not None:
        parts.append(f"compression {value:.4f}x")
    if (value := finite_float(summary.get("median_compression_vs_fp32"))) is not None:
        parts.append(f"compression {value:.4f}x")
    if (value := finite_float(summary.get("compression_ratio_vs_fp32_checked"))) is not None:
        parts.append(f"checked compression {value:.4f}x")
    if (value := finite_float(summary.get("guard_max_memory_used_ratio"))) is not None:
        parts.append(f"VRAM {value:.4f}")
    if (value := finite_float(summary.get("max_guard_vram_ratio"))) is not None:
        parts.append(f"VRAM {value:.4f}")
    return parts


def summarize_gate(label: str, path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    summary = payload.get("summary", {}) or {}
    failures = list(payload.get("failures", []) or [])
    passed = bool(payload.get("passed"))
    return {
        "label": label,
        "category": infer_category(label),
        "path": str(path),
        "passed": passed,
        "failures": failures,
        "metrics": "; ".join(metric_parts(summary)) or "n/a",
        "summary": summary,
    }


def build_ledger(gates: list[tuple[str, Path]]) -> dict[str, Any]:
    entries = [summarize_gate(label, path, load_json(path)) for label, path in gates]
    failed = [entry for entry in entries if not entry["passed"]]
    categories = sorted({entry["category"] for entry in entries})
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failed,
        "gate_count": len(entries),
        "passed_count": len(entries) - len(failed),
        "failed_count": len(failed),
        "categories": categories,
        "entries": entries,
        "failures": [
            {"label": entry["label"], "path": entry["path"], "failures": entry["failures"]}
            for entry in failed
        ],
    }


def write_markdown(path: Path, ledger: dict[str, Any]) -> None:
    lines = [
        "# Evidence Ledger",
        "",
        f"Date: `{ledger['date']}`",
        f"Status: **{'PASS' if ledger['passed'] else 'FAIL'}**",
        f"Gates: `{ledger['passed_count']} / {ledger['gate_count']}` passed",
        f"Categories: `{', '.join(ledger['categories'])}`",
        "",
        "## Gate Summary",
        "",
        "| gate | category | status | key metrics | source |",
        "|---|---|---|---|---|",
    ]
    for entry in ledger["entries"]:
        source = str(entry["path"]).replace("\\", "/")
        status = "PASS" if entry["passed"] else "FAIL"
        metrics = str(entry["metrics"]).replace("|", "\\|")
        lines.append(f"| `{entry['label']}` | {entry['category']} | **{status}** | {metrics} | `{source}` |")
    lines.extend(["", "## Failures", ""])
    if ledger["failures"]:
        for failure in ledger["failures"]:
            lines.append(f"- `{failure['label']}`: {failure['failures']}")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: each listed row is backed by an executable gate JSON that passed under its configured thresholds.",
            "- Invalid claim: passing this ledger proves SOTA quantization, mobile deployment, or full paper readiness.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an evidence ledger from gate JSON files.")
    parser.add_argument("--gate", action="append", required=True, help="LABEL=gate_json")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/evidence_ledger.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER.md"))
    args = parser.parse_args()

    gates = [parse_gate_spec(spec) for spec in args.gate]
    ledger = build_ledger(gates)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, ledger)
    print(json.dumps({"passed": ledger["passed"], "gate_count": ledger["gate_count"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if ledger["passed"] else 1)


if __name__ == "__main__":
    main()
