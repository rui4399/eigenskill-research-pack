# Wake-up Summary: Qwen3-0.6B Random16 Audit

Rui, this stage is now stronger than the previous uniform-only evidence.

Completed:

- Fixed the Qwen3-0.6B random16 eval config by removing the nonexistent
  `random_budget_seed_20260622`.
- Ran WikiText2-64 len96 and C4-64 with the 85% GPU-memory guard.
- Added a new C++ tool: `quant_random_baseline_audit`.
- Generated markdown/json/csv evidence matrices and random-seed audits.
- Updated README with the new results and reproduction command.

Key results:

- WikiText2-64 len96: loss-sensitive PPL `49.5352`; random_seed win/loss/tie
  `12/3/0`; margin vs random-seed mean `+0.9435`; margin vs best random seed
  `-1.0322`.
- C4-64: loss-sensitive PPL `47.5872`; random_seed win/loss/tie `15/0/0`;
  margin vs random-seed mean `+1.8556`; margin vs best random seed `+0.7969`.
- GPU peak stayed safe: `52.26%` and `52.39%` of VRAM.

What this means:

- It is now fair to say the allocation beats uniform INT4, category, and the
  random-seed mean on two public-text slices.
- It is not fair to claim world-best or SOTA.
- The WikiText2 best-random failure is important and should stay visible; it
  motivates consensus calibration and stronger quantization baselines.

Main files:

```text
inference_cpp/src/quant_random_baseline_audit.cpp
outputs/qwen3_0p6b_lowmem_cpp_random16_random_seed_audit.md
outputs/qwen3_0p6b_lowmem_cpp_random16_wikitext2_len96_c4_evidence_matrix.md
outputs/qwen3_0p6b_lowmem_cpp_random16_gpu_guard_summary.md
outputs/notion_ready_update_2026_06_05_qwen3_0p6b_random16_audit.md
```
