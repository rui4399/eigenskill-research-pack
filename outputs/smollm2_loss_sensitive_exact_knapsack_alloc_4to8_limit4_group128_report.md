# Loss-Sensitive Exact Knapsack Allocation

Source: `outputs\smollm2_module_loss_sensitivity_limit4_group128.json`
Base bits: `4`
High bits: `8`
Budget average bits: `4.5`
Solver: `exact_knapsack_dp`
Scaled unit: `61440` parameters

## Results

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_exact_knapsack_4to8 | 4.4993 | 0.9998 | {'4': 175, '8': 50} | 0.5787 |

## Interpretation

This allocation solves the measured-sensitivity 0/1 knapsack exactly
after integer scaling of module parameter costs. It is a policy
allocation artifact, not a production quantized runtime.
