# EigenSkill Research Pack

EigenSkill is the working codename for a small research pack on hybrid skill
routing for resource-constrained LLM inference.

The current repository is not a finished edge inference engine. Its verified
core is narrower:

1. synthetic skill datasets for routing and quantization-policy decisions;
2. deterministic bypass evaluators for low-entropy skills;
3. a small LoRA/adapter training pipeline around
   `HuggingFaceTB/SmolLM2-360M-Instruct`;
4. a C++ low-rank GEMV microbenchmark that measures an isolated best-case
   kernel, not an integrated model runtime.

The practical publication direction is therefore:

```text
semantic skill routing + deterministic quantization-policy bypass
```

Spectral/eigen-routing, physical swarm assembly, acoustic communication, and
real board-level energy claims are retained only as future research notes. They
are not completed results in this repository.

## What This Is

- A reproducible proof-of-concept for routing simple skills away from a small
  LLM when the output can be computed exactly.
- A cleaner quantization-policy track with no train/eval/test overlap in the
  committed v1 split.
- A lightweight place to collect negative evidence: short LoRA runs do not
  reliably learn numeric quantization policies, which motivates deterministic
  policy kernels.
- A C++ microbenchmark for the arithmetic gap between dense GEMV and a
  synthetic low-rank path.

## What This Is Not

- Not a proven `O(d)` Transformer inference method.
- Not a validated spectral/eigen-routing method through nonlinear Transformer
  blocks.
- Not an ARM NEON, RKNN, Ascend, Qualcomm NPU, ExecuTorch, or llama.cpp
  integration.
- Not a board-level latency or energy study.
- Not evidence that SmolLM2-360M 1-epoch LoRA proves a rate-distortion
  quantization method.
- Not a completed cross-medium swarm or acoustic communication system.

See `docs/scope-and-claims.md` for the allowed and disallowed external claims.

## Current Verified Evidence

### Quantization-policy bypass, v1

Committed dataset:

```text
data_eval/eigenskill_quant_v1/
```

Skills:

```text
outlier_detect
bit_allocate
rotation_select
residual_patch
kv_policy
```

Split audit:

```text
train: 1200 rows
eval:   400 rows
test:   400 rows
train/eval exact overlap: 0
train/eval input overlap: 0
train/test exact overlap: 0
train/test input overlap: 0
eval/test exact overlap: 0
eval/test input overlap: 0
```

Deterministic bypass baseline:

```text
eval exact_json:      400/400 = 100%
eval decision_exact:  400/400 = 100%
test exact_json:      400/400 = 100%
test decision_exact:  400/400 = 100%
parse_error:          0.0 on both splits
```

Evidence files:

```text
data_eval/eigenskill_quant_v1/audit.json
outputs/eigenskill_quant_v1_eval_hybrid_policy_summary.json
outputs/eigenskill_quant_v1_test_hybrid_policy_summary.json
docs/obsidian_quant_route/12-quant-v1-data-fix-and-bypass-baseline.md
```

### Pure LoRA negative evidence

A 60-sample generation check for the quantization-policy model did not learn
the numeric policy decisions:

```text
outputs/eigenskill_quant_v1_eval_policy_limit60_summary.json

overall n:              60
json_valid:             35%
schema_ok:              0%
exact_json:             0%
decision_exact:         0%
```

This is not a benchmark against GPTQ/AWQ/SmoothQuant/QuaRot. It is local
negative evidence that short SFT on a tiny model is the wrong place to execute
deterministic numeric policy rules.

### 8-skill hybrid routing, v2

Base model:

```text
HuggingFaceTB/SmolLM2-360M-Instruct
```

Skills:

```text
intent_routing
json_repair
field_extraction
command_normalization
sensor_event_triage
packet_encode
safety_gate
unit_time_normalize
```

Reported v2 eval:

```text
train samples:        7200
eval samples:         1440
pure model exact:     1391/1440 = 96.60%
hybrid runtime exact: 1439/1440 = 99.93%
hybrid overrides:     180 unit_time_normalize rows
```

Important limitation: the v2 split has severe overlap and must be treated only
as an engineering PoC:

```text
train/eval exact-row overlap:        1339/1440 = 92.99%
train/eval input overlap:            1339/1440 = 92.99%
train/eval skill+input overlap:      1339/1440 = 92.99%
train/eval output overlap:           1440/1440 = 100.00%
```

The v2 result is useful for demonstrating the mechanics of a deterministic
`unit_time_normalize` bypass, not for claiming generalization.

Evidence files:

```text
outputs/eigenskill_v2_package_manifest.json
outputs/eigenskill_v2_hybrid_eval_recheck.json
outputs/EigenSkill-v2-Hybrid-Training-Report.md
```

### C++ low-rank microbenchmark

The C++ artifact isolates this synthetic best-case computation:

```text
dense path: y = W x
skill path: z = U^T x; z2 = A z; y = U z2
```

Because `W` is generated as `U A U^T`, this benchmark measures the best-case
arithmetic ceiling, not approximation quality on a trained Transformer layer.

Selected local Windows/MSVC result:

```text
d=1024, k=8:  dense_ms=0.675749, skill_ms=0.007197, speedup=93.89
d=2048, k=8:  dense_ms=2.723404, skill_ms=0.014769, speedup=184.40
d=2048, k=32: dense_ms=2.762792, skill_ms=0.063888, speedup=43.24
```

Evidence file:

```text
outputs/eigenskill_cpp_benchmark.txt
```

## Repository Layout

```text
train_python/                 data generation, LoRA training, eval, bypass scripts
inference_cpp/                C++ low-rank GEMV microbenchmark
data_eval/eigenskill_v2/      older 8-skill PoC split with severe overlap
data_eval/eigenskill_quant_v1/cleaner quantization-policy split
outputs/                      selected summaries, reports, and benchmark outputs
docs/                         scope notes, Obsidian notes, NotebookLM source package
research_pack_2026-06-03/     historical mentor/paper drafts; not current claims
```

Large model artifacts are not committed. See `MODEL_ARTIFACTS.md`.

## Reproduce Without Model Weights

These commands validate the currently strongest public path: quantization-policy
dataset generation and deterministic bypass evaluation.

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

On Windows/PowerShell, the same commands work with `python` if the repo root is
the current directory.

## Reproduce The v2 Engineering PoC

This path requires local model artifacts or retraining. It is included for
engineering reproduction only because the split has high overlap.

```bash
python train_python/generate_skill_data_v2.py \
  --out data_eval/eigenskill_v2 \
  --train-per-skill 900 \
  --eval-per-skill 180

python train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_v2/train.jsonl \
  --eval-data data_eval/eigenskill_v2/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-v2-fp16

python train_python/hybrid_eval_skills.py \
  --model-eval outputs/eigenskill_v2_eval.json \
  --data data_eval/eigenskill_v2/eval.jsonl \
  --out outputs/eigenskill_v2_hybrid_eval_recheck.json

python train_python/verify_v2_package.py
```

## C++ Microbenchmark

Build on Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1
```

Run:

```powershell
.\inference_cpp\build\eigenskill_bench.exe --dims 1024,2048 --ks 4,8,16 --iters 300
```

More detail is in `inference_cpp/README.md`.

## Research Pack Status

`research_pack_2026-06-03/` contains early mentor-facing and paper-facing
drafts. Treat that directory as historical scaffolding. In particular:

- the swarm/acoustic/physical-assembly paper draft is speculative;
- the eigen-regularization draft is not backed by a nonlinear Transformer proof;
- the edge-runtime draft lacks real board-level latency and energy results;
- the current credible direction is quantization-policy bypass plus honest
  routing evaluation.

## Next Work

1. Replace the overlapping v2 skill split with a no-leak split and rerun the
   routing/bypass evaluation.
2. Add public baselines for quantization-policy decisions, including RTN, GPTQ,
   AWQ, SmoothQuant, QuaRot, and SpinQuant-style rotations where applicable.
3. Move the deterministic quantization policy kernels from Python into C++ and
   measure overhead against a real model runtime.
4. Run board-level latency and energy measurements on an ARM board before using
   "edge" as an empirical claim.
5. Keep spectral/eigen-routing as a separate theory track until a toy nonlinear
   proof and trained-layer experiment exist.
