# AAAI Sprint Calibration Alignment

Generated: 2026-07-09

| Model | N | Mean Jaccard | Avg bits | Downstream retention | Note |
|---|---:|---:|---:|---|---|
| 1p5b | 16 | 0.677 | 3.000 |  |  |
| 1p5b | 32 | 0.740 | 3.000 |  |  |
| 1p5b | 64 | 0.849 | 3.000 | mmlu100=0.01; gsm8k100=0.00 |  |
| 1p5b | 128 | 0.990 | 3.000 |  |  |
| 1p5b | 256 | 0.908 | 3.000 | mmlu100=0.05 (5/100); gsm8k100=0.00 (0/100) |  |
| 1p5b | 512 | n/a | 2.999 | mmlu100=0.05 (5/100); gsm8k100=0.00 (0/100) | single full-pool sensitivity/allocation with downstream retention; no two-split Jaccard or CSI consensus claimed |
| 7b | 16 | 0.682 | 3.000 |  |  |
| 7b | 32 | 0.700 | 3.000 |  |  |
| 7b | 64 | 0.825 | 3.000 | mmlu100=0.53; mmlu100=0.01; gsm8k100=0.02 |  |

Note: 1.5B n512 is completed full-pool sensitivity/downstream evidence, not independent split-perturbation consensus evidence.
