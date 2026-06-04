# EigenSkill Research Pack

EigenSkill is the working codename for a small research pack on hybrid skill
routing for resource-constrained LLM inference.

The current repository is not a finished edge inference engine. Its verified
core is narrower:

1. synthetic skill datasets for routing and quantization-policy decisions;
2. deterministic bypass evaluators for low-entropy skills, including a C++
   quantization-policy evaluator;
3. fake-quant PPL baselines on `HuggingFaceTB/SmolLM2-360M-Instruct`,
   `Qwen/Qwen2.5-0.5B-Instruct`, `Qwen/Qwen2.5-1.5B-Instruct`,
   `Qwen/Qwen3-0.6B`, `Qwen/Qwen3-1.7B`, and
   `allenai/OLMo-2-0425-1B-Instruct` short slices;
4. standalone C++ artifacts for low-rank GEMV, quantization-policy bypass,
   quant-kernel microbenchmarks, a reusable quant-kernel API, C++ allocation
   planning, C++ evidence summarization, and C++ consensus-allocation audit.

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
- C++ microbenchmarks for the arithmetic gap between dense GEMV, selected-row
  GEMV, synthetic low-rank paths, packed INT4 dequantization, and scalar
  bypass.
- C++ allocation/reporting utilities that consume measured sensitivity and PPL
  JSON to produce budgeted mixed-precision allocations, random-repeat
  baselines, and cross-dataset evidence matrices.

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

### Cross-dataset consensus fake-quant diagnostic

The strongest current quantization-track result is no longer a single-split
allocation. Two model families now have a WikiText2+C4 calibration-consensus
allocation evaluated against uniform INT4, structural category baselines, and
budget-matched random repeats on 64-prompt WikiText2/C4 slices.

This is still a short-slice PyTorch fake-quant diagnostic, not a packed
runtime, hardware result, or SOTA quantizer comparison.

```text
Qwen3-1.7B, group size 128, average 4.5 bits:
WikiText2-64  FP16 21.6552  uniform INT4 31.1885  consensus 26.3260
              random min/mean/max 27.6685 / 27.9124 / 28.1563
              consensus margin vs best random +1.3425 PPL
C4-64         FP16 25.5510  uniform INT4 30.7410  consensus 28.3303
              random min/mean/max 28.4562 / 28.7118 / 28.9674
              consensus margin vs best random +0.1259 PPL

OLMo2-0425-1B-Instruct, group size 128, average 4.5 bits:
WikiText2-64  FP16 18.8573  uniform INT4 22.4888  consensus 21.0349
              random min/mean/max 21.4637 / 21.6140 / 21.7550
              consensus margin vs best random +0.4288 PPL
C4-64         FP16 32.2736  uniform INT4 36.8334  consensus 35.4726
              random min/mean/max 35.8512 / 36.0334 / 36.3837
              consensus margin vs best random +0.3785 PPL
```

The consensus path is intentionally conservative: build one allocation from a
WikiText2 sensitivity split, one from a C4 sensitivity split, then prioritize
overlap and average loss-per-cost under the same bit budget. It addresses the
earlier Qwen3 failure mode where a one-split loss-sensitive allocation beat
random on WikiText2 but lost to the best random seed on C4.

Evidence files:

```text
data_eval/eval_configs/qwen3_1p7b_wikitext_c4_consensus_compare.json
outputs/qwen3_1p7b_wikitext_c4_consensus_evidence_matrix.md
outputs/qwen3_1p7b_wikitext_c4_consensus_audit.md
data_eval/eval_configs/olmo2_0425_1b_wikitext_c4_consensus_compare.json
outputs/olmo2_0425_1b_wikitext_c4_consensus_evidence_matrix.md
outputs/olmo2_0425_1b_wikitext_c4_consensus_audit.md
inference_cpp/src/quant_evidence_matrix.cpp
inference_cpp/src/quant_consensus_audit.cpp
```

### Quantization-policy bypass, v1

Committed dataset:

```text
data_eval/eigenskill_quant_v1/
```

Quantization-policy skills:

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

The fake-quant scaffold was also run on `Qwen/Qwen2.5-0.5B-Instruct`. First,
a uniform-only configuration verifies that the evaluator is not limited to
SmolLM2. Then Qwen-specific measured loss-sensitivity probes produce {4,8}-bit
allocations. The 2-prompt probe was the first smoke result; the 8-prompt probe
is the stronger current Qwen signal.

```text
Qwen2.5-0.5B-Instruct, group size 128:

WikiText2 validation slice, 128 prompts:
FP16                         PPL 17.43
uniform INT4                 PPL 27.74
uniform INT3                 PPL 514.09
loss-sensitive {4,8}, 2p     PPL 22.46
loss-sensitive {4,8}, 8p     PPL 21.98
consensus {4,8}, 2p+8p       PPL 22.08

C4 English validation slice, 64 prompts:
FP16                         PPL 23.95
uniform INT4                 PPL 36.51
uniform INT3                 PPL 779.27
loss-sensitive {4,8}, 2p     PPL 31.22
loss-sensitive {4,8}, 8p     PPL 30.80
consensus {4,8}, 2p+8p       PPL 30.80

Qwen loss-sensitive allocation, 2-prompt probe:
Linear modules           169
probe prompts            2
bit histogram            4-bit=114, 8-bit=55
weighted avg bits        4.4951
positive loss protected  63.36%

Qwen loss-sensitive allocation, 8-prompt probe:
Linear modules           169
probe prompts            8
bit histogram            4-bit=112, 8-bit=57
weighted avg bits        4.4969
positive loss protected  59.01%

2p vs 8p allocation stability:
8-bit module overlap     38 modules
8-bit set Jaccard        0.5135
changed bit decisions    36 / 169
8p PPL gain vs 2p        -0.48 on WikiText2-128, -0.42 on C4-64

Consensus allocation, 2p+8p:
Linear modules           169
bit histogram            4-bit=109, 8-bit=60
weighted avg bits        4.4997
2p overlap               49 / 55 high-bit modules
8p overlap               49 / 57 high-bit modules
Jaccard vs 2p / 8p       0.7424 / 0.7206
```

The moderate 2p/8p Jaccard is important: the allocation is useful but still
calibration-sensitive. The consensus allocation is a more stable paper-facing
point: it gives up only `+0.11` PPL versus the 8-prompt allocation on
WikiText2-128 and is nearly tied on C4-64, while substantially increasing
overlap with both calibration probes. Any paper-facing version should report
calibration stability, not only the best PPL.

The stronger-model smoke baseline now also includes a locally downloaded
`Qwen/Qwen2.5-1.5B-Instruct` checkpoint. This is a small 64-prompt WikiText2
and 64-prompt C4 slice, not a full benchmark:

```text
Qwen2.5-1.5B-Instruct, group size 128:

WikiText2 validation slice, 64 prompts:
FP16                         PPL 12.85
uniform INT4                 PPL 17.24
uniform INT3                 PPL 273.95
loss-sensitive {4,8}, 2p     PPL 16.18
loss-sensitive {4,8}, 8p     PPL 15.75
loss-sensitive consensus     PPL 15.80

C4 English validation slice, 64 prompts:
FP16                         PPL 18.17
uniform INT4                 PPL 23.99
uniform INT3                 PPL 293.82
loss-sensitive {4,8}, 2p     PPL 23.27
loss-sensitive {4,8}, 8p     PPL 22.36
loss-sensitive consensus     PPL 22.49

Local model path             C:\Users\18042\models\Qwen2.5-1.5B-Instruct
model.safetensors bytes      3,087,467,144
model.safetensors sha256     DD924A11B4C220F385B51FFA522DAEA7C9F3D850E31B162BB5661DF483C6D3EE
Linear modules touched       197
2p bit histogram             4-bit=137, 8-bit=60, avg bits=4.4993
8p bit histogram             4-bit=136, 8-bit=61, avg bits=4.4953
consensus bit histogram      4-bit=132, 8-bit=65, avg bits=4.4993
2p/8p 8-bit Jaccard          0.6351

WikiText2 validation slice, 128 prompts:
FP16                         PPL 13.13
uniform INT4                 PPL 17.50
loss-sensitive {4,8}, 2p     PPL 16.65
loss-sensitive {4,8}, 8p     PPL 16.08
loss-sensitive consensus     PPL 16.14
```

This result only validates that the fake-quant evaluator runs on a stronger
1.5B model and that measured loss-sensitive allocation improves over uniform
INT4 on the short PPL slice. It is not a packed INT4 runtime, latency, memory,
or energy claim.

The compact sensitivity summary separates absolute loss increase from
cost-normalized loss increase. Under the 4.5 average-bit budget, the allocation
protects 60.20% of measured positive loss increase with 60 upgraded modules,
but ranks modules by loss increase per parameter-cost. This is why small
attention `k_proj`/`v_proj` matrices dominate the selected 8-bit set, while the
large `lm_head` has the largest absolute loss increase but is not selected by
the cost-normalized objective.

The 8-prompt calibration is a stronger signal than the first 2-prompt probe.
It improves WikiText2-64 from `16.18` to `15.75`, improves C4-64 from `23.27`
to `22.36`, and changes 27 of 197 bit decisions relative to the 2-prompt
allocation. The consensus allocation prioritizes modules selected by both
probes, then fills the remaining budget by average loss-per-cost score. In this
slice it is slightly behind the direct 8-prompt allocation but remains
substantially better than uniform INT4 on both WikiText2-64 and C4-64.
The same ordering holds on a longer WikiText2-128 slice. The 128-prompt run
temporarily reached about 7.3 GiB of 8.15 GiB GPU memory, so larger 1.5B
evaluations should be staged carefully or run with smaller config batches.

The evaluator now uses in-place group-wise fake quantization to avoid full
matrix-sized temporary dequant tensors. A guarded 1.5B baseline comparison
stayed under the requested GPU limit: peak `4634/8151 MiB` (`56.85%`) and max
GPU utilization `62%` according to `train_python/run_with_gpu_guard.py`. On a
16-prompt and 64-prompt WikiText2 sanity slices, loss-sensitive allocation also
beats budgeted random and budgeted structural heuristics:

```text
Qwen2.5-1.5B-Instruct, WikiText2 16 prompts, group size 128:

FP16                         PPL 10.76
uniform INT4                 PPL 15.04
loss-sensitive {4,8}         PPL 13.14  avg bits 4.4953
random budget-matched {4,8}  PPL 14.19  avg bits 4.4952
category heuristic budget    PPL 14.44  avg bits 4.4709

C++ planner output, Qwen2.5-1.5B-Instruct, WikiText2 16 prompts:

FP16                         PPL 10.76
uniform INT4                 PPL 15.04
C++ loss-sensitive {4,8}     PPL 13.14  avg bits 4.4953
C++ random budget {4,8}      PPL 13.75  avg bits 4.4993
C++ category budget {4,8}    PPL 14.28  avg bits 4.4749

Qwen2.5-1.5B-Instruct, WikiText2 64 prompts, group size 128:

FP16                         PPL 12.29
uniform INT4                 PPL 16.41
loss-sensitive {4,8}         PPL 14.99  avg bits 4.4953
random budget-matched {4,8}  PPL 15.70  avg bits 4.4952
category heuristic budget    PPL 15.72  avg bits 4.4709

Qwen3-0.6B, WikiText2 16 prompts, group size 128:

FP16                         PPL 27.82
uniform INT4                 PPL 44.57
uniform INT3                 PPL 1079.79
C++ loss-sensitive {4,8}     PPL 34.84  avg bits 4.4997
C++ random budget {4,8}      PPL 39.18  avg bits 4.4997
C++ category budget {4,8}    PPL 37.57  avg bits 4.4997

Qwen3-0.6B, WikiText2 64 prompts, same 4-prompt calibration allocation:

FP16                         PPL 29.49
uniform INT4                 PPL 47.31
C++ loss-sensitive {4,8}     PPL 37.10  avg bits 4.4997
C++ random budget {4,8}      PPL 41.63  avg bits 4.4997
C++ category budget {4,8}    PPL 40.14  avg bits 4.4997

Qwen3-1.7B, WikiText2 16 prompts, uniform smoke:

FP16                         PPL 18.97
uniform INT4                 PPL 27.45
uniform INT3                 PPL 312.57

Qwen3-1.7B, WikiText2 16 prompts, C++ planner after low-memory sensitivity:

FP16                         PPL 18.97
uniform INT4                 PPL 27.45
C++ loss-sensitive {4,8}     PPL 24.80  avg bits 4.4973
C++ random budget {4,8}      PPL 25.39  avg bits 4.4973
C++ category budget {4,8}    PPL 23.84  avg bits 4.4827
C++ hybrid budget {4,8}      PPL 23.98  avg bits 4.4925
C++ blend sweep best {4,8}   PPL 23.52  avg bits 4.4827

Qwen3-1.7B, WikiText2 64 prompts, same 2-prompt calibration allocation:

FP16                         PPL 21.66
uniform INT4                 PPL 31.19
C++ loss-sensitive {4,8}     PPL 27.66  avg bits 4.4973
C++ random budget {4,8}      PPL 28.38  avg bits 4.4973
C++ category budget {4,8}    PPL 27.48  avg bits 4.4827
C++ hybrid budget {4,8}      PPL 27.68  avg bits 4.4925
C++ blend sweep best {4,8}   PPL 27.48  avg bits 4.4827

Qwen3-1.7B, random16 stress check, same 2-prompt calibration budget:

WikiText2-64:
loss-sensitive               PPL 27.6578
category                     PPL 27.4838
random16 min/mean/max        PPL 27.6685 / 28.2905 / 29.9682
target vs best random        +0.0107 PPL
target vs random mean        +0.6327 PPL

C4-64:
loss-sensitive               PPL 29.2030
category                     PPL 29.2760
random16 min/mean/max        PPL 28.4562 / 29.4357 / 30.0408
target vs best random        -0.7467 PPL
target vs random mean        +0.2327 PPL

Qwen3-1.7B, WikiText2+C4 two-split consensus allocation:

WikiText2-64:
consensus                    PPL 26.3260
WikiText-only sensitivity    PPL 27.6578
C4-only sensitivity          PPL 26.6878
category                     PPL 27.4838
best listed random           PPL 27.6685
target vs best random        +1.3425 PPL

C4-64:
consensus                    PPL 28.3303
WikiText-only sensitivity    PPL 29.2030
C4-only sensitivity          PPL 28.3505
category                     PPL 29.2760
best listed random           PPL 28.4562
target vs best random        +0.1259 PPL

OLMo-2-0425-1B-Instruct, WikiText2 16 prompts, uniform smoke:

FP16                         PPL 17.12
uniform INT4                 PPL 20.70
uniform INT3                 PPL 58.84

OLMo-2-0425-1B-Instruct, WikiText2 16 prompts, C++ planner after 2-prompt sensitivity:

FP16                         PPL 17.12
uniform INT4                 PPL 20.70
uniform INT3                 PPL 58.84
C++ category budget {4,8}    PPL 19.39  avg bits 4.4984
C++ random budget {4,8}      PPL 19.71  avg bits 4.4984
C++ loss-sensitive {4,8}     PPL 18.89  avg bits 4.4984
C++ blend sweep best {4,8}   PPL 18.76  avg bits 4.4984

OLMo-2-0425-1B-Instruct, WikiText2 64 prompts, same 2-prompt calibration allocation:

FP16                         PPL 18.86
uniform INT4                 PPL 22.49
C++ category budget {4,8}    PPL 21.63  avg bits 4.4984
C++ random budget {4,8}      PPL 21.64  avg bits 4.4984
C++ blend_sensitivity_85     PPL 21.13  avg bits 4.4984
C++ loss-sensitive {4,8}     PPL 21.12  avg bits 4.4984

OLMo-2-0425-1B-Instruct, C4 English 64 prompts, same 2-prompt calibration allocation:

FP16                         PPL 32.27
uniform INT4                 PPL 36.83
C++ category budget {4,8}    PPL 36.05  avg bits 4.4984
C++ random budget {4,8}      PPL 35.85  avg bits 4.4984
C++ blend_sensitivity_85     PPL 35.88  avg bits 4.4984
C++ loss-sensitive {4,8}     PPL 35.84  avg bits 4.4984

OLMo-2-0425-1B-Instruct, random8 check with the same allocation budget:

WikiText2-64:
loss-sensitive               PPL 21.12
random8 min/mean/max         PPL 21.46 / 21.61 / 21.76

C4-64:
loss-sensitive               PPL 35.84
random8 min/mean/max         PPL 35.85 / 36.03 / 36.38
```

This is still a small sanity slice, but it addresses a concrete reviewer
question: the allocation is no longer compared only against uniform INT4. The
budget-matched random baseline protects only `15.87%` of measured positive
loss increase, while the loss-sensitive allocation protects `54.45%` at nearly
the same average-bit budget. The new C++ planner reads the measured
module-sensitivity JSON directly and emits evaluator-compatible allocations;
on the same Qwen2.5-1.5B 16-prompt slice its loss-sensitive budget allocation
beats C++ random and category baselines under a similar average-bit budget.
On Qwen3-0.6B, a 4-prompt sensitivity calibration plus C++ planner allocation
also beats uniform INT4, random budget, and category budget on the 16-prompt
WikiText2 slice. On Qwen3-1.7B, the low-memory sensitivity probe completed at
`4520/8151 MiB` (`55.45%`) after the earlier high-memory path was killed at
`7628/8151 MiB` (`93.58%`). The 1.7B C++ loss-sensitive allocation beats
uniform INT4 and random budget, but does not beat the category budget baseline
on the 16-prompt slice. The same ordering holds on the 64-prompt external
check using the same 2-prompt allocation, where category is still slightly
better than loss-sensitive. A first C++ hybrid score that blends normalized
loss sensitivity with the structural category prior improves over uniform and
random but still does not beat category on Qwen3-1.7B; it is kept as an
ablation, not a new best result. A C++ blend sweep over sensitivity/category
weights does find a slightly stronger low-sensitivity blend: on Qwen3-1.7B it
improves the 16-prompt slice from category `23.84` to `23.52` PPL and the
64-prompt check from `27.4838` to `27.4756` PPL at the same average-bit budget.
This is the current best in-repo Qwen3-1.7B WikiText2 fake-quant allocation,
but the 64-prompt gain is small. The follow-up random16 stress check is mixed:
loss-sensitive beats the random mean on both WikiText2-64 and C4-64, barely
beats the best random seed on WikiText2-64, and loses to the best random seed
on C4-64. This is useful negative evidence for calibration/proxy overfitting:
the current two-prompt sensitivity score is a signal, not a robust allocator.
The follow-up WikiText2+C4 consensus allocation is the first stronger result:
using two calibration distributions improves WikiText2-64 to `26.3260` PPL and
C4-64 to `28.3303` PPL, beating the listed best random seeds on both slices.
This supports the next mathematical direction: multi-split robustness and
cross-distribution consensus matter more than a single calibration loss proxy.
It still remains a short-slice fake-quant diagnostic, not a production
quantizer or SOTA claim. The OLMo2 run adds a non-Qwen, 2025-era 1B model
check: uniform INT4 has a moderate short-slice PPL increase (`17.12` to
`20.70`), while uniform INT3 is much more destructive (`58.84`).
The 2-prompt low-memory sensitivity probe completed over all 113 Linear
modules at `4175/8151 MiB` (`51.22%`) and the C++ planner used that JSON
directly. On the 16-prompt slice, the best tested blend candidate improved
uniform INT4 from `20.70` to `18.76` PPL. On the 64-prompt check, the
loss-sensitive budget was slightly stronger than the blend candidate (`21.12`
vs `21.13`) and improved over uniform INT4, random budget, and category
budget. A C4-64 cross-dataset check kept the same qualitative advantage over
uniform INT4 and category, but random was nearly tied (`35.85` vs `35.84` PPL),
so this should be treated as weak cross-dataset support. A follow-up C++
`--random-repeats 8` run keeps loss-sensitive ahead of the best random seed on
both WikiText2-64 (`21.12` vs `21.46`) and C4-64 (`35.84` vs `35.85`), but the
C4 margin is tiny and still needs more calibration splits. This gives a second
model-family positive
allocator signal, but it is still a short-slice fake-quant diagnostic, not a
production quantizer. A
Gemma-3-1B candidate was also attempted, but the Hugging Face repository was
gated in this environment, so it is recorded only as an access blocker, not a
model result.

Evidence files:

```text
train_python/eval_weight_quant_ppl.py
train_python/build_baseline_allocations.py
train_python/run_with_gpu_guard.py
train_python/measure_module_quant_sensitivity.py
train_python/build_dataset_prompts.py
train_python/build_loss_sensitive_knapsack_alloc.py
train_python/build_consensus_allocation.py
train_python/summarize_ppl_results.py
train_python/summarize_sensitivity.py
train_python/search_allocation_swaps.py
inference_cpp/src/quant_allocation_planner.cpp
inference_cpp/src/quant_result_summarizer.cpp
inference_cpp/src/quant_evidence_matrix.cpp
inference_cpp/testdata/allocation_fixture.csv
inference_cpp/testdata/ppl_summary_fixture.json
data_eval/eval_configs/qwen25_1p5b_cpp_planner_budget_compare.json
data_eval/eval_configs/smollm2_group128_compare_allocations.json
data_eval/text_prompts/wikitext2_validation_32.txt
data_eval/text_prompts/wikitext2_validation_128.txt
outputs/smollm2_fake_quant_ppl_report.md
outputs/smollm2_fake_quant_ppl_4to8_limit8_summary.json
outputs/smollm2_fake_quant_ppl_4to8_group128_limit8_summary.json
outputs/smollm2_fake_quant_ppl_4to8_group64_limit8_summary.json
outputs/qwen25_1p5b_baseline_allocations_4to8_limit8_group128_summary.json
outputs/qwen25_1p5b_baseline_budget_ppl_wikitext2_16_summary.json
outputs/qwen25_1p5b_baseline_budget_ppl_wikitext2_64_summary.json
outputs/qwen25_1p5b_baseline_eval_gpu_guard_retry.json
outputs/qwen25_1p5b_baseline_eval_gpu_guard_wikitext2_64.json
outputs/qwen25_1p5b_cpp_allocation_planner_4p5_summary.json
outputs/qwen25_1p5b_cpp_planner_budget_ppl_wikitext2_16_summary.json
outputs/qwen25_1p5b_cpp_planner_budget_gpu_guard_wikitext2_16.json
outputs/qwen3_0p6b_uniform_fake_quant_ppl_wikitext2_16_summary.json
outputs/qwen3_0p6b_uniform_gpu_guard_wikitext2_16.json
outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json
outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128_report.md
outputs/qwen3_0p6b_sensitivity_gpu_guard_limit4_group128.json
outputs/qwen3_0p6b_cpp_allocation_planner_4p5_summary.json
data_eval/eval_configs/qwen3_0p6b_cpp_planner_budget_compare.json
outputs/qwen3_0p6b_cpp_planner_budget_ppl_wikitext2_16_summary.json
outputs/qwen3_0p6b_cpp_planner_budget_gpu_guard_wikitext2_16.json
outputs/qwen3_0p6b_cpp_planner_budget_ppl_wikitext2_64_summary.json
outputs/qwen3_0p6b_cpp_planner_budget_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_uniform_fake_quant_ppl_wikitext2_16_summary.json
outputs/qwen3_1p7b_uniform_gpu_guard_wikitext2_16.json
outputs/qwen3_1p7b_sensitivity_gpu_guard_limit2_group128.json
outputs/qwen3_1p7b_sensitivity_lowmem_gpu_guard_limit2_group128.json
outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json
outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128_report.md
outputs/qwen3_1p7b_cpp_allocation_planner_4p5_summary.json
data_eval/eval_configs/qwen3_1p7b_cpp_planner_budget_compare.json
outputs/qwen3_1p7b_cpp_planner_budget_ppl_wikitext2_16_summary.json
outputs/qwen3_1p7b_cpp_planner_budget_gpu_guard_wikitext2_16.json
outputs/qwen3_1p7b_cpp_planner_budget_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_cpp_planner_budget_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_cpp_allocation_planner_hybrid_4p5_summary.json
data_eval/eval_configs/qwen3_1p7b_cpp_planner_hybrid_budget_compare.json
outputs/qwen3_1p7b_cpp_hybrid_budget_ppl_wikitext2_16_summary.json
outputs/qwen3_1p7b_cpp_hybrid_budget_gpu_guard_wikitext2_16.json
outputs/qwen3_1p7b_cpp_hybrid_budget_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_cpp_hybrid_budget_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_cpp_allocation_planner_blend_sweep_4p5_summary.json
data_eval/eval_configs/qwen3_1p7b_cpp_blend_sweep_candidates.json
data_eval/eval_configs/qwen3_1p7b_cpp_blend_winners.json
outputs/qwen3_1p7b_cpp_blend_sweep_ppl_wikitext2_16_summary.json
outputs/qwen3_1p7b_cpp_blend_sweep_gpu_guard_wikitext2_16.json
outputs/qwen3_1p7b_cpp_blend_winners_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_cpp_blend_winners_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_cpp_blend_winners_ppl_c4_64_summary.json
outputs/qwen3_1p7b_cpp_blend_winners_gpu_guard_c4_64.json
outputs/qwen3_1p7b_cpp_allocation_planner_random16_4p5_summary.json
data_eval/eval_configs/qwen3_1p7b_cpp_random16_compare.json
outputs/qwen3_1p7b_cpp_random16_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_cpp_random16_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_cpp_random16_ppl_c4_64_summary.json
outputs/qwen3_1p7b_cpp_random16_gpu_guard_c4_64.json
outputs/qwen3_1p7b_cpp_random16_wikitext2_64_summary.md
outputs/qwen3_1p7b_cpp_random16_wikitext2_64_summary.csv
outputs/qwen3_1p7b_cpp_random16_c4_64_summary.md
outputs/qwen3_1p7b_cpp_random16_c4_64_summary.csv
outputs/qwen3_1p7b_cpp_random16_evidence_matrix.md
outputs/qwen3_1p7b_cpp_random16_evidence_matrix.csv
outputs/qwen3_1p7b_module_loss_sensitivity_c4_limit2_group128.json
outputs/qwen3_1p7b_module_loss_sensitivity_c4_limit2_group128_report.md
outputs/qwen3_1p7b_sensitivity_lowmem_gpu_guard_c4_limit2_group128.json
outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json
outputs/qwen3_1p7b_loss_sensitive_wikitext_c4_consensus_alloc_4to8_group128_summary.json
outputs/qwen3_1p7b_loss_sensitive_wikitext_c4_consensus_alloc_4to8_group128_report.md
data_eval/eval_configs/qwen3_1p7b_wikitext_c4_consensus_compare.json
outputs/qwen3_1p7b_wikitext_c4_consensus_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_wikitext_c4_consensus_gpu_guard_wikitext2_64.json
outputs/qwen3_1p7b_wikitext_c4_consensus_ppl_c4_64_summary.json
outputs/qwen3_1p7b_wikitext_c4_consensus_gpu_guard_c4_64.json
outputs/qwen3_1p7b_wikitext_c4_consensus_wikitext2_64_summary.md
outputs/qwen3_1p7b_wikitext_c4_consensus_c4_64_summary.md
outputs/qwen3_1p7b_wikitext_c4_consensus_evidence_matrix.md
outputs/qwen3_1p7b_wikitext_c4_consensus_evidence_matrix.csv
outputs/Qwen3-1.7B-Lowmem-Sensitivity-Cpp-Planner-2026-06-05.md
outputs/olmo2_0425_1b_instruct_uniform_fake_quant_ppl_wikitext2_16_summary.json
outputs/olmo2_0425_1b_instruct_uniform_gpu_guard_wikitext2_16.json
outputs/gemma3_1b_uniform_gpu_guard_wikitext2_16.json
outputs/OLMo2-0425-1B-Uniform-Smoke-2026-06-05.md
outputs/olmo2_0425_1b_sensitivity_lowmem_gpu_guard_limit2_group128.json
outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128.json
outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128_report.md
outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
outputs/olmo2_0425_1b_cpp_allocation_planner_blend_sweep_4p5_summary.json
data_eval/eval_configs/olmo2_0425_1b_cpp_blend_sweep_candidates.json
data_eval/eval_configs/olmo2_0425_1b_cpp_blend_winners.json
outputs/olmo2_0425_1b_cpp_blend_sweep_ppl_wikitext2_16_summary.json
outputs/olmo2_0425_1b_cpp_blend_sweep_gpu_guard_wikitext2_16.json
outputs/olmo2_0425_1b_cpp_blend_winners_ppl_wikitext2_64_summary.json
outputs/olmo2_0425_1b_cpp_blend_winners_gpu_guard_wikitext2_64.json
outputs/olmo2_0425_1b_cpp_blend_winners_ppl_c4_64_summary.json
outputs/olmo2_0425_1b_cpp_blend_winners_gpu_guard_c4_64.json
outputs/olmo2_0425_1b_cpp_allocation_planner_random8_4p5_summary.json
data_eval/eval_configs/olmo2_0425_1b_cpp_random8_compare.json
outputs/olmo2_0425_1b_cpp_random8_ppl_wikitext2_64_summary.json
outputs/olmo2_0425_1b_cpp_random8_gpu_guard_wikitext2_64.json
outputs/olmo2_0425_1b_cpp_random8_ppl_c4_64_summary.json
outputs/olmo2_0425_1b_cpp_random8_gpu_guard_c4_64.json
outputs/olmo2_0425_1b_cpp_random8_wikitext2_64_summary.md
outputs/olmo2_0425_1b_cpp_random8_wikitext2_64_summary.csv
outputs/olmo2_0425_1b_cpp_random8_c4_64_summary.md
outputs/olmo2_0425_1b_cpp_random8_c4_64_summary.csv
outputs/OLMo2-0425-1B-Cpp-Planner-2026-06-05.md
docs/small-model-candidates-2026-06-05.md
outputs/llama32_1b_uniform_gpu_guard_wikitext2_16.json
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
data_eval/eval_configs/qwen25_uniform_group128.json
data_eval/eval_configs/qwen25_group128_with_loss_sensitive.json
data_eval/eval_configs/qwen25_group128_with_loss_sensitive_limit8.json
data_eval/eval_configs/qwen25_group128_with_consensus.json
outputs/qwen25_0p5b_uniform_quant_baseline_report.md
outputs/qwen25_0p5b_loss_sensitive_quant_report.md
outputs/qwen25_0p5b_loss_sensitive_limit8_quant_report.md
outputs/qwen25_0p5b_consensus_quant_report.md
outputs/qwen25_0p5b_module_loss_sensitivity_limit2_group128.json
outputs/qwen25_0p5b_module_loss_sensitivity_limit8_group128.json
outputs/qwen25_0p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
outputs/qwen25_0p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json
outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json
outputs/qwen25_1p5b_uniform_smoke_report.md
outputs/qwen25_1p5b_fake_quant_ppl_uniform_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_uniform_smoke_ppl_table.md
data_eval/eval_configs/qwen25_1p5b_group128_with_loss_sensitive.json
data_eval/eval_configs/qwen25_1p5b_group128_with_loss_sensitive_limit8.json
data_eval/eval_configs/qwen25_1p5b_group128_with_consensus.json
data_eval/eval_configs/qwen25_1p5b_group128_compare_2p8p_consensus.json
outputs/qwen25_1p5b_loss_sensitive_update.md
outputs/qwen25_1p5b_module_loss_sensitivity_limit2_group128.json
outputs/qwen25_1p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_loss_sensitive_ppl_table.md
outputs/qwen25_1p5b_loss_sensitive_two_dataset_ppl_table.md
outputs/qwen25_1p5b_sensitivity_compact_summary.md
outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128.json
outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128_report.md
outputs/qwen25_1p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_limit8_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_loss_sensitive_limit8_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_sensitivity_limit8_compact_summary.md
outputs/qwen25_1p5b_loss_sensitive_2p_vs_8p_stability_report.md
outputs/qwen25_1p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json
outputs/qwen25_1p5b_loss_sensitive_consensus_alloc_4to8_group128_report.md
outputs/qwen25_1p5b_fake_quant_ppl_consensus_group128_wikitext2_16_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_consensus_group128_c4_en_validation_32_summary.json
outputs/qwen25_1p5b_loss_sensitive_2p8p_consensus_ppl_table.md
outputs/qwen25_1p5b_fake_quant_ppl_compare_2p8p_consensus_group128_wikitext2_64_summary.json
outputs/qwen25_1p5b_fake_quant_ppl_compare_2p8p_consensus_group128_c4_en_validation_64_summary.json
outputs/qwen25_1p5b_loss_sensitive_compare_2p8p_consensus_ppl64_table.md
outputs/qwen25_1p5b_fake_quant_ppl_compare_2p8p_consensus_group128_wikitext2_128_summary.json
outputs/qwen25_1p5b_loss_sensitive_compare_2p8p_consensus_wikitext2_128_table.md
outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_report.md
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_consensus_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_consensus_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_consensus_ppl_table.json
outputs/qwen25_0p5b_consensus_ppl_table.csv
outputs/qwen25_0p5b_consensus_ppl_table.md
train_python/compare_allocations.py
outputs/qwen25_0p5b_loss_sensitive_2p_vs_8p_stability_summary.json
outputs/qwen25_0p5b_loss_sensitive_2p_vs_8p_stability_report.md
```

### 8-skill hybrid routing, v2

Base model: `HuggingFaceTB/SmolLM2-360M-Instruct`

PoC skills:

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

### C++ quant-kernel microbenchmark

The newest C++ artifact benchmarks standalone kernel shapes through the reusable
`eigenskill_quant_kernels` API:

```text
fp32 dense GEMV
AVX2 fp32 dense GEMV when available
packed INT4 dequant GEMV with per-row scales
packed INT3 dequant GEMV with per-row scales
packed mixed-bit dequant GEMV with per-row 3/4/8-bit choices
policy-selected output-row GEMV
AVX2 policy-selected output-row GEMV when available
mixed-bit policy-selected output-row GEMV
scalar skill bypass, y = lambda x
```

Selected local Windows/MSVC result:

```text
d=512,  rows=16:  dense=0.159312 ms, dense_avx2=0.018234 ms, int4=0.225300 ms, selected_avx2=0.000536 ms
d=1024, rows=16:  dense=0.632122 ms, dense_avx2=0.067346 ms, int4=0.958060 ms, selected_avx2=0.001083 ms
d=2048, rows=16:  dense=2.591152 ms, dense_avx2=0.369847 ms, int4=3.986131 ms, selected_avx2=0.002425 ms
d=2048, rows=256: dense=2.620207 ms, dense_avx2=0.342829 ms, int4=4.547568 ms, selected_avx2=0.044658 ms
```

Interpretation:

```text
packed INT4 faster than dense: 0/9 cases
best dense AVX2 speedup:       10.26x versus scalar dense
best selected-row speedup:     1068.52x at d=2048, rows=16 with AVX2
selected-row AVX2 max error:   1.511e-06 against the corresponding dense rows
```

This is deliberately not framed as an INT4 speedup result. In this naive CPU
implementation, nibble unpacking and scalar dequantization dominate. The
positive systems signal is policy-selected row computation; the low-bit kernel
needs AVX2/NEON/native low-bit dot-product work before it can support a speed
claim.

The reusable API now includes a generic signed low-bit bitstream path for
2-to-7-bit row-scaled weights. The INT4 compatibility wrapper is implemented
on top of that path, and `quant_kernel_verify` checks both INT4 and INT3 finite
outputs. A WSL/g++ 11.4 smoke build on 2026-06-04 passed CTest and benchmarked
INT3/INT4, confirming correctness and exposing the expected negative systems
result: scalar bit-unpack low-bit GEMV is slower than AVX2 FP32 GEMV until a
vectorized low-bit dot path is added.

The current WSL mixed-bit benchmark adds per-row 3/4/8-bit storage and selected
row execution over that mixed representation:

```text
d=2048, rows=16:
dense=2.554907 ms, AVX2 dense=0.303719 ms
mixed full dequant=11.888089 ms
mixed selected-row=0.145753 ms
selected-row AVX2 fp32=0.002909 ms
mixed selected-row speedup vs scalar dense=17.53x
mixed selected-row rel_l2 vs mixed full output rows=0.0

mixed selected-row faster than dense: 7/9 cases
full mixed-bit dequant faster than dense: 0/9 cases
```

The key systems claim is therefore narrow: mixed-bit storage can be represented
and routed at row granularity, and selected-row execution over that format is a
measurable bypass baseline. It is still not a production low-bit matmul.

Evidence files:

```text
inference_cpp/include/eigenskill/quant_kernels.hpp
inference_cpp/src/quant_kernels.cpp
inference_cpp/src/quant_kernel_verify.cpp
inference_cpp/src/quant_kernel_bench.cpp
inference_cpp/CMakeLists.txt
inference_cpp/build-msvc.ps1
train_python/parse_quant_kernel_bench.py
outputs/eigenskill_quant_kernel_verify_msvc.json
outputs/EigenSkill-Q-Cpp-Quant-Kernel-API-Report.md
outputs/eigenskill_quant_kernel_benchmark.txt
outputs/eigenskill_quant_kernel_benchmark_summary.json
outputs/eigenskill_quant_kernel_mixedbit_benchmark.txt
outputs/eigenskill_quant_kernel_mixedbit_benchmark_summary.json
outputs/EigenSkill-Q-Cpp-Quant-Kernel-Benchmark-Report.md
```

WSL/CMake smoke verification also builds all three C++ artifacts with g++ 11.4:

```bash
cmake -S inference_cpp -B build/cpp-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build build/cpp-wsl -j2
ctest --test-dir build/cpp-wsl --output-on-failure
./build/cpp-wsl/quant_kernel_bench --dims 256,512 --active-rows 16,64 --iters 20 --warmup 5
./build/cpp-wsl/quant_policy_bypass --data data_eval/eigenskill_quant_v1/eval.jsonl --limit 20
```

## Repository Layout

```text
train_python/                 data generation, LoRA training, eval, bypass scripts
inference_cpp/                standalone C++ artifacts and MSVC build script
inference_cpp/src/eigenskill_bench.cpp
                              C++ low-rank GEMV microbenchmark
inference_cpp/src/quant_policy_bypass.cpp
                              C++ deterministic quantization-policy evaluator
inference_cpp/src/quant_kernel_bench.cpp
                              C++ quant-kernel and selected-row microbenchmark
data_eval/eigenskill_v2/      older 8-skill PoC split with severe overlap
data_eval/eigenskill_quant_v1/cleaner quantization-policy split
data_eval/eval_configs/       fake-quant evaluation configs
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

Build and run the low-rank GEMV benchmark on Windows/MSVC:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1
.\inference_cpp\build\eigenskill_bench.exe --dims 1024,2048 --ks 4,8,16 --iters 300
```

Build and run the quant-kernel benchmark:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-kernel
.\inference_cpp\build\quant_kernel_bench.exe --dims 512,1024,2048 --active-rows 16,64,256 --iters 200
python .\train_python\parse_quant_kernel_bench.py `
  --input outputs\eigenskill_quant_kernel_benchmark.txt `
  --out outputs\eigenskill_quant_kernel_benchmark_summary.json
```

More detail is in `inference_cpp/README.md`.

## Reproduce Qwen2.5 Uniform Fake-Quant Baseline

This requires the WSL GPU Python environment and a complete local Hugging Face
cache, network access, or a direct local download for:

```text
Qwen/Qwen2.5-0.5B-Instruct
Qwen/Qwen2.5-1.5B-Instruct
```

The first `Qwen/Qwen2.5-1.5B-Instruct` attempt did not reach evaluation because
the unauthenticated Hugging Face cache download stalled around a partial 325 MB
blob. That failed attempt is retained as blocker evidence:

```text
outputs/qwen25_1p5b_smoke_attempt_2026-06-04.md
```

The repository includes a cache-audited predownload helper:

```bash
python3 train_python/predownload_hf_model.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --out-json outputs/qwen25_1p5b_predownload_summary.json \
  --out-md outputs/qwen25_1p5b_predownload_report.md
```

It reports `.incomplete` cache blobs as `incomplete_cache`, even if
`snapshot_download` returns a local snapshot path. When the cache path is
unreliable, the direct resumable downloader can fetch the 1.5B model into the
repo-external model directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\download_qwen25_1p5b.ps1
```

The direct download used for the current smoke evidence produced:

```text
C:\Users\18042\models\Qwen2.5-1.5B-Instruct\model.safetensors
bytes: 3,087,467,144
sha256: DD924A11B4C220F385B51FFA522DAEA7C9F3D850E31B162BB5661DF483C6D3EE
```

Older cache-audit evidence:

```text
outputs/qwen25_0p5b_cache_audit_report.md
outputs/qwen25_1p5b_download_blocker_report.md
```

Commands:

```bash
python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 128 \
  --max-length 160 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_wikitext2_128_summary.json

python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/c4_en_validation_64.txt \
  --limit-prompts 64 \
  --max-length 160 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_c4_en_validation_64_summary.json

HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
python3 train_python/eval_weight_quant_ppl.py \
  --model /mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 16 \
  --max-length 128 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_1p5b_fake_quant_ppl_uniform_group128_wikitext2_16_summary.json
```

For multi-config evaluation, `--reuse-model` can avoid reloading the same model
once per config. A Qwen 8-prompt smoke check matched the old reload-per-config
outputs exactly on mean NLL for FP16, uniform INT4, uniform INT3, and the
loss-sensitive limit8 allocation:

```bash
python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-0.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 8 \
  --max-length 128 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_group128_with_loss_sensitive_limit8.json \
  --reuse-model \
  --out outputs/qwen25_0p5b_reuse_model_smoke_limit8_wikitext2_8_summary.json
```

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
