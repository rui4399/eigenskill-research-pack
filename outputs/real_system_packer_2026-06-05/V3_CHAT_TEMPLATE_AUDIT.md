# V3 Chat-Template Task Audit

Date: `2026-06-06`

This audit reruns the v3 task-style prompt suite using the new `--chat-template` evaluation path. The path formats each prompt as a single user chat message before generation. If `tokenizer.apply_chat_template` is blocked by the local `jinja2` version, the code falls back to a Qwen/ChatML-style prompt:

```text
<|im_start|>user
...
<|im_end|>
<|im_start|>assistant
```

This is a more appropriate path for instruct models than raw completion prompting.

## Code Changes

```text
train_python/measure_esmp_generation_latency.py
train_python/eval_fused_qkv_prompt_suite.py
train_python/test_generation_prompt_format.py
```

New behavior is opt-in:

```text
eval_fused_qkv_prompt_suite.py --chat-template
measure_esmp_generation_latency.py --chat-template
```

Default raw-prompt behavior is unchanged, preserving prior experiment reproducibility.

## Exact/Prefix Results

| policy | prompts | exact | mean edit | mean prefix | fused/baseline speed | fused tok/s | guard peak |
|---|---:|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | 24 | 24 / 24 | 1.0000 | 1.0000 | 0.9016x | 23.4792 | 3590 MiB / 44.04% |
| `full_v8` | 24 | 23 / 24 | 0.9978 | 0.9824 | 1.0297x | 26.2037 | 3585 MiB / 43.98% |
| `g0_1_2_4_5_6_7` | 24 | 22 / 24 | 0.9890 | 0.9469 | 0.9136x | 22.8044 | 3599 MiB / 44.15% |

Failure IDs:

| policy | failed prompt IDs |
|---|---|
| `baseline_layers17` | none |
| `full_v8` | `1` |
| `g0_1_2_4_5_6_7` | `1, 13` |

## Rule-Scored Results

| policy | baseline rule passes | fused rule passes | regressions |
|---|---:|---:|---:|
| `baseline_layers17` | 15 / 24 | 15 / 24 | 0 |
| `full_v8` | 15 / 24 | 15 / 24 | 0 |
| `g0_1_2_4_5_6_7` | 15 / 24 | 15 / 24 | 0 |

## Interpretation

- The raw-prompt v3 suite underestimated instruction-following quality. With chat-template prompting, the conservative `baseline_layers17` policy reaches `24/24` exact against the dense reference.
- `full_v8` and the rowguard remain slightly weaker on exact preservation (`23/24` and `22/24`), so the earlier rowguard caution remains valid.
- Rule-scored shallow task checks show no regressions for any candidate, but rule pass rate is still only `15/24`; stronger expected-answer tasks remain necessary.
- Prompt-suite speed remains noisy: `full_v8` is speed-positive in this run, while `baseline_layers17` and the rowguard are speed-negative. Do not claim general end-to-end acceleration from these values.
- Future prompt/task audits should use `--chat-template` for instruct models, while keeping raw-prompt results labeled as completion-style stress tests.

## Local Files

```text
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7_scored.md
```
