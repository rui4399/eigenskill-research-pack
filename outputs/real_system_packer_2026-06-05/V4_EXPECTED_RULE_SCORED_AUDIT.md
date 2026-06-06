# V4 Expected-Rule Prompt Audit

Date: `2026-06-06`

Purpose: make the v3 task-style prompt audit less dependent on prompt-string rule inference. The new suite keeps the same 24 prompt order as `heldout_prompt_suite_v3_taskstyle.txt`, but adds explicit JSONL scoring rules in `heldout_prompt_suite_v4_expected.jsonl`.

## Method

- Inputs are existing chat-template v3 generation JSON files.
- Scoring uses `train_python/score_prompt_suite.py --expected-jsonl ...`.
- Rules include explicit JSON keys, YAML fields, C++ signature detection, packed-byte arithmetic, sentence count, keyword-min-hit rules, and contains-all checks.
- This is a deterministic shallow task audit, not a full benchmark such as MMLU/GSM8K/IFEval.

## Results

| candidate | source JSON | baseline passes | fused passes | regressions | improvements | rules |
|---|---|---:|---:|---:|---:|---:|
| baseline_layers17 | `layer20_v_v3_chat_baseline_layers17.json` | 15 / 24 | 15 / 24 | 0 | 0 | 8 |
| full_v8 | `layer20_v_v3_chat_full_v8.json` | 15 / 24 | 15 / 24 | 0 | 0 | 8 |
| g0_1_2_4_5_6_7 | `layer20_v_v3_chat_g0_1_2_4_5_6_7.json` | 15 / 24 | 15 / 24 | 0 | 0 | 8 |

## Interpretation

- The explicit-rule scorer agrees with the previous rule-scored v3 audit at the aggregate level.
- The primary useful claim is narrow: no shallow task-rule regressions were detected for the three chat-template v3 candidates.
- This does not rescue weak structured-generation rows. Several rows fail for both baseline and fused outputs, especially strict JSON/YAML, exact arithmetic-only, and exact sentence-count prompts.
- `baseline_layers17` remains the conservative reference because it also has the best proxy-drift profile and strongest exact/edit/prefix preservation from the chat-template v3 audit.

## Files

- Expected suite: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v4_expected.jsonl`
- Baseline scored report: `outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17_expected_scored.md`
- Full-V8 scored report: `outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8_expected_scored.md`
- Rowguard scored report: `outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7_expected_scored.md`
