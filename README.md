Made as final project for CS 4414.

To build the project, you need to create a directory `data/`, download the following files and put them in `data/`.

```sh
wget -c https://cornell.box.com/shared/static/ffwnimisulvjyzp1t9u3201uj3p0w3bk.json -O documents.json
wget -c https://cornell.box.com/shared/static/eg115icq6oz2shnq63vzjw3776v30mwy.json -O queries.json
```

Also need to create `model/` and put this here.
```sh
wget -c "https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf/resolve/main/bge-base-en-v1.5-f32.gguf?download=true" -O bge-base-en-v1.5-f32.gguf
```

Your file tree should include the following:
.
├── README.md
├── data
│   ├── documents.json
│   └── queries.json
├── data_preprocess.py
├── justfile
├── models
│   └── bge-base-en-v1.5-f32.gguf
└── vector_db.py

## Running
We depend on python packages `faiss-cpu` and `llama-cpu-python`.

If you have the cli tool `just` installed, you can just run `just step1` and `just step2` to run either steps.

Otherwise, just look at the `justfile` to see what commands you need to run.
