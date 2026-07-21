## Automated Metrics

Automated metrics provide speed and reproducibility. They are useful for regression testing and benchmarking outputs. Examples include:

- String-based similarity (ROUGE, BLEU), comparing generated text to references.
- Embedding-based similarity (BERTScore, cosine similarity), measuring semantic closeness.
- Task-specific benchmarks, e.g ., TruthfulQA 2

Metrics are efficient but shallow: they capture surface similarity, not deeper reasoning or user value.
