import argparse
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    model = AutoModelForCausalLM.from_pretrained(args.model_dir, torch_dtype=torch.float32, device_map="cpu")
    quantized = torch.quantization.quantize_dynamic(
        model,
        {torch.nn.Linear},
        dtype=torch.qint8,
    )
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    torch.save(quantized.state_dict(), out / "pytorch_model_int8_dynamic_state_dict.pt")
    AutoTokenizer.from_pretrained(args.model_dir, use_fast=True).save_pretrained(str(out))
    (out / "README.md").write_text(
        "Dynamic INT8 CPU state_dict export. Use for high-precision CPU-side experiments; not a GGUF export.\n",
        encoding="utf-8",
    )
    print(f"saved dynamic int8 state_dict to {out}")


if __name__ == "__main__":
    main()

