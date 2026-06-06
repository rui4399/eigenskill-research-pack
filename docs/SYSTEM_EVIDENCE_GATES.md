# System Evidence Gates

This repository separates exploratory output from evidence that can survive a
paper review. A result should be treated as paper-facing only when it is backed
by an executable gate and an explicit claim boundary.

## Evidence Ledger

`train_python/build_evidence_ledger.py` is the top-level evidence index. It
loads individual gate JSON files, verifies that every listed gate passed, and
writes one paper-facing ledger table.

Current ledger:

```bash
python train_python/build_evidence_ledger.py \
  --gate public_hygiene=outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --gate calibration_instability=outputs/calibration_instability_benchmark_2026_06_06.json \
  --gate calibration_robustness_stress=outputs/calibration_robustness_stress_gate_2026_06_07.json \
  --gate esmp_package=outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json \
  --gate triton_shape_family=outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --gate selector_runtime=outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json \
  --gate selected_row=outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json \
  --gate cpp_runtime=outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json \
  --gate fused_sidecar=outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --gate fused_qkv_speed=outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --gate fused_qkv_quality=outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --gate chat_task_stress=outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --gate public_task_benchmark=outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json \
  --gate allocation_family_proxy=outputs/q_palette_style_allocation_family_gate_2026_06_06.json \
  --gate robust_lcb_consensus=outputs/robust_lcb_consensus_family_gate_2026_06_06.json \
  --gate robust_lcb_quality=outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json \
  --gate rotation_family_proxy=outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json \
  --gate awq_gptq_proxy=outputs/awq_gptq_proxy_gate_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

The current ledger passes with 18/18 gates across repo hygiene, calibration
robustness, artifact integrity, kernel, runtime wiring, selected-row, C++
runtime, decode integration, QKV replacement, quality, task-retention, and
capability-retention, allocation-comparator, rotation-comparator, and
PTQ-comparator evidence categories.

Valid claim:

- the listed paper-facing evidence is backed by executable gate JSON artifacts.

Invalid claim:

- the ledger itself proves SOTA, mobile deployment, or full paper readiness.

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
trees, NotebookLM/Obsidian exports, or blank README-style placeholder lines.

Example:

```bash
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

Valid claim:

- the current public tree excludes generated delivery bundles and private
  workbench exports.

Invalid claim:

- repository hygiene proves experimental correctness.

## Public Task Benchmark Gate

`train_python/gate_public_task_benchmark.py` verifies that real public-task
subset evaluations ran under GPU guard. It is deliberately a coverage gate, not
an accuracy or leaderboard gate.

Current gate:

```bash
python train_python/gate_public_task_benchmark.py \
  --case mmlu50=outputs/public_task_benchmark_mmlu_ollama_qwen35_4b_summary.json=outputs/public_task_benchmark_mmlu_ollama_qwen35_4b_gpu_guard_2026_06_06.json \
  --case gsm8k50=outputs/public_task_benchmark_gsm8k_ollama_qwen35_4b_summary.json=outputs/public_task_benchmark_gsm8k_ollama_qwen35_4b_gpu_guard_2026_06_06.json \
  --min-cases 2 \
  --min-total-tasks 100 \
  --require-formats mmlu,gsm8k \
  --max-memory-ratio 0.90 \
  --out-json outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json \
  --out-md outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN35_4B_GATE_2026_06_06.md
```

Current result: 100 public subset tasks, 4 total passes, mean accuracy `0.0400`,
mean throughput `83.0283` tok/s, mean TTFT `0.398259` s, and peak guard VRAM
ratio `0.8826`.

Valid claim:

- public MMLU/GSM8K subset evaluation is now wired and guarded.

Invalid claim:

- this proves leaderboard-scale quality, fused-retention quality, or SOTA
  reasoning performance.

## Allocation Family Proxy Gate

`train_python/gate_allocation_family_proxy.py` verifies Q-Palette-style
measured-sensitivity allocation proxy artifacts. It is a comparator-family gate,
not an official reproduction claim.

Current gate:

```bash
python train_python/gate_allocation_family_proxy.py \
  --case wikitext2=outputs/q_palette_style_qwen3_0p6b_wikitext2_group128_summary.json \
  --case c4=outputs/q_palette_style_qwen3_0p6b_c4_group128_summary.json \
  --min-cases 2 \
  --min-records 100 \
  --required-method-token q_palette \
  --out-json outputs/q_palette_style_allocation_family_gate_2026_06_06.json \
  --out-md outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md
```

Current result: 2 cases, 394 total records, and max average bits `4.4997`
under a `4.5` target budget.

Valid claim:

- a Q-Palette-style rate-distortion allocation comparator proxy is executable
  on measured Qwen3-0.6B sensitivity artifacts.

Invalid claim:

- this is a faithful official Q-Palette/IMPQ/WINDQuant reproduction.

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

- a dashboard row marked `missing`, `partial`, `package_only`,
  `evidence_without_package_audit`, or `partial_without_package_audit` supports
  paper-facing competitiveness.

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
versus uniform, and worst margin `+0.1120` PPL versus the best random seed.

Valid claim:

- current target policies pass a cross-model fake-quant short-slice robustness
  stress gate against uniform and random mixed-precision baselines.

Invalid claim:

- this proves SOTA PTQ, official baseline superiority, downstream task
  retention, or production runtime quality.

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
