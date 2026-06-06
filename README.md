# EigenSkill-Q Research Pack

Public repository: https://github.com/rui4399/eigenskill-research-pack

EigenSkill-Q is a small, reproducible research pack for **calibration
robustness in mixed-precision LLM quantization** and deterministic C++ policy
evaluation. The current code does not claim to be a production quantizer, a
validated edge runtime, or a new Transformer architecture.

The concrete research question is:

```text
How unstable are layer/module sensitivity rankings across small calibration
splits, and can a conservative consensus allocation preserve quality better
than single-split or random mixed-precision allocations under the same bit
budget?
```

## Current Scope

Implemented and committed:

- Synthetic no-leak quantization-policy dataset with five deterministic skills:
  `outlier_detect`, `bit_allocate`, `rotation_select`, `residual_patch`, and
  `kv_policy`.
- Python and C++ evaluators for those policy labels.
- Regex-free C++ quantization-policy bypass with a CTest accuracy gate.
- C++ utilities for allocation planning, consensus building, split-stability
  audits, random-seed audits, PPL summary merging, GPU-guard summaries,
  task-eval summaries, and task-accuracy retention comparison.
- A real ESMPQ001 mixed-precision package format layer shared by the C++
  packer/runtime bench and Python reconstruction/generation tools.
- C++ and Python artifact-integrity checks for ESMP package headers,
  per-module manifests, and pack-summary consistency.
- A PC-side Triton packed INT4/INT8 mixed-GEMM prototype plus an executable
  evidence gate for block-tuning results.
- Executable sidecar and fused-QKV generation gates that validate guarded HF
  generation integration, shallow QKV replacement behavior, and Q/K/V cache
  invariants.
- A fused-QKV prompt-suite quality gate that separates conservative text/task
  preservation evidence from acceleration claims.
- A deterministic 84-task chat stress-retention gate that records the remaining
  regression budget instead of hiding output drift.
- A real public-schema task smoke path using streamed GSM8K and MMLU
  abstract-algebra samples, kept as negative capability-retention evidence for
  the current small Qwen3-0.6B baseline.
- An AWQ/GPTQ-style PTQ proxy gate over measured Qwen3-0.6B WikiText2/C4
  sensitivity artifacts, plus a multi-environment baseline audit showing
  `optimum` availability in Windows Python and `triton` availability in WSL
  GPU Python.
- A QuaRot/SpinQuant-style rotation-family proxy gate over measured Qwen3-0.6B
  WikiText2/C4 sensitivity artifacts, kept explicitly separate from faithful
  official rotation implementations.
- A robust-LCB consensus allocation gate across Qwen3-0.6B, Qwen3-1.7B, and
  OLMo2-1B measured WikiText2/C4 allocation artifacts. This upgrades the
  cross-split consensus story from simple averaging toward a lower-confidence
  bound policy while keeping downstream quality claims separate.
- A top-level evidence ledger that aggregates the current paper-facing gates
  into one reproducible pass/fail table.
- A machine-readable baseline coverage manifest and gap dashboard that keep
  missing external PTQ, mobile, and faithful SOTA-comparison evidence
  visible instead of turning it into accidental claims.
- PyTorch fake-quant PPL experiments on small public models and short
  WikiText2/C4 slices.
- A LoRA training entry point with optional completion-only loss masking for
  JSON policy outputs.

Not claimed:

- No real board-level latency or energy evidence yet.
- No packed INT4/INT3 production matmul result yet. The Triton path is a
  prototype kernel benchmark, not a production transformer runtime.
- No official GPTQ/AWQ/SmoothQuant or faithful QuaRot/SpinQuant SOTA comparison yet.
- No proof that spectral/eigen routing survives nonlinear Transformer blocks.
- No committed model weights or LoRA adapter weights.

## Main Evidence

The strongest current result is the cross-dataset consensus diagnostic:
build one allocation from WikiText2 sensitivity, one from C4 sensitivity, then
prioritize overlap and averaged loss-per-cost under the same average-bit
budget.

```text
Qwen3-0.6B, group size 128, average 4.5 bits
WikiText2-64 len96:
  FP16 PPL                         33.9865
  uniform INT4 PPL                 54.6542
  wikitext_c4_consensus PPL        45.6559
  random_seed min/mean/max PPL     48.5030 / 50.4787 / 52.6347
  wins/losses/ties vs random_seed  15 / 0 / 0
  margin vs best random_seed       +2.8471 PPL
C4-64:
  FP16 PPL                         36.1380
  uniform INT4 PPL                 52.9352
  wikitext_c4_consensus PPL        44.9290
  random_seed min/mean/max PPL     48.3840 / 49.4427 / 50.7971
  wins/losses/ties vs random_seed  15 / 0 / 0
  margin vs best random_seed       +3.4551 PPL
```

```text
Qwen3-1.7B, group size 128, average 4.5 bits
WikiText2-64:
  FP16 21.6552  uniform INT4 31.1885  consensus 26.3260
  random16 min/mean/max 27.6685 / 28.2905 / 29.9682
  margin vs best random +1.3425 PPL
C4-64:
  FP16 25.5510  uniform INT4 30.7410  consensus 28.3303
  random16 min/mean/max 28.4562 / 29.4357 / 30.0408
  margin vs best random +0.1259 PPL
```

```text
OLMo2-0425-1B-Instruct, group size 128, average 4.5 bits
WikiText2-64:
  FP16 18.8573  uniform INT4 22.4888  consensus 21.0349
  random16 min/mean/max 21.4637 / 21.6140 / 21.7550
  margin vs best random +0.4288 PPL
C4-64:
  FP16 32.2736  uniform INT4 36.8334  consensus 35.4726
  random16 min/mean/max 35.8512 / 36.0334 / 36.3837
  margin vs best random +0.3785 PPL
```

The split-stability audits show why this should be framed as calibration
robustness, not as a new quantizer:

```text
Qwen3-1.7B: score/cost Spearman 0.0734, positive-set Jaccard 0.4512
OLMo2-1B:   score/cost Spearman 0.1845, positive-set Jaccard 0.4512
```

The multi-model calibration-instability benchmark now aggregates WikiText2-vs-C4
sensitivity movement across Qwen3-0.6B, Qwen3-1.7B, and OLMo2-1B:

```text
Cases:                    3
Unstable cases:           3
Mean score/cost Spearman: 0.0713
Mean positive-set Jaccard: 0.4349
Mean top-20 Jaccard:      0.1022
```

The corresponding report is
`outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md`.

The rotation-family proxy now covers the QuaRot/SpinQuant related-method family
without pretending to be an official implementation:

```text
Qwen3-0.6B measured module sensitivity, rotation budget 35% module cost
WikiText2: 197 records, 82 rotated candidates, cost fraction 0.3484,
           projected sensitivity reduction 0.0848
C4:        197 records, 85 rotated candidates, cost fraction 0.3484,
           projected sensitivity reduction 0.1020
Gate:      2 cases, 394 records, 167 rotated candidates, PASS
```

The corresponding report is
`outputs/QUAROT_SPINQUANT_ROTATION_FAMILY_GATE_2026_06_06.md`.

The AWQ/GPTQ proxy covers the common PTQ family as a measured-sensitivity
baseline proxy, not as an official quantizer run:

```text
Qwen3-0.6B measured module sensitivity, average 4.5 bits
WikiText2: GPTQ proxy protected sensitivity 0.6472,
           AWQ proxy protected sensitivity 0.6452
C4:        GPTQ proxy protected sensitivity 0.5865,
           AWQ proxy protected sensitivity 0.5772
Gate:      2 cases, 394 records, optimum package available, PASS
```

The corresponding report is `outputs/AWQ_GPTQ_PROXY_GATE_2026_06_06.md`.

Current active GPU runs are kept under the requested 90% VRAM guard. Older PPL
experiments stayed below the earlier 85% target; the guarded Ollama public-task
benchmark peaked at 0.8826, still below the current 90% cap.

The latest packed-kernel smoke moves the systems evidence beyond CPU-only
microbenchmarks:

```text
RTX 5070 Laptop GPU, Qwen-like Linear shapes
Shapes:                                  1024x1024, 2048x1024, 3072x1024, 1024x3072
Triton configs completed:                96/96
Configs faster than torch FP16:           10/96
Configs faster than row-wise mixed path:  78/96
Best grouped packed INT4/INT8 speedup:    2.7647x vs torch FP16
Best grouped speedup vs row-wise path:    5.1794x
Compression ratio vs FP16 weights:        3.7034x-3.7441x
Max grouped rel-L2:                       0.1492
Max observed VRAM ratio:                   0.4514
```

The evidence gate is executable and passed on the committed Qwen-shape family
sweep:
`outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md`.
The aggregate table is in
`outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_2026_06_06.md`.
The deploy-planning selector chooses one measured block config per
shape/batch group:
`outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_KERNEL_CONFIG_SELECTOR_2026_06_06.md`.
Selector-driven runtime wiring is smoke-tested in
`outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_2026_06_06.md`.
The corresponding automated gate is
`outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md`.
Selector-driven module-runtime benchmarking is tracked in
`outputs/real_system_packer_2026-06-05/ESMP_LINEAR_SELECTOR_BENCHMARK_2026_06_06.md`.
Selected-row routing/bypass evidence is gated in
`outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md`;
the focused current-environment q_proj smoke is in
`outputs/real_system_packer_2026-06-05/SELECTED_ROW_QPROJ64_FOCUS_2026_06_06.md`.
The decode-loop integration path is now gated separately:
`outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md`
checks that fused selected-row sidecars execute on real HF generation
activations with bounded additive overhead. The stronger replacement smoke is
gated in
`outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md`;
it verifies shallow fused packed QKV replacement inside HF generation, including
Q/K/V cache reuse, TTFT, throughput, compression, and GPU guard compliance.
Quality preservation for a conservative replacement candidate is gated in
`outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md`;
it passes on the layers `[1, 7]` QKV8 repack candidate with 6/6 exact
prompt-suite matches, 0 rule-score regressions, 3.9082x compression, and
43.59% peak guard memory. It is a quality gate, not a speed claim: mean
tokens/s is 0.8957x of the baseline on that suite.
Task-retention stress evidence is gated in
`outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md`.
The current K-only layers `[1, 7]` candidate passes the configured 84-task
stress gate with 45/84 fused passes versus 46/84 baseline passes, one explicit
JSON-key regression, 0.9746x mean speed, and 54.69% peak guard memory.
The first real public-schema smoke is intentionally small and negative:
Qwen3-0.6B scores `0/4` on streamed MMLU abstract-algebra and `0/4` on streamed
GSM8K under the 90% VRAM guard. This proves the public-task path is wired, not
that capability retention is solved.
The top-level evidence ledger is
`outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md`; it
currently passes with 16/16 paper-facing gates across repo hygiene,
calibration robustness, artifact integrity, kernel, runtime wiring,
selected-row, C++ runtime, decode integration, QKV replacement, quality,
task-retention, capability-retention, allocation-comparator,
rotation-comparator, and PTQ-comparator categories.
Gate policy and claim boundaries are in `docs/SYSTEM_EVIDENCE_GATES.md`.
Related-work positioning is tracked in `docs/RELATED_WORK_QUANTIZATION_2026.md`.
Baseline and readiness gaps are tracked by
`docs/BASELINE_COVERAGE_MANIFEST.json` and
`outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md`.

End-to-end smoke metrics are tracked separately from kernel evidence:

```text
Qwen3-0.6B, 16 generated tokens, same-loader warm baseline
same-loader warm baseline:  TTFT 0.0347 s, 25.0523 tok/s, 1173.2993 MiB
cached ESMP 3-module warm:  TTFT 0.0320 s, 28.8295 tok/s, 1175.2993 MiB
Triton ESMP 3-module cold:  TTFT 1.9611 s,  4.9957 tok/s, 1169.8462 MiB
fused QKV 3-layer warm:     TTFT 0.0315 s, 25.8158 tok/s, 1156.4868 MiB
fused QKV 1-layer 64tok:    TTFT 0.0330 s, 30.2441 tok/s, 1173.6138 MiB
```

The concise system table is in
`outputs/real_system_packer_2026-06-05/END_TO_END_SYSTEM_METRICS_2026_06_06.md`.
Interpretation: cached/fused smoke wiring is viable, while the Triton-swapped
end-to-end path still needs fusion and scheduling work before it can be claimed
as runtime acceleration. The fused QKV replacement gate supports only a shallow
1-layer smoke claim: it passes with 1.1300x tokens/s versus the same-loader
64-token baseline, 0.6839x TTFT ratio, 6.1682x compression versus FP32, and
192/64/128/64 wrapper/fused/cache-hit/cache-miss calls. The generated text is
not an exact match in the 64-token run, so quality preservation remains open.

## Negative Evidence Kept On Purpose

The older 8-skill routing run used
`HuggingFaceTB/SmolLM2-360M-Instruct` and reported:

```text
train samples:        7200
eval samples:         1440
pure model exact:     1391/1440 = 96.60%
hybrid runtime exact: 1439/1440 = 99.93%
```

That result is not a generalization claim. The audit found severe overlap:

```text
train/eval exact-row overlap:   1339/1440 = 92.99%
train/eval input overlap:       1339/1440 = 92.99%
train/eval output overlap:      1440/1440 = 100.00%
```

It remains only as an engineering PoC for deterministic bypass mechanics. It
should not be used as paper-facing model-ability evidence.

The first no-leak quant-policy LoRA smoke also failed as a generative policy
learner (`decision_exact = 0.0` on the small smoke eval). That is treated as a
training-objective bug and a baseline failure, not as proof of the method. The
new `--completion-only-loss` path is the next executable fix.

## Repository Layout

```text
train_python/                  data generation, LoRA training, fake-quant eval
inference_cpp/                 standalone C++ evaluators and report utilities
inference_cpp/include/         reusable quant-kernel API headers
data_eval/eigenskill_quant_v1/ no-leak quant-policy train/eval/test split
data_eval/eval_configs/        fake-quant allocation/evaluation configs
outputs/                       selected reports, summaries, and figures
docs/                          scope, claim matrix, and paper-readiness notes
```

Large model files are intentionally ignored. See `MODEL_ARTIFACTS.md`.
Generated delivery bundles and old private-workbench exports are intentionally
excluded from the public tree; see `docs/HISTORICAL_ARTIFACTS.md`.

## Reproduce: Policy Data And Python Bypass

```bash
python train_python/generate_quant_skill_data.py \
  --out data_eval/eigenskill_quant_v1 \
  --train-per-skill 240 \
  --eval-per-skill 80 \
  --test-per-skill 80 \
  --seed 20260603

python train_python/hybrid_eval_quant_policy.py \
  --data data_eval/eigenskill_quant_v1/eval.jsonl \
  --out outputs/eigenskill_quant_v1_eval_hybrid_policy_summary.json

python train_python/hybrid_eval_quant_policy.py \
  --data data_eval/eigenskill_quant_v1/test.jsonl \
  --out outputs/eigenskill_quant_v1_test_hybrid_policy_summary.json
```

Expected result for the deterministic policy path is 100% decision exact on
the generated eval/test split.

## Reproduce: C++ Policy Bypass

WSL/Linux CMake:

```bash
cmake -S inference_cpp -B build/cpp-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build build/cpp-wsl -j2
ctest --test-dir build/cpp-wsl --output-on-failure

./build/cpp-wsl/quant_policy_bypass \
  --data data_eval/eigenskill_quant_v1/eval.jsonl \
  --min-decision-exact 1.0 \
  --out outputs/eigenskill_quant_v1_eval_cpp_policy_summary.json
```

Windows/MSVC:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-policy

.\inference_cpp\build\quant_policy_bypass.exe `
  --data data_eval\eigenskill_quant_v1\eval.jsonl `
  --min-decision-exact 1.0 `
  --out outputs\eigenskill_quant_v1_eval_cpp_policy_summary.json
```

## Reproduce: Completion-Only LoRA Smoke

This path addresses the earlier 0.0 `decision_exact` failure by training only
on JSON response tokens instead of spending loss on the prompt.

```bash
python train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_quant_v1/train.jsonl \
  --eval-data data_eval/eigenskill_quant_v1/eval.jsonl \
  --out models/eigenskill-quant-v1-smollm2-360m-lora-completion-only \
  --epochs 1 \
  --batch-size 2 \
  --grad-accum 8 \
  --completion-only-loss
```

## C++ Microbenchmarks

```bash
./build/cpp-wsl/quant_kernel_verify --dim 512 --active-rows 32
./build/cpp-wsl/quant_kernel_bench --dims 512,1024,2048 --active-rows 16,64,256 --iters 200
```

The current CPU low-bit dequant path is not faster than AVX2 FP32 dense GEMV.
The useful systems signal is selected-row execution and C++ policy gating, not
a production low-bit dot-product kernel.

## Reproduce: ESMP Packed Runtime Slice

The ESMP path is the concrete system artifact boundary:

```text
FP32 Linear weight + row bit policy
  -> mixed_precision_packer
  -> ESMPQ001 binary package + JSON manifest
  -> mixed_precision_runtime_bench / Python reconstruction / generation swap checks
```

Smoke example:

```bash
./build/cpp-wsl/mixed_precision_packer \
  --synthetic \
  --rows 64 \
  --cols 96 \
  --default-bits 4 \
  --sensitive-every 8 \
  --sensitive-bits 8 \
  --out build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --manifest-out build/cpp-wsl/mixed_precision_packer_smoke.json \
  --verify

./build/cpp-wsl/mixed_precision_runtime_bench \
  --input build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --iters 5 \
  --warmup 1 \
  --active-rows 8

./build/cpp-wsl/esmp_inspect \
  --input build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --expect-rows 64 \
  --expect-cols 96 \
  --max-avg-bits 4.6 \
  --min-compression-vs-fp32 4.0 \
  --require-bits 4,8 \
  --verify-row-sums
```

The runtime bench reports package compression, full mixed GEMV latency,
selected-row latency, and `selected_speedup_vs_full_mixed_gemv`. This is still
module-level evidence, not end-to-end TTFT/tokens-per-second proof.

Format details are in `docs/ESMPQ001_FORMAT.md`.
Paper-facing claim boundaries are in `docs/PAPER_CLAIM_MATRIX.md`.

For real packed model slices, verify that `pack_summary.json`, per-module
manifest JSON, and ESMP binary headers agree:

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

Latest local smoke report:
`outputs/real_system_packer_2026-06-05/REAL_SYSTEM_SMOKE_2026_06_06.md`.

Selected-row evidence gate:

```bash
python train_python/gate_selected_row_benchmark.py \
  --benchmark-json outputs/real_system_packer_2026-06-05/esmp_selected_rows.json \
  --guard-json outputs/real_system_packer_2026-06-05/esmp_selected_rows_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md \
  --min-ok-rows 100 \
  --max-failed-rows 0 \
  --min-packed-cases 27 \
  --min-packed-wins-vs-full 4 \
  --min-best-packed-speedup-vs-full 2.0 \
  --max-rel-l2 0.25 \
  --min-cached-median-speedup-vs-full 1.1 \
  --min-dense-selected-wins-vs-full 17 \
  --max-memory-ratio 0.90
```

C++ runtime sweep gate:

```bash
python train_python/gate_cpp_runtime_sweep.py \
  --input-jsonl outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE_2026_06_06.md \
  --min-ok-rows 42 \
  --max-failed-rows 0 \
  --min-wins-vs-full 42 \
  --min-min-speedup-vs-full 10.0 \
  --min-median-speedup-vs-full 15.0 \
  --min-best-speedup-vs-full 45.0 \
  --max-median-selected-ms 0.25 \
  --min-median-compression-vs-fp32 7.0
```

## Reproduce: Triton Mixed-GEMM Prototype

This path benchmarks real packed INT4/INT8 storage on a CUDA GPU. It is still a
kernel-level experiment, not TTFT/tokens-per-second evidence.

```bash
for shape in 1024x1024 2048x1024 3072x1024 1024x3072; do
  rows=${shape%x*}
  cols=${shape#*x}
  python train_python/tune_triton_blocks.py \
    --out-dir outputs/real_system_packer_2026-06-05/gpu_tuning_shape_${shape}_2026_06_06 \
    --max-memory-ratio 0.90 \
    --iters 30 \
    --warmup 8 \
    --rows "$rows" \
    --cols "$cols" \
    --batches 8,16 \
    --high-every 16 \
    --block-ms 16,32 \
    --block-ns 8,16,32 \
    --block-ks 64,128
done

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

## Reproduce: Selector-Driven ESMP Generation Smoke

The grouped Triton ESMP runtime can consume the measured selector output and
choose a block config at each swapped Linear forward based on module shape and
runtime batch size. The generated JSON records the selected config history for
auditability.

```bash
python train_python/measure_esmp_generation_latency.py \
  --model Qwen/Qwen3-0.6B \
  --local-files-only \
  --runtime triton_grouped \
  --kernel-config-selector outputs/real_system_packer_2026-06-05/triton_qwen_shape_kernel_config_selector_2026_06_06.json \
  --module-filter self_attn.q_proj \
  --layers 0,1,2 \
  --max-modules 3 \
  --max-new-tokens 16 \
  --warmup-runs 1 \
  --out outputs/real_system_packer_2026-06-05/qwen3_esmp_selector_triton_3mod_16tok.json

python train_python/gate_selector_runtime_smoke.py \
  --generation-json outputs/real_system_packer_2026-06-05/qwen3_esmp_selector_triton_1mod_4tok.json \
  --guard-json outputs/real_system_packer_2026-06-05/selector_runtime_smoke_guard_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md \
  --min-kernel-configs 8 \
  --min-replaced-modules 1 \
  --min-selector-calls 2 \
  --min-compression-vs-fp32 7.0 \
  --min-generated-tokens 4 \
  --max-memory-ratio 0.90

python train_python/benchmark_esmp_linear_runtimes.py \
  --model Qwen/Qwen3-0.6B \
  --local-files-only \
  --module-filter self_attn.q_proj \
  --layers 0 \
  --max-modules 1 \
  --batches 1,12 \
  --warmup 2 \
  --iters 8 \
  --kernel-config-selector outputs/real_system_packer_2026-06-05/triton_qwen_shape_kernel_config_selector_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/esmp_linear_selector_benchmark_2026_06_06.json \
  --out-jsonl outputs/real_system_packer_2026-06-05/esmp_linear_selector_benchmark_2026_06_06.jsonl \
  --out-csv outputs/real_system_packer_2026-06-05/esmp_linear_selector_benchmark_2026_06_06.csv \
  --out-md outputs/real_system_packer_2026-06-05/ESMP_LINEAR_SELECTOR_BENCHMARK_2026_06_06.md
```

## Reproduce: Fused Generation Gates

The sidecar gate proves that fused selected-row kernels can run on live
generation activations without replacing dense QKV. The QKV replacement gate is
stronger: it verifies that selected Q/K/V projections are replaced by the fused
ESMP runtime and that QKV cache reuse occurred. The prompt-suite gate is a
separate quality-preservation check for a conservative replacement candidate.
The chat-task gate is a deterministic task-retention stress check.

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

python train_python/build_evidence_ledger.py \
  --gate public_hygiene=outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --gate calibration_instability=outputs/calibration_instability_benchmark_2026_06_06.json \
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
  --gate rotation_family_proxy=outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json \
  --gate awq_gptq_proxy=outputs/awq_gptq_proxy_gate_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

## Reproduce: End-to-End Metric Summary

This command summarizes already measured generation JSON artifacts and computes
ratios against the same-loader warm baseline.

```bash
python train_python/summarize_system_metrics.py \
  --baseline same_loader_warm_16tok \
  --case direct_fp16_cold_16tok=outputs/real_system_packer_2026-06-05/qwen3_fp16_16tok_latency.json \
  --case same_loader_cold_16tok=outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_latency.json \
  --case same_loader_warm_16tok=outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_warm_latency.json \
  --case cached_3mod_cold_16tok=outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_latency.json \
  --case cached_3mod_warm_16tok=outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_warm_latency.json \
  --case triton_3mod_cold_16tok=outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_latency.json \
  --case fused_qkv_3layer_warm_16tok=outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_16tok.json \
  --out-json outputs/real_system_packer_2026-06-05/end_to_end_system_metrics_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/END_TO_END_SYSTEM_METRICS_2026_06_06.md
```

## Paper Direction

The credible submission story is:

```text
Calibration Split Instability in LLM Mixed-Precision Quantization
```

Minimum next experiments before claiming a strong venue:

1. Replace AWQ/GPTQ/rotation proxies with faithful official PTQ baselines where applicable.
2. Add MMLU/GSM8K/IFEval/BBH-style task retention, not only PPL.
3. Repeat calibration splits and report variance, rank correlation, Jaccard,
   and allocation transfer across datasets.
4. Scale beyond 0.6B-1.7B where local hardware permits.
5. Replace fake-quant-only evidence with at least one packed/runtime-backed
   measurement.

## Claim Boundary

Use this repository as a reproducible diagnostic and engineering scaffold. Do
not present it as a finished CCF-A systems paper, a SOTA quantizer, or a proven
edge deployment until the missing baselines, task metrics, runtime kernels, and
larger-model experiments are complete.
