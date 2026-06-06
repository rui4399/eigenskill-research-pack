import unittest

import measure_esmp_generation_latency as gen


class FakeInputs(dict):
    def to(self, device):
        self["device"] = device
        return self


class FakeTokenizer:
    eos_token_id = 0

    def __init__(self) -> None:
        self.raw_calls = []
        self.chat_calls = []

    def __call__(self, prompt, return_tensors):
        self.raw_calls.append((prompt, return_tensors))
        return FakeInputs({"input_ids": [[1, 2, 3]]})

    def apply_chat_template(self, messages, tokenize, add_generation_prompt, return_tensors):
        self.chat_calls.append((messages, tokenize, add_generation_prompt, return_tensors))
        return FakeInputs({"input_ids": [[4, 5, 6]]})


class FakeBrokenChatTokenizer(FakeTokenizer):
    def apply_chat_template(self, messages, tokenize, add_generation_prompt, return_tensors):
        self.chat_calls.append((messages, tokenize, add_generation_prompt, return_tensors))
        raise ImportError("apply_chat_template requires jinja2>=3.1.0")


class GenerationPromptFormatTests(unittest.TestCase):
    def test_raw_prompt_mode_uses_tokenizer_call(self) -> None:
        tokenizer = FakeTokenizer()
        inputs = gen.build_generation_inputs(tokenizer, "hello", "cuda", use_chat_template=False)
        self.assertEqual(inputs["input_ids"], [[1, 2, 3]])
        self.assertEqual(tokenizer.raw_calls, [("hello", "pt")])
        self.assertEqual(tokenizer.chat_calls, [])
        self.assertEqual(inputs["device"], "cuda")

    def test_chat_template_mode_uses_user_message(self) -> None:
        tokenizer = FakeTokenizer()
        inputs = gen.build_generation_inputs(tokenizer, "hello", "cuda", use_chat_template=True)
        self.assertEqual(inputs["input_ids"], [[4, 5, 6]])
        self.assertEqual(tokenizer.raw_calls, [])
        self.assertEqual(tokenizer.chat_calls[0][0], [{"role": "user", "content": "hello"}])
        self.assertTrue(tokenizer.chat_calls[0][2])
        self.assertEqual(inputs["device"], "cuda")

    def test_chat_template_falls_back_to_chatml_when_jinja_is_unavailable(self) -> None:
        tokenizer = FakeBrokenChatTokenizer()
        inputs = gen.build_generation_inputs(tokenizer, "hello", "cuda", use_chat_template=True)
        self.assertEqual(inputs["input_ids"], [[1, 2, 3]])
        self.assertEqual(len(tokenizer.raw_calls), 1)
        rendered_prompt = tokenizer.raw_calls[0][0]
        self.assertIn("<|im_start|>user", rendered_prompt)
        self.assertIn("hello", rendered_prompt)
        self.assertIn("<|im_start|>assistant", rendered_prompt)
        self.assertEqual(inputs["device"], "cuda")


if __name__ == "__main__":
    unittest.main()
