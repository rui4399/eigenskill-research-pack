# Layer-20 V V3 Task-Style Prompt Audit

Date: `2026-06-06`

This audit scales the rowguard validation from 12-prompt held-out splits to a 24-prompt task-style suite. The suite mixes quantization reasoning, JSON/YAML formatting, C++ API wording, deployment claims, and proxy/drift explanations.

Prompt file:

```text
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v3_taskstyle.txt
```

## Results

| policy | layers | package / precision change | prompts | exact | mean edit | mean prefix | fused/baseline speed | fused tok/s | guard peak |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | `1,7` | QKV8 on layers 1 and 7 | 24 | 19 / 24 | 0.9144 | 0.8906 | 1.0806x | 25.8326 | 3588 MiB / 44.02% |
| `full_v8` | `1,7,20` | full layer-20 V8 control | 24 | 19 / 24 | 0.8966 | 0.8656 | 1.0308x | 26.0157 | 3596 MiB / 44.12% |
| `g0_1_2_4_5_6_7` | `1,7,20` | layer-20 V groups 0,1,2,4,5,6,7 at 8-bit; group 3 remains 4-bit | 24 | 16 / 24 | 0.8727 | 0.8278 | 0.9788x | 25.1418 | 3597 MiB / 44.13% |

## Failure IDs

| policy | failed prompt IDs |
|---|---|
| `baseline_layers17` | `4, 5, 11, 18, 22` |
| `full_v8` | `3, 11, 16, 17, 22` |
| `g0_1_2_4_5_6_7` | `3, 5, 11, 16, 17, 18, 19, 22` |

## Interpretation

- The larger v3 suite reinforces the proxy-augmented selector: the rowguard that looked perfect on the original six-prompt search split drops to `16/24`, below both the conservative `1,7` baseline and the full-V8 probe at `19/24`.
- `baseline_layers17` and `full_v8` tie on exact match, but `baseline_layers17` has better mean edit and prefix preservation in this run.
- The rowguard has the weakest quality and is also the only candidate with mean fused speed below the same-script baseline. Treat it as diagnostic evidence for prompt-conditioned overfitting, not as a deployable rowguard.
- The positive fused/baseline speed ratios for `baseline_layers17` and `full_v8` are useful local evidence, but prompt-suite speed is noisy. Do not promote this to a general end-to-end acceleration claim.

## Local Files

```text
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7_gpu_guard.json
```
