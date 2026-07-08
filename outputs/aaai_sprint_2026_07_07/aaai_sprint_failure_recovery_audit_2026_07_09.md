# AAAI Sprint Failure Recovery Audit

Generated: 2026-07-09

This deployment-audit table marks allocation settings that should be rejected when they collapse relative to INT4/FP16.

| Model | Task | Method | Acc | INT4 | FP16 | Audit |
|---|---|---|---:|---:|---:|---|
| 1p5b | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 0.41 | 0.54 | reject avg3 allocation; prefer INT4 or larger budget |
| 1p5b | mmlu100 | loss_sensitive_4to8 | 0.00 | 0.41 | 0.54 | reject avg3 allocation; prefer INT4 or larger budget |
| 1p5b | gsm8k100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.00 | 0.02 | 0.03 | reject avg3 allocation; prefer INT4 or larger budget |
| 1p5b | gsm8k100 | loss_sensitive_4to8 | 0.02 | 0.02 | 0.03 | allow as non-collapse slice |
| 3b | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.36 | 0.42 | 0.52 | allow as non-collapse slice |
| 3b | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 0.42 | 0.52 | reject avg3 allocation; prefer INT4 or larger budget |
| 3b | mmlu100 | loss_sensitive_4to8 | 0.30 | 0.42 | 0.52 | allow as non-collapse slice |
| 3b | mmlu100 | loss_sensitive_4to8 | 0.04 | 0.42 | 0.52 | reject avg3 allocation; prefer INT4 or larger budget |
| 3b | gsm8k100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.03 | 0.05 | 0.06 | allow as non-collapse slice |
| 3b | gsm8k100 | loss_sensitive_4to8 | 0.02 | 0.05 | 0.06 | reject avg3 allocation; prefer INT4 or larger budget |
| 7b | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.53 | 0.63 | 0.65 | allow as non-collapse slice |
| 7b | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 0.63 | 0.65 | reject avg3 allocation; prefer INT4 or larger budget |
| 7b | mmlu100 | loss_sensitive_4to8 | 0.55 | 0.63 | 0.65 | allow as non-collapse slice |
| 7b | mmlu100 | loss_sensitive_4to8 | 0.00 | 0.63 | 0.65 | reject avg3 allocation; prefer INT4 or larger budget |
| 7b | gsm8k100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.02 | 0.05 | 0.04 | reject avg3 allocation; prefer INT4 or larger budget |
| 7b | gsm8k100 | loss_sensitive_4to8 | 0.03 | 0.05 | 0.04 | allow as non-collapse slice |
| phi3_mini | gsm8k100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.00 | 0.02 | 0.02 | reject avg3 allocation; prefer INT4 or larger budget |
| phi3_mini | gsm8k100 | loss_sensitive_4to8 | 0.00 | 0.02 | 0.02 | reject avg3 allocation; prefer INT4 or larger budget |
| phi3_mini | mmlu100 | loss_sensitive_robust_lcb_consensus_4to8 | 0.08 | 0.42 | 0.41 | reject avg3 allocation; prefer INT4 or larger budget |
| phi3_mini | mmlu100 | loss_sensitive_4to8 | 0.09 | 0.42 | 0.41 | reject avg3 allocation; prefer INT4 or larger budget |
