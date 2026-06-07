# Evidence Ledger

Date: `2026-06-07T01:26:01+00:00`
Status: **PASS**
Gates: `23 / 23` passed
Categories: `allocation comparator, artifact integrity, c++ runtime, calibration robustness, capability retention, decode integration, kernel, paper alignment, ptq comparator, qkv replacement, quality, repo hygiene, rotation comparator, runtime wiring, selected-row, task retention`

## Gate Summary

| gate | category | status | key metrics | source |
|---|---|---|---|---|
| `public_hygiene` | repo hygiene | **PASS** | tracked files 1738; forbidden files 0; placeholders 0 | `outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json` |
| `calibration_instability` | calibration robustness | **PASS** | cases 3; unstable 3; mean Spearman 0.0713; mean Jaccard 0.4349; top20 Jaccard 0.1022 | `outputs/calibration_instability_benchmark_2026_06_06.json` |
| `calibration_robustness_stress` | calibration robustness | **PASS** | cases 11; wins/uniform 11; wins/best-random 11; wins/random-mean 11; mean margin/uniform 4.2942; mean margin/uniform CI [3.0664, 5.6886]; worst margin/uniform 1.3608; mean margin/best-random 1.1622; mean margin/best-random CI [0.6143, 1.7982]; worst margin/best-random 0.1120; mean margin/random-mean 2.7444; mean margin/random-mean CI [1.7921, 3.5862]; worst margin/random-mean 0.5656; mean FP16 regret 4.1683; max FP16 regret 11.6693; sign p/uniform 0.00048828; sign p/best-random 0.00048828; sign p/random-mean 0.00048828 | `outputs/calibration_robustness_stress_gate_2026_06_07.json` |
| `consensus_transfer_boundary` | allocation comparator | **PASS** | cases 2; slices 4; wins/left-single 4; wins/right-single 2; wins/best-single 2; wins/worst-single 4; min margin/worst-single 0.8726; mean regret/best-single 0.0043; max regret/best-single 0.3046 | `outputs/consensus_transfer_boundary_gate_2026_06_07.json` |
| `interaction_swap_boundary` | allocation comparator | **PASS** | cases 3; trials 16; improved cases 1; improved trials 5; interaction counterexamples 5; max best improvement 0.0502; transfer positives 1; transfer max regret 0.0087; VRAM 0.8487 | `outputs/interaction_swap_boundary_gate_2026_06_07.json` |
| `paper_evidence_alignment` | paper alignment | **PASS** | required refs 10; missing refs 0; paper paths 16; missing paths 0; unsafe claims 0; stale tokens 0; ledger gates 23 | `outputs/paper_evidence_alignment_gate_2026_06_07.json` |
| `esmp_package` | artifact integrity | **PASS** | checked modules 8/8; missing files 0; failed modules 0; checked compression 6.2797x | `outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json` |
| `triton_shape_family` | kernel | **PASS** | configs 96/96; FP16 wins 10; best FP16 2.7647x; VRAM 0.4514 | `outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json` |
| `selector_runtime` | runtime wiring | **PASS** | selector calls 4; VRAM 0.5721 | `outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json` |
| `selected_row` | selected-row | **PASS** | ok rows 108; VRAM 0.4369 | `outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json` |
| `cpp_runtime` | c++ runtime | **PASS** | ok rows 42; wins/full 42; median selected 16.8259x; compression 7.6413x | `outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json` |
| `fused_sidecar` | decode integration | **PASS** | sidecar calls 48; tok/s ratio 0.8080x; VRAM 0.4396 | `outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json` |
| `fused_qkv_speed` | qkv replacement | **PASS** | replacements 1; tok/s ratio 1.1300x; TTFT ratio 0.6839x; compression 6.1682x; VRAM 0.4401 | `outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json` |
| `fused_qkv_quality` | quality | **PASS** | exact 6/6; mean speed 0.8957x; compression 3.9082x; VRAM 0.4359 | `outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json` |
| `chat_task_stress` | task retention | **PASS** | regressions 1; fused 45/84; VRAM 0.5469 | `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json` |
| `public_task_benchmark` | capability retention | **PASS** | cases 2; tasks 100; passes 39; accuracy 0.3900; VRAM 0.8865 | `outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gate_2026_06_07.json` |
| `public_task_model_ladder` | capability retention | **PASS** | models 2; best passes 39; best accuracy 0.3900; tasks 200; passes 43; accuracy 0.2150; VRAM 0.8865 | `outputs/public_task_model_ladder_gate_2026_06_07.json` |
| `official_ptq_task_retention` | ptq comparator | **PASS** | cases 6; tasks 24; passes 2; accuracy 0.0833; VRAM 0.6108 | `outputs/official_ptq_task_retention_smoke_matrix_2026_06_07.json` |
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
