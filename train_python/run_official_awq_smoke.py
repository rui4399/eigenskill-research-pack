#!/usr/bin/env python3
from __future__ import annotations

"""Run a minimal AutoAWQ quantization smoke.

The quantized model directory is a local artifact and should not be committed.
Only the JSON/Markdown summaries are intended for the public evidence ledger.
"""

import argparse
import importlib.metadata
import json
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CALIBRATION_TEXTS = [
    "Mixed precision quantization protects sensitive transformer modules under a fixed memory budget.",
    "Calibration split instability means one small dataset may rank module sensitivity differently from another.",
    "AWQ searches activation-aware weight scales before packing low-bit model weights.",
    "A faithful baseline must report the package, quantization config, calibration size, and guard memory.",
]


def load_calibration_texts(paths: list[Path]) -> list[str]:
    if not paths:
        return list(CALIBRATION_TEXTS)
    texts: list[str] = []
    seen: set[str] = set()
    for path in paths:
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            text = raw_line.strip()
            if not text or text in seen:
                continue
            seen.add(text)
            texts.append(text)
    return texts


def build_calibration_plan(texts: list[str], tokenizer: Any, max_samples: int, max_seq_len: int) -> dict[str, Any]:
    accepted_lengths: list[int] = []
    skipped_lengths: list[int] = []
    for text in texts[:max_samples]:
        length = len(tokenizer.encode(text.strip()))
        if 0 < length <= max_seq_len:
            accepted_lengths.append(length)
        else:
            skipped_lengths.append(length)
    total_tokens = sum(accepted_lengths)
    expected_blocks = total_tokens // max_seq_len if max_seq_len > 0 else 0
    return {
        "accepted_sample_count": len(accepted_lengths),
        "skipped_sample_count": len(skipped_lengths),
        "accepted_token_lengths": accepted_lengths,
        "skipped_token_lengths": skipped_lengths,
        "total_accepted_tokens": total_tokens,
        "max_seq_len": max_seq_len,
        "expected_awq_blocks": expected_blocks,
        "ok": expected_blocks > 0,
    }


def artifact_summary(path: Path) -> dict[str, Any]:
    files = [item for item in path.rglob("*") if item.is_file()] if path.exists() else []
    total = sum(item.stat().st_size for item in files)
    suffix_counts: dict[str, int] = {}
    for item in files:
        suffix = item.suffix.lower() or "<none>"
        suffix_counts[suffix] = suffix_counts.get(suffix, 0) + 1
    return {
        "path": str(path),
        "file_count": len(files),
        "total_bytes": total,
        "suffix_counts": suffix_counts,
        "sample_files": [str(item.relative_to(path)) for item in files[:20]],
    }


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    artifact = payload.get("artifact", {})
    generation = payload.get("generation_smoke", {})
    calibration = payload.get("calibration", {})
    calibration_plan = calibration.get("plan", {}) if isinstance(calibration, dict) else {}
    lines = [
        "# Official AutoAWQ Smoke Summary",
        "",
        f"Date: `{payload['date']}`",
        f"Status: **{'PASS' if payload['passed'] else 'FAIL'}**",
        f"Model: `{payload['model']}`",
        f"Package: `{payload['package']['name']} {payload['package']['version']}`",
        f"Quant config: `{payload['quant_config']}`",
        f"Calibration samples: `{payload['calibration']['sample_count']}`",
        f"Calibration source: `{calibration.get('source')}`",
        f"Expected AWQ calibration blocks: `{calibration_plan.get('expected_awq_blocks')}`",
        f"Accepted calibration tokens: `{calibration_plan.get('total_accepted_tokens')}`",
        f"Elapsed seconds: `{payload['elapsed_seconds']:.3f}`",
        "",
        "## Artifact",
        "",
        f"- path: `{artifact.get('path')}`",
        f"- files: `{artifact.get('file_count')}`",
        f"- bytes: `{artifact.get('total_bytes')}`",
        f"- suffix counts: `{artifact.get('suffix_counts')}`",
        "",
        "## Generation Smoke",
        "",
        f"- ok: `{generation.get('ok')}`",
        f"- prompt: `{generation.get('prompt', '')}`",
        f"- text: `{generation.get('text', '')[:200]}`",
        "",
        "## Claim Boundary",
        "",
        "- This is a minimal official AutoAWQ execution smoke, not a competitive AWQ benchmark.",
        "- Quantized weights are local ignored artifacts; only this summary is intended for GitHub.",
    ]
    if payload.get("error"):
        lines.extend(["", "## Error", "", "```text", str(payload["error"]), "```"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a minimal official AutoAWQ smoke.")
    parser.add_argument("--model", default="Qwen/Qwen2.5-0.5B-Instruct")
    parser.add_argument("--save-dir", type=Path, default=Path("outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model"))
    parser.add_argument("--out-json", type=Path, default=Path("outputs/official_awq_smoke_qwen25_0p5b_summary_2026_06_07.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/OFFICIAL_AWQ_SMOKE_QWEN25_0P5B_2026_06_07.md"))
    parser.add_argument("--w-bit", type=int, default=4)
    parser.add_argument("--q-group-size", type=int, default=128)
    parser.add_argument("--version", default="GEMM")
    parser.add_argument("--max-calib-samples", type=int, default=4)
    parser.add_argument("--max-calib-seq-len", type=int, default=16)
    parser.add_argument("--calibration-prompts", type=Path, action="append", default=[])
    parser.add_argument("--max-chunk-memory-mib", type=int, default=256)
    parser.add_argument("--device-map", default="cuda:0")
    parser.add_argument("--max-new-tokens", type=int, default=12)
    args = parser.parse_args()

    started = time.time()
    payload: dict[str, Any] = {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": False,
        "model": args.model,
        "package": {"name": "autoawq", "version": ""},
        "quant_config": {
            "zero_point": True,
            "q_group_size": args.q_group_size,
            "w_bit": args.w_bit,
            "version": args.version,
        },
        "calibration": {
            "source": "default" if not args.calibration_prompts else [str(path) for path in args.calibration_prompts],
            "sample_count": 0,
            "max_calib_seq_len": args.max_calib_seq_len,
            "plan": {},
        },
        "artifact": {},
        "generation_smoke": {"ok": False},
        "error": "",
    }

    try:
        from awq import AutoAWQForCausalLM
        from transformers import AutoTokenizer

        calibration_texts = load_calibration_texts(args.calibration_prompts)
        payload["calibration"]["sample_count"] = min(args.max_calib_samples, len(calibration_texts))
        payload["package"]["version"] = importlib.metadata.version("autoawq")
        tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
        calibration_plan = build_calibration_plan(
            calibration_texts,
            tokenizer,
            args.max_calib_samples,
            args.max_calib_seq_len,
        )
        payload["calibration"]["plan"] = calibration_plan
        if not calibration_plan["ok"]:
            raise ValueError(
                "AutoAWQ calibration would produce zero blocks; lower --max-calib-seq-len "
                "or provide more short calibration samples."
            )
        model = AutoAWQForCausalLM.from_pretrained(
            args.model,
            device_map=args.device_map,
            safetensors=True,
            trust_remote_code=True,
        )
        model.quantize(
            tokenizer,
            quant_config=payload["quant_config"],
            calib_data=calibration_texts[: args.max_calib_samples],
            max_calib_samples=args.max_calib_samples,
            max_calib_seq_len=args.max_calib_seq_len,
            n_parallel_calib_samples=1,
            max_chunk_memory=args.max_chunk_memory_mib * 1024 * 1024,
        )
        args.save_dir.mkdir(parents=True, exist_ok=True)
        model.save_quantized(str(args.save_dir), safetensors=True)
        tokenizer.save_pretrained(str(args.save_dir))
        payload["artifact"] = artifact_summary(args.save_dir)

        generation_device = "cuda" if "cuda" in str(args.device_map) else "cpu"
        if hasattr(model, "model"):
            model.model.to(generation_device)
        prompt = "Give one short reason calibration robustness matters."
        inputs = tokenizer(prompt, return_tensors="pt").to(generation_device)
        generated = model.generate(**inputs, max_new_tokens=args.max_new_tokens)
        text = tokenizer.decode(generated[0], skip_special_tokens=True)
        payload["generation_smoke"] = {"ok": bool(text.strip()), "prompt": prompt, "text": text}
        payload["passed"] = payload["artifact"].get("file_count", 0) > 0 and payload["generation_smoke"]["ok"]
    except Exception as exc:  # pragma: no cover - runtime diagnostic path
        payload["error"] = repr(exc)
        payload["traceback"] = traceback.format_exc()

    payload["elapsed_seconds"] = time.time() - started
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, payload)
    print(json.dumps({"passed": payload["passed"], "out_json": str(args.out_json), "error": payload["error"]}, indent=2))
    raise SystemExit(0 if payload["passed"] else 1)


if __name__ == "__main__":
    main()
