# Local Qwen2.5-1.5B GPU fake-quant attempt - 2026-07-01

Attempted command: 	imeout 300 env PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 train_python/eval_weight_quant_ppl.py --model Qwen/Qwen2.5-1.5B-Instruct --device cuda --dtype float16 --prompts data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt --limit-prompts 1 --max-length 64 --allocation outputs/qwen25_1p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json --allocation-method loss_sensitive_consensus_4to8 --group-size 128 --reuse-model --out outputs/LOCAL_QWEN25_1P5B_GPU_WIKITEXT2_1_FAKE_QUANT_PPL_2026_07_01.json

Observed result: process exited with code 1 after several minutes and did not produce the requested JSON output in this Codex tool session. No traceback was returned by the captured output. At the time of local testing, the RTX 5070 Laptop GPU had roughly 5.5 GiB already allocated out of 8.1 GiB by other desktop processes.

Claim boundary: this is an environment/capacity attempt log, not a quality result. The 1.5B and 7B CSI/consensus downstream rows should be run on the RTX3090 machine or after freeing local GPU memory.
