#!/usr/bin/env python3
from __future__ import annotations

"""Create a small ESMP package-summary variant with selected modules repacked.

This is a targeted quality-preservation probe for fused QKV replacement. It
keeps the existing full-package summary and only replaces selected module
entries with newly packed ESMP files, for example layer-0 q_proj/k_proj at
8-bit. The generated package is local-only and should not be committed.
"""

import argparse
import json
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import torch
    from transformers import AutoModelForCausalLM
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    AutoModelForCausalLM = None

from eval_esmp_module_reconstruction import DEFAULT_MODEL, resolve_path, repo_root
from pack_qwen3_consensus import DEFAULT_PACKER, find_packer, run_packer, safe_name, write_weight_f32


DEFAULT_BASE_SUMMARY = "outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json"


def parse_module_bits(text: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"expected module=bits override, got: {part}")
        name, bits_text = part.split("=", 1)
        name = name.strip()
        bits = int(bits_text.strip())
        if bits not in (2, 3, 4, 5, 6, 7, 8):
            raise ValueError(f"unsupported bit width for {name}: {bits}")
        result[name] = bits
    if not result:
        raise ValueError("no module bit overrides provided")
    return result


def parse_optional_module_bits(text: str) -> dict[str, int]:
    if not text.strip():
        return {}
    return parse_module_bits(text)


def parse_row_overrides(text: str) -> dict[str, list[tuple[int, int, int]]]:
    """Parse module:start:end=bits row-range overrides.

    Entries are separated by semicolons or commas. Ranges are half-open
    [start, end). A single-row form module:row=bits is also accepted.
    """

    result: dict[str, list[tuple[int, int, int]]] = {}
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"expected module:start:end=bits row override, got: {part}")
        lhs, bits_text = part.rsplit("=", 1)
        bits = int(bits_text.strip())
        if bits not in (2, 3, 4, 5, 6, 7, 8):
            raise ValueError(f"unsupported row bit width in {part}: {bits}")
        fields = lhs.rsplit(":", 2)
        if len(fields) == 3:
            module_name, start_text, end_text = fields
            start = int(start_text)
            end = int(end_text)
        elif len(fields) == 2:
            module_name, row_text = fields
            start = int(row_text)
            end = start + 1
        else:
            raise ValueError(f"expected module:start:end=bits row override, got: {part}")
        module_name = module_name.strip()
        if not module_name:
            raise ValueError(f"empty module name in row override: {part}")
        if start < 0 or end <= start:
            raise ValueError(f"invalid row range in {part}: {start}:{end}")
        result.setdefault(module_name, []).append((start, end, bits))
    return result


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Repack selected ESMP modules at override bit widths.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-summary", default=DEFAULT_BASE_SUMMARY)
    parser.add_argument("--module-bits", default="", help="Comma-separated module=bits overrides.")
    parser.add_argument(
        "--row-overrides",
        default="",
        help="Comma/semicolon-separated module:start:end=bits row overrides; ranges are half-open.",
    )
    parser.add_argument("--packer", default=DEFAULT_PACKER)
    parser.add_argument("--out-dir", default="outputs/real_system_packer_2026-06-05/qwen3_0p6b_qkv_guard")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")

    root = repo_root()
    base_summary_path = resolve_path(args.base_summary, root)
    base_summary = load_json(base_summary_path)
    overrides = parse_optional_module_bits(args.module_bits)
    row_overrides = parse_row_overrides(args.row_overrides)
    targets = sorted(set(overrides) | set(row_overrides))
    if not targets:
        raise SystemExit("provide at least one --module-bits or --row-overrides entry")
    packer = find_packer(args.packer, root)
    out_dir = resolve_path(args.out_dir, root)
    manifest_dir = out_dir / "manifests"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_dir.mkdir(parents=True, exist_ok=True)

    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map=args.device,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model_modules = dict(model.named_modules())

    updated = deepcopy(base_summary)
    modules = list(updated.get("modules", []))
    by_name = {str(item.get("module")): item for item in modules if isinstance(item, dict)}
    missing = [name for name in targets if name not in by_name]
    if missing:
        raise SystemExit(f"override modules not present in base summary: {missing}")

    repacked: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="eigenskill_repack_") as tmp:
        tmp_dir = Path(tmp)
        for module_name in targets:
            module = model_modules.get(module_name)
            if module is None or not isinstance(module, torch.nn.Linear):
                raise SystemExit(f"model module is not Linear or does not exist: {module_name}")
            raw_path = tmp_dir / f"{safe_name(module_name)}.f32"
            rows, cols = write_weight_f32(module.weight, raw_path)
            item = by_name[module_name]
            default_bits = int(overrides.get(module_name, int(item.get("bits", 4))))
            row_ranges = row_overrides.get(module_name, [])
            row_bits_file: Path | None = None
            row_override_records = []
            if row_ranges:
                row_bits = [default_bits] * rows
                for start, end, bits in row_ranges:
                    if end > rows:
                        raise SystemExit(f"row override out of bounds for {module_name}: {start}:{end}, rows={rows}")
                    for row in range(start, end):
                        row_bits[row] = bits
                    row_override_records.append({"start": start, "end": end, "bits": bits})
                row_bits_file = tmp_dir / f"{safe_name(module_name)}.row_bits.txt"
                row_bits_file.write_text("\n".join(str(value) for value in row_bits) + "\n", encoding="ascii")
            suffix = f"__{default_bits}bit" if not row_ranges else "__rowguard"
            out_path = out_dir / f"{safe_name(module_name)}{suffix}.esmp"
            manifest_path = manifest_dir / f"{safe_name(module_name)}{suffix}.json"
            packer_result = run_packer(
                packer,
                raw_path,
                out_path,
                manifest_path,
                rows,
                cols,
                default_bits,
                args.verify,
                row_bits_file=row_bits_file,
            )
            item["bits"] = default_bits
            item["rows"] = rows
            item["cols"] = cols
            item["out"] = str(out_path)
            item["manifest"] = str(manifest_path)
            item["packer"] = packer_result
            if row_override_records:
                item["row_overrides"] = row_override_records
                item["avg_bits"] = packer_result.get("avg_bits")
            repacked.append(
                {
                    "module": module_name,
                    "bits": default_bits,
                    "row_overrides": row_override_records,
                    "rows": rows,
                    "cols": cols,
                    "out": str(out_path),
                    "manifest": str(manifest_path),
                    "packer": packer_result,
                }
            )

    total_package_bytes = sum(Path(str(item["out"])).stat().st_size for item in modules if "out" in item)
    raw_fp32_bytes = sum(int(item.get("rows", 0)) * int(item.get("cols", 0)) * 4 for item in modules)
    updated["base_summary"] = str(base_summary_path)
    updated["precision_guard_overrides"] = dict(sorted(overrides.items()))
    updated["precision_guard_row_overrides"] = {
        name: [{"start": start, "end": end, "bits": bits} for start, end, bits in ranges]
        for name, ranges in sorted(row_overrides.items())
    }
    updated["repacked_modules"] = repacked
    updated["total_package_bytes"] = int(total_package_bytes)
    updated["raw_fp32_bytes"] = int(raw_fp32_bytes)
    updated["compression_ratio_vs_fp32"] = float(raw_fp32_bytes / max(total_package_bytes, 1))

    out_summary = out_dir / "pack_summary.json"
    out_summary.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"out_summary": str(out_summary), "repacked": repacked, "compression_ratio_vs_fp32": updated["compression_ratio_vs_fp32"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
