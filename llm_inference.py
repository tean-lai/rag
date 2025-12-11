from llama_cpp import Llama


class Inference:
    def __init__(self, model, n_ctx=1024):
        model_path = "./models/" + model
        self.n_ctx = n_ctx
        self.llm = Llama(
            model_path=model_path,
            verbose=False,
            n_batch=1,
            n_ctx=n_ctx,
            n_gpu_layers=-1,
        )

    def query(self, q):
        out = self.llm(q[:self.n_ctx - 4], max_tokens=None)  # arbitrary to leave some space for generation
        out = out["choices"][0]["text"]
        markers = ["TEXT START", "TEXT END", "PROMPT START", "PROMPT END"]
        for m in markers:
            if m in out:
                return out[:out.index(m)]
        return out
