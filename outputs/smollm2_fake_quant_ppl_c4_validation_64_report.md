# SmolLM2-360M C4 Validation Fake-Quant Report

Date: 2026-06-04

## Purpose

This report adds a second public-text validation source for the EigenSkill-Q
loss-sensitive allocation track. The evaluation is still group-wise fake
quantization, not a production quantized runtime.

## Prompt Slice

The C4 validation prompts were built with Hugging Face streaming mode to avoid
downloading the full 1024-shard validation set:

```bash
python3 train_python/build_dataset_prompts.py \
  --dataset allenai/c4 \
  --name en \
  --split validation \
  --text-field text \
  --limit 64 \
  --min-chars 160 \
  --max-chars 900 \
  --streaming \
  --out data_eval/text_prompts/c4_en_validation_64.txt
```

Prompt build summary:

```text
scanned rows: 66
prompts:      64
streaming:    true
```

## Evaluation

Command:

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 \
  train_python/eval_weight_quant_ppl.py \
  --prompts data_eval/text_prompts/c4_en_validation_64.txt \
  --limit-prompts 64 \
  --max-length 160 \
  --group-size 128 \
  --config-json data_eval/eval_configs/smollm2_group128_compare_allocations.json \
  --out outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
```

## Result

| method | prompts | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 64 | 23.7821 | 0.0000 | 16:225 |
| uniform INT4 | 64 | 36.9390 | 0.4403 | 4:225 |
| uniform INT3 | 64 | 2990.7973 | 4.8344 | 3:225 |
| activation-stat RD 4/8 | 64 | 33.6940 | 0.3484 | 4:172, 8:53 |
| loss-sensitive 4/8 | 64 | 32.7675 | 0.3205 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 64 | 32.8657 | 0.3235 | 4:175, 8:50 |
| loss-sensitive swap-search 4/8 | 64 | 32.5731 | 0.3146 | 4:172, 8:53 |

## Interpretation

The C4 slice reproduces the WikiText2 ordering:

```text
uniform INT4             PPL 36.94
activation-stat RD 4/8   PPL 33.69
loss-sensitive 4/8       PPL 32.77
swap-search 4/8          PPL 32.57
```

This strengthens the evidence that measured one-module loss sensitivity is a
better allocation signal than the earlier activation-statistic proxy, and that a
small amount of global-feedback policy improvement can improve the allocation.

The result is still limited by fake quantization, a small 64-prompt slice, and
the absence of GPTQ/AWQ/SmoothQuant/rotation baselines.

## Evidence Files

```text
data_eval/text_prompts/c4_en_validation_64.txt
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
train_python/build_dataset_prompts.py
train_python/eval_weight_quant_ppl.py
```
