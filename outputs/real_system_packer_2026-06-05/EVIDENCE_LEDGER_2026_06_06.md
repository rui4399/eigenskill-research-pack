# Evidence Ledger

Date: `2026-06-06T10:29:16+00:00`
Status: **PASS**
Gates: `8 / 8` passed
Categories: `c++ runtime, decode integration, kernel, qkv replacement, quality, runtime wiring, selected-row, task retention`

## Gate Summary

| gate | category | status | key metrics | source |
|---|---|---|---|---|
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
