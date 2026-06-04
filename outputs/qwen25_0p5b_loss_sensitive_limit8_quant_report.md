# Qwen2.5-0.5B Loss-Sensitive Mixed-Precision Fake-Quant Report, 8-Prompt Probe

Date: 2026-06-04

## Scope

This report upgrades the earlier Qwen loss-sensitivity probe from 2 calibration
prompts to 8 calibration prompts. It is still fake weight quantization, not a
packed runtime or hardware memory/latency result.

Model:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

Probe:

```text
Linear modules: 169
probe prompts: 8
probe bits: 4
group size: 128
target allocation: 4-bit base, selected 8-bit modules
budget: 4.5 average bits
```

Allocation summary:

```text
bit histogram: 4-bit=112, 8-bit=57
weighted avg bits: 4.4969
positive loss protected: 59.01%
```

## Results

WikiText2 validation slice, 128 prompts:

```text
FP16                         PPL 17.4294
uniform INT4                 PPL 27.7411   delta NLL +0.4648
uniform INT3                 PPL 514.0862  delta NLL +3.3842
loss-sensitive {4,8}, 2p     PPL 22.4605   delta NLL +0.2536
loss-sensitive {4,8}, 8p     PPL 21.9762   delta NLL +0.2318
```

C4 English validation slice, 64 prompts:

```text
FP16                         PPL 23.9539
uniform INT4                 PPL 36.5128   delta NLL +0.4215
uniform INT3                 PPL 779.2680  delta NLL +3.4822
loss-sensitive {4,8}, 2p     PPL 31.2151   delta NLL +0.2648
loss-sensitive {4,8}, 8p     PPL 30.7970   delta NLL +0.2513
```

## Interpretation

The 8-prompt measured loss-sensitivity allocation improves over both uniform
INT4 and the earlier 2-prompt allocation on WikiText2-128 and C4-64. This is a
stronger short-cycle signal that the measured-loss allocation is not merely a
single tiny-calibration accident.

Remaining limitations:

- the evaluator is fake quantization and dequantizes weights back to floating
  point;
- the calibration set is still small;
- there are no GPTQ/AWQ/SmoothQuant/rotation baselines yet;
- there is no packed runtime latency or memory measurement.

Evidence files:

```text
data_eval/eval_configs/qwen25_group128_with_loss_sensitive_limit8.json
outputs/qwen25_0p5b_module_loss_sensitivity_limit8_group128.json
outputs/qwen25_0p5b_module_loss_sensitivity_limit8_group128_report.md
outputs/qwen25_0p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_c4_en_validation_64_summary.json
```
