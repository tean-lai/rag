import json
import cProfile, pstats, io
from pstats import SortKey

import faiss
import numpy as np
from llama_cpp import Llama

from encode import Encoder
from llm_inference import Inference
from vector_db import VectorDB


def augment(prompt, encoder, vector_db):
    emb = encoder.encode(prompt)
    D, I = vector_db.search(emb, 1)
    texts = [vector_db.data[i] for i in I[0]]
    prompt = f"Please answer the following prompt using text if needed. Ignore the text if it's unrelated. End your answer with 'PROMPT END'. TEXT START {' '.join(texts)} TEXT END PROMPT START {prompt} PROMPT END ANSWER START"
    return prompt


if __name__ == "__main__":
    encoder = Encoder()
    vector_db = VectorDB()
    inference = Inference("tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf")
    print("Type 'quit' to quit")
    pr = cProfile.Profile()
    pr.enable()
    while True:
        prompt = input("> ")
        if prompt in ["q", "quit"]:
            break
        prompt = augment(prompt, encoder, vector_db)
        print(inference.query(prompt))
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    