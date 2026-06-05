# SmolLM2-1.7B Loss-Sensitive Retry Result

This is the first closed-loop fake-quant result for
`HuggingFaceTB/SmolLM2-1.7B-Instruct` after repairing the PyTorch weight cache.

## Sensitivity Probe

```text
calibration prompts: WikiText2 validation, 8 prompts
max length: 128
measured Linear modules: 32
probe bits: 4
group size: 128
budget avg bits: 4.5
```

Allocation summary:

```text
uniform INT4 modules:          32 x 4-bit
loss-sensitive modules:        27 x 4-bit, 5 x 8-bit
loss-sensitive avg bits:       4.4706
budget used:                   0.9935
protected positive delta ratio: 0.6298
```

## PPL Evaluation

```text
evaluation prompts: WikiText2 validation, 16 prompts
max length: 128

FP16 PPL:                  12.6903
uniform INT4 PPL:          18.1431
loss_sensitive_limit8 PPL: 12.8844
```

Margins:

```text
loss-sensitive vs uniform INT4: +5.2587 PPL
loss-sensitive gap vs FP16:      +0.1941 PPL
```

## GPU Guard

```text
sensitivity max memory: 4939 / 8151 MiB = 60.59%
PPL max memory:         5117 / 8151 MiB = 62.78%
killed by guard:        false
```

## Interpretation

This is a useful third-model positive result: a small loss-sensitive mixed
precision allocation recovers most of the uniform INT4 degradation on
SmolLM2-1.7B. Scope remains limited: only 32 Linear modules were measured and
only 16 WikiText2 prompts were evaluated. It should be expanded to all Linear
modules and random-budget baselines before being treated as a main paper
result.

## Random16 Follow-Up

The same 16-prompt slice was evaluated against 16 random budget allocations:

```text
loss_sensitive_limit8 PPL: 12.8844
best random16 PPL:        12.8503
random16 mean PPL:        12.9795
target vs best random16:  -0.0341 PPL
target vs random16 mean:  +0.0951 PPL
```

This is a useful negative/ambiguous result. The small loss-sensitive allocation
beats uniform INT4 and random16 mean, but it does not beat the best random
allocation in this tiny 32-module / 16-prompt setting. The right next step is
to expand measurement coverage and use a more stable cross-dataset consensus
or interaction-aware search before making strong robustness claims for
SmolLM2-1.7B.

## Full-Module Follow-Up

The next run expanded measurement coverage from 32 Linear modules to all 169
Linear modules, still under the same PyTorch fake-quant diagnostic path.

```text
calibration prompts:        8
evaluation prompts:         16
measured Linear modules:    169 / 169
loss-sensitive allocation:  156 x 4-bit, 13 x 8-bit
average bits:               4.5
protected positive delta:   0.7179

FP16 PPL:                   12.6903
uniform INT4 PPL:           18.1431
loss_sensitive_full PPL:    13.9866
best random16 PPL:          14.7340
target vs uniform INT4:     +4.1565 PPL
target vs best random16:    +0.7474 PPL
target vs random16 mean:    +3.5992 PPL
```

This repairs the small-run failure against best-of-16 random. It should still
be treated as a short-slice diagnostic, because the evaluation uses only 16
WikiText2 prompts and does not use a packed quantized runtime.

Artifacts:

```text
outputs/smollm2_1p7b_module_loss_sensitivity_limit8_group128.json
outputs/smollm2_1p7b_module_loss_sensitivity_limit8_group128_report.md
outputs/smollm2_1p7b_loss_sensitive_alloc_4to8_limit8_group128_summary.json
outputs/smollm2_1p7b_retry_loss_sensitive_ppl_wikitext2_16_summary.json
outputs/smollm2_1p7b_retry_loss_sensitive_ppl_wikitext2_16_guard.json
outputs/smollm2_1p7b_retry_random16_ppl_wikitext2_16_summary.json
outputs/smollm2_1p7b_retry_random16_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_result.md
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_16_summary.json
outputs/smollm2_1p7b_full_random16_evidence_matrix.md
data_eval/eval_configs/smollm2_1p7b_retry_loss_sensitive_compare.json
data_eval/eval_configs/smollm2_1p7b_retry_random16_compare.json
data_eval/eval_configs/smollm2_1p7b_full_random16_compare.json
```
