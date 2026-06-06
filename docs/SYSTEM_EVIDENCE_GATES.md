# System Evidence Gates

This repository separates exploratory output from evidence that can survive a
paper review. A result should be treated as paper-facing only when it is backed
by an executable gate and an explicit claim boundary.

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

Valid claim:

- measured Triton tuning artifacts can now drive the prototype ESMP generation
  path instead of remaining an offline report;
- output JSON exposes which measured block config was used.
- a small selector-driven runtime smoke is automatically gated for selector use,
  compression, generated-token presence, and GPU memory guard compliance.

Invalid claim:

- selector-driven generation is faster end-to-end;
- selector coverage generalizes to unmeasured shapes;
- mobile, Tensor Core production, or CCF-A system claims are established.
