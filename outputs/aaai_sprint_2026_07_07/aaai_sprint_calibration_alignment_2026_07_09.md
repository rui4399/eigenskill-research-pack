# AAAI Sprint Calibration Alignment

Generated: 2026-07-09

| Model | N | Mean Jaccard | Avg bits | Downstream n64 CSI |
|---|---:|---:|---:|---|
| 1p5b | 16 | 0.677 | 3.000 |  |
| 1p5b | 32 | 0.740 | 3.000 |  |
| 1p5b | 64 | 0.849 | 3.000 | mmlu100=0.01; gsm8k100=0.00 |
| 1p5b | 128 | 0.990 | 3.000 |  |
| 1p5b | 256 | 0.908 | 3.000 |  |
| 7b | 16 | 0.682 | 3.000 |  |
| 7b | 32 | 0.700 | 3.000 |  |
| 7b | 64 | 0.825 | 3.000 | mmlu100=0.53; mmlu100=0.01; gsm8k100=0.02 |

Note: 1.5B n256 is a completed sensitivity/consensus row from the new 512-prompt public WikiText2 pool; downstream task retention is not rerun at n256.
