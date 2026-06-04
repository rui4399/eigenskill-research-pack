# Qwen2.5-1.5B Uniform Fake-Quant Smoke

Date: 2026-06-04

This is a completed local smoke run for `Qwen/Qwen2.5-1.5B-Instruct`.
It replaces the earlier failed-at-download note. The model weights are stored
outside this repository and are not committed.

## Local Model

```text
path: C:\Users\18042\models\Qwen2.5-1.5B-Instruct
model.safetensors bytes: 3,087,467,144
model.safetensors sha256: DD924A11B4C220F385B51FFA522DAEA7C9F3D850E31B162BB5661DF483C6D3EE
tensor count: 338
model type: qwen2
hidden size: 1536
layers: 28
parameters: 1,543,714,304
```

The model was loaded offline with `HF_HUB_OFFLINE=1` and
`TRANSFORMERS_OFFLINE=1`, confirming the local snapshot is usable.

## Command

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
python3 train_python/eval_weight_quant_ppl.py \
  --model /mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 16 \
  --max-length 128 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_1p5b_fake_quant_ppl_uniform_group128_wikitext2_16_summary.json
```

## Result

WikiText2 validation slice, 16 prompts, group size 128:

| config | PPL | delta NLL vs FP16 | ratio vs FP16 | bit hist |
|---|---:|---:|---:|---|
| FP16 | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| uniform INT4 | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| uniform INT3 | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |

## Scope

These are fake weight-quantization quality diagnostics. They are not packed
runtime latency, memory, or energy results. The 16-prompt slice is a smoke
baseline for stronger-model coverage, not a full benchmark.

Evidence files:

```text
outputs/qwen25_1p5b_fake_quant_ppl_uniform_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_uniform_smoke_ppl_table.json
outputs/qwen25_1p5b_uniform_smoke_ppl_table.csv
outputs/qwen25_1p5b_uniform_smoke_ppl_table.md
```
