#!/usr/bin/env python3
from __future__ import annotations

"""Export selected Qwen linear weights into real ESMP mixed-precision packages.

The C++ ``mixed_precision_packer`` consumes raw FP32 row-major matrices plus a
per-row bit assignment. This script bridges Hugging Face checkpoints and the
existing EigenSkill-Q allocation JSONs:

1. load a causal LM;
2. parse a module-level consensus/allocation file;
3. export each selected Linear weight to a temporary FP32 file;
4. invoke the C++ packer to produce ``.esmp`` binary packages and JSON manifests.

Large model files and generated ``.esmp`` packages are intentionally local-only.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    import torch
    from transformers import AutoModelForCausalLM
except ModuleNotFoundError:  # pragma: no cover - dependency checked at runtime
    torch = None
    AutoModelForCausalLM = None


DEFAULT_MODEL = "Qwen/Qwen3-0.6B"
DEFAULT_ALLOCATION = "outputs/qwen3_0p6b_cpp_allocation_planner_4p5_summary.json"
DEFAULT_PACKER = "build/cpp-wsl/mixed_precision_packer"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def resolve_path(path: str | Path, base: Path) -> Path:
    value = Path(path)
    return value if value.is_absolute() else base / value


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def allocation_bits(data: dict[str, Any], method: str) -> list[int]:
    allocations = data.get("allocations", {})
    if method not in allocations:
        raise KeyError(f"allocation method not found: {method}; available={list(allocations)}")
    value = allocations[method]
    if isinstance(value, list):
        if all(isinstance(item, int) for item in value):
            return [int(item) for item in value]
        bits = []
        for item in value:
            if not isinstance(item, dict):
                raise TypeError(f"unsupported allocation item: {item!r}")
            for key in ("bits", "bit", "assigned_bits", "precision_bits"):
                if key in item:
                    bits.append(int(item[key]))
                    break
            else:
                raise KeyError(f"allocation item has no bits field: {item}")
        return bits
    if isinstance(value, dict):
        for key in ("bits", "allocation", "assignments"):
            if key in value and isinstance(value[key], list):
                return [int(item) if not isinstance(item, dict) else int(item.get("bits", item.get("bit"))) for item in value[key]]
    raise TypeError(f"unsupported allocation structure for {method}: {type(value).__name__}")


def module_names(data: dict[str, Any], allocation_path: Path) -> list[str]:
    groups = data.get("groups", [])
    names = [str(group.get("module") or group.get("name") or "") for group in groups if isinstance(group, dict)]
    if names and all(names):
        return names

    stats_json = data.get("stats_json")
    if stats_json:
        stats_path = resolve_path(str(stats_json).replace("\\", "/"), allocation_path.parent)
        if not stats_path.exists():
            stats_path = resolve_path(str(stats_json).replace("\\", "/"), repo_root())
        stats = load_json(stats_path)
        stats_groups = stats.get("groups", [])
        names = [str(group.get("module") or group.get("name") or "") for group in stats_groups if isinstance(group, dict)]
        if names and all(names):
            return names
    raise ValueError("allocation JSON does not contain recoverable module names")


def load_module_bits(allocation_path: Path, method: str) -> tuple[dict[str, int], dict[str, Any]]:
    data = load_json(allocation_path)
    bits = allocation_bits(data, method)
    names = module_names(data, allocation_path)
    if len(bits) != len(names):
        raise ValueError(f"allocation/module length mismatch: bits={len(bits)} names={len(names)}")
    return {name: int(bit) for name, bit in zip(names, bits)}, data


def find_packer(path: str, root: Path) -> Path:
    packer = resolve_path(path, root)
    if os.name == "nt" and not packer.exists():
        exe = packer.with_suffix(".exe")
        if exe.exists():
            return exe
    if not packer.exists():
        raise FileNotFoundError(f"mixed_precision_packer not found: {packer}")
    return packer


def write_weight_f32(weight: "torch.Tensor", path: Path) -> tuple[int, int]:
    if weight.ndim != 2:
        raise ValueError(f"expected 2D Linear weight, got shape={tuple(weight.shape)}")
    rows, cols = int(weight.shape[0]), int(weight.shape[1])
    array = weight.detach().to(device="cpu", dtype=torch.float32).contiguous().numpy()
    array.tofile(path)
    return rows, cols


def run_packer(
    packer: Path,
    raw_path: Path,
    out_path: Path,
    manifest_path: Path,
    rows: int,
    cols: int,
    bits: int,
    verify: bool,
    row_bits_file: Path | None = None,
) -> dict[str, Any]:
    cmd = [
        str(packer),
        "--weights-f32",
        str(raw_path),
        "--rows",
        str(rows),
        "--cols",
        str(cols),
        "--default-bits",
        str(bits),
        "--out",
        str(out_path),
        "--manifest-out",
        str(manifest_path),
    ]
    if row_bits_file is not None:
        cmd.extend(["--row-bits-file", str(row_bits_file)])
    if verify:
        cmd.append("--verify")
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"packer failed for {out_path.name}:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}


def safe_name(module_name: str) -> str:
    return module_name.replace(".", "__").replace("/", "_")


def main() -> None:
    parser = argparse.ArgumentParser(description="Pack Qwen Linear weights into ESMP mixed-precision binaries.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--allocation", default=DEFAULT_ALLOCATION)
    parser.add_argument("--method", default="loss_sensitive_budget")
    parser.add_argument("--packer", default=DEFAULT_PACKER)
    parser.add_argument("--out-dir", default="outputs/real_system_packer_2026-06-05/qwen3_esmp")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--limit-modules", type=int, default=0)
    parser.add_argument("--module-filter", default="")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")

    root = repo_root()
    allocation_path = resolve_path(args.allocation, root)
    packer = find_packer(args.packer, root)
    out_dir = resolve_path(args.out_dir, root)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_dir = out_dir / "manifests"
    manifest_dir.mkdir(parents=True, exist_ok=True)

    module_bits, allocation_data = load_module_bits(allocation_path, args.method)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map=args.device,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )

    packed = []
    skipped = []
    with tempfile.TemporaryDirectory(prefix="eigenskill_pack_") as tmp:
        tmp_dir = Path(tmp)
        for module_name, module in model.named_modules():
            if args.module_filter and args.module_filter not in module_name:
                continue
            if module_name not in module_bits:
                continue
            if not isinstance(module, torch.nn.Linear):
                skipped.append({"module": module_name, "reason": "not_linear"})
                continue
            bits = int(module_bits[module_name])
            raw_path = tmp_dir / f"{safe_name(module_name)}.f32"
            rows, cols = write_weight_f32(module.weight, raw_path)
            out_path = out_dir / f"{safe_name(module_name)}.esmp"
            manifest_path = manifest_dir / f"{safe_name(module_name)}.json"
            result = run_packer(packer, raw_path, out_path, manifest_path, rows, cols, bits, args.verify)
            packed.append(
                {
                    "module": module_name,
                    "bits": bits,
                    "rows": rows,
                    "cols": cols,
                    "out": str(out_path),
                    "manifest": str(manifest_path),
                    "packer": result,
                }
            )
            if args.limit_modules and len(packed) >= args.limit_modules:
                break

    total_package_bytes = sum(Path(item["out"]).stat().st_size for item in packed)
    raw_fp32_bytes = sum(int(item["rows"]) * int(item["cols"]) * 4 for item in packed)
    summary = {
        "model": args.model,
        "allocation": str(allocation_path),
        "method": args.method,
        "group_count": allocation_data.get("group_count"),
        "packed_module_count": len(packed),
        "skipped": skipped,
        "raw_fp32_bytes": raw_fp32_bytes,
        "total_package_bytes": total_package_bytes,
        "compression_ratio_vs_fp32": raw_fp32_bytes / max(total_package_bytes, 1),
        "modules": packed,
    }
    summary_path = out_dir / "pack_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
