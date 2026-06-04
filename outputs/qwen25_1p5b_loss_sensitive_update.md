# Qwen2.5-1.5B Loss-Sensitive Allocation Update

Date: 2026-06-04

This update extends the 1.5B smoke baseline from uniform fake quantization to a
measured loss-sensitive `{4,8}` mixed-precision allocation.

## Calibration

```text
model: /mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct
calibration prompts: 2 from WikiText2 validation slice
max length: 128
probe bits: 4
group size: 128
linear modules measured: 197
```

Allocation summary:

```text
uniform INT4:
  bit histogram: 4-bit=197
  avg bits: 4.0000

loss-sensitive {4,8}:
  bit histogram: 4-bit=137, 8-bit=60
  avg bits: 4.4993
  budget used: 0.9999
  protected positive delta NLL: 60.20%
```

## Downstream PPL

WikiText2 validation slice, 16 prompts:

| config | PPL | delta NLL vs FP16 | ratio vs FP16 | bit hist |
|---|---:|---:|---:|---|
| FP16 | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| uniform INT4 | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| uniform INT3 | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |
| loss-sensitive `{4,8}`, 2p | 13.7652 | 0.198844 | 1.2200 | `{"4": 137, "8": 60}` |

Compared with uniform INT4, the 2-prompt loss-sensitive allocation reduces PPL
from `15.8383` to `13.7652` on the same 16-prompt slice.

C4 English validation slice, 32 prompts:

| config | PPL | delta NLL vs FP16 | ratio vs FP16 | bit hist |
|---|---:|---:|---:|---|
| FP16 | 17.8832 | 0.000000 | 1.0000 | `{"16": 197}` |
| uniform INT4 | 23.5711 | 0.276159 | 1.3181 | `{"4": 197}` |
| uniform INT3 | 289.1918 | 2.783229 | 16.1700 | `{"3": 197}` |
| loss-sensitive `{4,8}`, 2p | 22.8859 | 0.246660 | 1.2797 | `{"4": 137, "8": 60}` |

The same allocation also improves the C4 smoke slice, but the gain is smaller:
PPL drops from `23.5711` to `22.8859`.

## Scope

This is still fake weight quantization, not a packed low-bit runtime. It is a
stronger-model quality diagnostic that shows the measured allocation signal is
useful on Qwen2.5-1.5B under a small calibration budget across two short text
slices.

## 8-prompt calibration and consensus update

An 8-prompt sensitivity probe was added on the same model, prompt source, max
length, and group size:

```text
linear modules measured:       197
8p allocation bit histogram:   4-bit=136, 8-bit=61
8p weighted average bits:      4.4953
8p protected positive delta:   54.45%
2p/8p high-bit Jaccard:        0.6351
changed bit decisions:         27/197
```

Downstream fake-quant PPL:

| dataset | uniform INT4 | 2p loss-sensitive | 8p loss-sensitive | consensus |
|---|---:|---:|---:|---:|
| WikiText2-16 | 15.8383 | 13.7652 | 13.7622 | 13.7140 |
| C4-32 | 23.5711 | 22.8859 | 21.9642 | 22.1526 |

The 8-prompt calibration improves the C4 slice materially and is tied with the
2-prompt allocation on WikiText2. The consensus allocation is more stable with
respect to both probes: it selects 65 modules for 8-bit, overlaps 57 of the 60
2-prompt high-bit modules, and overlaps 55 of the 61 8-prompt high-bit modules.
It is the best WikiText2-16 point in this short smoke slice, while the direct
8-prompt allocation is the best C4-32 point.

Evidence files:

```text
data_eval/eval_configs/qwen25_1p5b_group128_with_loss_sensitive.json
data_eval/eval_configs/qwen25_1p5b_group128_with_loss_sensitive_limit8.json
data_eval/eval_configs/qwen25_1p5b_group128_with_consensus.json
outputs/qwen25_1p5b_module_loss_sensitivity_limit2_group128.json
outputs/qwen25_1p5b_module_loss_sensitivity_limit2_group128_report.md
outputs/qwen25_1p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_loss_sensitive_ppl_table.md
outputs/qwen25_1p5b_loss_sensitive_two_dataset_ppl_table.md
outputs/qwen25_1p5b_sensitivity_compact_summary.md
outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128.json
outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128_report.md
outputs/qwen25_1p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_limit8_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_limit8_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_sensitivity_limit8_compact_summary.md
outputs/qwen25_1p5b_loss_sensitive_2p_vs_8p_stability_report.md
outputs/qwen25_1p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json
outputs/qwen25_1p5b_loss_sensitive_consensus_alloc_4to8_group128_report.md
outputs/qwen25_1p5b_fake_quant_ppl_consensus_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_consensus_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_loss_sensitive_2p8p_consensus_ppl_table.md
```
