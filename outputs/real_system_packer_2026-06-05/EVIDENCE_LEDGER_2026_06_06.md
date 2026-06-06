# Evidence Ledger

Date: `2026-06-06T17:10:16+00:00`
Status: **PASS**
Gates: `18 / 18` passed
Categories: `allocation comparator, artifact integrity, c++ runtime, calibration robustness, capability retention, decode integration, kernel, ptq comparator, qkv replacement, quality, repo hygiene, rotation comparator, runtime wiring, selected-row, task retention`

## Gate Summary

| gate | category | status | key metrics | source |
|---|---|---|---|---|
| `public_hygiene` | repo hygiene | **PASS** | tracked files 1647; forbidden files 0; placeholders 0 | `outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json` |
| `calibration_instability` | calibration robustness | **PASS** | cases 3; unstable 3; mean Spearman 0.0713; mean Jaccard 0.4349; top20 Jaccard 0.1022 | `outputs/calibration_instability_benchmark_2026_06_06.json` |
| `calibration_robustness_stress` | calibration robustness | **PASS** | cases 11; wins/uniform 11; wins/best-random 11; wins/random-mean 11; mean margin/uniform 4.2942; worst margin/uniform 1.3608; mean margin/best-random 1.1622; worst margin/best-random 0.1120; mean margin/random-mean 2.7444; worst margin/random-mean 0.5656; mean FP16 regret 4.1683; max FP16 regret 11.6693 | `outputs/calibration_robustness_stress_gate_2026_06_07.json` |
| `esmp_package` | artifact integrity | **PASS** | checked modules 8/8; missing files 0; failed modules 0; checked compression 6.2797x | `outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json` |
| `triton_shape_family` | kernel | **PASS** | configs 96/96; FP16 wins 10; best FP16 2.7647x; VRAM 0.4514 | `outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json` |
| `selector_runtime` | runtime wiring | **PASS** | selector calls 4; VRAM 0.5721 | `outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json` |
| `selected_row` | selected-row | **PASS** | ok rows 108; VRAM 0.4369 | `outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json` |
| `cpp_runtime` | c++ runtime | **PASS** | ok rows 42; wins/full 42; median selected 16.8259x; compression 7.6413x | `outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json` |
| `fused_sidecar` | decode integration | **PASS** | sidecar calls 48; tok/s ratio 0.8080x; VRAM 0.4396 | `outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json` |
| `fused_qkv_speed` | qkv replacement | **PASS** | replacements 1; tok/s ratio 1.1300x; TTFT ratio 0.6839x; compression 6.1682x; VRAM 0.4401 | `outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json` |
| `fused_qkv_quality` | quality | **PASS** | exact 6/6; mean speed 0.8957x; compression 3.9082x; VRAM 0.4359 | `outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json` |
| `chat_task_stress` | task retention | **PASS** | regressions 1; fused 45/84; VRAM 0.5469 | `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json` |
| `public_task_benchmark` | capability retention | **PASS** | cases 2; tasks 100; passes 4; accuracy 0.0400; VRAM 0.8826 | `outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json` |
| `allocation_family_proxy` | allocation comparator | **PASS** | cases 2; records 394; max avg bits 4.4997; target bits 4.5000 | `outputs/q_palette_style_allocation_family_gate_2026_06_06.json` |
| `robust_lcb_consensus` | allocation comparator | **PASS** | cases 3; high-bit modules 99; consistent selected 80; selected modules 80; max avg bits 4.4997 | `outputs/robust_lcb_consensus_family_gate_2026_06_06.json` |
| `robust_lcb_quality` | quality | **PASS** | cases 2; wins/uniform 2; wins/mean 0; margin vs uniform 5.6188; margin vs mean -2.8834; VRAM 0.7032 | `outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json` |
| `rotation_family_proxy` | rotation comparator | **PASS** | cases 2; records 394; rotated 167; rotation cost 0.3484; projected reduction 0.0934 | `outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json` |
| `awq_gptq_proxy` | ptq comparator | **PASS** | cases 2; records 394; packages 1; methods 4 | `outputs/awq_gptq_proxy_gate_2026_06_06.json` |

## Failures

- none

## Claim Boundary

- Valid claim: each listed row is backed by an executable gate JSON that passed under its configured thresholds.
- Invalid claim: passing this ledger proves SOTA quantization, mobile deployment, or full paper readiness.
