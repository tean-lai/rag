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
    n_batch=16,
)

# print("hello world")
# documents = documents[:20]
embeddings = []

texts = [doc["text"] for doc in documents]
n = len(documents)
for i, doc in enumerate(documents):
    #     print(doc)
    #     # output = llm(question, max_tokens=32, stop=["Q:"])
    embedding = llm.embed(doc["text"])
    # embeddings.append(embedding)
    # print(embedding)
    doc["embedding"] = embedding
    if i % 10 == 0:
        print(f"progress: {i}/{n}")
print("done")
# print(json.dumps(documents))
with open("processed.json", "w") as f:
    json.dump(documents, f)
