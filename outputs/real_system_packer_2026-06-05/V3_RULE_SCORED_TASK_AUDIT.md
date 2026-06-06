# V3 Rule-Scored Task Audit

Date: `2026-06-06`

This report adds a lightweight rule-scoring layer on top of the v3 prompt-suite outputs. Unlike dense-vs-fused exact text match, these rules check shallow external task properties such as JSON keys, byte-count arithmetic, sentence count, C++ signature shape, YAML fields, and claim-caveat keywords.

Scoring code:

```text
train_python/score_prompt_suite.py
train_python/test_score_prompt_suite.py
```

TDD verification:

```text
python3 train_python/test_score_prompt_suite.py
python3 -m py_compile train_python/score_prompt_suite.py train_python/test_score_prompt_suite.py
```

Both passed.

## Aggregate

| policy | baseline passes | fused passes | preserved passes | regressions | improvements | rules used |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | 12 / 24 | 13 / 24 | 12 | 0 | 1 | 16 |
| `full_v8` | 12 / 24 | 12 / 24 | 12 | 0 | 0 | 16 |
| `g0_1_2_4_5_6_7` | 12 / 24 | 13 / 24 | 12 | 0 | 1 | 16 |

## Interpretation

- The rule-scored layer shows no shallow task-rule regressions for the three v3 candidates: whenever the dense baseline passed a rule, the fused path also passed it.
- This does not rescue the rowguard. Dense-vs-fused exact/prefix drift still shows the rowguard is less stable on v3 (`16/24` exact) than `baseline_layers17` or `full_v8` (`19/24` each).
- Baseline task-rule pass rate is only `12/24`, so the current scored suite is a diagnostic wrapper, not a strong benchmark. It is useful for separating textual drift from task-level failure, but it should be replaced or extended with established task benchmarks before paper claims.
- The next credible quality step is to add a stronger scored suite: deterministic format tasks with explicit expected answers, plus small established tasks such as GSM-style arithmetic, JSON validity, and instruction-following constraints.

## Local Files

```text
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7_scored.json
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7_scored.md
```
