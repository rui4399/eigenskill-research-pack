# System Evidence Runbook

This file preserves the expanded gate commands for reproducibility. The short
reader-facing evidence map is `docs/SYSTEM_EVIDENCE_GATES.md`.

This repository separates exploratory output from evidence that can survive a
paper review. A result should be treated as paper-facing only when it is backed
by an executable gate and an explicit claim boundary.

## Evidence Ledger

`train_python/build_current_evidence_ledger.py` is the stable public entry
point for the current paper-facing gate set. It fixes the 64 gate paths in one
manifest, rebuilds the ledger, and avoids copying a long `--gate` list across
README files and paper appendices.

Current ledger:

```bash
python train_python/build_current_evidence_ledger.py
```

`train_python/build_evidence_ledger.py` is the lower-level builder for custom
or future gate manifests. The expanded form of the current 64-gate ledger is:

```bash
python train_python/build_evidence_ledger.py \
  --gate public_hygiene=outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --gate calibration_instability=outputs/calibration_instability_benchmark_2026_06_06.json \
  --gate sensitivity_perturbation_matrix=outputs/sensitivity_perturbation_matrix_qwen25_2026_06_07.json \
  --gate calibration_seed_stability=outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --gate csi_vs_n_curve=outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json \
  --gate csi_trend_significance=outputs/csi_trend_significance_qwen25_0p5b_2026_06_07.json \
  --gate csi_null_permutation=outputs/csi_null_permutation_qwen25_0p5b_2026_06_07.json \
  --gate rank_inversion_theory=outputs/rank_inversion_theory_qwen25_0p5b_2026_06_07.json \
  --gate calibration_robustness_stress=outputs/calibration_robustness_stress_gate_2026_06_07.json \
  --gate consensus_transfer_boundary=outputs/consensus_transfer_boundary_gate_2026_06_07.json \
  --gate interaction_swap_boundary=outputs/interaction_swap_boundary_gate_2026_06_07.json \
  --gate paper_evidence_alignment=outputs/paper_evidence_alignment_gate_2026_06_08.json \
  --gate esmp_package=outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json \
  --gate triton_shape_family=outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --gate w4a8_activation_reconstruction=outputs/w4a8_activation_reconstruction_2026_06_08/w4a8_activation_reconstruction_gate.json \
  --gate w4a8_activation_reconstruction_extended=outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended_gate.json \
  --gate selector_runtime=outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json \
  --gate selected_row=outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json \
  --gate cpp_runtime=outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json \
  --gate fused_sidecar=outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --gate fused_qkv_speed=outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --gate fused_qkv_quality=outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --gate chat_task_stress=outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --gate public_task_benchmark=outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_gate_2026_06_08.json \
  --gate public_task_gsm8k_full_7b=outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_gate_2026_06_08.json \
  --gate public_task_model_ladder=outputs/public_task_model_ladder_gate_2026_06_07.json \
  --gate official_ptq_task_retention=outputs/official_ptq_task_retention_smoke_matrix_2026_06_07.json \
  --gate official_ptq_runtime_profile=outputs/official_ptq_runtime_profile_2026_06_07.json \
  --gate official_ptq_task_subset50=outputs/official_ptq_task_subset50_matrix_2026_06_07.json \
  --gate official_ptq_subset50_runtime_profile=outputs/official_ptq_subset50_runtime_profile_2026_06_07.json \
  --gate official_ptq_task_subset100=outputs/official_ptq_task_subset100_matrix_2026_06_07.json \
  --gate official_ptq_subset100_runtime_profile=outputs/official_ptq_subset100_runtime_profile_2026_06_07.json \
  --gate official_ptq_ifeval_v2=outputs/official_ptq_task_ifeval_v2_matrix_2026_06_07.json \
  --gate official_ptq_ifeval_v2_runtime_profile=outputs/official_ptq_runtime_ifeval_v2_profile_2026_06_07.json \
  --gate official_ptq_matched_baseline_pack=outputs/official_ptq_matched_baseline_pack_qwen25_0p5b_2026_06_07.json \
  --gate official_awq_public_calib_16_eval=outputs/official_awq_public_calib_qwen25_0p5b_bundle_16_gate_2026_06_07.json \
  --gate official_awq_public_calib_1p5b_16_eval=outputs/official_awq_public_calib_qwen25_1p5b_bundle_16_gate_2026_06_07.json \
  --gate official_gptqmodel_public_calib_1p5b_16_eval=outputs/official_gptqmodel_public_calib_qwen25_1p5b_16_gate_2026_06_08.json \
  --gate official_gptqmodel_task_execution_qwen25_1p5b_subset100=outputs/official_gptqmodel_task_execution_qwen25_1p5b_subset100_matrix_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_subset100_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_subset100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_statistics=outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_statistics=outputs/official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_statistics=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_statistics=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --gate official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_runtime_profile=outputs/official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --gate official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_statistics=outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --gate allocation_family_proxy=outputs/q_palette_style_allocation_family_gate_2026_06_06.json \
  --gate robust_lcb_consensus=outputs/robust_lcb_consensus_family_gate_2026_06_06.json \
  --gate robust_lcb_quality=outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json \
  --gate rotation_family_proxy=outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json \
  --gate awq_gptq_proxy=outputs/awq_gptq_proxy_gate_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

The current ledger passes with 64/64 gates across repo hygiene, calibration
robustness, CSI trend significance, CSI null permutation, rank-inversion theory, artifact integrity, kernel, runtime wiring, selected-row, C++
runtime, decode integration, QKV replacement, quality, task-retention, runtime profile, and
capability-retention/model-ladder, allocation-comparator, rotation-comparator, and
matched PTQ baseline, true subset100 official PTQ task/runtime evidence, deterministic IFEval-style PTQ execution, expanded AutoAWQ public PPL, Qwen2.5-1.5B GPTQModel task-execution subset evidence, Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel subset100 plus GSM8K200/MMLU100 plus sharded GSM8K500 plus full GSM8K1319 plus MMLU Broad5x20/Broad10x20/Broad20x20 task/runtime/statistical-interval evidence, full-GSM8K local 7B public-task coverage, PTQ-comparator, and
paper-alignment evidence categories, plus extended W4A8 attention/MLP real-activation reconstruction.

Valid claim:

- the listed paper-facing evidence is backed by executable gate JSON artifacts.

Invalid claim:

- the ledger itself proves SOTA, mobile deployment, or full paper readiness.

## W4A8 Extended Real-Activation Reconstruction Gate

This gate extends the first eight-module self-attention audit to 24 selected
Qwen3-0.6B attention and MLP projections across layers 0/7/14/21. It is a
module-level drift audit, not a quality or runtime benchmark.

WSL/GPU command:

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.80 \
  --min-disk-free-gb 5 \
  --disk-check-path . \
  --timeout-sec 1200 \
  --out outputs/w4a8_activation_reconstruction_extended_2026_06_08/gpu_guard.json \
  -- \
  python3 train_python/eval_w4a8_activation_reconstruction.py \
    --local-files-only \
    --layers 0,7,14,21 \
    --module-filter self_attn \
    --module-filter mlp \
    --max-modules 24 \
    --limit-prompts 4 \
    --max-length 96 \
    --sample-rows-per-module 64 \
    --chunk-rows 32 \
    --out-json outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended.json \
    --out-jsonl outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended.jsonl \
    --out-md outputs/w4a8_activation_reconstruction_extended_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_EXTENDED.md
```

Gate command:

```bash
python train_python/gate_w4a8_activation_reconstruction.py \
  --json outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended.json \
  --min-modules 24 \
  --max-activation-added-rel-l2 0.09 \
  --max-p90-w4a8-rel-l2 0.30 \
  --min-median-compression 3.5 \
  --max-memory-ratio 0.90 \
  --out-json outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended_gate.json \
  --out-md outputs/w4a8_activation_reconstruction_extended_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_EXTENDED_GATE.md
```

Current result: 24/24 modules pass. Median W4A8 output rel-L2 is `0.144851`,
p90 W4A8 output rel-L2 is `0.212923`, max activation-added rel-L2 versus W4A16
is `0.084533`, median activation input rel-L2 is `0.035115`, median compression
versus FP32 is `7.6413x`, and the outer GPU guard peaks at `0.7220`.

Valid claim:

- selected real Qwen3 attention and MLP module activations have measured W4A8
  reconstruction drift under a guarded local run.

Invalid claim:

- this does not prove full-model quality retention, downstream task retention,
  end-to-end generation speedup, mobile deployment, energy savings, or SOTA
  quantization.

Interpretation: the worst two cases are MLP down projections. The extended gate
therefore strengthens the systems evidence by exposing integration risk instead
of hiding it.

## ESMP Artifact Integrity Gate

`mixed_precision_packer` writes an ESMPQ001 binary package plus a per-module
manifest. `train_python/verify_esmp_package.py` verifies that the pack summary,
the manifest, and the binary header agree before a packed model slice is used as
paper-facing evidence.

Example:

```bash
python train_python/verify_esmp_package.py \
  --summary outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json \
  --limit-modules 8 \
  --min-checked 8 \
  --max-missing 0 \
  --min-compression-vs-fp32 6.0 \
  --out-json outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/ESMP_PACKAGE_VERIFY_QWEN3_0P6B_LIMIT8_2026_06_06.md
```

The C++ binary inspector gives a lower-level package check:

```bash
./build/cpp-wsl/esmp_inspect \
  --input build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --expect-rows 64 \
  --expect-cols 96 \
  --max-avg-bits 4.6 \
  --min-compression-vs-fp32 4.0 \
  --require-bits 4,8 \
  --verify-row-sums
```

Valid claim:

- ESMP package metadata and manifests can be independently checked without
  trusting README prose.

Invalid claim:

- package integrity proves the quantized model is accurate or fast.

## Public Repository Hygiene Gate

`train_python/gate_public_repo_hygiene.py` protects the public branch from
drifting back into private workbench state. It fails if tracked files include
generated delivery bundles (`.docx`, `.pdf`, `.zip`), old `research_pack_*`
trees, NotebookLM/Obsidian exports, root Codex resume handoff files,
Notion/wake-up/nightly delivery snippets, old swarm/acoustic concept drafts,
or blank README-style placeholder lines.

Example:

```bash
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

Valid claim:

- the current public tree excludes generated delivery bundles, private
  workbench exports, process logs, and speculative concept drafts.

Invalid claim:

- repository hygiene proves experimental correctness.

## Paper Evidence Alignment Gate

`train_python/gate_paper_evidence_alignment.py` checks that the current paper
draft cites committed evidence artifacts, does not reference removed process
files, and keeps high-risk phrases such as SOTA, production runtime, mobile
deployment, and board-level measurements inside explicit non-claim language.

Current gate:

```bash
python train_python/gate_paper_evidence_alignment.py \
  --paper paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md \
  --expected-gate-count 64 \
  --out-json outputs/paper_evidence_alignment_gate_2026_06_08.json \
  --out-md outputs/PAPER_EVIDENCE_ALIGNMENT_GATE_2026_06_08.md
```

Current result: the generated alignment artifact records all configured required
evidence references present, referenced repo paths found, 0 stale forbidden
tokens, 0 unsafe non-negated claim lines, and the paper mentions the current
64-gate ledger.

Valid claim:

- the current paper draft is aligned with the committed evidence boundary and
  does not contain unguarded high-risk claims detected by this scanner.

Invalid claim:

- this proves the paper is accepted, complete, or sufficient for any target
  venue.

## Public Task Benchmark Gate

`train_python/gate_public_task_benchmark.py` verifies that real public-task
subset evaluations ran under GPU guard. It is deliberately a coverage gate, not
an accuracy or leaderboard gate.

Current gate:

```bash
python train_python/gate_public_task_benchmark.py \
  --case mmlu100=outputs/public_task_benchmark_mmlu_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_summary.json=outputs/public_task_benchmark_mmlu_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case gsm8k200=outputs/public_task_benchmark_gsm8k_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_summary.json=outputs/public_task_benchmark_gsm8k_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --min-cases 2 \
  --min-total-tasks 300 \
  --require-formats mmlu,gsm8k \
  --max-memory-ratio 0.90 \
  --out-json outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_gate_2026_06_08.json \
  --out-md outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN25_ABLITERATE_7B_GSM8K200_MMLU100_GATE_2026_06_08.md
```

Current result: 300 public subset tasks, 84 total passes, mean accuracy
`0.2800`, mean throughput `19.9987` tok/s, mean TTFT `0.478812` s, and peak
guard VRAM ratio `0.7135`. The MMLU100 case is 50/100; the GSM8K200 case is
34/200.

Valid claim:

- public MMLU/GSM8K subset evaluation is now wired and guarded.

Invalid claim:

- this proves leaderboard-scale quality, fused-retention quality, or SOTA
  reasoning performance.

## Full GSM8K 7B Public Task Gate

This gate uses the same public-task evaluator but runs the full 1319-row GSM8K
test fixture through the local Ollama 7B model. It is a single-task public
coverage gate, not quantized retention and not a multi-task leaderboard.

Build the fixture:

```bash
python train_python/build_public_task_smoke.py \
  --out-dir data_eval/public_task_benchmark_v1 \
  --gsm8k-count 1319 \
  --mmlu-count 0 \
  --file-tag gsm8kfull \
  --title "Public Task Benchmark GSM8K Full Manifest" \
  --claim-boundary "Full GSM8K test fixture for guarded local execution; not leaderboard-scale multi-task evaluation or quantized retention." \
  --source datasets-server \
  --out-json outputs/public_task_benchmark_gsm8kfull_manifest_2026_06_08.json \
  --out-md outputs/PUBLIC_TASK_BENCHMARK_GSM8KFULL_MANIFEST_2026_06_08.md
```

Run the guarded Ollama evaluation:

```bash
python train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --poll-seconds 2 \
  --timeout-sec 7200 \
  --cleanup-repo-caches \
  --cleanup-root . \
  --min-disk-free-gb 2 \
  --disk-check-path . \
  --out outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_gpu_guard_2026_06_08.json \
  python train_python/eval_chat_task_ollama.py \
    --tasks-jsonl data_eval/public_task_benchmark_v1/gsm8k_test_gsm8kfull.jsonl \
    --task-format gsm8k \
    --model huihui_ai/qwen2.5-abliterate:7b-instruct \
    --max-new-tokens 64 \
    --no-think \
    --out-json outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_summary_2026_06_08.json \
    --out-md outputs/PUBLIC_TASK_BENCHMARK_GSM8KFULL_OLLAMA_QWEN25_ABLITERATE_7B_2026_06_08.md
```

Gate it:

```bash
python train_python/gate_public_task_benchmark.py \
  --case gsm8kfull=outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_summary_2026_06_08.json=outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_gpu_guard_2026_06_08.json \
  --min-cases 1 \
  --min-total-tasks 1319 \
  --require-formats gsm8k \
  --max-memory-ratio 0.90 \
  --out-json outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_gate_2026_06_08.json \
  --out-md outputs/PUBLIC_TASK_BENCHMARK_GSM8KFULL_OLLAMA_QWEN25_ABLITERATE_7B_GATE_2026_06_08.md
```

Current result: 1319 GSM8K test rows, 183 passes, mean accuracy `0.1387`,
mean throughput `16.8942` tok/s, mean TTFT `0.463880` s, and peak guard VRAM
ratio `0.6934`.

Valid claim:

- full GSM8K public-task execution is wired and guarded for the local 7B model.

Invalid claim:

- this proves quantized retention, multi-task leaderboard quality, fused-runtime
  quality, or SOTA reasoning performance.

## Public Task Model Ladder Gate

`train_python/gate_public_task_model_ladder.py` combines already-passing
public-task gates into a compact multi-model ladder. This keeps the stronger 7B
subset result next to the weaker local 4B result, so the public artifact is less
vulnerable to single-model cherry-picking.

Current gate:

```bash
python train_python/gate_public_task_model_ladder.py \
  --case qwen35_4b=outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json \
  --case qwen25_7b=outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gate_2026_06_07.json \
  --min-models 2 \
  --min-tasks-per-model 100 \
  --require-formats mmlu,gsm8k \
  --max-memory-ratio 0.90 \
  --min-best-total-passes 30 \
  --min-best-accuracy 0.30 \
  --out-json outputs/public_task_model_ladder_gate_2026_06_07.json \
  --out-md outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md
```

Current result: 2 local Ollama models, 200 total public-task rows, 43 total
passes, best case Qwen2.5-abliterate-7B with 39/100, retained weaker 4B case
with 4/100, and peak guard VRAM ratio `0.8865`.

Valid claim:

- public-task coverage is reported as a guarded two-model ladder rather than a
  single isolated result.

Invalid claim:

- this proves monotonic scaling, fused quantized retention, leaderboard-scale
  quality, or SOTA reasoning performance.

## Official PTQ Task-Execution Smoke Matrix

`train_python/gate_official_ptq_task_retention.py` combines guarded task-smoke
runs for the same Qwen2.5-0.5B family under FP16, AutoAWQ, and GPTQModel. It
exists to ensure official PTQ artifacts are not reported with PPL-only evidence.
The matrix is intentionally tiny and negative-friendly. Formats where the FP16
baseline is already zero are execution-only evidence.

Current gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_mmlu_smoke_summary_2026_06_07.json=outputs/official_ptq_task_fp16_mmlu_smoke_gpu_guard_2026_06_07.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_gsm8k_smoke_summary_2026_06_07.json=outputs/official_ptq_task_fp16_gsm8k_smoke_gpu_guard_2026_06_07.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_mmlu_smoke_summary_2026_06_07.json=outputs/official_ptq_task_awq_mmlu_smoke_gpu_guard_2026_06_07.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_gsm8k_smoke_summary_2026_06_07.json=outputs/official_ptq_task_awq_gsm8k_smoke_gpu_guard_2026_06_07.json \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_mmlu_smoke_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_mmlu_smoke_gpu_guard_2026_06_07.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_gsm8k_smoke_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_gsm8k_smoke_gpu_guard_2026_06_07.json \
  --max-accuracy-drop 0.25 \
  --out-json outputs/official_ptq_task_retention_smoke_matrix_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_RETENTION_SMOKE_MATRIX_2026_06_07.md
```

Current result: 6 cases, 3 variants, 2 task formats, 24 total task executions,
2 total passes, max accuracy drop versus FP16 `0.25`, and peak guard VRAM ratio
`0.6108`. The current matrix marks `gsm8k` as a zero-accuracy FP16 baseline
format.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants can all be loaded and
  evaluated on the same tiny public MMLU/GSM8K smoke fixtures under GPU guard.
  The GSM8K slice is valid only as execution-path evidence because FP16 is 0/4.

Invalid claim:

- this proves broad task retention, leaderboard quality, official AWQ/GPTQ
  competitiveness, or production inference performance.

## Official PTQ Runtime Profile Gate

`train_python/gate_official_ptq_runtime_profile.py` summarizes PC-side runtime
metrics from the guarded FP16/AutoAWQ/GPTQModel task-smoke matrix. It exists so
TTFT, tokens/s, and peak guarded VRAM are visible as runtime evidence instead
of being buried inside task-smoke JSON files.

Current gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_retention_smoke_matrix_2026_06_07.json \
  --out-json outputs/official_ptq_runtime_profile_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_RUNTIME_PROFILE_2026_06_07.md
```

Current result: 3 variants, 6 cases, 24 tasks, mean `11.4608` tokens/s, mean
TTFT `0.508495` s, peak guarded VRAM ratio `0.6108`, and peak guarded VRAM
`4979` MiB.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants have PC-side TTFT,
  tokens/s, and peak VRAM measurements on the same guarded task-smoke path.

Invalid claim:

- this proves Redmi/mobile deployment, production runtime speedup, energy
  improvement, or official AWQ/GPTQ competitiveness.

## Official PTQ Matched Task Subset50 Matrix

The same task gate can also summarize a larger matched public subset. The six
input summaries are produced with `eval_chat_task_benchmark.py --limit 50` over
the public MMLU and GSM8K subset files for FP16, AutoAWQ, and GPTQModel.

Current gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --matrix-title "Official PTQ Matched Task Subset50 Matrix" \
  --evidence-label "50-row matched public MMLU/GSM8K subsets" \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_mmlu_subset50_summary_2026_06_07.json=outputs/official_ptq_task_fp16_mmlu_subset50_gpu_guard_2026_06_07.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_gsm8k_subset50_summary_2026_06_07.json=outputs/official_ptq_task_fp16_gsm8k_subset50_gpu_guard_2026_06_07.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_mmlu_subset50_summary_2026_06_07.json=outputs/official_ptq_task_awq_mmlu_subset50_gpu_guard_2026_06_07.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_gsm8k_subset50_summary_2026_06_07.json=outputs/official_ptq_task_awq_gsm8k_subset50_gpu_guard_2026_06_07.json \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_mmlu_subset50_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_mmlu_subset50_gpu_guard_2026_06_07.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_gsm8k_subset50_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_gsm8k_subset50_gpu_guard_2026_06_07.json \
  --min-tasks-per-case 50 \
  --max-accuracy-drop 0.25 \
  --out-json outputs/official_ptq_task_subset50_matrix_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_SUBSET50_MATRIX_2026_06_07.md
```

Current result: 6 cases, 3 variants, 2 task formats, 300 total task executions,
37 total passes, max accuracy drop versus FP16 `0.04`, and peak guard VRAM ratio
`0.6148`. MMLU is 13/50 for FP16, 11/50 for AutoAWQ, and 13/50 for GPTQModel;
GSM8K remains execution-only because FP16 is 0/50.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants can all be loaded and
  evaluated on the same 50-row public MMLU and 50-row public GSM8K subsets under
  GPU guard.

Invalid claim:

- this proves leaderboard-scale task retention, reasoning quality, official
  AWQ/GPTQ competitiveness, or production inference performance.

## Official PTQ Subset50 Runtime Profile Gate

Current gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_subset50_matrix_2026_06_07.json \
  --out-json outputs/official_ptq_subset50_runtime_profile_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_SUBSET50_RUNTIME_PROFILE_2026_06_07.md
```

Current result: 3 variants, 6 cases, 300 tasks, mean `15.8107` tokens/s, mean
TTFT `0.250121` s, peak guarded VRAM ratio `0.6148`, and peak guarded VRAM
`5011` MiB. AutoAWQ and GPTQModel reduce guarded VRAM versus FP16 on this local
Transformers/GPTQModel path, but both are slower than FP16.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants have PC-side TTFT,
  tokens/s, and peak VRAM measurements on the same guarded subset50 path.

Invalid claim:

- this proves Redmi/mobile deployment, production runtime speedup, energy
  improvement, or official AWQ/GPTQ competitiveness.

## Official PTQ Matched Task Subset100 Matrix

The same task gate also summarizes the regenerated true 100-row public subset
fixtures. These files are produced by `build_public_task_smoke.py` with
`--gsm8k-count 100 --mmlu-count 100 --file-tag subset100`; the resulting JSONL
fixtures contain 100 rows each.

Current gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --matrix-title "Official PTQ Matched Task Subset100 Matrix" \
  --evidence-label "100-row matched public MMLU/GSM8K subsets" \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_mmlu_subset100_summary_2026_06_07.json=outputs/official_ptq_task_fp16_mmlu_subset100_gpu_guard_2026_06_07.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_gsm8k_subset100_summary_2026_06_07.json=outputs/official_ptq_task_fp16_gsm8k_subset100_gpu_guard_2026_06_07.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_mmlu_subset100_summary_2026_06_07.json=outputs/official_ptq_task_awq_mmlu_subset100_gpu_guard_2026_06_07.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_gsm8k_subset100_summary_2026_06_07.json=outputs/official_ptq_task_awq_gsm8k_subset100_gpu_guard_2026_06_07.json \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_mmlu_subset100_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_mmlu_subset100_gpu_guard_2026_06_07.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_gsm8k_subset100_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_gsm8k_subset100_gpu_guard_2026_06_07.json \
  --min-tasks-per-case 100 \
  --max-memory-ratio 0.85 \
  --max-accuracy-drop 0.25 \
  --out-json outputs/official_ptq_task_subset100_matrix_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_SUBSET100_MATRIX_2026_06_07.md
```

Current result: 6 cases, 3 variants, 2 task formats, 600 total task executions,
75 total passes, max accuracy drop versus FP16 `0.03`, no zero-accuracy FP16
baseline format, and peak guard VRAM ratio `0.5210`. MMLU is 25/100 for FP16,
23/100 for AutoAWQ, and 22/100 for GPTQModel; GSM8K is 2/100 for FP16, 1/100
for AutoAWQ, and 2/100 for GPTQModel.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants can all be loaded and
  evaluated on the same true 100-row public MMLU and 100-row public GSM8K
  subsets under GPU guard.

Invalid claim:

- this proves leaderboard-scale task retention, reasoning quality, official
  AWQ/GPTQ competitiveness, or production inference performance.

## Official PTQ Subset100 Runtime Profile Gate

Current gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_subset100_matrix_2026_06_07.json \
  --out-json outputs/official_ptq_subset100_runtime_profile_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_SUBSET100_RUNTIME_PROFILE_2026_06_07.md
```

Current result: 3 variants, 6 cases, 600 tasks, mean `14.8764` tokens/s, mean
TTFT `0.251615` s, peak guarded VRAM ratio `0.5210`, and peak guarded VRAM
`4247` MiB. AutoAWQ and GPTQModel reduce guarded VRAM versus FP16 on this local
Transformers/GPTQModel path, but both are slower than FP16.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants have PC-side TTFT,
  tokens/s, and peak VRAM measurements on the same guarded subset100 path.

Invalid claim:

- this proves Redmi/mobile deployment, production runtime speedup, energy
  improvement, or official AWQ/GPTQ competitiveness.

## Qwen2.5-1.5B Matched Official PTQ Task Matrices

`tools/run_qwen25_1p5b_subset100_task_matrix.sh` reruns the larger local
official-package task path. By default it evaluates FP16 and the saved AutoAWQ
W4/G128 Qwen2.5-1.5B artifact on the same 100-row MMLU abstract-algebra and
100-row GSM8K public subset fixtures under a 90% VRAM guard.

WSL/GPU entry point:

```bash
export NVIDIA_SMI_PATH=/usr/lib/wsl/lib/nvidia-smi
DATE_TAG=2026_06_07 bash tools/run_qwen25_1p5b_subset100_task_matrix.sh
```

The same entry point is parameterized for larger local slices. The current
prepared fixture is `TASK_TAG=gsm8k200_mmlu100`: it contains 200 GSM8K test
rows and the full 100-row MMLU abstract-algebra test split. This fixture is
larger than subset100 for GSM8K, but it is still not leaderboard-scale.

```bash
python train_python/build_public_task_smoke.py \
  --out-dir data_eval/public_task_benchmark_v1 \
  --gsm8k-count 200 \
  --mmlu-count 100 \
  --file-tag gsm8k200_mmlu100 \
  --title "Public Task Benchmark GSM8K200 MMLU100 Manifest" \
  --claim-boundary "200-row public GSM8K plus full 100-row MMLU abstract-algebra fixtures for guarded local task retention; not leaderboard-scale evaluation." \
  --source datasets-server \
  --out-json outputs/public_task_benchmark_gsm8k200_mmlu100_manifest_2026_06_08.json \
  --out-md outputs/PUBLIC_TASK_BENCHMARK_GSM8K200_MMLU100_MANIFEST_2026_06_08.md

DATE_TAG=2026_06_08 TASK_TAG=gsm8k200_mmlu100 TASK_LIMIT=200 \
  HF_DEVICE_MAP=auto HF_MAX_GPU_MEMORY_MIB=2400 \
  HF_OFFLOAD_FOLDER=/home/rui/eigenskill_artifacts/hf_offload_qwen25_1p5b \
  bash tools/run_qwen25_1p5b_subset100_task_matrix.sh
```

The FP16 path for the 2026-06-08 GSM8K200/MMLU100 run uses HF `device_map=auto`
with CPU/GPU offload to keep the local RTX 5070 Laptop run below the 90% VRAM
guard. This makes the task-retention comparison useful, but the runtime ratios
must be read as a local guarded profile rather than a production speedup claim.

Task-retention gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_subset100_summary_2026_06_07.json=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_subset100_gpu_guard_2026_06_07.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_subset100_summary_2026_06_07.json=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_subset100_gpu_guard_2026_06_07.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_subset100_summary_2026_06_07.json=outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_subset100_gpu_guard_2026_06_07.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_subset100_summary_2026_06_07.json=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_subset100_gpu_guard_2026_06_07.json \
  --baseline-variant fp16 \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --required-format mmlu \
  --required-format gsm8k \
  --min-tasks-per-case 100 \
  --max-memory-ratio 0.90 \
  --max-accuracy-drop 0.08 \
  --matrix-title "Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel Subset100 Task Matrix" \
  --evidence-label "matched Qwen2.5-1.5B local subset100 task evidence for FP16, AutoAWQ, and GPTQModel" \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_subset100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_subset100_gpu_guard_2026_06_08.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_subset100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_subset100_gpu_guard_2026_06_08.json \
  --out-json outputs/official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_SUBSET100_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md
```

Current subset100 result: 600 guarded public task executions across FP16,
AutoAWQ, and GPTQModel. FP16 obtains 33/100 MMLU and 12/100 GSM8K; AutoAWQ
obtains 34/100 MMLU and 11/100 GSM8K; GPTQModel obtains 25/100 MMLU and
8/100 GSM8K. The max drop versus FP16 is `0.0800`, and the peak guard VRAM
ratio is `0.8013`. This is matched local subset evidence, not leaderboard-scale
task retention or PTQ superiority.

Larger GSM8K200/MMLU100 gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --baseline-variant fp16 \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --required-format mmlu \
  --required-format gsm8k \
  --min-tasks-per-case 100 \
  --max-memory-ratio 0.90 \
  --max-accuracy-drop 0.05 \
  --matrix-title "Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K200/MMLU100 task matrix" \
  --evidence-label "matched Qwen2.5-1.5B local GSM8K200 plus MMLU100 task evidence for FP16, AutoAWQ, and GPTQModel" \
  --out-json outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md
```

Runtime-profile gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --baseline-variant fp16 \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --min-cases-per-variant 2 \
  --max-memory-ratio 0.90 \
  --min-mean-tokens-per-second 1 \
  --max-mean-ttft-seconds 2.0 \
  --out-json outputs/official_ptq_qwen25_1p5b_subset100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_QWEN25_1P5B_SUBSET100_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_2026_06_08.md
```

Current subset100 runtime result: FP16 averages `18.3348` tokens/s and
`0.130220` s TTFT with peak guarded VRAM `6531` MiB; AutoAWQ averages
`11.7637` tokens/s and `0.208924` s TTFT with peak guarded VRAM `4919` MiB;
GPTQModel averages `10.6469` tokens/s and `0.236180` s TTFT with peak guarded
VRAM `5438` MiB. Quantized packages reduce guarded VRAM but remain slower on
this local loader path.

Larger GSM8K200/MMLU100 runtime-profile gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_matrix_2026_06_08.json \
  --baseline-variant fp16 \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --min-cases-per-variant 2 \
  --max-memory-ratio 0.90 \
  --min-mean-tokens-per-second 1 \
  --max-mean-ttft-seconds 2.0 \
  --out-json outputs/official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_QWEN25_1P5B_GSM8K200_MMLU100_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_2026_06_08.md
```

Larger GSM8K200/MMLU100 statistical-interval gate:

```bash
python train_python/gate_official_ptq_task_statistics.py \
  --case fp16:mmlu=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json \
  --case autoawq:mmlu=outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json \
  --baseline-variant fp16 \
  --min-tasks-per-case 100 \
  --min-shared-tasks 100 \
  --max-ci-accuracy-drop 0.22 \
  --bootstrap-samples 10000 \
  --bootstrap-seed 20260608 \
  --matrix-title "Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K200/MMLU100 task statistics" \
  --out-json outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_statistics_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_FP16_AWQ_GPTQMODEL_STATISTICS_2026_06_08.md
```

Historical 2026-06-07 subset100 result: 400 guarded task executions for FP16
and AutoAWQ only. It is superseded in the paper-facing ledger by the 2026-06-08
matched FP16/AutoAWQ/GPTQModel subset100 matrix above, but remains useful as a
reproducibility input for the larger GSM8K200/MMLU100 AutoAWQ-only follow-up.

The larger 2026-06-08 run covers 900 guarded task executions. FP16 gets 33/100
MMLU and 19/200 GSM8K; AutoAWQ gets 34/100 MMLU and 22/200 GSM8K; GPTQModel
gets 25/100 MMLU and 20/200 GSM8K. The gate records max measured drop `0.0800`
versus FP16 and peak guard VRAM ratio `0.8295`. The paired runtime profile
reports FP16 at 5.0148 tok/s and 0.453859 s mean TTFT under HF offload, AutoAWQ
at 12.9601 tok/s and 0.187606 s mean TTFT, GPTQModel at 10.5705 tok/s and
0.234437 s mean TTFT, and peak guarded VRAM falling from 6761 MiB to 6024 MiB
for AutoAWQ and 5516 MiB for GPTQModel.

Sharded GSM8K500 extension:

```bash
# The first 200 GSM8K rows are reused from TASK_TAG=gsm8k200_mmlu100.
# The second shard uses eval_chat_task_benchmark.py --offset 200 --limit 300
# on data_eval/public_task_benchmark_v1/gsm8k_test_gsm8kfull.jsonl for
# FP16, AutoAWQ, and GPTQModel under the same 90% GPU guard.

python train_python/merge_chat_task_shards.py \
  --shard outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_gpu_guard_2026_06_08.json \
  --shard outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_shard0200_0499_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_shard0200_0499_gpu_guard_2026_06_08.json \
  --out-json outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_FP16_QWEN25_1P5B_GSM8K_GSM8KFULL_500_2026_06_08.md \
  --out-guard-json outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_500_gpu_guard_2026_06_08.json
```

The same merge command is repeated for AutoAWQ and GPTQModel, then gated with
`gate_official_ptq_task_retention.py`, `gate_official_ptq_runtime_profile.py`,
and `gate_official_ptq_task_statistics.py`.

Current GSM8K500 result: 1500 guarded task executions across FP16, AutoAWQ, and
GPTQModel. FP16 gets 43/500, AutoAWQ gets 46/500, and GPTQModel gets 40/500.
The task gate records max measured drop `0.0060` versus FP16 and peak guard VRAM
ratio `0.8295`. The paired statistics gate reports minimum bootstrap lower
bound `-0.034` under 10,000 samples. This is a larger single-task local
retention slice, not full GSM8K quantized retention or leaderboard-scale
evidence.

Full GSM8K1319 extension:

```bash
# Reuse the merged 800-row prefix plus the 800-1099 and 1100-1318 shards for
# FP16, AutoAWQ, and GPTQModel, then merge with merge_chat_task_shards.py and
# gate the resulting matrix/runtime/statistics reports.
python train_python/gate_official_ptq_task_retention.py \
  --case fp16:gsm8k=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_1319_gpu_guard_2026_06_08.json \
  --case autoawq:gsm8k=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json=outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_1319_gpu_guard_2026_06_08.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_1319_gpu_guard_2026_06_08.json
```

Current full-GSM8K result: 3957 guarded task executions across FP16, AutoAWQ,
and GPTQModel. FP16 gets 107/1319, AutoAWQ gets 104/1319, and GPTQModel gets
96/1319. The task gate records max measured drop `0.00834` versus FP16 and peak
guard VRAM ratio `0.8295`. The runtime profile reports mean `9.7071` tok/s and
mean TTFT `0.320392` s. The paired statistics gate reports minimum bootstrap
lower bound `-0.0243` under 10,000 samples. This is full single-task local
retention evidence, not leaderboard-scale quality or production runtime
evidence.

Current MMLU Broad5x20 result: 300 guarded task executions across FP16,
AutoAWQ, and GPTQModel over five MMLU subjects. FP16 gets 56/100, AutoAWQ gets
54/100, and GPTQModel gets 50/100. The task gate records max measured drop
`0.0600` versus FP16 and peak guard VRAM ratio `0.8114`. The runtime profile
reports mean `8.5774` tok/s and mean TTFT `0.252645` s. The paired statistics
gate reports minimum bootstrap lower bound `-0.1500` under 2,000 samples. This
broadens MMLU beyond abstract algebra, but is not full MMLU or leaderboard-scale
retention evidence.

Current MMLU Broad10x20 result: 600 guarded task executions across FP16,
AutoAWQ, and GPTQModel over ten MMLU subjects. FP16 gets 101/200, AutoAWQ gets
96/200, and GPTQModel gets 94/200. The task gate records max measured drop
`0.0350` versus FP16 and peak guard VRAM ratio `0.8189`. The runtime profile
reports mean `8.8134` tok/s and mean TTFT `0.245115` s. The paired statistics
gate reports minimum bootstrap lower bound `-0.0950` under 4,000 samples. This
further broadens MMLU coverage, but is still not full MMLU or leaderboard-scale
retention evidence.

The earlier GSM8K200/MMLU100 statistical gate reports paired bootstrap
candidate-minus-FP16 deltas:
AutoAWQ GSM8K `+0.0150` with CI `[-0.0350, +0.0650]`, AutoAWQ MMLU `+0.0100`
with CI `[-0.1000, +0.1200]`, GPTQModel GSM8K `+0.0050` with CI `[-0.0400,
+0.0500]`, and GPTQModel MMLU `-0.0800` with CI `[-0.1900, +0.0300]`. These
intervals are deliberately reported as uncertainty evidence, not statistical
superiority.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-1.5B variants have matched local
  subset100, GSM8K200/MMLU100, GSM8K500, full GSM8K1319, and MMLU Broad10x20
  task/runtime/VRAM evidence under the GPU guard.

Invalid claim:

- this proves leaderboard-scale task retention, reasoning-quality superiority,
  mobile deployment, production runtime speedup, energy improvement, or
  official AWQ/GPTQ/SmoothQuant competitiveness.

## Official PTQ IFEval-Style Execution Matrix

The same task gate can summarize a deterministic IFEval-style fixture covering
JSON validity, required/forbidden keywords, sentence count, and word count. The
fixture is intentionally small and strict; because the FP16 baseline is 0/8, it
is execution-path evidence rather than task-retention evidence.

Current gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --case fp16:ifeval=outputs/official_ptq_task_fp16_ifeval_v2_summary_2026_06_07.json=outputs/official_ptq_task_fp16_ifeval_v2_gpu_guard_2026_06_07.json \
  --case autoawq:ifeval=outputs/official_ptq_task_awq_ifeval_v2_summary_2026_06_07.json=outputs/official_ptq_task_awq_ifeval_v2_gpu_guard_2026_06_07.json \
  --case gptqmodel:ifeval=outputs/official_ptq_task_gptqmodel_ifeval_v2_summary_2026_06_07.json=outputs/official_ptq_task_gptqmodel_ifeval_v2_gpu_guard_2026_06_07.json \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --required-format ifeval \
  --min-tasks-per-case 8 \
  --max-memory-ratio 0.85 \
  --max-accuracy-drop 0.25 \
  --matrix-title "Official PTQ IFEval Deterministic V2 Execution Matrix" \
  --evidence-label "deterministic IFEval-style instruction-following v2 tasks" \
  --out-json outputs/official_ptq_task_ifeval_v2_matrix_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_TASK_IFEVAL_V2_MATRIX_2026_06_07.md
```

Current result: 3 variants, 24 total executions, 2 total passes, mean accuracy
`0.0833`, peak guarded VRAM ratio `0.5113`, and `ifeval` marked as a
zero-accuracy FP16 baseline format.

Valid claim:

- FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants load and execute the same
  deterministic IFEval-style instruction-following fixture under GPU guard.

Invalid claim:

- this proves broad IFEval retention, instruction-following superiority,
  leaderboard-scale task quality, or official AWQ/GPTQ competitiveness.

## Official PTQ IFEval-Style Runtime Profile Gate

Current gate:

```bash
python train_python/gate_official_ptq_runtime_profile.py \
  --matrix-json outputs/official_ptq_task_ifeval_v2_matrix_2026_06_07.json \
  --baseline-variant fp16 \
  --required-variant fp16 \
  --required-variant autoawq \
  --required-variant gptqmodel \
  --min-cases-per-variant 1 \
  --max-memory-ratio 0.85 \
  --min-mean-tokens-per-second 1.0 \
  --max-mean-ttft-seconds 2.0 \
  --out-json outputs/official_ptq_runtime_ifeval_v2_profile_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_RUNTIME_IFEVAL_V2_PROFILE_2026_06_07.md
```

Current result: 3 variants, 3 cases, 24 tasks, mean `16.5678` tokens/s, mean
TTFT `0.425468` s, peak guarded VRAM ratio `0.5113`, and peak guarded VRAM
`4168` MiB.

Valid claim:

- the deterministic IFEval-style execution path exposes PC-side TTFT, tokens/s,
  and peak VRAM for FP16, AutoAWQ, and GPTQModel on the same fixture.

Invalid claim:

- this proves Redmi/mobile deployment, production runtime speedup, energy
  improvement, or official AWQ/GPTQ competitiveness.

## Official PTQ Matched Baseline Pack Gate

`train_python/gate_official_ptq_matched_baseline_pack.py` bundles the local
AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 public-calibration PPL slices, matched
subset50 task matrix, and matched subset50 runtime profile into one
paper-facing baseline pack. It exists to prevent scattered PTQ evidence from
being cited more strongly than the data supports.

Current gate:

```bash
python train_python/gate_official_ptq_matched_baseline_pack.py \
  --ppl-case autoawq:wikitext2=outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_16_summary_2026_06_07.json \
  --ppl-case autoawq:c4=outputs/official_awq_public_calib_qwen25_0p5b_c4_16_summary_2026_06_07.json \
  --ppl-case gptqmodel:wikitext2=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_16_summary_2026_06_07.json \
  --ppl-case gptqmodel:c4=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_c4_16_summary_2026_06_07.json \
  --task-matrix-json outputs/official_ptq_task_subset50_matrix_2026_06_07.json \
  --runtime-profile-json outputs/official_ptq_subset50_runtime_profile_2026_06_07.json \
  --out-json outputs/official_ptq_matched_baseline_pack_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md
```

Current result: 4 PPL slices, 5714 PPL tokens, 300 task executions, 300
runtime executions, max PPL ratio `1.2570`, max task accuracy drop `0.0400`,
max VRAM ratio `0.9010`, and max quantized tokens/s ratio `0.3315` versus
FP16.

Valid claim:

- local official AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 artifacts have
  matched public-calibration PPL, matched subset50 task execution, and PC-side
  runtime/VRAM evidence.

Invalid claim:

- this is leaderboard-scale, large-model competitive AWQ/GPTQ evidence, a
  production runtime, mobile deployment, energy result, or SOTA PTQ evidence.

## Allocation Family Proxy Gate

`train_python/gate_allocation_family_proxy.py` verifies Q-Palette-style
measured-sensitivity allocation proxy artifacts. It is a comparator-family gate,
not an official reproduction claim.

Current gate:

```bash
python train_python/gate_allocation_family_proxy.py \
  --case qwen3_0p6b_wikitext2=outputs/q_palette_style_qwen3_0p6b_wikitext2_group128_summary.json \
  --case qwen3_0p6b_c4=outputs/q_palette_style_qwen3_0p6b_c4_group128_summary.json \
  --case qwen25_0p5b_limit2=outputs/q_palette_style_qwen25_0p5b_limit2_group128_summary.json \
  --case qwen25_0p5b_limit8=outputs/q_palette_style_qwen25_0p5b_limit8_group128_summary.json \
  --case qwen25_1p5b_limit2=outputs/q_palette_style_qwen25_1p5b_limit2_group128_summary.json \
  --case qwen25_1p5b_limit8=outputs/q_palette_style_qwen25_1p5b_limit8_group128_summary.json \
  --min-cases 6 \
  --min-records 100 \
  --required-method-token q_palette \
  --required-formula-token log2 \
  --min-distinct-bits 3 \
  --min-budget-utilization 0.999 \
  --budget-tolerance 0.0005 \
  --out-json outputs/q_palette_style_allocation_family_gate_2026_06_06.json \
  --out-md outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md
```

Current result: 6 cases, 1126 total records, max average bits `4.4999`,
minimum budget utilization `0.9999`, 6/6 finite lambda solutions, and 6/6
non-trivial bit histograms under a `4.5` target budget.

Valid claim:

- a Q-Palette-style closed-form Lagrangian allocation comparator proxy is
  executable on measured Qwen3 and Qwen2.5 sensitivity artifacts.

Invalid claim:

- this is a faithful official Q-Palette/IMPQ/WINDQuant reproduction or
  downstream quality-retention result.

## AWQ/GPTQ Proxy Gate

`train_python/build_awq_gptq_proxy.py` and
`train_python/gate_awq_gptq_proxy.py` provide an executable AWQ/GPTQ-style PTQ
proxy. The generator consumes measured module loss-sensitivity artifacts and
produces two budgeted 4/8-bit policies:

- `gptq_loss_hessian_proxy`: protects modules by loss/Hessian-style sensitivity.
- `awq_activation_saliency_proxy`: protects modules by sensitivity plus
  role/shape saliency.

`train_python/merge_baseline_environment_audits.py` merges package audits across
local environments, so the dashboard can truthfully see both Windows `optimum`
availability and WSL GPU `triton` availability without pretending they came from
the same Python interpreter.

Current generation:

```bash
python train_python/build_awq_gptq_proxy.py \
  --input outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json \
  --environment-audit outputs/baseline_environment_audit.json \
  --target-avg-bits 4.5 \
  --out-json outputs/awq_gptq_proxy_qwen3_0p6b_wikitext2_group128_summary.json \
  --out-md outputs/AWQ_GPTQ_PROXY_QWEN3_0P6B_WIKITEXT2_GROUP128.md

python train_python/build_awq_gptq_proxy.py \
  --input outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json \
  --environment-audit outputs/baseline_environment_audit.json \
  --target-avg-bits 4.5 \
  --out-json outputs/awq_gptq_proxy_qwen3_0p6b_c4_group128_summary.json \
  --out-md outputs/AWQ_GPTQ_PROXY_QWEN3_0P6B_C4_GROUP128.md
```

Current gate:

```bash
python train_python/gate_awq_gptq_proxy.py \
  --case wikitext2=outputs/awq_gptq_proxy_qwen3_0p6b_wikitext2_group128_summary.json \
  --case c4=outputs/awq_gptq_proxy_qwen3_0p6b_c4_group128_summary.json \
  --min-cases 2 \
  --min-records 100 \
  --required-artifact-token awq_gptq \
  --required-method-tokens awq,gptq \
  --target-avg-bits 4.5 \
  --min-protected-ratio 0.50 \
  --require-external-package \
  --out-json outputs/awq_gptq_proxy_gate_2026_06_06.json \
  --out-md outputs/AWQ_GPTQ_PROXY_GATE_2026_06_06.md
```

Current result: 2 cases, 394 records, `optimum` available in the merged audit,
and both AWQ/GPTQ proxy policies satisfy the `4.5` average-bit budget. Protected
positive-sensitivity ratios are `0.6472/0.6452` on WikiText2 and
`0.5865/0.5772` on C4 for GPTQ/AWQ respectively.

Valid claim:

- AWQ/GPTQ-style proxy baselines are executable over measured Qwen3-0.6B
  sensitivity artifacts.

Invalid claim:

- this is an official AWQ/GPTQ quantizer run, a GPU PTQ implementation, or a
  SOTA PTQ comparison.

## Rotation Family Proxy Gate

`train_python/build_rotation_family_proxy.py` and
`train_python/gate_rotation_family_proxy.py` provide a QuaRot/SpinQuant-style
rotation/outlier-mitigation family proxy. The generator consumes measured
module loss-sensitivity artifacts, selects plausible rotation targets under a
fixed module-cost budget, and records a conservative projected sensitivity
reduction. This is a related-family coverage gate, not an official rotation
implementation.

Current generation:

```bash
python train_python/build_rotation_family_proxy.py \
  --input outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json \
  --rotation-budget-fraction 0.35 \
  --out-json outputs/quarot_spinquant_rotation_baseline_qwen3_0p6b_wikitext2_group128_summary.json \
  --out-md outputs/QUAROT_SPINQUANT_ROTATION_BASELINE_QWEN3_0P6B_WIKITEXT2_GROUP128.md

python train_python/build_rotation_family_proxy.py \
  --input outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json \
  --rotation-budget-fraction 0.35 \
  --out-json outputs/quarot_spinquant_rotation_baseline_qwen3_0p6b_c4_group128_summary.json \
  --out-md outputs/QUAROT_SPINQUANT_ROTATION_BASELINE_QWEN3_0P6B_C4_GROUP128.md
```

Current gate:

```bash
python train_python/gate_rotation_family_proxy.py \
  --case wikitext2=outputs/quarot_spinquant_rotation_baseline_qwen3_0p6b_wikitext2_group128_summary.json \
  --case c4=outputs/quarot_spinquant_rotation_baseline_qwen3_0p6b_c4_group128_summary.json \
  --min-cases 2 \
  --min-records 100 \
  --min-rotated 20 \
  --required-method-token rotation \
  --required-policy-tokens quarot,spinquant \
  --min-reduction-ratio 0.05 \
  --out-json outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json \
  --out-md outputs/QUAROT_SPINQUANT_ROTATION_FAMILY_GATE_2026_06_06.md
```

Current result: 2 cases, 394 measured module records, 167 rotation candidates,
max rotated cost fraction `0.3484` under the `0.35` budget, and mean projected
sensitivity reduction ratio `0.0934`.

Valid claim:

- a QuaRot/SpinQuant-style rotation-family proxy is executable on measured
  Qwen3-0.6B sensitivity artifacts.

Invalid claim:

- this is a faithful official QuaRot/SpinQuant implementation, an activation
  rotation kernel, or proof of activation/KV quality retention.

## Baseline Gap Dashboard

`train_python/build_baseline_gap_dashboard.py` reads
`docs/BASELINE_COVERAGE_MANIFEST.json`, committed evidence artifacts, and the
baseline package audit to produce a reviewer-facing gap index. This is not a
success gate. It is a guard against accidentally claiming missing comparisons.

Example:

```bash
python train_python/audit_baseline_environment.py

python train_python/build_baseline_gap_dashboard.py \
  --manifest docs/BASELINE_COVERAGE_MANIFEST.json \
  --baseline-audit outputs/baseline_environment_audit.json \
  --out-json outputs/baseline_gap_dashboard_2026_06_06.json \
  --out-md outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
```

Valid claim:

- the repository explicitly tracks whether reviewer-critical baseline families
  have committed evidence.

Invalid claim:

- a dashboard row marked `missing`, `partial`, `proxy_only`,
  `package_only`, `evidence_without_package_audit`,
  `partial_without_package_audit`, or `proxy_without_package_audit` supports
  paper-facing competitiveness.

## Official AutoAWQ Smoke Probe

`train_python/run_official_awq_smoke.py` is a minimal package-readiness probe.
It exists to verify that AutoAWQ can execute, save local quantized artifacts,
and run one short generation smoke under the GPU guard. It is intentionally not
part of the 64-gate paper-facing ledger.

Example WSL/GPU command:

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --min-disk-free-gb 8 \
  --poll-seconds 2 \
  --timeout-sec 1800 \
  --out outputs/official_awq_smoke_qwen25_0p5b_gpu_guard_2026_06_07.json \
  -- \
  python3 train_python/run_official_awq_smoke.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --save-dir outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model \
    --out-json outputs/official_awq_smoke_qwen25_0p5b_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_AWQ_SMOKE_QWEN25_0P5B_2026_06_07.md \
    --max-calib-samples 4 \
    --max-calib-seq-len 16 \
    --max-chunk-memory-mib 256 \
    --device-map cuda:0 \
    --max-new-tokens 12
```

Gate command:

```bash
python train_python/gate_official_awq_smoke.py \
  --summary-json outputs/official_awq_smoke_qwen25_0p5b_summary_2026_06_07.json \
  --guard-json outputs/official_awq_smoke_qwen25_0p5b_gpu_guard_2026_06_07.json \
  --out-json outputs/official_awq_smoke_gate_2026_06_07.json \
  --out-md outputs/OFFICIAL_AWQ_SMOKE_GATE_2026_06_07.md
```

Current result: AutoAWQ 0.2.9, Qwen2.5-0.5B-Instruct, W4 group-128, six local
artifact files, 469,809,733 artifact bytes, peak guard VRAM ratio `0.6153`.

Valid claim:

- AutoAWQ can run a minimal local quantization and generation smoke under the
  configured guard.

Invalid claim:

- this is a matched AWQ/GPTQ baseline, a quality-retention comparison, a
  leaderboard result, or production runtime evidence.

## Official AutoAWQ Matched PPL Probe

`train_python/run_official_awq_matched_ppl.py` evaluates the same prompt slice
with the FP16 model and the local AutoAWQ artifact. This is a readiness bridge
between package smoke and a future full AWQ/GPTQ baseline.

Example WSL/GPU command:

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --min-disk-free-gb 8 \
  --poll-seconds 2 \
  --timeout-sec 900 \
  --out outputs/official_awq_matched_ppl_qwen25_0p5b_gpu_guard_2026_06_07.json \
  -- \
  python3 train_python/run_official_awq_matched_ppl.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --awq-artifact outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model \
    --limit-prompts 4 \
    --max-length 96 \
    --device cuda \
    --dtype float16 \
    --out-json outputs/official_awq_matched_ppl_qwen25_0p5b_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_2026_06_07.md
```

Gate command:

```bash
python train_python/gate_official_awq_matched_ppl.py \
  --summary-json outputs/official_awq_matched_ppl_qwen25_0p5b_summary_2026_06_07.json \
  --guard-json outputs/official_awq_matched_ppl_qwen25_0p5b_gpu_guard_2026_06_07.json \
  --out-json outputs/official_awq_matched_ppl_gate_2026_06_07.json \
  --out-md outputs/OFFICIAL_AWQ_MATCHED_PPL_GATE_2026_06_07.md
```

Current result: 4 prompts, 73 tokens, FP16 PPL `197.532`, AutoAWQ W4 group-128
PPL `232.863`, PPL ratio `1.1789`, delta NLL `0.1645`, peak guard VRAM ratio
`0.6057`.

Public-slice prompt builder:

```bash
python train_python/build_public_ppl_prompts.py \
  --wikitext2-count 8 \
  --c4-count 8 \
  --min-chars 40 \
  --max-chars 512
```

The public-slice probes use the same command shape as above, with
`--prompts data_eval/public_ppl_prompts_2026_06_07/<file>` and `--max-length
96`. Current guarded results:

| slice | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2 test | 8 | 760 | 24.676 | 31.351 | 1.2705 | 0.6005 |
| C4 validation | 8 | 727 | 32.952 | 38.961 | 1.1824 | 0.6005 |

Artifacts:

```text
outputs/PUBLIC_PPL_PROMPT_MANIFEST_2026_06_07.md
outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_WIKITEXT2_GATE_2026_06_07.md
outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_C4_GATE_2026_06_07.md
```

Public-calibration AutoAWQ bundle:

```bash
python train_python/build_public_ppl_prompts.py \
  --out-dir data_eval/public_calib_prompts_2026_06_07 \
  --wikitext2-count 8 \
  --c4-count 8 \
  --min-chars 40 \
  --max-chars 384 \
  --offset 128 \
  --manifest-title "Public Calibration Prompt Manifest" \
  --claim-boundary "Tiny public text slices used as AutoAWQ calibration prompts; not an evaluation benchmark or leaderboard definition." \
  --out-json outputs/public_calib_prompt_manifest_2026_06_07.json \
  --out-md outputs/PUBLIC_CALIB_PROMPT_MANIFEST_2026_06_07.md
```

The guarded AutoAWQ quantization command uses the generated calibration prompt
files with `--max-calib-samples 12` and `--max-calib-seq-len 128`, saving the
local ignored artifact under:

```text
outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model
```

Current public-calibrated bundle result:

| slice | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| quantization | n/a | n/a | n/a | n/a | n/a | 0.6960 |
| WikiText2 test eval | 8 | 760 | 24.676 | 29.081 | 1.1785 | 0.6116 |
| C4 validation eval | 8 | 727 | 32.952 | 38.173 | 1.1584 | 0.6116 |

Expanded 16-prompt public PPL slices:

```bash
python train_python/build_public_ppl_prompts.py \
  --out-dir data_eval/public_ppl_prompts_16_2026_06_07 \
  --wikitext2-count 16 \
  --c4-count 16 \
  --min-chars 40 \
  --max-chars 512 \
  --out-json outputs/public_ppl_prompt_manifest_16_2026_06_07.json \
  --out-md outputs/PUBLIC_PPL_PROMPT_MANIFEST_16_2026_06_07.md
```

The expanded eval reuses the public-calibrated AutoAWQ artifact above rather
than re-quantizing it. On this machine AutoAWQ is available in WSL, while the
Windows Python environment lacks `awq`.

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --min-disk-free-gb 8 \
  --poll-seconds 2 \
  --timeout-sec 900 \
  --out outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_16_gpu_guard_2026_06_07.json \
  -- \
  python3 train_python/run_official_awq_matched_ppl.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --awq-artifact outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model \
    --prompts data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --limit-prompts 16 \
    --max-length 96 \
    --device cuda \
    --dtype float16 \
    --out-json outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_16_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_WIKITEXT2_16_2026_06_07.md

python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --min-disk-free-gb 8 \
  --poll-seconds 2 \
  --timeout-sec 900 \
  --out outputs/official_awq_public_calib_qwen25_0p5b_c4_16_gpu_guard_2026_06_07.json \
  -- \
  python3 train_python/run_official_awq_matched_ppl.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --awq-artifact outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model \
    --prompts data_eval/public_ppl_prompts_16_2026_06_07/c4_validation_ppl_prompts.txt \
    --limit-prompts 16 \
    --max-length 96 \
    --device cuda \
    --dtype float16 \
    --out-json outputs/official_awq_public_calib_qwen25_0p5b_c4_16_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_C4_16_2026_06_07.md
```

Expanded 16-prompt gate:

```bash
python train_python/gate_official_awq_public_calib.py \
  --smoke-summary-json outputs/official_awq_public_calib_qwen25_0p5b_summary_2026_06_07.json \
  --smoke-guard-json outputs/official_awq_public_calib_qwen25_0p5b_gpu_guard_2026_06_07.json \
  --eval-summary wikitext2_16=outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_16_summary_2026_06_07.json \
  --eval-guard wikitext2_16=outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_16_gpu_guard_2026_06_07.json \
  --eval-summary c4_16=outputs/official_awq_public_calib_qwen25_0p5b_c4_16_summary_2026_06_07.json \
  --eval-guard c4_16=outputs/official_awq_public_calib_qwen25_0p5b_c4_16_gpu_guard_2026_06_07.json \
  --min-eval-slices 2 \
  --min-total-tokens 2800 \
  --min-awq-blocks 8 \
  --max-memory-ratio 0.90 \
  --max-ppl-ratio 2.0 \
  --out-json outputs/official_awq_public_calib_qwen25_0p5b_bundle_16_gate_2026_06_07.json \
  --out-md outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md
```

Current expanded AutoAWQ result:

| slice | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2 test eval | 16 | 1413 | 24.591 | 29.789 | 1.2114 | 0.5493 |
| C4 validation eval | 16 | 1444 | 29.918 | 35.375 | 1.1824 | 0.5678 |

Public-calibration GPTQModel budget-aligned fresh quantization plus WikiText2 eval:

```bash
python train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.85 \
  --max-start-memory-ratio 0.75 \
  --min-disk-free-gb 5 \
  --disk-check-path . \
  --poll-seconds 1.0 \
  --timeout-sec 2400 \
  --out outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_gpu_guard_2026_06_07.json \
  -- \
  python train_python/run_official_gptqmodel_public_calib.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --save-dir outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt \
    --prompts data_eval/public_ppl_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --limit-prompts 8 \
    --max-calib-samples 12 \
    --calibration-data-min-length 4 \
    --max-length 96 \
    --bits 4 \
    --group-size 128 \
    --backend gptq_torch \
    --device cuda \
    --local-files-only \
    --out-json outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_WIKITEXT2_2026_06_07.md
```

The GPTQModel script also supports `--reuse-existing-artifact` for
maintenance-only reload checks. Do not overwrite the formal quantize-save-reload
evidence with a reuse-only run.

Current C4 eval slice reuses the artifact from the fresh quantization run:

```bash
python train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.85 \
  --max-start-memory-ratio 0.75 \
  --min-disk-free-gb 5 \
  --disk-check-path . \
  --poll-seconds 1.0 \
  --timeout-sec 900 \
  --out outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_c4_gpu_guard_2026_06_07.json \
  -- \
  python train_python/run_official_gptqmodel_public_calib.py \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --save-dir outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt \
    --prompts data_eval/public_ppl_prompts_2026_06_07/c4_validation_ppl_prompts.txt \
    --limit-prompts 8 \
    --max-calib-samples 12 \
    --calibration-data-min-length 4 \
    --max-length 96 \
    --bits 4 \
    --group-size 128 \
    --backend gptq_torch \
    --device cuda \
    --local-files-only \
    --reuse-existing-artifact \
    --out-json outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_c4_summary_2026_06_07.json \
    --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_C4_2026_06_07.md
```

Current GPTQModel public-calibrated readiness result:

| slice | prompts | tokens | FP16 PPL | GPTQModel PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| WikiText2 test eval | 8 | 760 | 24.676 | 31.953 | 1.2949 | false | 0.6111 |
| C4 validation eval | 8 | 727 | 32.952 | 39.810 | 1.2081 | true | 0.6097 |

Expanded 16-prompt GPTQModel eval reuses the saved public-calibrated artifact:

| slice | prompts | tokens | FP16 PPL | GPTQModel PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| WikiText2 test eval | 16 | 1413 | 24.591 | 30.910 | 1.2570 | true | 0.5747 |
| C4 validation eval | 16 | 1444 | 29.918 | 36.362 | 1.2154 | true | 0.5566 |

GPTQModel 16-prompt readiness gate:

```bash
python train_python/gate_official_gptqmodel_public_calib.py \
  --summary-json outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_summary_2026_06_07.json \
  --guard-json outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_gpu_guard_2026_06_07.json \
  --eval-summary wikitext2=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_16_summary_2026_06_07.json \
  --eval-guard wikitext2=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_wikitext2_16_gpu_guard_2026_06_07.json \
  --eval-summary c4=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_c4_16_summary_2026_06_07.json \
  --eval-guard c4=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_c4_16_gpu_guard_2026_06_07.json \
  --min-eval-slices 2 \
  --min-total-tokens 2800 \
  --min-calibration-texts 12 \
  --max-memory-ratio 0.90 \
  --max-ppl-ratio 2.0 \
  --out-json outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_16_gate_2026_06_07.json \
  --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md
```

Qwen2.5-1.5B GPTQModel scale-up smoke:

```bash
export NVIDIA_SMI_PATH=/usr/lib/wsl/lib/nvidia-smi
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --max-length-ceiling 0 \
  --poll-seconds 2 \
  --timeout-sec 3600 \
  --min-disk-free-gb 20 \
  --disk-check-path /home/rui \
  --out outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_gpu_guard_2026_06_08.json \
  -- \
  python3 train_python/run_official_gptqmodel_public_calib.py \
    --model Qwen/Qwen2.5-1.5B-Instruct \
    --save-dir /home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08 \
    --out-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_summary_2026_06_08.json \
    --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_1P5B_SMOKE4_2026_06_08.md \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --calibration-prompts data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt \
    --prompts data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt \
    --limit-prompts 4 \
    --max-calib-samples 4 \
    --max-length 96 \
    --bits 4 \
    --group-size 128 \
    --device cuda \
    --backend gptq_torch \
    --dtype float16 \
    --local-files-only
```

The artifact path is intentionally outside the repo (`/home/rui/eigenskill_artifacts`)
because it is a 1.1 GB local model package.

Qwen2.5-1.5B GPTQModel 4-prompt smoke gate:

```bash
python train_python/gate_official_gptqmodel_public_calib.py \
  --summary-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_summary_2026_06_08.json \
  --guard-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_gpu_guard_2026_06_08.json \
  --min-calibration-texts 4 \
  --min-tokens 300 \
  --max-memory-ratio 0.90 \
  --max-ppl-ratio 1.30 \
  --out-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_gate_2026_06_08.json \
  --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_1P5B_SMOKE4_GATE_2026_06_08.md
```

Qwen2.5-1.5B GPTQModel 16-prompt eval gate:

```bash
python train_python/gate_official_gptqmodel_public_calib.py \
  --summary-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_summary_2026_06_08.json \
  --guard-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_smoke4_gpu_guard_2026_06_08.json \
  --eval-summary wikitext2=outputs/official_gptqmodel_public_calib_qwen25_1p5b_wikitext2_16_summary_2026_06_08.json \
  --eval-guard wikitext2=outputs/official_gptqmodel_public_calib_qwen25_1p5b_wikitext2_16_gpu_guard_2026_06_08.json \
  --eval-summary c4=outputs/official_gptqmodel_public_calib_qwen25_1p5b_c4_16_summary_2026_06_08.json \
  --eval-guard c4=outputs/official_gptqmodel_public_calib_qwen25_1p5b_c4_16_gpu_guard_2026_06_08.json \
  --min-eval-slices 2 \
  --min-total-tokens 2800 \
  --min-calibration-texts 4 \
  --max-memory-ratio 0.90 \
  --max-ppl-ratio 1.30 \
  --out-json outputs/official_gptqmodel_public_calib_qwen25_1p5b_16_gate_2026_06_08.json \
  --out-md outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_1P5B_16_GATE_2026_06_08.md
```

Current Qwen2.5-1.5B GPTQModel scale-up results:

| slice | prompts | tokens | FP16 PPL | GPTQModel PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| smoke | 4 | 380 | 14.1567 | 16.3179 | 1.1527 | false | 0.8543 |
| WikiText2 16 | 16 | 1413 | 16.9841 | 19.2981 | 1.1363 | true | 0.7698 |
| C4 16 | 16 | 1444 | 21.4055 | 23.3815 | 1.0923 | true | 0.8266 |

Qwen2.5-1.5B GPTQModel subset100 task-execution gate:

```bash
python train_python/gate_official_ptq_task_retention.py \
  --baseline-variant gptqmodel \
  --required-variant gptqmodel \
  --required-format mmlu \
  --required-format gsm8k \
  --min-tasks-per-case 100 \
  --max-memory-ratio 0.90 \
  --max-accuracy-drop 1.0 \
  --matrix-title "Official GPTQModel Qwen2.5-1.5B Subset100 Task-Execution Matrix" \
  --evidence-label "GPTQModel Qwen2.5-1.5B MMLU100/GSM8K100 task-execution slice" \
  --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_subset100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_subset100_gpu_guard_2026_06_08.json \
  --case gptqmodel:gsm8k=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_subset100_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_subset100_gpu_guard_2026_06_08.json \
  --out-json outputs/official_gptqmodel_task_execution_qwen25_1p5b_subset100_matrix_2026_06_08.json \
  --out-md outputs/OFFICIAL_GPTQMODEL_TASK_EXECUTION_QWEN25_1P5B_SUBSET100_MATRIX_2026_06_08.md
```

Current subset100 result: 200 guarded public task executions, MMLU 25/100,
GSM8K 8/100, mean `10.6469` tokens/s, mean TTFT `0.236180` s, and peak guard
VRAM ratio `0.6672`. This is a native-package execution check only; it is not a
matched FP16/AWQ comparison or leaderboard-scale retention result.

Official PTQ readiness matrix:

```bash
python train_python/gate_official_ptq_readiness_matrix.py \
  --case autoawq=outputs/official_awq_public_calib_qwen25_0p5b_bundle_16_gate_2026_06_07.json \
  --case gptqmodel=outputs/official_gptqmodel_public_calib_qwen25_0p5b_budget8_16_gate_2026_06_07.json \
  --required-package autoawq \
  --required-package gptqmodel \
  --required-label wikitext2 \
  --required-label c4 \
  --min-packages 2 \
  --min-eval-slices 2 \
  --min-total-tokens 2800 \
  --max-ppl-ratio 2.0 \
  --max-memory-ratio 0.90 \
  --out-json outputs/official_ptq_readiness_matrix_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/OFFICIAL_PTQ_READINESS_MATRIX_QWEN25_0P5B_2026_06_07.md
```

Current matrix result: 2 packages (`autoawq`, `gptqmodel`), one model
(`Qwen/Qwen2.5-0.5B-Instruct`), normalized W4 group-128 quant shape, common
WikiText2/C4 eval labels, matched 2857-token public eval budgets per package,
and 5714 total eval tokens across the readiness probes. This matrix is for
alignment and auditability; it is not a fair head-to-head quality comparison
because package kernels/backend settings, complete task-retention coverage, and
broader official baseline settings still differ.

Aggregate gate:

```bash
python train_python/gate_official_awq_public_calib.py \
  --smoke-summary-json outputs/official_awq_public_calib_qwen25_0p5b_summary_2026_06_07.json \
  --smoke-guard-json outputs/official_awq_public_calib_qwen25_0p5b_gpu_guard_2026_06_07.json \
  --eval-summary wikitext2=outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_summary_2026_06_07.json \
  --eval-guard wikitext2=outputs/official_awq_public_calib_qwen25_0p5b_wikitext2_gpu_guard_2026_06_07.json \
  --eval-summary c4=outputs/official_awq_public_calib_qwen25_0p5b_c4_summary_2026_06_07.json \
  --eval-guard c4=outputs/official_awq_public_calib_qwen25_0p5b_c4_gpu_guard_2026_06_07.json \
  --min-eval-slices 2 \
  --min-total-tokens 512 \
  --min-awq-blocks 4 \
  --max-memory-ratio 0.90 \
  --max-ppl-ratio 2.0 \
  --out-json outputs/official_awq_public_calib_qwen25_0p5b_bundle_gate_2026_06_07.json \
  --out-md outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_GATE_2026_06_07.md
```

Valid claim:

- minimal same-prompt FP16-vs-AutoAWQ PPL comparisons completed under guard,
  including two tiny public text slices;
- one public-calibrated AutoAWQ W4 group-128 bundle completed guarded
  quantization and two tiny public PPL eval slices;
- the same public-calibrated AutoAWQ bundle has an expanded 16-prompt-per-split
  WikiText2/C4 PPL gate totaling 2857 eval tokens, with max PPL ratio 1.2114;
- one public-calibrated GPTQModel W4 group-128 smoke completed guarded
  quantization with 12 public calibration texts, local artifact save/reload
  through `gptq_torch`, and an expanded 16-prompt-per-split WikiText2/C4 PPL
  gate totaling 2857 eval tokens, with max PPL ratio 1.2570;
- the official PTQ readiness matrix verifies that the current AutoAWQ and
  GPTQModel probes share the same model, W4/G128 quantization shape,
  WikiText2/C4 eval labels, and 2857-token public eval budget before being
  presented together.

Invalid claim:

- this is a full WikiText2/C4 baseline, task-retention result, official GPTQ
  comparison, matched calibration-budget competition, or SOTA PTQ result.

## Calibration Instability Benchmark Gate

`train_python/build_calibration_instability_benchmark.py` aggregates multiple
WikiText2-vs-C4 module-sensitivity split comparisons into one benchmark table.
It is the research-problem gate: it checks whether sensitivity rankings are
unstable across calibration distributions on multiple model families.

Current gate:

```bash
python train_python/build_calibration_instability_benchmark.py \
  --case qwen3_0p6b=outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json=outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json \
  --case qwen3_1p7b=outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json=outputs/qwen3_1p7b_module_loss_sensitivity_c4_limit2_group128.json \
  --case olmo2_1b=outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128.json=outputs/olmo2_0425_1b_module_loss_sensitivity_c4_limit2_group128.json \
  --top-k 10,20,40 \
  --min-cases 3 \
  --min-unstable-cases 3 \
  --instability-spearman-threshold 0.30 \
  --instability-jaccard-threshold 0.55 \
  --out-json outputs/calibration_instability_benchmark_2026_06_06.json \
  --out-md outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md
```

Current result: 3/3 unstable cases, mean score/cost Spearman `0.0713`, mean
positive-set Jaccard `0.4349`, and mean top-20 Jaccard `0.1022`.

Valid claim:

- sensitivity ranking from one small calibration distribution is unstable
  across the measured model/dataset cases.

Invalid claim:

- instability alone proves consensus allocation is better. Downstream PPL/task
  gates are still required.

## Sensitivity Perturbation Matrix Gate

`train_python/gate_sensitivity_perturbation_matrix.py` compares sensitivity
rankings under two different perturbation axes. The current gate asks whether
same-model calibration sample-size changes are more stable than directly
transferring sensitivity rankings across Qwen2.5 model scale.

Current gate:

```bash
python train_python/gate_sensitivity_perturbation_matrix.py \
  --case sample_size:qwen25_0p5b_limit2_vs_limit8=outputs/qwen25_0p5b_module_loss_sensitivity_limit2_group128.json=outputs/qwen25_0p5b_module_loss_sensitivity_limit8_group128.json \
  --case sample_size:qwen25_1p5b_limit2_vs_limit8=outputs/qwen25_1p5b_module_loss_sensitivity_limit2_group128.json=outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128.json \
  --case model_scale:qwen25_0p5b_vs_1p5b_limit2=outputs/qwen25_0p5b_module_loss_sensitivity_limit2_group128.json=outputs/qwen25_1p5b_module_loss_sensitivity_limit2_group128.json \
  --out-json outputs/sensitivity_perturbation_matrix_qwen25_2026_06_07.json \
  --out-md outputs/SENSITIVITY_PERTURBATION_MATRIX_QWEN25_2026_06_07.md
```

Current result: 3 cases, sample-size mean Spearman `0.6356`, sample-size min
top-20 Jaccard `0.4815`, model-scale mean Spearman `0.1273`, model-scale
mean top-20 Jaccard `0.2903`, and perturbation separation margin `0.5082`.

Valid claim:

- within the measured Qwen2.5 sensitivity artifacts, increasing calibration
  sample count inside the same model preserves sensitivity rankings
  substantially better than cross-model-scale transfer.

Invalid claim:

- this proves downstream quality retention, a universal scaling law, or a
  production quantization method.

## Calibration Seed Stability Gate

`train_python/gate_calibration_seed_stability.py` audits whether deterministic
prompt sampling changes the module-sensitivity ranking for the same model and
prompt pool. The current gate uses six Qwen2.5-0.5B-Instruct sensitivity
artifacts, each sampled as four prompts from the same 16-prompt public
WikiText2 pool, and reports pair-bootstrap confidence intervals over the
pairwise stability metrics.

Current gate:

```bash
python train_python/gate_calibration_seed_stability.py \
  --case seed11=outputs/qwen25_0p5b_seed11_module_loss_sensitivity_group128_2026_06_07.json \
  --case seed12=outputs/qwen25_0p5b_seed12_module_loss_sensitivity_group128_2026_06_07.json \
  --case seed13=outputs/qwen25_0p5b_seed13_module_loss_sensitivity_group128_2026_06_07.json \
  --case seed14=outputs/qwen25_0p5b_seed14_module_loss_sensitivity_group128_2026_06_07.json \
  --case seed15=outputs/qwen25_0p5b_seed15_module_loss_sensitivity_group128_2026_06_07.json \
  --case seed16=outputs/qwen25_0p5b_seed16_module_loss_sensitivity_group128_2026_06_07.json \
  --min-cases 6 \
  --min-pairs 15 \
  --bootstrap-samples 5000 \
  --out-json outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/CALIBRATION_SEED_STABILITY_QWEN25_0P5B_2026_06_07.md
```

Current result: 6 prompt selections, 15 finite pairwise comparisons, mean
score/cost Spearman `0.4324` with bootstrap 95% CI `[0.3557, 0.5174]`,
minimum score/cost Spearman `0.2284`, mean top-20 Jaccard `0.4672` with CI
`[0.4200, 0.5292]`, minimum top-20 Jaccard `0.3793`, and mean positive-set
Jaccard `0.5734` with CI `[0.5375, 0.6120]`.

Valid claim:

- same-model prompt-seed sensitivity artifacts can be audited for ranking and
  top-sensitive-set stability under a fixed public prompt pool.

Invalid claim:

- this proves downstream quality retention, broad calibration-seed coverage,
  deployment speed, or SOTA quantization.

## CSI vs Calibration Size Gate

`train_python/gate_csi_vs_n_curve.py` turns multiple seed-stability gates into
the paper-facing CSI-vs-calibration-size curve. It consumes the n=2, n=4, and
n=8 Qwen2.5-0.5B-Instruct gates, verifies that each source gate passed, and
requires mean score/cost Spearman, mean top-20 Jaccard, and mean positive-set
Jaccard to increase monotonically with calibration prompt count.

The n=2 source gate uses `seed11`, `seed12`, `seed13`, `seed14`, `seed15`, and
`seed17`. The originally measured `seed16` artifact is retained, but it selects
the same two prompts as `seed13` and is therefore excluded from the formal n=2
gate to preserve six unique prompt selections.

Current gate:

```bash
python train_python/gate_csi_vs_n_curve.py \
  --case 2=outputs/calibration_seed_stability_qwen25_0p5b_n2_2026_06_07.json \
  --case 4=outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --case 8=outputs/calibration_seed_stability_qwen25_0p5b_n8_2026_06_07.json \
  --min-points 3 \
  --out-json outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/CSI_VS_N_CURVE_QWEN25_0P5B_2026_06_07.md \
  --out-svg outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.svg
```

Current result: three calibration sizes pass. Mean score/cost Spearman rises
from `0.3725` at n=2 to `0.4324` at n=4 and `0.6645` at n=8, for a total gain
of `0.2920`. Mean top-20 Jaccard rises from `0.3797` to `0.4672` to `0.6449`,
and mean positive-set Jaccard rises from `0.5485` to `0.5734` to `0.7282`.

Valid claim:

- in this fixed Qwen2.5-0.5B public-prompt setting, increasing calibration
  prompt count from 2 to 8 improves measured sensitivity-ranking stability.

Invalid claim:

- this proves a universal scaling law, downstream task retention, large-model
  behavior, deployment speed, or SOTA quantization.

## CSI Trend Significance Gate

`train_python/gate_csi_trend_significance.py` adds a statistical check on top
of the CSI-vs-n curve. It consumes the same n=2/4/8 seed-stability gates, then
compares the n=8 seed-pair metric distribution against the n=2 distribution
with independent bootstrap mean-gain confidence intervals and random pair
dominance probabilities.

Current gate:

```bash
python train_python/gate_csi_trend_significance.py \
  --case 2=outputs/calibration_seed_stability_qwen25_0p5b_n2_2026_06_07.json \
  --case 4=outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --case 8=outputs/calibration_seed_stability_qwen25_0p5b_n8_2026_06_07.json \
  --bootstrap-samples 5000 \
  --min-full-range-gain-low 0.0 \
  --min-full-range-dominance-probability 0.90 \
  --out-json outputs/csi_trend_significance_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/CSI_TREND_SIGNIFICANCE_QWEN25_0P5B_2026_06_07.md
```

Current result: the n=8-vs-n=2 full-range bootstrap gain 95% CI is positive
for all three audited metrics. The minimum lower CI bound is `0.1352`, and the
minimum random seed-pair dominance probability is `0.9422`.

Valid claim:

- in this fixed Qwen2.5-0.5B public-prompt setting, the measured n=8 stability
  distribution statistically dominates the measured n=2 distribution.

Invalid claim:

- this proves a universal scaling law, downstream task retention, large-model
  behavior, deployment speed, or SOTA quantization.

## CSI Null Permutation Gate

`train_python/gate_csi_null_permutation.py` adds a pooled-label null test for
the same n=2 and n=8 seed-pair stability metrics. It shuffles the calibration
size labels over the pooled metric values, estimates a one-sided p-value for
the observed n=8-minus-n=2 mean gain, and reports Holm-adjusted p-values across
the audited metrics.

Current gate:

```bash
python train_python/gate_csi_null_permutation.py \
  --case 2=outputs/calibration_seed_stability_qwen25_0p5b_n2_2026_06_07.json \
  --case 4=outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --case 8=outputs/calibration_seed_stability_qwen25_0p5b_n8_2026_06_07.json \
  --permutation-samples 20000 \
  --max-holm-p-value 0.01 \
  --out-json outputs/csi_null_permutation_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/CSI_NULL_PERMUTATION_QWEN25_0P5B_2026_06_07.md
```

Current result: all three audited metrics have positive observed n=8-vs-n=2
gains. Under the 20,000-sample Monte-Carlo null, each metric has raw
`p=4.99975e-05` and the maximum Holm-adjusted p-value is `0.000149993`.

Valid claim:

- in this fixed Qwen2.5-0.5B public-prompt setting, the n=8 stability gain is
  unlikely under a pooled n=2/n=8 seed-pair label-shuffle null.

Invalid claim:

- this proves a universal scaling law, downstream task retention, large-model
  behavior, deployment speed, or SOTA quantization.

## Rank-Inversion Theory Gate

`train_python/gate_rank_inversion_theory.py` instantiates the paper's
Chebyshev-style inversion-risk argument with the committed n=2/4/8 Qwen2.5
seed-stability artifacts. For each calibration size, it loads the underlying
module-sensitivity JSON files, estimates seed-level means and variances for
each module score, and summarizes pairwise ranking inversions. The bound proxy
is `(Var_i + Var_j) / gap_ij^2`, clipped to 1.0.

Current gate:

```bash
python train_python/gate_rank_inversion_theory.py \
  --case 2=outputs/calibration_seed_stability_qwen25_0p5b_n2_2026_06_07.json \
  --case 4=outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json \
  --case 8=outputs/calibration_seed_stability_qwen25_0p5b_n8_2026_06_07.json \
  --margin-quantile 0.75 \
  --max-final-margin-inversion-rate 0.10 \
  --out-json outputs/rank_inversion_theory_qwen25_0p5b_2026_06_07.json \
  --out-md outputs/RANK_INVERSION_THEORY_QWEN25_0P5B_2026_06_07.md
```

Current result: mean empirical inversion rate falls from `0.2418` at n=2 to
`0.1442` at n=8, and the mean Chebyshev proxy bound falls from `0.8473` to
`0.6097`. On the top 25% largest-gap module pairs, empirical inversion falls
from `0.0969` to `0.0427`, and the bound proxy falls from `0.5974` to `0.2713`.

Valid claim:

- the observed calibration-size stability curve is consistent with a
  variance-over-gap rank-inversion analysis on the measured Qwen2.5-0.5B seed
  artifacts.

Invalid claim:

- this proves a tight bound, downstream quality retention, large-model
  universality, deployment speed, or SOTA quantization.

## Calibration Robustness Stress Gate

`train_python/build_calibration_robustness_stress.py` converts committed
fake-quant PPL summaries into a risk table. Unlike the split-instability gate,
this gate is method-facing: it checks whether the chosen target policy beats
uniform INT4, the best random mixed-precision seed, and the random-seed mean
across the current cross-model short-slice evidence set.

Current gate:

```bash
python train_python/build_calibration_robustness_stress.py \
  --case qwen3_0p6b_wikitext2_64=outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_wikitext2_64_len96_summary.json \
  --case qwen3_0p6b_c4_64=outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_c4_64_summary.json \
  --case qwen3_1p7b_wikitext2_64=outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_wikitext2_64_summary.json \
  --case qwen3_1p7b_wikitext2_128=outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_wikitext2_128_summary.json \
  --case qwen3_1p7b_c4_64=outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_c4_64_summary.json \
  --case olmo2_1b_wikitext2_64=outputs/olmo2_0425_1b_consensus_vs_random16_ppl_wikitext2_64_summary.json \
  --case olmo2_1b_c4_64=outputs/olmo2_0425_1b_consensus_vs_random16_ppl_c4_64_summary.json \
  --case smollm2_1p7b_wikitext2_16=outputs/smollm2_1p7b_full_random16_ppl_wikitext2_16_summary.json \
  --case smollm2_1p7b_wikitext2_64=outputs/smollm2_1p7b_full_random16_ppl_wikitext2_64_summary.json \
  --case smollm2_1p7b_wikitext2_128=outputs/smollm2_1p7b_full_random16_ppl_wikitext2_128_summary.json \
  --case smollm2_1p7b_c4_64=outputs/smollm2_1p7b_full_random16_ppl_c4_64_summary.json \
  --min-cases 11 \
  --min-uniform-win-rate 1.0 \
  --min-best-random-win-rate 1.0 \
  --min-random-mean-win-rate 1.0 \
  --out-json outputs/calibration_robustness_stress_gate_2026_06_07.json \
  --out-md outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md
```

Current result: 11/11 wins versus uniform INT4, 11/11 wins versus the best
random seed, 11/11 wins versus the random-seed mean, mean margin `+4.2942` PPL
versus uniform, worst margin `+0.1120` PPL versus the best random seed,
bootstrap 95% CI `[+0.6143, +1.7982]` PPL for the mean best-random margin, and
one-sided sign-test p-value `0.000488`.

Valid claim:

- current target policies pass a cross-model fake-quant short-slice robustness
  stress gate against uniform and random mixed-precision baselines.

Invalid claim:

- this proves SOTA PTQ, official baseline superiority, downstream task
  retention, or production runtime quality.

## Consensus Transfer Boundary Gate

`train_python/build_consensus_transfer_boundary.py` compares the WikiText2-only,
C4-only, and cross-split consensus policies on paired WikiText2/C4 PPL summaries.
This is a boundary gate: consensus is allowed to have small regret versus the
best single-split policy, but it must avoid the worse single-split policy on the
paired slices.

Current gate:

```bash
python train_python/build_consensus_transfer_boundary.py \
  --case qwen3_0p6b=outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_wikitext2_64_len96_summary.json=outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_c4_64_summary.json \
  --case qwen3_1p7b=outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_wikitext2_64_summary.json=outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_c4_64_summary.json \
  --min-cases 2 \
  --max-regret-vs-best-single 0.5 \
  --min-worst-single-win-rate 1.0 \
  --out-json outputs/consensus_transfer_boundary_gate_2026_06_07.json \
  --out-md outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md
```

Current result: 2 cases and 4 paired slices. Consensus wins 4/4 versus the
worse single-split policy, wins 2/4 versus the best single-split policy, has
minimum margin `+0.8726` PPL versus the worse single split, and maximum regret
`+0.3046` PPL versus the best single split.

Valid claim:

- consensus reduces the worst-single-split risk on the current paired Qwen3
  transfer slices while keeping regret versus the best single split bounded.

Invalid claim:

- consensus always beats the best single-split allocation, or this gate proves
  broad downstream task retention.

## Interaction-Aware Swap Boundary Gate

`train_python/build_interaction_swap_boundary.py` turns bounded one-step
swap-search outputs into a machine-checkable global-feedback diagnostic. It
starts from additive sensitivity allocations, evaluates proposed one-out/one-in
swaps with global PPL, and records whether global feedback exposes interactions
that the local proxy would miss.

Current gate:

```bash
python train_python/build_interaction_swap_boundary.py \
  --search-case wikitext2_32=outputs/smollm2_1p7b_full_swap_search_wikitext2_32_summary.json=outputs/smollm2_1p7b_full_swap_search_wikitext2_32_guard.json \
  --search-case wikitext2_64=outputs/smollm2_1p7b_full_swap_search_wikitext2_64_summary.json=outputs/smollm2_1p7b_full_swap_search_wikitext2_64_guard.json \
  --search-case c4_64=outputs/smollm2_1p7b_full_swap_search_c4_64_summary.json=outputs/smollm2_1p7b_full_swap_search_c4_64_guard.json \
  --transfer-matrix outputs/smollm2_1p7b_swap_transfer_matrix.json \
  --min-cases 3 \
  --min-improved-cases 1 \
  --min-interaction-counterexamples 1 \
  --min-total-trials 12 \
  --max-transfer-regret-ppl 0.02 \
  --max-guard-vram-ratio 0.85 \
  --out-json outputs/interaction_swap_boundary_gate_2026_06_07.json \
  --out-md outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md
```

Current result: 3 search cases, 16 evaluated swaps, 5 improved trials, and 5
locally-negative-but-globally-improved counterexamples. The best local
improvement is `+0.0502` PPL. Transfer has 1/2 positive rows and maximum regret
`0.0087` PPL. Peak guard VRAM ratio is `0.8487`.

Valid claim:

- bounded global-PPL feedback exposes interaction effects beyond independent
  module ranking in the committed SmolLM2-1.7B fake-quant diagnostic.

Invalid claim:

- this proves a globally optimal allocator, broad transfer, SOTA quantization,
  or production runtime behavior.

## Robust-LCB Consensus Allocation Gate

`train_python/gate_robust_lcb_consensus.py` verifies that robust lower-confidence
bound consensus allocation artifacts exist across the current measured model
family. This gate exists because average-score consensus is too weak as a paper
claim by itself: the robust-LCB policy discounts one-sided calibration spikes
and requires selected modules to expose positive cross-split consistency.

Current gate:

```bash
python train_python/gate_robust_lcb_consensus.py \
  --case qwen3_0p6b=outputs/qwen3_0p6b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json \
  --case qwen3_1p7b=outputs/qwen3_1p7b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json \
  --case olmo2_0425_1b=outputs/olmo2_0425_1b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json \
  --out-json outputs/robust_lcb_consensus_family_gate_2026_06_06.json \
  --out-md outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md
```

Current result: 3 cases, max average bits `4.4997` under the `4.5` target,
99 total high-bit modules, and 80/80 selected modules with positive consistency
evidence.

Valid claim:

- robust-LCB consensus allocation artifacts are executable and budget-respecting
  across the current three measured model families.

Invalid claim:

- robust-LCB consensus alone proves downstream PPL/task quality, mobile
  deployment, or SOTA quantization quality.

## Robust-LCB Quality Boundary Gate

`train_python/gate_robust_lcb_quality.py` verifies the downstream fake-quant
PPL boundary for robust-LCB on the current Qwen3-0.6B WikiText2/C4 slices. It
requires robust-LCB to beat uniform INT4 under the GPU guard, but it does not
require robust-LCB to beat mean consensus; that comparison is reported as
boundary evidence.

Current gate:

```bash
python train_python/gate_robust_lcb_quality.py \
  --case wikitext2_64_len96=outputs/qwen3_0p6b_robust_lcb_vs_mean_ppl_wikitext2_64_len96_summary.json=outputs/qwen3_0p6b_robust_lcb_vs_mean_gpu_guard_wikitext2_64_len96.json \
  --case c4_64=outputs/qwen3_0p6b_robust_lcb_vs_mean_ppl_c4_64_summary.json=outputs/qwen3_0p6b_robust_lcb_vs_mean_gpu_guard_c4_64.json \
  --out-json outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json \
  --out-md outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md
```

Current result: robust-LCB wins 2/2 versus uniform INT4, wins 0/2 versus mean
consensus, has mean PPL margin `+5.6188` versus uniform and `-2.8834` versus
mean consensus, and stays below the 90% guard with max VRAM ratio `0.7032`.

Valid claim:

- robust-LCB has guarded downstream PPL evidence that it is better than uniform
  INT4 on these two Qwen3-0.6B slices.

Invalid claim:

- robust-LCB is superior to mean consensus, SOTA, or quality-preserving across
  broader tasks.

## Triton Mixed-GEMM Gate

The Triton gate consumes `tuning_results.jsonl` from `train_python/tune_triton_blocks.py`.
It verifies:

- enough valid kernel configurations completed;
- at least one grouped packed INT4/INT8 config beat torch FP16;
- grouped execution beat the row-wise dynamic path;
- grouped relative L2 error stayed below a configured ceiling;
- the GPU guard stayed below the configured VRAM ratio.

Example:

```bash
python train_python/gate_triton_tuning.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_smoke_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_tuning_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_TUNING_GATE_2026_06_06.md \
  --min-valid-configs 24 \
  --min-fp16-wins 2 \
  --min-best-fp16-speedup 1.20 \
  --min-rowwise-wins 20 \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90
```

The `--input` flag is repeatable, so the same gate can validate a multi-shape
family sweep.

Current Qwen-shape family gate:

```bash
python train_python/gate_triton_tuning.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_2048x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_3072x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x3072_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md \
  --min-valid-configs 96 \
  --min-fp16-wins 8 \
  --min-best-fp16-speedup 2.00 \
  --min-rowwise-wins 70 \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90
```

Passing this gate supports only this narrow claim:

```text
For the measured shape family, grouped packed INT4/INT8 Triton execution can
remove row-wise dispatch overhead and can beat torch FP16 in selected tuned
kernel configurations under the configured VRAM guard.
```

It does not support claims about end-to-end LLM speedup, mobile latency, Tensor
Core production readiness, or quantization SOTA.

## Triton Kernel Config Selector

`train_python/select_triton_kernel_configs.py` converts the measured tuning
family into one deterministic config per shape/batch/high_every group. It is a
deployment-planning artifact for the prototype runtime.

Current selector gate:

```bash
python train_python/select_triton_kernel_configs.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_2048x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_3072x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x3072_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_qwen_shape_kernel_config_selector_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_KERNEL_CONFIG_SELECTOR_2026_06_06.md \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90 \
  --min-valid-groups 8 \
  --min-fp16-winning-groups 5 \
  --min-best-fp16-speedup 2.00
```

The current selector passes with 8 valid groups, 6 FP16-winning groups, 7
row-wise-winning groups, and max selected grouped/FP16 speedup 2.7647x.

## Selector-Driven Runtime Wiring

`train_python/measure_esmp_generation_latency.py` accepts
`--kernel-config-selector` for the `triton_grouped` runtime. During each swapped
Linear forward, it matches the module shape and runtime batch size to the
nearest measured selector row and records the chosen config in
`replaced_modules[].runtime_config_summary`.

`train_python/gate_selector_runtime_smoke.py` verifies that this wiring actually
used selector configs under the GPU guard. The current smoke gate passes with 8
configs loaded, 4 selector calls, 7.6413x selected-module compression vs FP32,
4 generated tokens, and 57.21% peak guard memory.

`train_python/benchmark_esmp_linear_runtimes.py` also accepts the selector. The
current 1-module Qwen3-0.6B q_proj benchmark confirms selector calls for batch
1 and batch 12, but `triton_grouped` remains slower than dense/cached in those
small-batch cases. Treat this as evidence for the next systems work item:
fusion, persistent scheduling, or a lower-launch-overhead decode path.

## Selected-Row Runtime Gate

`train_python/gate_selected_row_benchmark.py` gates the selected-row routing
benchmark. The current formal gate uses
`outputs/real_system_packer_2026-06-05/esmp_selected_rows.json` and passes with:

- 108 successful rows and 0 failed rows;
- 27 `triton_selected` cases;
- 4 `triton_selected` wins over dense full output;
- best `triton_selected` speedup vs dense full: 2.2406x;
- median `cached_selected` speedup vs dense full: 1.2565x;
- peak guard memory below 90%.

A fresh focused q_proj batch-12 selected-64 smoke was also run. It confirms the
selected-row cached path can win on the current environment (`1.1767x` vs dense
full), while `triton_selected` remains launch-bound (`0.5668x` vs dense full).
Use this as a constraint for kernel/runtime work, not as an acceleration claim.

## Fused Sidecar Generation Gate

`train_python/gate_fused_sidecar_generation.py` gates the fused selected-row
sidecar smoke. This is an integration check, not a replacement claim: sidecar
kernels run on real HF generation activations and discard their outputs while
the dense Transformer path still executes.

Current gate:

```bash
python train_python/gate_fused_sidecar_generation.py \
  --generation-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async.json \
  --baseline-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok.json \
  --guard-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md \
  --min-layers 3 \
  --min-sidecars 3 \
  --min-sidecar-calls 48 \
  --min-calls-per-sidecar 16 \
  --min-selected-rows-total 192 \
  --min-generated-tokens 16 \
  --min-tokens-per-second 20.0 \
  --max-median-sidecar-ms 0.30 \
  --max-max-sidecar-ms 0.50 \
  --require-prefill-shape \
  --require-decode-shape \
  --min-tps-ratio-vs-baseline 0.75 \
  --max-memory-ratio 0.90
```

The current gate passes with 3 sidecars, 48 sidecar calls, exact generated-text
match versus the same-loader baseline, 0.8080x baseline throughput, 0.206160 ms
median sidecar CUDA event time, and 43.96% peak guard memory.

Valid claim:

- fused selected-row ESMP kernels execute inside the real HF generation loop
  with measured CUDA event timing and bounded additive overhead.

Invalid claim:

- sidecar execution proves end-to-end acceleration. It does not replace dense
  QKV computation.

## Fused QKV Replacement Generation Gate

`train_python/gate_fused_qkv_generation.py` gates the stronger replacement
smoke from `train_python/measure_esmp_fused_qkv_generation.py`. This path
actually replaces selected `q_proj`, `k_proj`, and `v_proj` modules with a
shared fused ESMP runtime. The gate checks generation success, compression,
TTFT/throughput versus a same-loader baseline, GPU guard compliance, and the
QKV cache invariant:

```text
wrapper_calls == fused_compute_calls + cache_hits
fused_compute_calls == cache_misses
```

Current gate:

```bash
python train_python/gate_fused_qkv_generation.py \
  --generation-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok.json \
  --baseline-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_64tok.json \
  --guard-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md \
  --min-replacements 1 \
  --min-generated-tokens 64 \
  --min-tokens-per-second 25.0 \
  --min-compression-vs-fp32 6.0 \
  --max-median-replacement-ms 0.25 \
  --max-max-replacement-ms 0.70 \
  --min-wrapper-calls-per-replacement 192 \
  --min-fused-compute-calls-per-replacement 64 \
  --min-cache-hits-per-replacement 128 \
  --min-cache-misses-per-replacement 64 \
  --min-tps-ratio-vs-baseline 1.05 \
  --max-ttft-ratio-vs-baseline 1.00 \
  --min-common-prefix-chars 100 \
  --max-memory-ratio 0.90
```

The current gate passes on Qwen3-0.6B layer-0 QKV replacement with 64 generated
tokens, 1.1300x tokens/s versus the same-loader baseline, 0.6839x TTFT ratio,
6.1682x compression versus FP32, 192/64/128/64 wrapper/fused/hit/miss calls,
0.192896 ms median replacement CUDA event time, and 44.01% peak guard memory.
The generated text is not an exact match, but it keeps a 210-character common
prefix in this smoke; quality preservation remains a separate open gate.

Valid claim:

- a shallow fused packed QKV replacement can execute inside HF generation and
  shows guarded smoke-level speed and memory evidence.

Invalid claim:

- this establishes full-model quality-preserving quantized generation.

## Fused QKV Prompt-Suite Quality Gate

`train_python/gate_fused_qkv_prompt_suite.py` gates the prompt-suite quality
audit from `train_python/eval_fused_qkv_prompt_suite.py`, optionally combined
with deterministic shallow task scoring from `train_python/score_prompt_suite.py`.
This gate deliberately separates quality preservation from speed. It checks:

- exact/similarity/prefix preservation across the prompt suite;
- optional rule-scored pass-rate preservation and zero new regressions;
- replacement compression and median CUDA event latency;
- QKV cache invariants;
- GPU guard compliance.

Current gate:

```bash
python train_python/score_prompt_suite.py \
  --input-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_scored.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS17_QKV8_REPACK_SCORED.md

python train_python/gate_fused_qkv_prompt_suite.py \
  --prompt-suite-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json \
  --scored-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_scored.json \
  --guard-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md \
  --min-prompts 6 \
  --min-exact-matches 6 \
  --min-exact-match-rate 1.0 \
  --min-mean-char-edit-similarity 0.99 \
  --min-median-char-edit-similarity 0.99 \
  --min-mean-common-prefix-ratio 0.99 \
  --min-mean-speed-ratio 0.80 \
  --max-median-ttft-ratio 1.25 \
  --min-compression-vs-fp32 3.5 \
  --max-median-replacement-ms 0.25 \
  --min-wrapper-calls 1152 \
  --min-fused-compute-calls 384 \
  --min-cache-hits 768 \
  --min-cache-misses 384 \
  --min-scored-prompts 6 \
  --max-rule-regressions 0 \
  --min-fused-rule-pass-rate 0.80 \
  --max-fused-rule-pass-drop 0 \
  --max-memory-ratio 0.90
```

The current gate passes on the layers `[1, 7]` QKV8 repack candidate with 6/6
exact prompt-suite matches, 1.0 mean edit similarity, 0 rule regressions,
3.9082x compression versus FP32, 1152/384/768/384 wrapper/fused/hit/miss calls,
0.141008 ms median replacement CUDA event time, and 43.59% peak guard memory.
It is slower than the baseline on this suite (0.8957x mean tokens/s), so it is
quality-preservation evidence rather than acceleration evidence.

Valid claim:

- a conservative QKV8 repack candidate preserves the measured prompt-suite
  outputs and shallow rule scores under the configured gate.

Invalid claim:

- this proves semantic quality preservation across tasks, datasets, or larger
  prompt distributions.

## Chat Task Stress-Retention Gate

`train_python/gate_chat_task_regression_analysis.py` gates deterministic
chat-task retention results from `train_python/eval_chat_task_benchmark.py` and
`train_python/analyze_chat_task_regressions.py`. This is stronger than pure
text similarity because rows are scored by task-specific rules, but it is still
a local stress suite rather than a public benchmark replacement.

Current gate:

```bash
python train_python/gate_chat_task_regression_analysis.py \
  --analysis-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json \
  --candidate konly_layers17 \
  --guard-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_qwen3_0p6b_no_think_layers17_konly_32tok_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md \
  --min-candidates 3 \
  --min-tasks 84 \
  --min-task-types 8 \
  --min-baseline-passes 46 \
  --min-fused-passes 45 \
  --min-fused-accuracy 0.535 \
  --max-pass-loss 1 \
  --max-regressions 1 \
  --max-regressions-per-type 1 \
  --min-speedup 0.95 \
  --max-memory-ratio 0.90
```

The current gate passes for `konly_layers17` with 84 tasks across 8 task types.
Baseline passes 46/84 and fused passes 45/84, so the candidate has one allowed
regression and a pass delta of -1. Mean fused/baseline speed is 0.9746x and
peak guard memory is 54.69%. The single regression is preserved in the report:
`stress_json_keys_001` loses a required JSON-key parse.

Valid claim:

- the K-only layers `[1, 7]` replacement candidate survives a deterministic
  84-task stress-retention gate under a one-regression budget.

Invalid claim:

- this is a public benchmark result or proof of broad task-quality
  preservation.

## C++ ESMP Runtime Sweep Gate

`train_python/gate_cpp_runtime_sweep.py` gates the C++ ESMP selected-row runtime
sweep. The current gate uses
`outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.jsonl` and
passes with:

- 42 successful module runs and 0 failures;
- 42/42 selected-row wins over full mixed GEMV;
- min selected/full speedup: 12.7607x;
- median selected/full speedup: 16.8259x;
- best selected/full speedup: 56.4888x;
- median selected-row latency: 0.205620 ms;
- median compression vs FP32: 7.6413x.

A fresh C++ q_proj focus bench was also run against the current binary and
package, giving 29.1892x selected/full speedup for 64 active rows. This is the
strongest current systems evidence for deterministic routed/bypass execution,
but it is still module-level evidence rather than end-to-end generation
latency.

Valid claim:

- measured Triton tuning artifacts can now drive the prototype ESMP generation
  path instead of remaining an offline report;
- output JSON exposes which measured block config was used.
- a small selector-driven runtime smoke is automatically gated for selector use,
  compression, generated-token presence, and GPU memory guard compliance.
- selector-driven module-runtime benchmark records per-case selector calls and
  currently exposes low-batch kernel overhead rather than speedup.
- selected-row routing has a formal gate for module-level evidence, while the
  focused current-environment smoke keeps the low-batch Triton limitation
  explicit.
- fused selected-row sidecars have a formal decode-loop integration gate with
  bounded additive overhead.
- fused packed QKV replacement has a formal guarded smoke gate for shallow
  replacement, including cache-invariant checks.
- fused QKV prompt-suite quality has a formal gate for the conservative
  layers `[1, 7]` QKV8 repack candidate.
- chat-task stress retention has a formal 84-task gate with the remaining
  one-row regression explicitly reported.
- C++ ESMP selected-row runtime has a formal sweep gate; it supports
  module-level bypass claims but not full LLM acceleration claims.

Invalid claim:

- selector-driven generation is faster end-to-end;
- selector coverage generalizes to unmeasured shapes;
- fused QKV replacement is quality-preserving across prompts or layers;
- prompt-suite exact preservation on six prompts is a broad semantic benchmark;
- deterministic chat-task stress passing under a regression budget replaces
  public MMLU/GSM8K/IFEval-style evaluation;
- mobile, Tensor Core production, or CCF-A system claims are established.
