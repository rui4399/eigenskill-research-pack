# Proxy-Augmented Rowguard Selector

Date: `2026-06-06T01:43:31+00:00`
Proxy weight: `0.25`

The augmented score combines multi-split prompt robustness with normalized hidden/logit/KV drift. Lower proxy drift is better.

## Recommendations

- `best_overall`: `baseline_layers17`, augmented score `0.8718`, proxy penalty `0.0000`, min exact `0.9167`
- `best_rowguard`: `g0_1_2_4_5_6_7`, augmented score `0.6027`, proxy penalty `0.6176`, min exact `0.7500`
- `stable_rowguard`: none

## Ranking

| rank | label | family | augmented | prompt score | proxy penalty | min exact | exact span | final hidden | logits | KV mean | KV max |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | baseline_layers17 | baseline | 0.8718 | 0.8290 | 0.0000 | 0.9167 | 0.0833 | 0.003705 | 0.003827 | 0.007135 | 0.013254 |
| 2 | full_v8 | full_precision_probe | 0.7923 | 0.7661 | 0.1293 | 0.8333 | 0.1667 | 0.005322 | 0.006759 | 0.009603 | 0.019436 |
| 3 | g0_1_2_4_5_6_7 | rowguard | 0.6027 | 0.6761 | 0.6176 | 0.7500 | 0.2500 | 0.009189 | 0.015244 | 0.021926 | 0.093375 |
| 4 | g0_1_2_4_5_6 | rowguard | 0.5337 | 0.6818 | 0.9106 | 0.7500 | 0.0833 | 0.011246 | 0.020944 | 0.029307 | 0.137661 |
| 5 | g0_2_3_4_5_6 | rowguard | 0.3985 | 0.5201 | 0.9665 | 0.5000 | 0.4167 | 0.011301 | 0.018647 | 0.033858 | 0.164967 |

## Interpretation

- This is a diagnostic selector, not final proof of quality.
- Proxy drift strongly separates the stable baseline/full-V8 probes from the rowguard candidates in this slice.
- Rowguards remain candidates for larger-suite testing only if their worst-split exact rate and proxy drift both improve.
