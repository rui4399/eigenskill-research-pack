# Prompt-Split Transfer Audit

Date: `2026-06-06T00:36:49+00:00`

This audit compares a precision policy on the prompt suite used during search against a held-out prompt suite. It is designed to catch prompt-conditioned overfitting.

## Summary

| candidate | train exact | held-out exact | exact gap | min exact rate | train prefix | held-out prefix | held-out speed | risk |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_layers17 | 6/6 | 11/12 | 0.0833 | 0.9167 | 1.0000 | 0.9172 | 0.8316x | small_gap |
| full_v8 | 5/6 | 11/12 | -0.0833 | 0.8333 | 0.9096 | 0.9172 | 0.9427x | stable_or_improved |
| g0_1_2_4_5_6 | 5/6 | 9/12 | 0.0833 | 0.7500 | 0.9612 | 0.7725 | 0.9129x | small_gap |
| g0_1_2_4_5_6_7 | 6/6 | 9/12 | 0.2500 | 0.7500 | 1.0000 | 0.7725 | 0.7947x | high_overfit |
| g0_1_2_3_4_5_6 | 4/6 | 11/12 | -0.2500 | 0.6667 | 0.8457 | 0.9172 | 0.8546x | stable_or_improved |

## Candidate Details

### `baseline_layers17`

- Train failures: `[]`
- Held-out failures: `[4]`
- Harmonic exact rate: `0.9565`
- Prefix gap: `0.0828`
- Train JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json`
- Held-out JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/baseline_layers17.json`

### `full_v8`

- Train failures: `[0]`
- Held-out failures: `[4]`
- Harmonic exact rate: `0.8730`
- Prefix gap: `-0.0075`
- Train JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_qkv8_repack.json`
- Held-out JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/full_v8.json`

### `g0_1_2_4_5_6`

- Train failures: `[1]`
- Held-out failures: `[4, 7, 8]`
- Harmonic exact rate: `0.7895`
- Prefix gap: `0.1887`
- Train JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_sweep/groups_0_1_2_4_5_6_prompt_suite.json`
- Held-out JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/g0_1_2_4_5_6.json`

### `g0_1_2_4_5_6_7`

- Train failures: `[]`
- Held-out failures: `[4, 7, 8]`
- Harmonic exact rate: `0.8571`
- Prefix gap: `0.2275`
- Train JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sevengroup_focus/groups_0_1_2_4_5_6_7_prompt_suite.json`
- Held-out JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/g0_1_2_4_5_6_7.json`

### `g0_1_2_3_4_5_6`

- Train failures: `[1, 5]`
- Held-out failures: `[4]`
- Harmonic exact rate: `0.7719`
- Prefix gap: `-0.0715`
- Train JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sevengroup_focus/groups_0_1_2_3_4_5_6_prompt_suite.json`
- Held-out JSON: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/g0_1_2_3_4_5_6.json`

## Interpretation

- Best worst-split candidate: `baseline_layers17` with min exact rate `0.9167`.
- Best held-out candidate: `baseline_layers17` with held-out exact rate `0.9167`.
- A candidate with high train exact but lower held-out exact should be treated as diagnostic evidence, not as a deployable precision policy.
