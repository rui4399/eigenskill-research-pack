import argparse
import json
import random
from pathlib import Path

from generate_skill_data import (
    GENERATORS,
    SKILLS,
    dumps,
    example,
    full_schema,
    maybe_wrap,
    write_jsonl,
)


UNIT_TIME_KEYS = ["kind", "duration_minutes", "value", "unit", "date", "time"]

CHAT_INTENTS = [
    "陪我聊会儿",
    "你觉得这个想法怎么样",
    "talk to me for a minute",
    "我有点烦，陪我说两句",
    "不用提醒我，就陪我说说话",
    "我现在不想设闹钟，只想聊会儿",
    "别安排任务，陪我放松一下",
    "I just want to chat, no reminder",
]

REMINDER_INTENTS = [
    "明早八点提醒我开会",
    "半小时后叫我喝水",
    "remind me to call mom at 7pm",
    "今晚九点提醒我关灯",
    "明天上午十点提醒我检查训练",
    "二十分钟后提醒我回来",
]

UNIT_TIME_CASES = [
    ("两小时后", {"kind": "duration", "duration_minutes": 120}),
    ("半小时后", {"kind": "duration", "duration_minutes": 30}),
    ("十五分钟后提醒我", {"kind": "duration", "duration_minutes": 15}),
    ("20分钟后", {"kind": "duration", "duration_minutes": 20}),
    ("1.5kg是多少克", {"kind": "unit", "value": 1500, "unit": "g"}),
    ("1.5千克是多少克", {"kind": "unit", "value": 1500, "unit": "g"}),
    ("750克是多少千克", {"kind": "unit", "value": 0.75, "unit": "kg"}),
    ("750g to kg", {"kind": "unit", "value": 0.75, "unit": "kg"}),
    ("3.2公里换成米", {"kind": "unit", "value": 3200, "unit": "m"}),
    ("3.2km是多少米", {"kind": "unit", "value": 3200, "unit": "m"}),
    ("2米是多少厘米", {"kind": "unit", "value": 200, "unit": "cm"}),
    ("2m to cm", {"kind": "unit", "value": 200, "unit": "cm"}),
    ("0.8米换成厘米", {"kind": "unit", "value": 80, "unit": "cm"}),
    ("明天上午九点", {"kind": "datetime", "date": "tomorrow", "time": "09:00"}),
    ("今天下午三点半", {"kind": "datetime", "date": "today", "time": "15:30"}),
    ("后天晚上8点", {"kind": "datetime", "date": "day_after_tomorrow", "time": "20:00"}),
]

STRICT_UNIT_SUFFIXES = [
    "",
    "，只输出JSON",
    "，不要输出单位字符串",
    "，必须给完整JSON对象",
    " please return JSON only",
]


def gen_intent_v2(rng):
    if rng.random() < 0.55:
        text = rng.choice(CHAT_INTENTS)
        label = "chat"
    else:
        text = rng.choice(REMINDER_INTENTS)
        label = "reminder"
    if rng.random() < 0.25:
        text += rng.choice(["，谢谢", "，尽快", "。", " please"])
    return example("intent_routing", text, label)


def gen_unit_v2(rng):
    text, value = rng.choice(UNIT_TIME_CASES)
    if rng.random() < 0.7:
        text = maybe_wrap(text + rng.choice(STRICT_UNIT_SUFFIXES), rng)
    return example("unit_time_normalize", text, full_schema(UNIT_TIME_KEYS, value))


def gen_unit_counterexample(rng):
    text, value = rng.choice(UNIT_TIME_CASES)
    bad = rng.choice(["1500g", "2m", "3200.0imeter", "750 kilograms is equal to 750000 grams", "14:30"])
    prompt = (
        "<skill:unit_time_normalize>\n"
        "You are an EigenSkill micro-kernel for edge inference.\n"
        "Contract: Return one JSON object with all keys: kind,duration_minutes,value,unit,date,time. Use null when absent.\n"
        "Rules: Return exactly one line. No explanation. No extra text. For JSON tasks, output a complete JSON object, never a bare span or markdown.\n"
        f"Bad answer to avoid: {bad}\n"
        f"Input: {text}\n"
        "Output:"
    )
    row = example("unit_time_normalize", text, full_schema(UNIT_TIME_KEYS, value))
    row["prompt"] = prompt
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--train-per-skill", type=int, default=800)
    parser.add_argument("--eval-per-skill", type=int, default=180)
    parser.add_argument("--seed", type=int, default=520)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    train = []
    eval_rows = []
    for skill in SKILLS:
        gen = GENERATORS[skill]
        train_n = args.train_per_skill
        eval_n = args.eval_per_skill
        if skill == "intent_routing":
            for _ in range(train_n):
                train.append(gen_intent_v2(rng) if rng.random() < 0.65 else gen(rng))
            for _ in range(eval_n):
                eval_rows.append(gen_intent_v2(rng))
            continue
        if skill == "unit_time_normalize":
            for _ in range(train_n):
                train.append(gen_unit_counterexample(rng) if rng.random() < 0.35 else gen_unit_v2(rng))
            for _ in range(eval_n):
                eval_rows.append(gen_unit_v2(rng))
            continue
        for _ in range(train_n):
            train.append(gen(rng))
        for _ in range(eval_n):
            eval_rows.append(gen(rng))

    rng.shuffle(train)
    rng.shuffle(eval_rows)

    write_jsonl(out / "train.jsonl", train)
    write_jsonl(out / "eval.jsonl", eval_rows)
    (out / "manifest.json").write_text(
        json.dumps(
            {
                "skills": SKILLS,
                "train_count": len(train),
                "eval_count": len(eval_rows),
                "train_per_skill": args.train_per_skill,
                "eval_per_skill": args.eval_per_skill,
                "seed": args.seed,
                "focus": ["unit_time_normalize", "intent_routing"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {len(train)} train and {len(eval_rows)} eval examples to {out}")


if __name__ == "__main__":
    main()
