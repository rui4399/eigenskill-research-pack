# Layer-20 V Prompt-Conditioned Row-Group Sweep

Date: `2026-06-05T23:19:18+00:00`
Model: `Qwen/Qwen3-0.6B`
Base summary: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qkv8_guard/pack_summary.json`
Module: `model.layers.20.self_attn.v_proj`
Layers evaluated: `1,7,20`
Group size: `128`

## Results

| group | rows | exact | edit | prefix | speed | package compression | guard peak MiB |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | `0:128` | 2 / 6 | 0.6421 | 0.4764 | 0.8473x | 6.7540x | 3561 |
| 1 | `128:256` | 1 / 6 | 0.5424 | 0.3256 | 0.9272x | 6.7540x | 3554 |
| 2 | `256:384` | 1 / 6 | 0.5498 | 0.3569 | 0.8657x | 6.7540x | 3554 |
| 3 | `384:512` | 1 / 6 | 0.5605 | 0.3141 | 0.9490x | 6.7540x | 3554 |
| 4 | `512:640` | 2 / 6 | 0.7169 | 0.5374 | 0.9750x | 6.7540x | 3554 |
| 5 | `640:768` | 1 / 6 | 0.5789 | 0.3642 | 1.0029x | 6.7540x | 3558 |
| 6 | `768:896` | 1 / 6 | 0.6673 | 0.4753 | 0.9540x | 6.7540x | 3557 |
| 7 | `896:1024` | 1 / 6 | 0.5789 | 0.3642 | 0.9965x | 6.7540x | 3555 |

## Interpretation

- Best exact/prefix candidate: group `4` rows `512:640` with `2/6` exact and prefix `0.5374`.
- Highest prefix candidate: group `4` rows `512:640` with prefix `0.5374`.
- This sweep is prompt-conditioned: each row group is selected by measured generation behavior on the fixed prompt suite, not by local reconstruction error alone.
