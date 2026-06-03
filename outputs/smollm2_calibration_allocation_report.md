# SmolLM2-360M Calibration Allocation Report

Date: 2026-06-04

## Purpose

This report is the first real-model bridge after the short-cycle paper delivery.
It connects a cached small LLM to the EigenSkill-Q rate-distortion allocation
scaffold:

```text
SmolLM2-360M activation calibration
  -> Linear-module statistics
  -> allocator-compatible GroupStat records
  -> mixed-precision bit allocation over {2, 3, 4, 8}
```

This is not yet a real quantized-model benchmark. It does not report
perplexity, downstream accuracy, or end-to-end latency after applying the
allocation. It reports proxy weighted distortion under collected activation
statistics.

## Environment

WSL GPU check:

```text
GPU: NVIDIA GeForce RTX 5070 Laptop GPU
VRAM: about 8 GB
torch: 2.12.0+cu130
CUDA available: true
model cache: HuggingFaceTB/SmolLM2-360M-Instruct
```

Available Python packages in WSL:

```text
transformers: yes
datasets: yes
accelerate: yes
bitsandbytes: no
auto_gptq: no
awq: no
```

## Calibration Command

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 \
  train_python/collect_calibration_stats.py \
  --limit-prompts 4 \
  --max-length 128 \
  --out outputs/calibration_stats_smollm2_360m_limit4.json
```

Result:

```text
model: HuggingFaceTB/SmolLM2-360M-Instruct
prompt_count: 4
linear_modules: 225
```

## Allocation Commands

```powershell
python train_python\rate_distortion_allocator.py `
  --stats-json outputs\calibration_stats_smollm2_360m_limit4.json `
  --budget-avg-bits 2.8 `
  --out-json outputs\smollm2_calib_limit4_rd_alloc_budget28_summary.json `
  --out-md outputs\smollm2_calib_limit4_rd_alloc_budget28_report.md

python train_python\rate_distortion_allocator.py `
  --stats-json outputs\calibration_stats_smollm2_360m_limit4.json `
  --budget-avg-bits 3.2 `
  --out-json outputs\smollm2_calib_limit4_rd_alloc_summary.json `
  --out-md outputs\smollm2_calib_limit4_rd_alloc_report.md
```

## Results

| budget avg bits | method | avg_bits | budget_used | proxy distortion | bit histogram |
|---:|---|---:|---:|---:|---|
| 2.8 | random_budgeted | 2.800 | 1.000 | 234.06147887 | 2:173, 3:17, 4:16, 8:19 |
| 2.8 | rate_distortion | 2.799 | 1.000 | 1.01598835 | 2:97, 3:63, 4:61, 8:4 |
| 3.2 | random_budgeted | 3.200 | 1.000 | 233.62059058 | 2:137, 3:24, 4:34, 8:30 |
| 3.2 | rate_distortion | 3.199 | 1.000 | 0.68940810 | 2:67, 3:35, 4:113, 8:10 |

The large gap against `random_budgeted` is expected because both the collected
stats and the allocator optimize the same proxy objective. The scientific value
of this step is the runnable chain from a real model to an allocation map.

## Next Required Step

The next experiment must apply an allocation to actual quantized weights and
measure:

```text
perplexity
task accuracy
memory footprint
latency
dequant overhead
```

Until that is done, these numbers should be described only as calibration-policy
proxy results.
