# EigenSkill Model Package Plan

## Skill Adapters

The first deliverable should produce one multi-skill LoRA adapter:

```text
models/eigenskill-smollm2-360m-lora-fp16
```

It covers 8 skills:

```text
intent_routing
json_repair
field_extraction
command_normalization
sensor_event_triage
packet_encode
safety_gate
unit_time_normalize
```

## High-Precision Export Policy

Default:

```text
LoRA adapter + tokenizer
merged FP16 model
```

Optional:

```text
dynamic INT8 CPU export
```

Avoid in v0:

```text
INT4
GPTQ
AWQ
1-bit / 1.58-bit
```

Reason: v0 should preserve skill fidelity and validate the EigenSkill idea
before chasing extreme compression.

