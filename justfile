setup:
    source .venv/bin/activate
    pip install llama-cpp-python
    pip install faiss-cpu
    pip install tqdm

step1:
    source .venv/bin/activate
    python3 data_preprocess.py 2>/dev/null

step2:
    source .venv/bin/activate
    python3 vector_db.py 2>/dev/null
