import json
import cProfile, pstats, io
from pstats import SortKey
from pathlib import Path

import faiss
import numpy as np
from llama_cpp import Llama

from encode import Encoder
from llm_inference import Inference
from vector_db import VectorDB

TEST_PARAMS = {
    "top_k": [1, 3],
    "inference_models": [
        "tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf",
        "qwen2-7b-instruct-q4_0.gguf",
    ],
    "ivf": [False, True],
}

TEST_PARAMS = {
    "top_k": [1, 3, 7, 15, 31, 63],
    "inference_models": [
        "qwen2-7b-instruct-q4_0.gguf",
        "tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf",
        "bge-base-en-v1.5-f32.gguf",
    ],
    "ivf": [False, True],
}


TEST_PROMPTS = [
    "What do squirrels like to eat?",
    "I want to smoke some marijuana, want to join me?",
    "Tell me about the cost of living in Massachusetts.",
]

def augment(prompt, encoder, vector_db, top_k):
    emb = encoder.encode(prompt)
    D, I = vector_db.search(emb, top_k)
    texts = [vector_db.data[i] for i in I[0]]
    prompt = f"Please answer the following prompt using text if needed. Ignore the text if it's unrelated. End your answer with 'PROMPT END'. TEXT START {' '.join(texts)} TEXT END PROMPT START {prompt} PROMPT END ANSWER START"
    return prompt


if __name__ == "__main__":
    encoder = Encoder()
    
    for inference_model in TEST_PARAMS["inference_models"]:
        inference = Inference(inference_model)
        for ivf in TEST_PARAMS["ivf"]:
            vector_db = VectorDB(ivf)
        
            for top_k in TEST_PARAMS["top_k"]:

                file_name = "artifact3/" + "-".join([inference_model, str(ivf), str(top_k)])
                pr = cProfile.Profile()
                if Path.exists(file_name): continue
                try:
                    pr.enable()
                    for prompt in TEST_PROMPTS:
                        prompt = augment(prompt, encoder, vector_db, top_k)
                        inference.query(prompt)
                            # print(Error)
                            # print("error with + " "-".join([inference_model, str(ivf), str(top_k), str(vector_search_batch)]))
                    pr.disable()
                    s = io.StringIO()
                    sortby = SortKey.CUMULATIVE
                    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
                    ps.print_stats()
                    with open(file_name, "w") as fout:
                        fout.write(s.getvalue())
                except Exception as e:
                    print("something wrong happened with " + file_name)
                    print(" ", e)
                    pr.disable()
    

    