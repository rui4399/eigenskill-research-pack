# SmolLM2-360M Output-Sensitivity Proxy Report

Date: 2026-06-04

## Purpose

This experiment adds a cheaper quantization sensitivity proxy between the early
activation-statistic proxy and the expensive one-module loss probe.

For each Linear module, it samples calibration inputs `x` and estimates the
normalized output perturbation after group-wise INT4 fake quantization:

```text
E ||x(W - Q(W))^T||^2 / E ||xW^T||^2
```

The proxy allocation upgrades modules with high normalized output MSE to 8-bit
under the same 4.5 average-bit budget.

## Measurement

Command:

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 \
  train_python/measure_module_output_sensitivity.py \
  --prompts data_eval/text_prompts/wikitext2_validation_32.txt \
  --limit-prompts 4 \
  --max-length 128 \
  --group-size 128 \
  --sample-rows-per-module 128 \
  --progress-every 24 \
  --out-json outputs/smollm2_module_output_sensitivity_limit4_group128.json \
  --out-md outputs/smollm2_module_output_sensitivity_limit4_group128_report.md \
  --out-allocation outputs/smollm2_output_sensitive_alloc_4to8_limit4_group128_summary.json
```

Summary:

```text
Linear modules:              225
sample rows per module:      128
budget avg bits:             4.5
output-sensitive allocation: 4-bit=135, 8-bit=90
protected output proxy:      54.50%
```

## PPL Results

WikiText2 validation, 128 prompts:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 17.3436 | 0.0000 | 16:225 |
| uniform INT4 | 27.8236 | 0.4727 | 4:225 |
| activation-stat RD 4/8 | 24.5117 | 0.3459 | 4:172, 8:53 |
| loss-sensitive 4/8 | 24.1374 | 0.3305 | 4:172, 8:53 |
| loss-sensitive swap-search 4/8 | 24.0661 | 0.3276 | 4:172, 8:53 |
| output-sensitive 4/8 | 25.2084 | 0.3739 | 4:135, 8:90 |

C4 English validation, 64 streamed prompts:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 23.7821 | 0.0000 | 16:225 |
| uniform INT4 | 36.9390 | 0.4403 | 4:225 |
| activation-stat RD 4/8 | 33.6940 | 0.3484 | 4:172, 8:53 |
| loss-sensitive 4/8 | 32.7675 | 0.3205 | 4:172, 8:53 |
| loss-sensitive swap-search 4/8 | 32.5731 | 0.3146 | 4:172, 8:53 |
| output-sensitive 4/8 | 33.7088 | 0.3488 | 4:135, 8:90 |

## Interpretation

Output reconstruction error is a useful engineering proxy, but in this scaffold
it is weaker than measured one-module loss sensitivity:

```text
WikiText2-128: output-sensitive 25.21 vs loss-sensitive 24.14
C4-64:         output-sensitive 33.71 vs loss-sensitive 32.77
```

It also performs slightly worse than the activation-stat RD allocation on both
public-text slices. This is a valuable negative result for the paper: local
reconstruction objectives are not automatically aligned with global language
model loss, even when they measure the actual output perturbation of a module.

The result supports a more careful proxy comparison section:

```text
activation-stat proxy < output reconstruction proxy < measured loss proxy
```

is not guaranteed. The current evidence is:

```text
measured loss proxy > activation-stat proxy ~= output reconstruction proxy
```

under this fake-quant scaffold.

## Evidence Files

```text
train_python/measure_module_output_sensitivity.py
outputs/smollm2_module_output_sensitivity_limit4_group128.json
outputs/smollm2_module_output_sensitivity_limit4_group128_report.md
outputs/smollm2_output_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_c4_en_validation_64_summary.json
```
