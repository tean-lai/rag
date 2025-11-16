Made as final project for CS 4414.

To build the project, you need to create a directory `data/`, download the following files and put them in `data/`.

```sh
wget -c https://cornell.box.com/shared/static/ffwnimisulvjyzp1t9u3201uj3p0w3bk.json -O documents.json
wget -c https://cornell.box.com/shared/static/eg115icq6oz2shnq63vzjw3776v30mwy.json -O queries.json
```

```sh
wget -c "https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf/resolve/main/bge-base-en-v1.5-f32.gguf?download=true" -O bge-base-en-v1.5-f32.gguf
```

## Python
```sh
pip install --user faiss-cpu
```
