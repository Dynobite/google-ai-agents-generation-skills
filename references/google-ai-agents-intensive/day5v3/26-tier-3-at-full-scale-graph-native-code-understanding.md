## Tier 3 at Full Scale: Graph-Native Code Understanding

Custom Code Review Runtime (Tier 3) stretches further than a single ADK agent reading diffs. The same architecture supports the heavier components a serious reviewer needs on a hundred-million-line legacy codebase - a graph database holding the code's structure, a vector store for semantic retrieval, a sub-agent pipeline for decomposition. Loading code as flat text into a context window runs out of room at that scale, and standard RAG strips out the structure that makes code legible: a class belongs to a file, a function call traces to a requirements doc written a decade ago. Flatten that into a vector store and the map is gone.

Figure 1: Example of a Custom Code Review Runtime Architecture

<!-- image -->

The pattern that has emerged on the largest legacy modernisations is to build the agent on a knowledge graph. Ingest code, docs, tickets, and design PDFs into a graph database (e.g. Spanner Graph 11 ), then let agents combine three retrieval modes: graph traversal (GQL) for structural queries ("every function that transitively calls payment.process()"), vector search

(ANN over node embeddings) for semantic queries ("find code that does what this paragraph describes"), and full-text search for exact identifier matches. The combination answers "what breaks if I change this?" with a precise impact map instead of a confident guess.

The second half is decomposition. A single agent told to "refactor this module" will fail. Split the same job across an ADK 12  sub-agent pipeline - a Search agent that explores the graph, a Story agent that captures requirements, an Impact agent that predicts side-effects, a Taskbreakdown agent that produces atomic units of work, and only then a Coding agent - and the work becomes manageable. Pilots in production on million-line codebases have moved equivalent refactor work from two weeks to a few hours. This is Tier 3 at full scale: not an agent that watches PRs, but one that understands the system the PRs live in.

A Managed Code Review Runtime (Tier 1) gets you a generic reviewer in minutes. A Hybrid Code Review Runtime gets you your reviewer in a day, where the Custom Code Review Runtime (Tier 3) gets you a reviewer that understands the whole system - at the cost of owning the runtime, and the evaluation. Pick the lowest tier that catches what matters.
