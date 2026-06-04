# Qwen2.5-0.5B Uniform Fake-Quant Baseline

Date: 2026-06-04

## Scope

This is a stronger-model sanity check for the existing fake weight-quantization
scaffold. It does not apply EigenSkill-Q mixed-precision allocation to Qwen yet.
Only three configurations are evaluated:

- FP16
- uniform INT4, group size 128
- uniform INT3, group size 128

Model:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

Commands:

```bash
python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 128 \
  --max-length 160 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_wikitext2_128_summary.json

python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/c4_en_validation_64.txt \
  --limit-prompts 64 \
  --max-length 160 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_c4_en_validation_64_summary.json
```

## Results

WikiText2 validation slice, 128 prompts:

```text
FP16          PPL 17.4294
uniform INT4  PPL 27.7411   delta NLL +0.4648
uniform INT3  PPL 514.0862  delta NLL +3.3842
```

C4 English validation slice, 64 prompts:

```text
FP16          PPL 23.9539
uniform INT4  PPL 36.5128   delta NLL +0.4215
uniform INT3  PPL 779.2680  delta NLL +3.4822
```

## Interpretation

The fake-quant scaffold now runs on a stronger cached model than SmolLM2-360M.
The result is a baseline only: INT4 degrades PPL but stays finite on both text
slices, while INT3 is much more destructive. No Qwen-specific mixed-precision
allocation is claimed yet because the existing allocation files are tied to
SmolLM2 module names and sensitivity probes.

Evidence files:

```text
data_eval/eval_configs/qwen25_uniform_group128.json
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_c4_en_validation_64_summary.json
```
