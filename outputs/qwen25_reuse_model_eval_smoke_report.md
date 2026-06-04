# Qwen2.5 Reuse-Model Evaluation Smoke Check

Date: 2026-06-04

## Purpose

`train_python/eval_weight_quant_ppl.py` now supports `--reuse-model`. In this
mode the evaluator loads the model once, caches the original Linear weights on
CPU, restores those weights before each config, and then applies the requested
fake-quant mode. The default behavior remains unchanged.

## Smoke Check

Command shape:

```bash
python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 8 \
  --max-length 128 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_group128_with_loss_sensitive_limit8.json \
  --reuse-model \
  --out outputs/qwen25_0p5b_reuse_model_smoke_limit8_wikitext2_8_summary.json
```

The same 8-prompt smoke was also run with the old reload-per-config behavior:

```text
outputs/qwen25_0p5b_reload_model_smoke_limit8_wikitext2_8_summary.json
```

Result:

```text
fp16                         mean NLL diff 0.0
uniform_int4                 mean NLL diff 0.0
uniform_int3                 mean NLL diff 0.0
loss_sensitive_4to8_limit8   mean NLL diff 0.0
```

This verifies that `--reuse-model` preserves the measured outputs for this
smoke case while avoiding repeated model loads.
