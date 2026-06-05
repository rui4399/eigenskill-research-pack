# SmolLM2-1.7B Full-Module Random16 Result

Date: `2026-06-05`
Model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`

This closes the earlier small SmolLM2 ambiguity by expanding the sensitivity
probe from 32 Linear modules to all 169 Linear modules. It is still a
short-slice PyTorch fake-quant diagnostic, not a packed runtime or hardware
latency result.

## Sensitivity Probe

```text
calibration prompts: WikiText2 validation, 8 prompts
max length: 128
measured Linear modules: 169 / 169
probe bits: 4
group size: 128
budget avg bits: 4.5
```

Allocation summary:

```text
uniform INT4 modules:        169 x 4-bit
loss-sensitive full modules: 156 x 4-bit, 13 x 8-bit
loss-sensitive avg bits:     4.5
protected positive delta:    0.7179
```

## PPL Evaluation

Short slice:

```text
evaluation prompts: WikiText2 validation, 16 prompts
max length: 128

FP16 PPL:                12.6903
uniform INT4 PPL:        18.1431
loss_sensitive_full PPL: 13.9866
best random16 PPL:       14.7340
random16 mean PPL:       17.5858
```

Margins:

```text
loss-sensitive full vs uniform INT4: +4.1565 PPL
loss-sensitive full vs best random16: +0.7474 PPL
loss-sensitive full vs random16 mean: +3.5992 PPL
gap vs FP16:                           +1.2963 PPL
```

Longer slice:

```text
evaluation prompts: WikiText2 validation, 64 prompts
max length: 128

FP16 PPL:                12.6568
uniform INT4 PPL:        18.5164
loss_sensitive_full PPL: 14.8877
best random16 PPL:       15.6654
random16 mean PPL:       18.1114
```

Margins:

```text
loss-sensitive full vs uniform INT4: +3.6286 PPL
loss-sensitive full vs best random16: +0.7777 PPL
loss-sensitive full vs random16 mean: +3.2236 PPL
gap vs FP16:                           +2.2309 PPL
```

Cross-dataset slice:

```text
evaluation prompts: C4 English validation, 64 prompts
max length: 128

FP16 PPL:                18.4497
uniform INT4 PPL:        26.3475
loss_sensitive_full PPL: 21.4269
best random16 PPL:       22.5529
random16 mean PPL:       26.1102
```

Margins:

```text
loss-sensitive full vs uniform INT4: +4.9206 PPL
loss-sensitive full vs best random16: +1.1260 PPL
loss-sensitive full vs random16 mean: +4.6833 PPL
gap vs FP16:                           +2.9772 PPL
```

Longest WikiText2 slice in this run:

```text
evaluation prompts: WikiText2 validation, 128 prompts
max length: 128

FP16 PPL:                13.2171
uniform INT4 PPL:        18.7966
loss_sensitive_full PPL: 15.3641
best random16 PPL:       16.2050
random16 mean PPL:       18.5168
```

Margins:

```text
loss-sensitive full vs uniform INT4: +3.4325 PPL
loss-sensitive full vs best random16: +0.8409 PPL
loss-sensitive full vs random16 mean: +3.1527 PPL
gap vs FP16:                           +2.1469 PPL
```

The full-module result repairs the earlier 32-module failure mode:
`loss_sensitive_limit8` beat uniform INT4 and random mean, but lost to the
best random16 seed by `-0.0341` PPL. With all Linear modules measured, the
same style of loss-sensitive budget beats the best random16 allocation by
`+0.7474` PPL on the 16-prompt WikiText2 slice and `+0.7777` PPL on the
64-prompt WikiText2 slice. The 128-prompt WikiText2 slice remains positive at
`+0.8409` PPL versus best random16. The same allocation also stays positive on
the 64-prompt C4 slice, which is a useful overfitting check because the
allocation was built from WikiText2 calibration prompts.

## GPU Guard

```text
sensitivity max memory: 4971 / 8151 MiB = 60.99%
PPL-16 max memory:      5133 / 8151 MiB = 62.97%
PPL-64 max memory:      5679 / 8151 MiB = 69.67%
PPL-128 max memory:     5027 / 8151 MiB = 61.67%
C4-64 max memory:       5674 / 8151 MiB = 69.61%
max-memory-ratio:       0.85
killed by guard:        false
```

## Artifacts

```text
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.csv
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.json
outputs/smollm2_1p7b_full_gpu_guard_summary.md
outputs/smollm2_1p7b_full_gpu_guard_summary.csv
outputs/smollm2_1p7b_full_gpu_guard_summary.json
outputs/smollm2_1p7b_sensitivity_full_limit8_gpu_guard.json
outputs/smollm2_1p7b_module_loss_sensitivity_full_limit8_group128.json
outputs/smollm2_1p7b_module_loss_sensitivity_full_limit8_group128_report.md
outputs/smollm2_1p7b_loss_sensitive_alloc_full_4to8_limit8_group128_summary.json
outputs/smollm2_1p7b_full_cpp_random16_4p5_summary.json
outputs/smollm2_1p7b_full_cpp_random16_4p5_summary.csv
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_16_summary.json
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_16_guard.json
outputs/smollm2_1p7b_full_random16_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_evidence_matrix.csv
outputs/smollm2_1p7b_full_random16_evidence_matrix.json
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_64_summary.json
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_64_guard.json
outputs/smollm2_1p7b_full_random16_wikitext2_64_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_wikitext2_64_evidence_matrix.csv
outputs/smollm2_1p7b_full_random16_wikitext2_64_evidence_matrix.json
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_128_summary.json
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_128_guard.json
outputs/smollm2_1p7b_full_random16_wikitext2_128_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_wikitext2_128_evidence_matrix.csv
outputs/smollm2_1p7b_full_random16_wikitext2_128_evidence_matrix.json
outputs/smollm2_1p7b_full_random16_ppl_c4_64_summary.json
outputs/smollm2_1p7b_full_random16_ppl_c4_64_guard.json
outputs/smollm2_1p7b_full_random16_c4_64_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_c4_64_evidence_matrix.csv
outputs/smollm2_1p7b_full_random16_c4_64_evidence_matrix.json
data_eval/eval_configs/smollm2_1p7b_full_random16_compare.json
```
