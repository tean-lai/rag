import json

import faiss
import numpy as np
from llama_cpp import Llama


def load_embeddings(path):
    with open(path, "r") as f:
        data = json.load(f)
    ids = [entry["id"] for entry in data]
    embeddings = np.array([entry["embedding"] for entry in data])
    print(embeddings.shape)
    return ids, embeddings


def build_index(embeddings, dim=768):
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def test_query(index, query_emb, top_k=5):
    query_emb.reshape(1, 768)
    D, I = index.search(query_emb, top_k)
    print("Distances:", D)
    print("Indices:", I)


def load_model():
    return Llama(
        model_path="./models/bge-base-en-v1.5-f32.gguf",
        verbose=False,
        n_batch=16,
        embedding=True,
    )


if __name__ == "__main__":
    ids, embeddings = load_embeddings("processed.json")
    index = build_index(embeddings, dim=embeddings.shape[1])
    llm = load_model()
    query = "What causes squirrels to lose fur?"
    query_emb = llm.embed(query)
    query_emb = np.array(
        [query_emb], dtype=float
    )  # need to wrap this to get type (1, 768) instead of (767,)
    test_query(index, query_emb, top_k=5)
