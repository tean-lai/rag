Made as final project for CS 4414.

To build the project, you need to create a directory `data/`, download the following files and put them in `data/`.

```sh
wget -c https://cornell.box.com/shared/static/ffwnimisulvjyzp1t9u3201uj3p0w3bk.json -O documents.json
wget -c https://cornell.box.com/shared/static/eg115icq6oz2shnq63vzjw3776v30mwy.json -O queries.json
```

Also need to create `model/` and include the following models.
```sh
wget -c "https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf/resolve/main/bge-base-en-v1.5-f32.gguf?download=true" -O bge-base-en-v1.5-f32.gguf
wget "https://huggingface.co/Qwen/Qwen2-7B-Instruct-GGUF/resolve/main/qwen2-7b-instruct-q4_0.gguf"      -O qwen2-7b-instruct-q4_0.gguf
```

We also depend on python packages `faiss-cpu` and `llama-cpu-python`.


## Preprocess code by

```sh
python3 data_preprocess.py 2>/dev/null
```

## File tree
Your file tree should include the following:
├── README.md
├── data
│   ├── documents.json
│   └── queries.json
├── data_preprocess.py
├── encode.py
├── llm_inference.py
├── main.py
├── models
│   ├── bge-base-en-v1.5-f32.gguf
│   ├── qwen2-7b-instruct-q4_0.gguf
├── processed.json
└── vector_db.py


## Running ChatGPT wannabe
```sh
python3 main.py
```
