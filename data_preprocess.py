import json

from llama_cpp import Llama

documents = json.load(open("data/documents.json"))

# TODO: make sure that to remove duplicate urls from embeddings

llm = Llama(
    model_path="./models/bge-base-en-v1.5-f32.gguf",
    # n_gpu_layers=-1,
    # seed=1337,
    # n_ctx=2048,  #uncomment to increase context window
    verbose=False,
    embedding=True,
    n_batch=64,
    n_threads=8,
    n_gpu_layers=-1,
)

embeddings = []

texts = [doc["text"] for doc in documents]
n = len(documents)
for i, doc in enumerate(documents):
    embedding = llm.embed(doc["text"])
    doc["embedding"] = embedding
    if i % 100 == 0:
        print(f"Progress: {i}/{n}")

with open("processed.json", "w") as f:
    json.dump(documents, f)
