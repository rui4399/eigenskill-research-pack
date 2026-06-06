# Public Task Benchmark Gate

Date: `2026-06-06T19:04:48+00:00`
Status: **PASS**
Cases: `2`
Total tasks: `100`
Total passes: `39`
Mean accuracy: `0.3900`
Peak guard VRAM ratio: `0.8865`

## Cases

| case | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | VRAM ratio |
|---|---|---:|---:|---:|---:|---:|---:|
| `mmlu50` | `mmlu` | 50 | 28 | 0.5600 | 23.3929 | 0.871185 | 0.8865 |
| `gsm8k50` | `gsm8k` | 50 | 11 | 0.2200 | 18.6902 | 0.762850 | 0.8865 |

## Failures

- none

## Claim Boundary

- Valid claim: public MMLU/GSM8K subset evaluation ran under guard. Invalid claim: this is leaderboard-scale or SOTA quality evidence.
