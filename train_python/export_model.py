import argparse
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--adapter", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--precision", choices=["fp16", "fp32"], default="fp16")
    args = parser.parse_args()

    dtype = torch.float16 if args.precision == "fp16" else torch.float32
    base = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype, device_map="cpu")
    model = PeftModel.from_pretrained(base, args.adapter)
    merged = model.merge_and_unload()
    merged = merged.to(dtype=dtype)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    merged.save_pretrained(str(out), safe_serialization=True)
    tokenizer = AutoTokenizer.from_pretrained(args.adapter or args.model, use_fast=True)
    tokenizer.save_pretrained(str(out))
    print(f"saved merged {args.precision} model to {out}")


if __name__ == "__main__":
    main()

