import json

import faiss
import numpy as np
from llama_cpp import Llama

from encode import Encoder
from llm_inference import Inference
from vector_db import VectorDB


def augment(prompt, encoder, vector_db):
    emb = encoder.encode(prompt)
    D, I = vector_db.search(emb, 3)
    texts = [vector_db.data[i] for i in I[0]]
    prompt = f"Please answer the following prompt using text if needed. Ignore the text if it's unrelated. TEXT START {' '.join(texts)} TEXT END PROMPT START {prompt} PROMPT END ANSWER START"
    return prompt


if __name__ == "__main__":
    encoder = Encoder()
    vector_db = VectorDB()
    inference = Inference()
    print("Press ctrl+c to exit")
    while True:
        prompt = input("> ")
        prompt = augment(prompt, encoder, vector_db)
        print(inference.query(prompt))

    # print(inference.query(prompt))
