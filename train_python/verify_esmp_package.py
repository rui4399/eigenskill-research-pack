#!/usr/bin/env python3
from __future__ import annotations

"""Verify ESMP package summaries against manifests and binary package headers."""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from esmp_format import read_esmp


WINDOWS_ABS = re.compile(r"^[A-Za-z]:[\\/]")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_external_path(raw: str | Path, base: Path) -> Path:
    text = str(raw)
    normalized = text.replace("\\", "/")
    if normalized.startswith("/mnt/") and len(normalized) > 7 and normalized[6] == "/":
        drive = normalized[5].upper()
        rest = normalized[7:].replace("/", "\\")
        return Path(f"{drive}:\\{rest}")
    if WINDOWS_ABS.match(text):
        return Path(text)
    value = Path(text)
    return value if value.is_absolute() else base / value


def close_enough(left: Any, right: Any, tolerance: float = 1.0e-5) -> bool:
    try:
        return abs(float(left) - float(right)) <= tolerance
    except (TypeError, ValueError):
        return False


def require_equal(failures: list[str], label: str, observed: Any, expected: Any) -> None:
    if observed != expected:
        failures.append(f"{label}: observed={observed!r} expected={expected!r}")


def require_close(failures: list[str], label: str, observed: Any, expected: Any, tolerance: float = 1.0e-5) -> None:
    if not close_enough(observed, expected, tolerance):
        failures.append(f"{label}: observed={observed!r} expected={expected!r}")


def verify_module(module: dict[str, Any], summary_dir: Path) -> dict[str, Any]:
    name = str(module.get("module", "unknown"))
    package_path = normalize_external_path(module.get("out", ""), summary_dir)
    manifest_path = normalize_external_path(module.get("manifest", ""), summary_dir)
    failures: list[str] = []
    missing: list[str] = []
    if not package_path.exists():
        missing.append(str(package_path))
    if not manifest_path.exists():
        missing.append(str(manifest_path))
    if missing:
        return {
            "module": name,
            "passed": False,
            "missing": missing,
            "failures": [],
            "package_path": str(package_path),
            "manifest_path": str(manifest_path),
        }

    manifest = load_json(manifest_path)
    esmp = read_esmp(package_path)
    hist = esmp.bit_histogram

    require_equal(failures, "format", manifest.get("format"), "ESMPQ001")
    require_equal(failures, "rows", int(manifest.get("rows", -1)), esmp.rows)
    require_equal(failures, "cols", int(manifest.get("cols", -1)), esmp.cols)
    require_close(failures, "avg_bits", manifest.get("avg_bits"), esmp.avg_bits)
    require_equal(failures, "raw_fp32_bytes", int(manifest.get("raw_fp32_bytes", -1)), esmp.raw_fp32_bytes)
    require_equal(failures, "packed_payload_bytes", int(manifest.get("packed_payload_bytes", -1)), esmp.data_bytes)
    require_equal(failures, "total_package_bytes", int(manifest.get("total_package_bytes", -1)), esmp.package_bytes)
    require_close(
        failures,
        "compression_ratio_vs_fp32",
        manifest.get("compression_ratio_vs_fp32"),
        esmp.compression_vs_fp32,
    )
    require_equal(failures, "row_bits_histogram", manifest.get("row_bits_histogram", {}), hist)

    packer = module.get("packer", {}) or {}
    if packer:
        require_equal(failures, "packer.rows", int(packer.get("rows", -1)), esmp.rows)
        require_equal(failures, "packer.cols", int(packer.get("cols", -1)), esmp.cols)
        require_equal(failures, "packer.total_package_bytes", int(packer.get("total_package_bytes", -1)), esmp.package_bytes)
        if packer.get("verify_ok") is False:
            failures.append("packer.verify_ok: observed=false expected=true")

    return {
        "module": name,
        "passed": not failures,
        "missing": [],
        "failures": failures,
        "package_path": str(package_path),
        "manifest_path": str(manifest_path),
        "rows": esmp.rows,
        "cols": esmp.cols,
        "avg_bits": esmp.avg_bits,
        "bit_histogram": hist,
        "package_bytes": esmp.package_bytes,
        "raw_fp32_bytes": esmp.raw_fp32_bytes,
        "compression_ratio_vs_fp32": esmp.compression_vs_fp32,
    }


def verify_summary(
    summary_path: Path,
    limit_modules: int = 0,
    min_checked: int = 1,
    max_missing: int = 0,
    min_compression_vs_fp32: float = 0.0,
) -> dict[str, Any]:
    summary = load_json(summary_path)
    modules = list(summary.get("modules", []) or [])
    if limit_modules > 0:
        modules = modules[:limit_modules]
    entries = [verify_module(module, summary_path.parent) for module in modules]
    checked = [entry for entry in entries if not entry["missing"]]
    failed = [entry for entry in entries if entry["failures"]]
    missing_count = sum(len(entry["missing"]) for entry in entries)
    raw_fp32_bytes = sum(int(entry.get("raw_fp32_bytes", 0)) for entry in checked)
    package_bytes = sum(int(entry.get("package_bytes", 0)) for entry in checked)
    compression = raw_fp32_bytes / max(float(package_bytes), 1.0)

    failures: list[str] = []
    if len(checked) < min_checked:
        failures.append(f"checked module count below threshold: {len(checked)} < {min_checked}")
    if missing_count > max_missing:
        failures.append(f"missing file count above threshold: {missing_count} > {max_missing}")
    if failed:
        failures.append(f"module metadata mismatches: {len(failed)}")
    if min_compression_vs_fp32 > 0.0 and compression < min_compression_vs_fp32:
        failures.append(f"compression below threshold: {compression:.6f} < {min_compression_vs_fp32:.6f}")

    summary_metrics = {
        "checked_module_count": len(checked),
        "requested_module_count": len(modules),
        "missing_file_count": missing_count,
        "failed_module_count": len(failed),
        "compression_ratio_vs_fp32_checked": compression,
    }

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary_path": str(summary_path),
        "model": summary.get("model"),
        "method": summary.get("method"),
        "module_count_in_summary": len(summary.get("modules", []) or []),
        "module_count_requested": len(modules),
        "checked_module_count": len(checked),
        "missing_file_count": missing_count,
        "failed_module_count": len(failed),
        "raw_fp32_bytes_checked": raw_fp32_bytes,
        "package_bytes_checked": package_bytes,
        "compression_ratio_vs_fp32_checked": compression,
        "summary": summary_metrics,
        "failures": failures,
        "entries": entries,
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    status = "PASS" if report["passed"] else "FAIL"
    lines = [
        "# ESMP Package Verification",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{status}**",
        f"Summary: `{str(report['summary_path']).replace(chr(92), '/')}`",
        f"Model: `{report.get('model')}`",
        f"Method: `{report.get('method')}`",
        "",
        "## Aggregate",
        "",
        f"- checked modules: `{report['checked_module_count']} / {report['module_count_requested']}`",
        f"- missing files: `{report['missing_file_count']}`",
        f"- failed modules: `{report['failed_module_count']}`",
        f"- checked compression vs FP32: `{report['compression_ratio_vs_fp32_checked']:.6f}x`",
        "",
        "## Module Checks",
        "",
        "| module | status | shape | avg bits | compression | notes |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for entry in report["entries"]:
        row_status = "PASS" if entry["passed"] else "FAIL"
        shape = f"{entry.get('rows', 'n/a')}x{entry.get('cols', 'n/a')}"
        avg_bits = entry.get("avg_bits")
        avg_bits_text = f"{float(avg_bits):.4f}" if avg_bits is not None else "n/a"
        compression = entry.get("compression_ratio_vs_fp32")
        compression_text = f"{float(compression):.4f}x" if compression is not None else "n/a"
        notes = "; ".join(entry.get("failures") or entry.get("missing") or ["ok"]).replace("|", "\\|")
        lines.append(f"| `{entry['module']}` | **{row_status}** | {shape} | {avg_bits_text} | {compression_text} | {notes} |")
    lines.extend(["", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify ESMP pack_summary.json against manifests and binary headers.")
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--limit-modules", type=int, default=0)
    parser.add_argument("--min-checked", type=int, default=1)
    parser.add_argument("--max-missing", type=int, default=0)
    parser.add_argument("--min-compression-vs-fp32", type=float, default=0.0)
    parser.add_argument("--out-json", type=Path)
    parser.add_argument("--out-md", type=Path)
    args = parser.parse_args()

    report = verify_summary(
        args.summary,
        limit_modules=args.limit_modules,
        min_checked=args.min_checked,
        max_missing=args.max_missing,
        min_compression_vs_fp32=args.min_compression_vs_fp32,
    )
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.out_md:
        write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "checked": report["checked_module_count"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
