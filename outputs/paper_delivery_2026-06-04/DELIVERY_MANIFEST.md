# EigenSkill-Q Delivery Manifest

Date: 2026-06-04

## Included Main Files

```text
EigenSkill-Q_CCF-A_Draft.md
EigenSkill-Q_CCF-A_Draft.docx
EigenSkill-Q_CCF-A_Draft.pdf
EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.md
EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.docx
EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.html
导师速览.md
导师速览.docx
导师速览.pdf
authorization-and-channel-audit.md
authorization-and-channel-audit.docx
notion_ready/EigenSkill-Q_Notion_Page.md
notion_ready/EigenSkill-Q_Notion_Page.docx
notion_ready/EigenSkill-Q_Notion_Page.pdf
```

## Included Evidence Files

```text
../EigenSkill-Q-Cpp-Policy-Bypass-Report.md
../eigenskill_quant_v1_eval_cpp_policy_summary.json
../eigenskill_quant_v1_test_cpp_policy_summary.json
../eigenskill_quant_v1_eval_hybrid_policy_summary.json
../eigenskill_quant_v1_test_hybrid_policy_summary.json
../smollm2_fake_quant_ppl_report.md
../smollm2_fake_quant_ppl_c4_validation_64_report.md
../smollm2_output_sensitivity_proxy_report.md
../smollm2_allocation_swap_search_group128_wikitext2_128_report.md
../smollm2_allocation_swap_search_group128_wikitext2_128_summary.json
../smollm2_fake_quant_ppl_compare_allocations_swap_group128_wikitext2_128_summary.json
../smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
../smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_wikitext2_128_summary.json
../smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_c4_en_validation_64_summary.json
../smollm2_module_output_sensitivity_limit4_group128.json
../smollm2_output_sensitive_alloc_4to8_limit4_group128_summary.json
../../data_eval/eigenskill_quant_v1/audit.json
../../data_eval/text_prompts/c4_en_validation_64.txt
```

## Current Verified Metrics

Python strict oracle:

```text
eval/test exact_json      = 1.0
eval/test decision_exact  = 1.0
eval/test parse_error     = 0.0
```

C++ policy evaluator:

```text
eval/test policy_fields_exact = 1.0
eval/test decision_exact      = 1.0
eval/test parse_error         = 0.0
```

SmolLM2-360M group-wise fake-quant, WikiText2 validation 128 prompts:

```text
FP16                              PPL 17.3436
uniform INT4                      PPL 27.8236
activation-stat RD 4/8            PPL 24.5117
loss-sensitive greedy 4/8         PPL 24.1374
loss-sensitive exact knapsack 4/8 PPL 24.3565
loss-sensitive swap-search 4/8    PPL 24.0661
```

SmolLM2-360M group-wise fake-quant, C4 English validation 64 streamed prompts:

```text
FP16                              PPL 23.7821
uniform INT4                      PPL 36.9390
activation-stat RD 4/8            PPL 33.6940
loss-sensitive greedy 4/8         PPL 32.7675
loss-sensitive exact knapsack 4/8 PPL 32.8657
loss-sensitive swap-search 4/8    PPL 32.5731
```

Output-reconstruction proxy baseline:

```text
allocation bit hist: 4-bit=135, 8-bit=90
protected output proxy: 54.50%
WikiText2-128 PPL: 25.2084
C4-64 PPL:         33.7088
interpretation: improves over uniform INT4 but underperforms measured-loss allocation
```

## Claim Boundary

This package is a short-cycle research draft and stage report. It is not yet a
submission-ready CCF-A paper because real-model quantization baselines and
end-to-end compressed-runtime latency/quality measurements are still missing.
