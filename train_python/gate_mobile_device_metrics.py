#!/usr/bin/env python3
from __future__ import annotations

"""Gate real mobile device TTFT/tokens/s/peak-memory metrics."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def metric(metrics: dict[str, Any], *names: str) -> float:
    for name in names:
        if name in metrics:
            try:
                return float(metrics[name])
            except (TypeError, ValueError):
                return 0.0
    return 0.0


def memory_mb(metrics: dict[str, Any]) -> float:
    mb = metric(metrics, "peak_memory_mb", "peak_rss_mb", "peak_pss_mb", "max_rss_mb")
    if mb > 0.0:
        return mb
    kb = metric(metrics, "peak_memory_kb", "peak_rss_kb", "peak_pss_kb", "max_rss_kb")
    if kb > 0.0:
        return kb / 1024.0
    bytes_value = metric(metrics, "peak_memory_bytes", "peak_rss_bytes", "peak_pss_bytes", "max_rss_bytes")
    return bytes_value / (1024.0 * 1024.0) if bytes_value > 0.0 else 0.0


def identity_text(props: dict[str, Any]) -> str:
    values = []
    for key, value in sorted(props.items()):
        if isinstance(value, (str, int, float)) and value != "":
            values.append(f"{key}={value}")
    return " ".join(values).lower()


def build_result(payload: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    props = payload.get("device_props", {}) or {}
    metrics = payload.get("benchmark_metrics", {}) or {}
    model = str(props.get("ro.product.marketname") or props.get("ro.product.model") or "")
    device = str(props.get("ro.product.device") or "")
    ttft = metric(metrics, "ttft_seconds", "ttft_s", "time_to_first_token_seconds")
    tok_s = metric(metrics, "tokens_per_second", "tok_s", "tps")
    peak_mb = memory_mb(metrics)
    generated_tokens = metric(metrics, "generated_tokens", "tokens")

    if not payload.get("real_device_connected"):
        failures.append("real_device_connected is false")
    required_tokens = [token.strip().lower() for token in args.required_model_tokens.split(",") if token.strip()]
    identity = identity_text(props)
    for token in required_tokens:
        if token not in identity:
            failures.append(f"device identity lacks token {token!r}: {identity!r}")
    if ttft <= 0.0 or ttft > args.max_ttft_seconds:
        failures.append(f"ttft {ttft:.6f} is not in (0, {args.max_ttft_seconds}]")
    if tok_s < args.min_tokens_per_second:
        failures.append(f"tokens/s {tok_s:.6f} < required {args.min_tokens_per_second:.6f}")
    if peak_mb <= 0.0:
        failures.append("peak memory metric is missing")
    if generated_tokens < args.min_generated_tokens:
        failures.append(f"generated tokens {generated_tokens:.0f} < required {args.min_generated_tokens}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "model": model,
            "device": device,
            "identity": identity,
            "ttft_seconds": ttft,
            "tokens_per_second": tok_s,
            "peak_memory_mb": peak_mb,
            "generated_tokens": generated_tokens,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: real mobile metrics exist for the selected device and satisfy configured thresholds. "
            "Invalid claim: this gate says anything about unmeasured devices, thermal stability, or energy."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Mobile Device Metrics Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- device: `{summary['device']}`",
        f"- TTFT seconds: `{summary['ttft_seconds']:.6f}`",
        f"- tokens/s: `{summary['tokens_per_second']:.6f}`",
        f"- peak memory MB: `{summary['peak_memory_mb']:.2f}`",
        f"- generated tokens: `{summary['generated_tokens']:.0f}`",
        "",
        "## Failures",
        "",
    ]
    if result["failures"]:
        for failure in result["failures"]:
            lines.append(f"- {failure}")
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate real mobile device metrics.")
    parser.add_argument("--input-json", type=Path, required=True)
    parser.add_argument("--required-model-tokens", default="redmi,k80")
    parser.add_argument("--max-ttft-seconds", type=float, default=30.0)
    parser.add_argument("--min-tokens-per-second", type=float, default=0.1)
    parser.add_argument("--min-generated-tokens", type=int, default=1)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    result = build_result(load_json(args.input_json), args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "out_json": str(args.out_json)}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
