# Loss-Sensitive Exact Knapsack Allocation

Source: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n16_seed1_sensitivity_2to4_budget3.json`
Base bits: `2`
High bits: `4`
Budget average bits: `4.0`
Solver: `exact_knapsack_dp`
Scaled unit: `256` parameters

## Results

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.5000 | {'2': 197} | 0.0000 |
| loss_sensitive_exact_knapsack_4to8 | 3.4217 | 0.8554 | {'4': 124, '2': 73} | 1.0000 |

## Interpretation

This allocation solves the measured-sensitivity 0/1 knapsack exactly
after integer scaling of module parameter costs. It is a policy
allocation artifact, not a production quantized runtime.
