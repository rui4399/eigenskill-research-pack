# Local GPU fake-quant PPL smoke - Qwen2.5-0.5B

Source: `outputs/LOCAL_SMOKE_QWEN25_0P5B_GPU_FAKE_QUANT_PPL_2026_07_01.json`

Model: `Qwen/Qwen2.5-0.5B-Instruct`

Prompts: `1`

Device/dtype: `cuda` / `float16`

| variant | PPL | delta NLL vs FP16 |
|---|---:|---:|
| FP16 | 47.5798 | 0.0000 |
| uniform INT4 | 124.2689 | 0.9600 |
| uniform INT3 | 12393.2436 | 5.5625 |
| consensus 4-to-8 allocation | 68.2091 | 0.3602 |

Allocation/uniform-INT4 PPL ratio: `0.5489`

Claim boundary: local GPU smoke only over one prompt; useful for feasibility and direction, not paper-facing downstream retention or SOTA evidence.
