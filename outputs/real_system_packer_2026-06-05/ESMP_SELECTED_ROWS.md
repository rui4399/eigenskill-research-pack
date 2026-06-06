# ESMP Selected-Row Runtime Benchmark

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `3`
Batch shapes: `[1, 12, 64]`
Selected rows: `[16, 64, 256]`
Warmup/iters: `10/80`

## Summary By Runtime

| runtime | cases | median ms | mean ms | median speedup vs dense full | median speedup vs dense selected | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|
| dense_full | 27 | 0.019498 | 0.037452 | 1.0000 | 0.8652 | 0.000000 |
| dense_selected | 27 | 0.019366 | 0.031042 | 1.1558 | 1.0000 | 0.000000 |
| cached_selected | 27 | 0.019374 | 0.029179 | 1.2565 | 1.1026 | 0.143407 |
| triton_selected | 27 | 0.048981 | 0.067899 | 0.4235 | 0.4466 | 0.143411 |

## Per-Case Results

| module | batch | selected rows | runtime | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |
|---|---:|---:|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.k_proj` | 1 | 16 | cached_selected | 0.017523 | 6.2861 | 1.8169 | 0.169634 |
| `model.layers.0.self_attn.k_proj` | 1 | 16 | dense_full | 0.110151 | 1.0000 | 0.2890 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 16 | dense_selected | 0.031837 | 3.4598 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 16 | triton_selected | 0.207108 | 0.5319 | 0.1537 | 0.169634 |
| `model.layers.0.self_attn.k_proj` | 1 | 64 | cached_selected | 0.099880 | 1.1028 | 1.0063 | 0.195754 |
| `model.layers.0.self_attn.k_proj` | 1 | 64 | dense_full | 0.110151 | 1.0000 | 0.9125 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 64 | dense_selected | 0.100514 | 1.0959 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 64 | triton_selected | 0.095422 | 1.1544 | 1.0534 | 0.195754 |
| `model.layers.0.self_attn.k_proj` | 1 | 256 | cached_selected | 0.014969 | 7.3587 | 1.2269 | 0.140651 |
| `model.layers.0.self_attn.k_proj` | 1 | 256 | dense_full | 0.110151 | 1.0000 | 0.1667 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 256 | dense_selected | 0.018366 | 5.9976 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | 256 | triton_selected | 0.049162 | 2.2406 | 0.3736 | 0.140651 |
| `model.layers.0.self_attn.k_proj` | 12 | 16 | cached_selected | 0.027251 | 0.7155 | 0.5648 | 0.130565 |
| `model.layers.0.self_attn.k_proj` | 12 | 16 | dense_full | 0.019498 | 1.0000 | 0.7894 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 16 | dense_selected | 0.015392 | 1.2668 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 16 | triton_selected | 0.053829 | 0.3622 | 0.2859 | 0.130565 |
| `model.layers.0.self_attn.k_proj` | 12 | 64 | cached_selected | 0.012282 | 1.5876 | 1.3974 | 0.164359 |
| `model.layers.0.self_attn.k_proj` | 12 | 64 | dense_full | 0.019498 | 1.0000 | 0.8802 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 64 | dense_selected | 0.017162 | 1.1361 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 64 | triton_selected | 0.054296 | 0.3591 | 0.3161 | 0.164359 |
| `model.layers.0.self_attn.k_proj` | 12 | 256 | cached_selected | 0.032418 | 0.6015 | 1.0273 | 0.153790 |
| `model.layers.0.self_attn.k_proj` | 12 | 256 | dense_full | 0.019498 | 1.0000 | 1.7081 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 256 | dense_selected | 0.033305 | 0.5855 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | 256 | triton_selected | 0.047500 | 0.4105 | 0.7011 | 0.153795 |
| `model.layers.0.self_attn.k_proj` | 64 | 16 | cached_selected | 0.037113 | 0.4966 | 1.1204 | 0.143407 |
| `model.layers.0.self_attn.k_proj` | 64 | 16 | dense_full | 0.018430 | 1.0000 | 2.2563 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 16 | dense_selected | 0.041582 | 0.4432 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 16 | triton_selected | 0.053379 | 0.3453 | 0.7790 | 0.143411 |
| `model.layers.0.self_attn.k_proj` | 64 | 64 | cached_selected | 0.038741 | 0.4757 | 0.8683 | 0.151426 |
| `model.layers.0.self_attn.k_proj` | 64 | 64 | dense_full | 0.018430 | 1.0000 | 1.8253 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 64 | dense_selected | 0.033640 | 0.5478 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 64 | triton_selected | 0.048981 | 0.3763 | 0.6868 | 0.151433 |
| `model.layers.0.self_attn.k_proj` | 64 | 256 | cached_selected | 0.014592 | 1.2630 | 1.2897 | 0.146858 |
| `model.layers.0.self_attn.k_proj` | 64 | 256 | dense_full | 0.018430 | 1.0000 | 1.0212 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 256 | dense_selected | 0.018820 | 0.9793 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | 256 | triton_selected | 0.039351 | 0.4683 | 0.4783 | 0.146858 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | cached_selected | 0.016028 | 1.4152 | 1.1603 | 0.104553 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | dense_full | 0.022682 | 1.0000 | 0.8199 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | dense_selected | 0.018598 | 1.2196 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | triton_selected | 0.050696 | 0.4474 | 0.3668 | 0.104553 |
| `model.layers.0.self_attn.q_proj` | 1 | 64 | cached_selected | 0.012929 | 1.7544 | 1.0342 | 0.182233 |
| `model.layers.0.self_attn.q_proj` | 1 | 64 | dense_full | 0.022682 | 1.0000 | 0.5895 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 64 | dense_selected | 0.013371 | 1.6964 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 64 | triton_selected | 0.063848 | 0.3553 | 0.2094 | 0.182233 |
| `model.layers.0.self_attn.q_proj` | 1 | 256 | cached_selected | 0.018044 | 1.2571 | 0.8816 | 0.143234 |
| `model.layers.0.self_attn.q_proj` | 1 | 256 | dense_full | 0.022682 | 1.0000 | 0.7013 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 256 | dense_selected | 0.015907 | 1.4259 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 256 | triton_selected | 0.168631 | 0.1345 | 0.0943 | 0.143236 |
| `model.layers.0.self_attn.q_proj` | 12 | 16 | cached_selected | 0.062236 | 1.4292 | 1.1782 | 0.150741 |
| `model.layers.0.self_attn.q_proj` | 12 | 16 | dense_full | 0.088947 | 1.0000 | 0.8244 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 16 | dense_selected | 0.073329 | 1.2130 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 16 | triton_selected | 0.096040 | 0.9261 | 0.7635 | 0.150741 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | cached_selected | 0.049951 | 1.7807 | 1.0634 | 0.171355 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | dense_full | 0.088947 | 1.0000 | 0.5972 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | dense_selected | 0.053116 | 1.6746 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | triton_selected | 0.040664 | 2.1874 | 1.3062 | 0.171355 |
| `model.layers.0.self_attn.q_proj` | 12 | 256 | cached_selected | 0.029052 | 3.0617 | 0.6906 | 0.163543 |
| `model.layers.0.self_attn.q_proj` | 12 | 256 | dense_full | 0.088947 | 1.0000 | 0.2256 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 256 | dense_selected | 0.020063 | 4.4333 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 256 | triton_selected | 0.039933 | 2.2274 | 0.5024 | 0.163548 |
| `model.layers.0.self_attn.q_proj` | 64 | 16 | cached_selected | 0.016824 | 1.0136 | 1.2323 | 0.155137 |
| `model.layers.0.self_attn.q_proj` | 64 | 16 | dense_full | 0.017053 | 1.0000 | 1.2158 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 16 | dense_selected | 0.020733 | 0.8225 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 16 | triton_selected | 0.040265 | 0.4235 | 0.5149 | 0.155133 |
| `model.layers.0.self_attn.q_proj` | 64 | 64 | cached_selected | 0.023883 | 0.7140 | 0.7963 | 0.169535 |
| `model.layers.0.self_attn.q_proj` | 64 | 64 | dense_full | 0.017053 | 1.0000 | 1.1153 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 64 | dense_selected | 0.019019 | 0.8966 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 64 | triton_selected | 0.092659 | 0.1840 | 0.2053 | 0.169530 |
| `model.layers.0.self_attn.q_proj` | 64 | 256 | cached_selected | 0.013153 | 1.2965 | 1.0054 | 0.164098 |
| `model.layers.0.self_attn.q_proj` | 64 | 256 | dense_full | 0.017053 | 1.0000 | 0.7755 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 256 | dense_selected | 0.013224 | 1.2896 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | 256 | triton_selected | 0.046313 | 0.3682 | 0.2855 | 0.164098 |
| `model.layers.0.self_attn.v_proj` | 1 | 16 | cached_selected | 0.013129 | 1.2565 | 1.1026 | 0.010827 |
| `model.layers.0.self_attn.v_proj` | 1 | 16 | dense_full | 0.016497 | 1.0000 | 0.8775 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 16 | dense_selected | 0.014477 | 1.1396 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 16 | triton_selected | 0.038343 | 0.4303 | 0.3776 | 0.010827 |
| `model.layers.0.self_attn.v_proj` | 1 | 64 | cached_selected | 0.020115 | 0.8202 | 0.6702 | 0.007681 |
| `model.layers.0.self_attn.v_proj` | 1 | 64 | dense_full | 0.016497 | 1.0000 | 0.8172 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 64 | dense_selected | 0.013481 | 1.2237 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 64 | triton_selected | 0.132026 | 0.1250 | 0.1021 | 0.007681 |
| `model.layers.0.self_attn.v_proj` | 1 | 256 | cached_selected | 0.058381 | 0.2826 | 1.1740 | 0.009140 |
| `model.layers.0.self_attn.v_proj` | 1 | 256 | dense_full | 0.016497 | 1.0000 | 4.1546 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 256 | dense_selected | 0.068539 | 0.2407 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | 256 | triton_selected | 0.038424 | 0.4293 | 1.7838 | 0.009141 |
| `model.layers.0.self_attn.v_proj` | 12 | 16 | cached_selected | 0.019374 | 0.8390 | 1.1230 | 0.007419 |
| `model.layers.0.self_attn.v_proj` | 12 | 16 | dense_full | 0.016255 | 1.0000 | 1.3384 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 16 | dense_selected | 0.021756 | 0.7471 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 16 | triton_selected | 0.038499 | 0.4222 | 0.5651 | 0.007419 |
| `model.layers.0.self_attn.v_proj` | 12 | 64 | cached_selected | 0.013662 | 1.1898 | 1.0294 | 0.008624 |
| `model.layers.0.self_attn.v_proj` | 12 | 64 | dense_full | 0.016255 | 1.0000 | 0.8652 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 64 | dense_selected | 0.014064 | 1.1558 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 64 | triton_selected | 0.133514 | 0.1217 | 0.1053 | 0.008624 |
| `model.layers.0.self_attn.v_proj` | 12 | 256 | cached_selected | 0.074446 | 0.2183 | 1.1651 | 0.008218 |
| `model.layers.0.self_attn.v_proj` | 12 | 256 | dense_full | 0.016255 | 1.0000 | 5.3358 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 256 | dense_selected | 0.086735 | 0.1874 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | 256 | triton_selected | 0.043676 | 0.3722 | 1.9858 | 0.008196 |
| `model.layers.0.self_attn.v_proj` | 64 | 16 | cached_selected | 0.022738 | 1.2118 | 1.2475 | 0.008032 |
| `model.layers.0.self_attn.v_proj` | 64 | 16 | dense_full | 0.027553 | 1.0000 | 1.0295 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 16 | dense_selected | 0.028365 | 0.9714 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 16 | triton_selected | 0.039397 | 0.6994 | 0.7200 | 0.008011 |
| `model.layers.0.self_attn.v_proj` | 64 | 64 | cached_selected | 0.017604 | 1.5651 | 1.1001 | 0.008355 |
| `model.layers.0.self_attn.v_proj` | 64 | 64 | dense_full | 0.027553 | 1.0000 | 0.7029 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 64 | dense_selected | 0.019366 | 1.4227 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 64 | triton_selected | 0.043365 | 0.6354 | 0.4466 | 0.008358 |
| `model.layers.0.self_attn.v_proj` | 64 | 256 | cached_selected | 0.011519 | 2.3920 | 1.1618 | 0.008436 |
| `model.layers.0.self_attn.v_proj` | 64 | 256 | dense_full | 0.027553 | 1.0000 | 0.4857 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 256 | dense_selected | 0.013382 | 2.0589 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | 256 | triton_selected | 0.037950 | 0.7260 | 0.3526 | 0.008436 |

## Interpretation Guardrails

- This benchmark measures selected output rows only; it is a routing/bypass microbenchmark, not full generation throughput.
- `speedup vs dense full` is the system-routing comparison: avoid materializing all rows when only a skill slice is needed.
- `speedup vs dense selected` is the kernel comparison against torch operating on the selected FP16 rows only.
