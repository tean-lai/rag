import numpy as np
from llama_cpp import llama

import vector_db


class Encoder:
    def __init__(self):
        self.llm = llama.Llama(
            model_path="./models/bge-base-en-v1.5-f32.gguf",
            verbose=False,
            n_batch=16,
            embedding=True,
        )

    def encode(self, query):
        emb = self.llm.embed(query)
        emb = np.array([emb], dtype=float)
        assert emb.shape == (1, 768)
        return emb
