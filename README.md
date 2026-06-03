# EigenSkill Research Pack

This repository contains the current EigenSkill proof-of-concept package for
skill-oriented edge LLM inference.

EigenSkill is currently best framed as a hybrid micro-kernel runtime: a small
LLM handles semantic routing and non-deterministic language understanding, while
low-entropy skills are routed to deterministic or low-rank bypass kernels.

## Current Results

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

Key v2 metrics:

```text
train samples:        7200
eval samples:         1440
pure model exact:     1391/1440 = 96.60%
hybrid runtime exact: 1439/1440 = 99.93%
```

The strongest current result is the hybrid runtime: `unit_time_normalize` is
handled by a deterministic bypass path, while the remaining skills use the
fine-tuned model output.

## Repository Layout

```text
train_python/                 Python data generation, LoRA training, eval, hybrid runtime
inference_cpp/                C++ low-rank microbenchmark
data_eval/eigenskill_v2/      v2 train/eval JSONL data
outputs/                      selected eval outputs and technical reports
research_pack_2026-06-03/     mentor report, route map, paper drafts, DOCX/Markdown pack
docs/                         NotebookLM-generated business and Q&A notes
```

Large model artifacts are not committed. The verified local package paths are
recorded in `outputs/eigenskill_v2_package_manifest.json`.

## Reproduce The Core Evaluation

Set up a Python environment with PyTorch, Transformers, PEFT, TRL, datasets,
and supporting packages, then follow:

```text
train_python/README.md
```

Useful commands:

```bash
python train_python/generate_skill_data_v2.py --out data_eval/eigenskill_v2 --train-per-skill 900 --eval-per-skill 180
python train_python/train_lora.py --model HuggingFaceTB/SmolLM2-360M-Instruct --data data_eval/eigenskill_v2/train.jsonl --eval-data data_eval/eigenskill_v2/eval.jsonl --out models/eigenskill-smollm2-360m-lora-v2-fp16
python train_python/hybrid_eval_skills.py --model-eval outputs/eigenskill_v2_eval.json --data data_eval/eigenskill_v2/eval.jsonl --out outputs/eigenskill_v2_hybrid_eval_recheck.json
python train_python/verify_v2_package.py
```

## C++ Microbenchmark

The C++ artifact isolates the low-rank skill-path claim:

```text
dense path: y = W x
skill path: z = U^T x; z2 = A z; y = U z2
```

Build on Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1
```

Run:

```powershell
.\inference_cpp\build\eigenskill_bench.exe --dims 1024,2048 --ks 4,8,16 --iters 300
```

## Research Pack

The mentor-facing and paper-facing material is under
`research_pack_2026-06-03/`:

```text
导师汇报版_EigenSkill阶段性科研报告.md/.docx
EigenSkill投稿路线图_期刊会议建议.md/.docx
论文初稿A_MLSys_ASPLOS方向_HybridMicroKernel.md/.docx
论文初稿B_IEEEIoTJ_TECS方向_EdgeSkillRuntime.md/.docx
论文初稿C_NeurIPSWorkshop方向_EigenRegularization.md/.docx
论文初稿D_TCPS_TOSN方向_SwarmLLMArchitecture.md/.docx
EigenSkill_research_pack_2026-06-03.zip
```

## Scope Notes

Completed evidence covers:

- 8-skill synthetic data generation and LoRA fine-tuning.
- Pure-model exact match and hybrid-runtime exact match evaluation.
- Deterministic bypass for `unit_time_normalize`.
- A C++ low-rank microbenchmark.
- Research reports and early paper drafts.

Not yet completed:

- End-to-end edge-board latency and energy measurement.
- Real NPU/ARM NEON bypass integration.
- True spectral/eigen-routing proof across nonlinear Transformer layers.
- Cross-medium acoustic communication or physical swarm assembly.

Do not present the swarm or spectral-routing pieces as completed experimental
results yet; they are research directions and architecture proposals.

## EigenSkill-Q Quantization Policy Update

The repository now includes a quantization-policy skill track. The latest
dataset is:

```text
data_eval/eigenskill_quant_v1/
```

It covers five policy skills:

```text
outlier_detect
bit_allocate
rotation_select
residual_patch
kv_policy
```

The v1 split is deliberately small and auditable:

```text
train: 1200 rows
eval:   400 rows
test:   400 rows
train/eval/test exact overlap: 0
train/eval/test input overlap: 0
```

The deterministic quantization bypass baseline reaches:

```text
eval exact_json:      400/400 = 100%
eval decision_exact:  400/400 = 100%
test exact_json:      400/400 = 100%
test decision_exact:  400/400 = 100%
```

The pure LoRA smoke runs are intentionally reported as negative evidence:
short SFT on SmolLM2-360M learns JSON-like surface form but does not reliably
learn the numeric threshold policies. This supports the current EigenSkill-Q
framing: let the model route/trigger the skill contract, then execute
rate-distortion, outlier, rotation, residual, and KV-cache decisions through a
verified lightweight bypass micro-kernel.

Useful files:

```text
train_python/generate_quant_skill_data.py
train_python/eval_quant_policy.py
train_python/hybrid_eval_quant_policy.py
outputs/eigenskill_quant_v1_eval_hybrid_policy_summary.json
outputs/eigenskill_quant_v1_test_hybrid_policy_summary.json
docs/obsidian_quant_route/12-quant-v1-data-fix-and-bypass-baseline.md
```

Current direction: treat the old v2 hybrid result as an engineering PoC and move
the publication track toward sensitivity-rate-distortion guided mixed-precision
LLM quantization with a verified bypass runtime.
