# EigenSkill / Eigen-Swarm OS 资源索引：100 个相关链接

生成日期：2026-06-01

用途：作为 NotebookLM source，集中索引 EigenSkill、低维技能旁路、端侧小模型、量化、C++ 推理引擎、国产/移动硬件、微控制器、函数调用数据集、跨介质水声通信、机器人对接与安全鉴权等资源。

## 建议阅读顺序

1. 先看 001-020：选择最小可训练模型。
2. 再看 021-045：训练、LoRA、量化、SVD 与低秩压缩。
3. 再看 046-074：C++/端侧推理引擎与硬件后端。
4. 再看 075-088：JSON、工具调用、意图分类、Schema 数据集。
5. 最后看 089-100：水声通信、形态学群体组合、安全与功耗测量。

## A. 超小模型与 on-device 模型

001. HuggingFaceTB/SmolLM2-135M-Instruct  
https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct

002. HuggingFaceTB/SmolLM2-360M-Instruct  
https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct

003. HuggingFaceTB/SmolLM2-1.7B-Instruct  
https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct

004. Hugging Face SmolLM GitHub  
https://github.com/huggingface/smollm

005. SmolTalk / smol-smoltalk SFT dataset  
https://huggingface.co/datasets/HuggingFaceTB/smol-smoltalk

006. Qwen2.5-0.5B-Instruct  
https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

007. Qwen2.5-1.5B-Instruct  
https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct

008. Qwen2.5-Coder-0.5B-Instruct  
https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct

009. Qwen2.5-Coder-1.5B-Instruct  
https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct

010. Qwen2.5 Technical Report  
https://arxiv.org/abs/2412.15115

011. facebook/MobileLLM-125M  
https://huggingface.co/facebook/MobileLLM-125M

012. facebook/MobileLLM-350M  
https://huggingface.co/facebook/MobileLLM-350M

013. MobileLLM GitHub  
https://github.com/facebookresearch/MobileLLM

014. MobileLLM paper  
https://arxiv.org/abs/2402.14905

015. TinyLlama-1.1B-Chat-v1.0  
https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0

016. TinyLlama paper  
https://arxiv.org/abs/2401.02385

017. Llama-3.2-1B-Instruct  
https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

018. Gemma 3 270M  
https://huggingface.co/google/gemma-3-270m

019. LiquidAI/LFM2-350M  
https://huggingface.co/LiquidAI/LFM2-350M

020. Microsoft BitNet b1.58 2B4T  
https://huggingface.co/microsoft/bitnet-b1.58-2B-4T

## B. 训练、LoRA、PEFT 与微调工具链

021. LoRA paper  
https://arxiv.org/abs/2106.09685

022. Hugging Face PEFT docs  
https://huggingface.co/docs/peft

023. Hugging Face PEFT GitHub  
https://github.com/huggingface/peft

024. TRL SFTTrainer docs  
https://huggingface.co/docs/trl/sft_trainer

025. Hugging Face TRL GitHub  
https://github.com/huggingface/trl

026. Unsloth GitHub  
https://github.com/unslothai/unsloth

027. LLaMA-Factory GitHub  
https://github.com/hiyouga/LLaMA-Factory

028. Axolotl GitHub  
https://github.com/axolotl-ai-cloud/axolotl

029. QLoRA paper  
https://arxiv.org/abs/2305.14314

030. bitsandbytes GitHub  
https://github.com/bitsandbytes-foundation/bitsandbytes

031. Hugging Face Transformers  
https://github.com/huggingface/transformers

032. Hugging Face Accelerate  
https://github.com/huggingface/accelerate

033. Hugging Face Datasets  
https://github.com/huggingface/datasets

## C. 量化、BitNet、SVD 与低秩压缩

034. AWQ paper  
https://arxiv.org/abs/2306.00978

035. llm-awq GitHub  
https://github.com/mit-han-lab/llm-awq

036. SmoothQuant paper  
https://arxiv.org/abs/2211.10438

037. SmoothQuant GitHub  
https://github.com/mit-han-lab/smoothquant

038. GPTQ paper  
https://arxiv.org/abs/2210.17323

039. AutoGPTQ GitHub  
https://github.com/AutoGPTQ/AutoGPTQ

040. 1-bit AI Infra / BitNet b1.58 CPU inference  
https://arxiv.org/abs/2410.16144

041. Microsoft BitNet GitHub  
https://github.com/microsoft/BitNet

042. bitnet.cpp paper  
https://arxiv.org/abs/2502.11880

043. Swift-SVD paper  
https://arxiv.org/abs/2604.01609

044. TensorSLM paper  
https://arxiv.org/abs/2506.13514

045. llama.cpp quantization evaluation  
https://arxiv.org/abs/2601.14277

## D. C++ / 端侧 LLM 推理引擎

046. llama.cpp GitHub  
https://github.com/ggml-org/llama.cpp

047. llama.cpp build docs  
https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md

048. GGUF format documentation  
https://github.com/ggml-org/ggml/blob/master/docs/gguf.md

049. Ollama GitHub  
https://github.com/ollama/ollama

050. MLC LLM GitHub  
https://github.com/mlc-ai/mlc-llm

051. MLC LLM docs  
https://llm.mlc.ai/docs/

052. WebLLM GitHub  
https://github.com/mlc-ai/web-llm

053. WebLLM docs  
https://webllm.mlc.ai/docs/

054. ExecuTorch website  
https://executorch.ai/

055. ExecuTorch GitHub  
https://github.com/pytorch/executorch

056. ONNX Runtime GenAI  
https://github.com/microsoft/onnxruntime-genai

057. LiteRT / Google AI Edge  
https://ai.google.dev/edge/litert

058. vLLM GitHub  
https://github.com/vllm-project/vllm

## E. 微控制器、SIMD、NPU 与国产/移动硬件后端

059. TensorFlow Lite Micro GitHub  
https://github.com/tensorflow/tflite-micro

060. TensorFlow Lite Micro paper  
https://arxiv.org/abs/2010.08678

061. CMSIS-NN GitHub  
https://github.com/ARM-software/CMSIS-NN

062. Arm Compute Library GitHub  
https://github.com/ARM-software/ComputeLibrary

063. Arm KleidiAI GitHub  
https://github.com/ARM-software/kleidiai

064. XNNPACK GitHub  
https://github.com/google/XNNPACK

065. Espressif TensorFlow Lite Micro component  
https://components.espressif.com/components/espressif/esp-tflite-micro

066. Espressif ESP-DL  
https://github.com/espressif/esp-dl

067. RKNN Toolkit2  
https://github.com/airockchip/rknn-toolkit2

068. RKNN-LLM  
https://github.com/airockchip/rknn-llm

069. RKNN Model Zoo  
https://github.com/airockchip/rknn_model_zoo

070. RK Platform NPU SDK docs  
https://docs.aim-linux.advantech.com/docs/processors/rockchip/RK3588/Edge_AI_SDK_ASR-A501/edge_ai/edge_ai_wiki_data/RK_Platform_NPU_SDK

071. Qualcomm AI Engine Direct / QNN docs  
https://docs.qualcomm.com/nav/home/onnx_to_qnn_tutorial_linux_host.html?product=1601111740009302

072. Qualcomm on-device generative AI whitepaper  
https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Unlocking-on-device-generative-AI-with-an-NPU-and-heterogeneous-computing.pdf

073. Huawei Ascend CANN documentation  
https://www.hiascend.com/document

074. MindSpore Lite  
https://www.mindspore.cn/lite

## F. JSON、工具调用、意图分类与 Schema 数据集

075. Berkeley Function Calling Leaderboard  
https://gorilla.cs.berkeley.edu/leaderboard

076. BFCL dataset on Hugging Face  
https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard

077. ToolBench GitHub  
https://github.com/OpenBMB/ToolBench

078. API-Bank GitHub  
https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank

079. Glaive function calling v2 dataset  
https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2

080. Salesforce xLAM function calling 60K  
https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k

081. narrative-function-calling-v1  
https://huggingface.co/datasets/narrative-io/narrative-function-calling-v1

082. Schema-Guided Dialogue GitHub  
https://github.com/google-research-datasets/dstc8-schema-guided-dialogue

083. GEM schema_guided_dialog dataset  
https://huggingface.co/datasets/GEM/schema_guided_dialog

084. CLINC OOS / CLINC150 dataset  
https://github.com/clinc/oos-eval

085. Banking77 dataset  
https://huggingface.co/datasets/PolyAI/banking77

086. MASSIVE intent dataset  
https://huggingface.co/datasets/AmazonScience/massive

087. Gorilla OpenFunctions dataset  
https://huggingface.co/datasets/gorilla-llm/gorilla_openfunctions_v1

088. lm-evaluation-harness  
https://github.com/EleutherAI/lm-evaluation-harness

## G. 跨介质通信、形态学组合、安全与功耗测量

089. WHOI Micro-Modem  
https://acomms.whoi.edu/micro-modem

090. WHOI Acoustic Communications Group  
https://acomms.whoi.edu/

091. EvoLogics MINI 48/78 acoustic modem  
https://www.evologics.com/acoustic-modem/48-78/m-serie

092. TUHH AHOI acoustic modem  
https://www.tuhh.de/acps/research/acoustic-modem

093. AHOI underwater acoustic modem hardware  
https://www.labmaker.org/products/ahoi-underwater-acoustic-modem

094. Event-Based Stack for Underwater Multimodal Networks  
https://arxiv.org/abs/2103.01711

095. Compressed Underwater Acoustic Communications  
https://arxiv.org/abs/1911.04072

096. Electromagnetic terminal phase navigation for AUV docking  
https://arxiv.org/abs/2311.13078

097. RFC 8439: ChaCha20 and Poly1305 for IETF Protocols  
https://www.rfc-editor.org/rfc/rfc8439

098. libsodium authenticated encryption docs  
https://doc.libsodium.org/secret-key_cryptography/aead/chacha20-poly1305

099. Nordic Power Profiler Kit II  
https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2

100. Joulescope JS220 precision energy analyzer  
https://www.joulescope.com/products/js220-joulescope-precision-energy-analyzer

## H. 视频与教程发现入口

这些不是计入 100 个核心链接的独立 sources，而是后续找视频时最有用的检索入口：

- llama.cpp GGUF tutorial  
  https://www.youtube.com/results?search_query=llama.cpp+GGUF+tutorial

- MLC LLM / WebLLM tutorial  
  https://www.youtube.com/results?search_query=MLC+LLM+WebLLM+tutorial

- RK3588 NPU LLM / RKNN tutorial  
  https://www.youtube.com/results?search_query=RK3588+NPU+LLM+RKNN+tutorial

- TensorFlow Lite Micro ESP32-S3 tutorial  
  https://www.youtube.com/results?search_query=TensorFlow+Lite+Micro+ESP32-S3+tutorial

- AWQ / GPTQ / SmoothQuant tutorial  
  https://www.youtube.com/results?search_query=LLM+quantization+AWQ+GPTQ+SmoothQuant+tutorial

- Underwater acoustic modem tutorial  
  https://www.youtube.com/results?search_query=underwater+acoustic+modem+tutorial

