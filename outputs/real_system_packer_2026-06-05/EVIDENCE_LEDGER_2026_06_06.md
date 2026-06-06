# Evidence Ledger

Date: `2026-06-06T11:35:27+00:00`
Status: **PASS**
Gates: `11 / 11` passed
Categories: `artifact integrity, c++ runtime, calibration robustness, decode integration, kernel, qkv replacement, quality, repo hygiene, runtime wiring, selected-row, task retention`

## Gate Summary

| gate | category | status | key metrics | source |
|---|---|---|---|---|
| `public_hygiene` | repo hygiene | **PASS** | tracked files 1549; forbidden files 0; placeholders 0 | `outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json` |
| `calibration_instability` | calibration robustness | **PASS** | cases 3; unstable 3; mean Spearman 0.0713; mean Jaccard 0.4349; top20 Jaccard 0.1022 | `outputs/calibration_instability_benchmark_2026_06_06.json` |
| `esmp_package` | artifact integrity | **PASS** | checked modules 8/8; missing files 0; failed modules 0; checked compression 6.2797x | `outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json` |
| `triton_shape_family` | kernel | **PASS** | configs 96/96; FP16 wins 10; best FP16 2.7647x; VRAM 0.4514 | `outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json` |
| `selector_runtime` | runtime wiring | **PASS** | selector calls 4; VRAM 0.5721 | `outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json` |
| `selected_row` | selected-row | **PASS** | ok rows 108; VRAM 0.4369 | `outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json` |
| `cpp_runtime` | c++ runtime | **PASS** | ok rows 42; wins/full 42; median selected 16.8259x; compression 7.6413x | `outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json` |
| `fused_sidecar` | decode integration | **PASS** | sidecar calls 48; tok/s ratio 0.8080x; VRAM 0.4396 | `outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json` |
| `fused_qkv_speed` | qkv replacement | **PASS** | replacements 1; tok/s ratio 1.1300x; TTFT ratio 0.6839x; compression 6.1682x; VRAM 0.4401 | `outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json` |
| `fused_qkv_quality` | quality | **PASS** | exact 6/6; mean speed 0.8957x; compression 3.9082x; VRAM 0.4359 | `outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json` |
| `chat_task_stress` | task retention | **PASS** | regressions 1; fused 45/84; VRAM 0.5469 | `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json` |

## Failures

- none

## Claim Boundary

- Valid claim: each listed row is backed by an executable gate JSON that passed under its configured thresholds.
- Invalid claim: passing this ledger proves SOTA quantization, mobile deployment, or full paper readiness.
