

= CS 4414 Hw 3 Part 3 Report
Tean Lai

== Intro
This document is a performance analysis of my implementation of Hw 3.


== Evaluation
I use the Python library `cProfile` to measure the performance of the system. It tracks time spent in each function call, as well as the number of times each function was called.

I do not profile the setup of the encoder model, vector database, and inference model because those are one-time costs that are likely amortized away.

Experiments are run on an 14" Macbook Pro with 16GB of unified RAM. Background apps are not closed while running, which may decrease the amount fo effective RAM.

The prompts used were:
+ "What do squirrels like to eat?"
+ "I want to smoke some marijuana, want to join me?"
+ "Tell me about the cost of living in Massachusetts."

These prompts were selected because there are related sentences in the documents.

Results can be reproduced by running the file `evaluation.py`. Profile results are dumped in `artifacts/`. The functions `encode`, `search`, and `query` corresponds to encode step, vector database search step, and llm generation step respectively.


#let results = csv("data.csv")
#figure(
    table(
    columns: 6,
    inset: 9pt,
    align: horizon,
    table.header(
        
    ),
    ..results.flatten()
    ),
    caption:"Experimental results"
) <tab>



== Analysis
@tab shows the results of the experiments. I varied top_k, models used, as well as index type for the vector search part.

It seems the inference time completely dominates the run-time, vector search and encoding time is relatively trivial. However, even changing top_k does not have much of an impact on performance.

It seems often a top_k of 1 has poor inference performance, I thikn it's likely that the answer just becomes too long becaues it's not coherent enough to terminate.

It's possible the number of documents is not high enough for searching to be a bottleneck.

The best place to optimize is likely by batching up prompts for inference.

== Optimizing inference

As said before, the best place to optimize here is with inference. One way to do that is buy utilizing more GPU layers.

I did a change where instead I intialize the LLM with `n_gpu_layers = -1`, and inference speed improved. @tab2 shows some of these results.

#figure(
    table(
    columns: 3,
    inset: 9pt,
    align: horizon,
    table.header(
        [model], [top_k], [inference_time]
    ),
    [qwen], [7], [7.481],
    [qwen], [15], [11.718],
    [qwen], [31], [15.690],
    [tinyllm], [63], [25.031],
    ),
    caption:"Some results with inference optimization"
) <tab2>