#!/usr/bin/env python3
from __future__ import annotations

"""Measure real generation TTFT, tokens/s, and GPU memory for a HF causal LM."""

import argparse
import json
import time
from pathlib import Path

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None
    TextIteratorStreamer = None

from threading import Thread


DEFAULT_PROMPT = "Explain mixed-precision quantization in one concise paragraph."


def sync_if_cuda(device: str) -> None:
    if torch is not None and device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.synchronize()


def peak_memory_mib(device: str) -> float:
    if torch is None or not device.startswith("cuda") or not torch.cuda.is_available():
        return 0.0
    return float(torch.cuda.max_memory_allocated() / (1024 * 1024))


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure TTFT, tokens/s, and peak GPU memory.")
    parser.add_argument("--model", default="Qwen/Qwen3-0.6B")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--max-new-tokens", type=int, default=64)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--out", default="outputs/real_system_packer_2026-06-05/qwen3_generation_latency.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    else:
        prompt = args.prompt
    if not prompt:
        raise SystemExit("empty prompt")

    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    if args.device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map=args.device,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    gen_kwargs = {
        **inputs,
        "max_new_tokens": args.max_new_tokens,
        "do_sample": False,
        "streamer": streamer,
        "pad_token_id": tokenizer.eos_token_id,
    }

    sync_if_cuda(args.device)
    start = time.perf_counter()
    thread = Thread(target=model.generate, kwargs=gen_kwargs)
    thread.start()

    first_text_time = None
    chunks: list[str] = []
    for chunk in streamer:
        now = time.perf_counter()
        if first_text_time is None and chunk:
            first_text_time = now
        chunks.append(chunk)
    thread.join()
    sync_if_cuda(args.device)
    end = time.perf_counter()

    generated_text = "".join(chunks)
    generated_ids = tokenizer(generated_text, return_tensors="pt", add_special_tokens=False).input_ids
    generated_tokens = int(generated_ids.numel())
    elapsed = end - start
    ttft = None if first_text_time is None else first_text_time - start
    result = {
        "model": args.model,
        "device": str(model.device),
        "dtype": args.dtype,
        "prompt_tokens": int(inputs.input_ids.numel()),
        "generated_tokens_text_retokenized": generated_tokens,
        "max_new_tokens": args.max_new_tokens,
        "ttft_seconds": ttft,
        "elapsed_seconds": elapsed,
        "tokens_per_second": generated_tokens / elapsed if elapsed > 0 else None,
        "peak_gpu_memory_mib": peak_memory_mib(args.device),
        "generated_text": generated_text,
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
