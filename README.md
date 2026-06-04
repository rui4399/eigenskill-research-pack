# EigenSkill Research Pack

EigenSkill is the working codename for a small research pack on hybrid skill
routing for resource-constrained LLM inference.

The current repository is not a finished edge inference engine. Its verified
core is narrower:

1. synthetic skill datasets for routing and quantization-policy decisions;
2. deterministic bypass evaluators for low-entropy skills, including a C++
   quantization-policy evaluator;
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
outputs/eigenskill_quant_v1_eval_cpp_policy_summary.json
outputs/eigenskill_quant_v1_test_cpp_policy_summary.json
docs/obsidian_quant_route/12-quant-v1-data-fix-and-bypass-baseline.md
```

C++ policy bypass check, Windows/MSVC:

```text
eval n:                 400
eval policy_fields:     400/400 = 100%
eval decision_exact:    400/400 = 100%
eval parse_error:       0/400 = 0%
eval throughput:        8261 rows/s

test n:                 400
test policy_fields:     400/400 = 100%
test decision_exact:    400/400 = 100%
test parse_error:       0/400 = 0%
test throughput:        6924 rows/s
```

The C++ metric `policy_fields_exact` checks the decision-bearing fields for
each skill. The stricter full-response `exact_json`, including auxiliary
fields such as `risk` and `score`, is covered by the Python baseline above.

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

### Sensitivity-rate-distortion allocation scaffold

The next experiment scaffold is a dependency-free allocator that compares
uniform, random budgeted, greedy, and rate-distortion bit allocation over
synthetic layer/group statistics:

```powershell
python train_python\rate_distortion_allocator.py `
  --budget-avg-bits 3.2 `
  --out-json outputs\rate_distortion_allocation_summary.json `
  --out-md outputs\rate_distortion_allocation_report.md
```

It is not a real model-quantization result. It validates the allocation API and
reporting format before replacing synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.

Evidence files:

```text
train_python/rate_distortion_allocator.py
outputs/rate_distortion_sweep_report.md
outputs/rate_distortion_allocation*_summary.json
outputs/rate_distortion_allocation*_report.md
```

### Real-model calibration bridge

The allocation scaffold has also been connected to cached
`HuggingFaceTB/SmolLM2-360M-Instruct` activation statistics. This is still not a
quantized-model quality benchmark, but it verifies the chain:

```text
small LLM -> Linear-module activation stats -> allocator GroupStat records
          -> mixed-precision bit allocation
```

Local WSL evidence:

```text
GPU: NVIDIA GeForce RTX 5070 Laptop GPU
torch: 2.12.0+cu130
CUDA available: true
calibrated Linear modules: 225
```

Evidence files:

```text
train_python/collect_calibration_stats.py
outputs/calibration_stats_smollm2_360m_limit4.json
outputs/smollm2_calibration_allocation_report.md
outputs/smollm2_calib_limit4_rd_alloc*.json
outputs/smollm2_calib_limit4_rd_alloc*.md
```

First fake-quant quality signal, per-row scale:

```text
method                 PPL       delta NLL vs FP16
FP16                   179.14    0.0000
uniform INT4           2196.14   2.5063
uniform INT3           9460848   10.8745
RD allocation {4,8}    1931.25   2.3778
```

This uses naive per-output-channel symmetric fake quantization and short prompts.
It is not a production quantizer or a memory/latency claim. It does show that a
conservative `{4,8}` rate-distortion allocation can improve the short-prompt PPL
signal over uniform INT4 in this scaffold.

After adding group-wise scales, uniform INT4 becomes much stronger:

```text
group size 128:
FP16                   PPL 179.14
uniform INT4           PPL 272.18
uniform INT3           PPL 9212.20
RD allocation {4,8}    PPL 292.01

group size 64:
uniform INT4           PPL 281.15
RD allocation {4,8}    PPL 296.80
```

This is useful negative evidence: the current activation-stat sensitivity proxy
is not yet aligned with actual PPL sensitivity. The next allocator should use
measured loss increase, activation reconstruction error, or Hessian/Fisher
proxies.

Measured per-module loss sensitivity closes that gap on the same fake-quant
scaffold. The probe quantizes one Linear module at a time with group-wise INT4,
measures the short-prompt loss increase, restores the original weight, and then
assigns 8-bit precision to the highest loss-per-cost modules under a 4.5
average-bit budget:

```text
sensitivity probe:
Linear modules          225
probe prompts           4
group size              128
allocation bits         4:172, 8:53
weighted avg bits       4.4993
positive loss protected 57.83%

8-prompt group-wise PPL:
FP16                         179.14
uniform INT4                 272.18
activation-stat RD {4,8}     292.01
loss-sensitive {4,8}         212.69

WikiText2 validation slice, 32 prompts:
FP16                          18.24
uniform INT4                  30.26
uniform INT3                1678.70
activation-stat RD {4,8}      26.13
loss-sensitive {4,8}          25.92

WikiText2 validation slice, 128 prompts:
FP16                          17.34
uniform INT4                  27.82
uniform INT3                1154.44
activation-stat RD {4,8}      24.51
loss-sensitive {4,8}          24.14
loss-sensitive exact knapsack 24.36
loss-sensitive swap-search    24.07
```

This is the first positive real-model signal for the quantization track: the
activation-stat proxy was weaker than uniform INT4, while measured per-module
loss sensitivity substantially improves over both uniform INT4 and the earlier
RD allocation. The WikiText2 slice shows the same direction on a public text
dataset; there, the margin over the old activation-stat RD allocation is small
but still positive on both the 32-prompt and 128-prompt slices. An exact
0/1-knapsack optimizer over the measured one-module sensitivity objective
protects slightly more local loss than the greedy allocator, but gives slightly
worse 128-prompt PPL (`24.36` vs `24.14`). This is useful evidence that module
interactions matter and that a serious paper should compare greedy, exact
knapsack, Fisher/Hessian proxies, and learned policy/RL allocation. It is still
fake quantization and does not prove compressed runtime memory, latency, or
board-level energy savings.

A bounded one-step interaction-aware policy-improvement search then evaluates
candidate module swaps with global WikiText2-128 PPL feedback. The best tested
swap demotes `model.layers.17.self_attn.v_proj` from 8-bit to 4-bit and promotes
`model.layers.24.self_attn.v_proj` from 4-bit to 8-bit:

```text
base loss-sensitive PPL: 24.1374
best swap-search PPL:   24.0661
evaluated swaps:        8
```

The gain is modest, but it is the cleanest current evidence that interaction
terms can be optimized beyond the additive one-module sensitivity objective.

The same allocation set was then evaluated on a streamed C4 English validation
slice with 64 prompts:

```text
C4 validation slice, 64 prompts:
FP16                              23.78
uniform INT4                      36.94
uniform INT3                    2990.80
activation-stat RD {4,8}          33.69
loss-sensitive {4,8}              32.77
loss-sensitive exact knapsack     32.87
loss-sensitive swap-search        32.57
```

This reproduces the WikiText2 ordering on a second public-text source.

An additional output-reconstruction sensitivity proxy was tested. It samples
Linear-module inputs and ranks modules by normalized output perturbation
`E||x(W-Q(W))^T||^2 / E||xW^T||^2`. It is cheaper than full one-module PPL
probing, but it underperforms the measured loss proxy:

```text
output-sensitive {4,8} allocation:
bit histogram: 4-bit=135, 8-bit=90
protected output proxy: 54.50%

WikiText2-128 PPL: 25.21
C4-64 PPL:         33.71
```

This is useful negative evidence: local output reconstruction error is not
automatically aligned with global next-token loss.

Evidence files:

```text
train_python/eval_weight_quant_ppl.py
train_python/measure_module_quant_sensitivity.py
train_python/build_dataset_prompts.py
train_python/build_loss_sensitive_knapsack_alloc.py
train_python/search_allocation_swaps.py
data_eval/eval_configs/smollm2_group128_compare_allocations.json
data_eval/text_prompts/wikitext2_validation_32.txt
data_eval/text_prompts/wikitext2_validation_128.txt
outputs/smollm2_fake_quant_ppl_report.md
outputs/smollm2_fake_quant_ppl_4to8_limit8_summary.json
outputs/smollm2_fake_quant_ppl_4to8_group128_limit8_summary.json
outputs/smollm2_fake_quant_ppl_4to8_group64_limit8_summary.json
outputs/smollm2_module_loss_sensitivity_limit4_group128.json
outputs/smollm2_module_loss_sensitivity_limit4_group128_report.md
outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_limit8_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_activation_rd_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_group128_wikitext2_128_summary.json
outputs/smollm2_loss_sensitive_exact_knapsack_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_loss_sensitive_exact_knapsack_alloc_4to8_limit4_group128_report.md
outputs/smollm2_fake_quant_ppl_compare_allocations_exact_group128_wikitext2_128_summary.json
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_summary.json
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_report.md
outputs/smollm2_loss_sensitive_swap_search_alloc_4to8_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_wikitext2_128_summary.json
data_eval/text_prompts/c4_en_validation_64.txt
outputs/smollm2_fake_quant_ppl_c4_validation_64_report.md
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
train_python/measure_module_output_sensitivity.py
outputs/smollm2_output_sensitivity_proxy_report.md
outputs/smollm2_module_output_sensitivity_limit4_group128.json
outputs/smollm2_output_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_c4_en_validation_64_summary.json
```

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
inference_cpp/src/quant_policy_bypass.cpp
                              C++ deterministic quantization-policy evaluator
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

## Reproduce The C++ Quantization-Policy Bypass

Build and run the standalone C++ evaluator on Windows/MSVC:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-policy

.\inference_cpp\build\quant_policy_bypass.exe `
  --data data_eval\eigenskill_quant_v1\eval.jsonl `
  --out outputs\eigenskill_quant_v1_eval_cpp_policy_summary.json

.\inference_cpp\build\quant_policy_bypass.exe `
  --data data_eval\eigenskill_quant_v1\test.jsonl `
  --out outputs\eigenskill_quant_v1_test_cpp_policy_summary.json
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

The current paper-facing draft is:

```text
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.md
```

It reframes the project around loss-sensitive constrained mixed-precision
allocation, deterministic policy kernels, interaction-aware policy improvement,
and a contextual-bandit/RL extension.

## Next Work

1. Expand the loss-sensitive allocation benchmark to WikiText2/C4 slices,
   repeated calibration sets, and larger prompt counts.
2. Add public baselines for quantization decisions, including RTN, GPTQ,
   AWQ, SmoothQuant, QuaRot, and SpinQuant-style rotations where applicable.
3. Compare measured loss sensitivity against Fisher/Hessian proxies and
   activation reconstruction error after fake quantization.
4. Expand interaction-aware allocation beyond one-step swaps into pairwise
   features, learned reward models, and constrained bandit/RL policies.
5. Move the deterministic quantization policy kernels from Python into C++ and
   measure overhead against a real model runtime.
6. Replace the overlapping v2 skill split with a no-leak split and rerun the
   routing/bypass evaluation.
7. Run board-level latency and energy measurements on an ARM board before using
   "edge" as an empirical claim.
8. Keep spectral/eigen-routing as a separate theory track until a toy nonlinear
   proof and trained-layer experiment exist.
