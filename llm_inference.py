from llama_cpp import Llama


class Inference:
    def __init__(self):
        self.llm = Llama(
            model_path="./models/qwen2-7b-instruct-q4_0.gguf",
            verbose=False,
            n_batch=16,
        )

    def query(self, q):
        out = self.llm(q, max_tokens=None)
        out = out["choices"][0]["text"]
        return out
