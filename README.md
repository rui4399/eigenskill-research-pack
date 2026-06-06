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
- A PC-side Triton packed INT4/INT8 mixed-GEMM prototype plus an executable
  evidence gate for block-tuning results.
- PyTorch fake-quant PPL experiments on small public models and short
  WikiText2/C4 slices.
- A LoRA training entry point with optional completion-only loss masking for
  JSON policy outputs.

Not claimed:

- No real board-level latency or energy evidence yet.
- No packed INT4/INT3 production matmul result yet. The Triton path is a
  prototype kernel benchmark, not a production transformer runtime.
- No GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant SOTA comparison yet.
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

All listed GPU runs stayed below the requested 85% VRAM guard. Example peaks:
Qwen3-0.6B consensus eval stayed near 60% of an 8 GB GPU; Qwen3-1.7B stayed
near 62%; OLMo2-1B stayed near 54%.

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
Gate policy and claim boundaries are in `docs/SYSTEM_EVIDENCE_GATES.md`.

End-to-end smoke metrics are tracked separately from kernel evidence:

```text
Qwen3-0.6B, 16 generated tokens, same-loader warm baseline
same-loader warm baseline:  TTFT 0.0347 s, 25.0523 tok/s, 1173.2993 MiB
cached ESMP 3-module warm:  TTFT 0.0320 s, 28.8295 tok/s, 1175.2993 MiB
Triton ESMP 3-module cold:  TTFT 1.9611 s,  4.9957 tok/s, 1169.8462 MiB
fused QKV 3-layer warm:     TTFT 0.0315 s, 25.8158 tok/s, 1156.4868 MiB
```

The concise system table is in
`outputs/real_system_packer_2026-06-05/END_TO_END_SYSTEM_METRICS_2026_06_06.md`.
Interpretation: cached/fused smoke wiring is viable, while the Triton-swapped
end-to-end path still needs fusion and scheduling work before it can be claimed
as runtime acceleration.

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
docs/                          scope, claim boundaries, and paper-readiness notes
research_pack_2026-06-03/      historical drafts; not current public claims
```

Large model files are intentionally ignored. See `MODEL_ARTIFACTS.md`.

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
```

The runtime bench reports package compression, full mixed GEMV latency,
selected-row latency, and `selected_speedup_vs_full_mixed_gemv`. This is still
module-level evidence, not end-to-end TTFT/tokens-per-second proof.

Format details are in `docs/ESMPQ001_FORMAT.md`.

Latest local smoke report:
`outputs/real_system_packer_2026-06-05/REAL_SYSTEM_SMOKE_2026_06_06.md`.

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

1. Add GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant-style baselines where applicable.
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
