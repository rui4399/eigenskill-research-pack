# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n64_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n64_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'2': 99, '4': 98} |
| 2p 8-bit overlap | 90 |
| 8p 8-bit overlap | 90 |
| locked intersection modules | 83 |
| ranked additions | 15 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.007366 | 0.007319 | 0.9936 | 0.007413 | 0.007319 | 1.860e-08 | 1 | 1 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.001987 | 0.001590 | 0.8000 | 0.001590 | 0.002385 | 4.040e-09 | 3 | 2 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.052093 | 0.051770 | 0.9938 | 0.051770 | 0.052417 | 3.762e-09 | 4 | 3 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001392 | 0.001333 | 0.9573 | 0.001333 | 0.001452 | 3.387e-09 | 5 | 4 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001141 | 0.001008 | 0.8833 | 0.001275 | 0.001008 | 2.562e-09 | 6 | 11 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001098 | 0.000953 | 0.8673 | 0.000953 | 0.001244 | 2.421e-09 | 12 | 7 |
| `model.layers.9.self_attn.v_proj` | 393472 | 0.001118 | 0.000908 | 0.8121 | 0.000908 | 0.001328 | 2.308e-09 | 14 | 6 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.032346 | 0.031259 | 0.9664 | 0.033434 | 0.031259 | 2.271e-09 | 11 | 13 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.032894 | 0.031078 | 0.9448 | 0.031078 | 0.034709 | 2.258e-09 | 15 | 12 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.000862 | 0.000838 | 0.9724 | 0.000885 | 0.000838 | 2.129e-09 | 16 | 15 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000902 | 0.000723 | 0.8007 | 0.000723 | 0.001082 | 1.836e-09 | 17 | 9 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.000911 | 0.000715 | 0.7849 | 0.000715 | 0.001107 | 1.817e-09 | 18 | 8 |
| `model.layers.10.self_attn.k_proj` | 393472 | 0.000705 | 0.000683 | 0.9684 | 0.000683 | 0.000727 | 1.735e-09 | 19 | 16 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.000756 | 0.000660 | 0.8731 | 0.000660 | 0.000852 | 1.678e-09 | 20 | 14 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001163 | 0.000655 | 0.5632 | 0.001670 | 0.000655 | 1.664e-09 | 2 | 18 |
| `model.layers.20.self_attn.v_proj` | 393472 | 0.000841 | 0.000618 | 0.7348 | 0.000618 | 0.001065 | 1.571e-09 | 22 | 10 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.000903 | 0.000616 | 0.6826 | 0.001189 | 0.000616 | 1.566e-09 | 8 | 20 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.000968 | 0.000562 | 0.5808 | 0.000562 | 0.001374 | 1.429e-09 | 23 | 5 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.000601 | 0.000497 | 0.8280 | 0.000497 | 0.000704 | 1.264e-09 | 24 | 17 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.000763 | 0.000497 | 0.6518 | 0.001028 | 0.000497 | 1.263e-09 | 9 | 23 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.002955 | 0.002950 | 0.9983 | 0.002960 | 0.002950 | 1.250e-09 | 26 | 24 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.002882 | 0.002557 | 0.8873 | 0.002557 | 0.003207 | 1.084e-09 | 29 | 22 |
| `model.layers.24.self_attn.k_proj` | 393472 | 0.000443 | 0.000390 | 0.8794 | 0.000497 | 0.000390 | 9.909e-10 | 25 | 27 |
| `model.layers.15.self_attn.k_proj` | 393472 | 0.000360 | 0.000359 | 0.9977 | 0.000361 | 0.000359 | 9.126e-10 | 30 | 28 |
| `model.layers.19.self_attn.k_proj` | 393472 | 0.000332 | 0.000312 | 0.9374 | 0.000312 | 0.000353 | 7.921e-10 | 31 | 29 |
| `model.layers.26.self_attn.o_proj` | 2359296 | 0.002196 | 0.001762 | 0.8025 | 0.001762 | 0.002630 | 7.470e-10 | 32 | 25 |
| `model.layers.12.self_attn.v_proj` | 393472 | 0.000445 | 0.000293 | 0.6588 | 0.000293 | 0.000597 | 7.449e-10 | 33 | 21 |
| `model.layers.27.mlp.down_proj` | 13762560 | 0.010495 | 0.010134 | 0.9656 | 0.010134 | 0.010855 | 7.364e-10 | 34 | 32 |
| `model.layers.25.self_attn.o_proj` | 2359296 | 0.001915 | 0.001483 | 0.7743 | 0.001483 | 0.002347 | 6.284e-10 | 37 | 26 |
| `model.layers.13.self_attn.k_proj` | 393472 | 0.000291 | 0.000234 | 0.8046 | 0.000234 | 0.000348 | 5.954e-10 | 38 | 30 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
