# Qwen2.5-0.5B Loss-Sensitive Mixed-Precision Fake-Quant Report

Date: 2026-06-04

## Scope

This extends the Qwen uniform baseline with a Qwen-specific measured
loss-sensitivity allocation. It is still fake weight quantization, not a packed
runtime or hardware memory/latency result.

Model:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

Probe:

```text
Linear modules: 169
probe prompts: 2
probe bits: 4
group size: 128
target allocation: 4-bit base, selected 8-bit modules
budget: 4.5 average bits
```

Allocation summary:

```text
bit histogram: 4-bit=114, 8-bit=55
weighted avg bits: 4.4951
positive loss protected: 63.36%
```

## Results

WikiText2 validation slice, 128 prompts:

```text
FP16                  PPL 17.4294
uniform INT4          PPL 27.7411   delta NLL +0.4648
uniform INT3          PPL 514.0862  delta NLL +3.3842
loss-sensitive {4,8}  PPL 22.4605   delta NLL +0.2536
```

C4 English validation slice, 64 prompts:

```text
FP16                  PPL 23.9539
uniform INT4          PPL 36.5128   delta NLL +0.4215
uniform INT3          PPL 779.2680  delta NLL +3.4822
loss-sensitive {4,8}  PPL 31.2151   delta NLL +0.2648
```

## Interpretation

The Qwen-specific measured loss-sensitivity allocation improves over uniform
INT4 on both public-text slices while keeping the same fake-quant evaluator and
group size. This is stronger than the previous uniform-only Qwen baseline and
shows the mixed-precision scaffold transfers beyond SmolLM2.

The probe used only two prompts, so this should be treated as a short-cycle
engineering result. A paper-quality result still needs repeated calibration
sets, larger prompt counts, GPTQ/AWQ/SmoothQuant/rotation baselines, and packed
runtime measurements.

Evidence files:

```text
data_eval/eval_configs/qwen25_group128_with_loss_sensitive.json
outputs/qwen25_0p5b_module_loss_sensitivity_limit2_group128.json
outputs/qwen25_0p5b_module_loss_sensitivity_limit2_group128_report.md
outputs/qwen25_0p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_c4_en_validation_64_summary.json
```
