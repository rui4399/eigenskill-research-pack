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

Qwen2.5-1.5B group-wise fake-quant, 64/128 prompt slices:

```text
WikiText2-64:
FP16                         PPL 12.8516
uniform INT4                 PPL 17.2441
loss-sensitive 2p 4/8        PPL 16.1788
loss-sensitive 8p 4/8        PPL 15.7520
consensus 4/8                PPL 15.7966

C4-64:
FP16                         PPL 18.1669
uniform INT4                 PPL 23.9949
loss-sensitive 2p 4/8        PPL 23.2682
loss-sensitive 8p 4/8        PPL 22.3620
consensus 4/8                PPL 22.4891

WikiText2-128:
FP16                         PPL 13.1290
uniform INT4                 PPL 17.4996
loss-sensitive 2p 4/8        PPL 16.6503
loss-sensitive 8p 4/8        PPL 16.0781
consensus 4/8                PPL 16.1356
```

C++ low-bit kernel API:

```text
PackedLowBitMatrix supports signed row-scaled 2..8-bit storage.
PackedMixedBitMatrix supports per-row mixed 2..8-bit storage.
INT3, INT4, mixed-bit, selected-row, and scalar bypass checks pass in quant_kernel_verify.
WSL/CMake/g++ 11.4 build and CTest pass.
Naive scalar bit-unpack is slower than AVX2 FP32 GEMV; no low-bit speed claim.
Mixed-bit selected-row GEMV is faster than scalar dense in 7/9 local benchmark cases,
with best speedup 17.53x at d=2048 active_rows=16 and exact agreement with the
corresponding mixed full-output rows.
```

Qwen2.5-1.5B budget-matched baseline sanity slice:

```text
WikiText2-16:
FP16                         PPL 10.76298
uniform INT4                 PPL 15.04498
loss-sensitive 4/8           PPL 13.13882
random budget-matched 4/8    PPL 14.18543
category heuristic budget    PPL 14.43989

GPU guard:
peak memory                  4634 / 8151 MiB = 56.85%
max utilization              62%
killed_by_guard              false
```

## Claim Boundary

This package is a short-cycle research draft and stage report. It is not yet a
submission-ready CCF-A paper because real-model quantization baselines and
end-to-end compressed-runtime latency/quality measurements are still missing.
