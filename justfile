setup:
    source .venv/bin/activate
    pip install llama-cpp-python
    pip install faiss-cpu

preprocess:
    source .venv/bin/activate
    python3 ./data_preprocess.py 2>/dev/null
