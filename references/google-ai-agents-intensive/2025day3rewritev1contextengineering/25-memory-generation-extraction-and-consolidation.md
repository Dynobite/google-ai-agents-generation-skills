## Memory Generation: Extraction and Consolidation

Memory generation autonomously transforms raw conversational data into structured, meaningful insights, functioning. Think of it as an LLM-driven ETL (Extract, Transform, Load) pipeline designed to extract and condense memories. Memory generation's ETL pipeline distinguishes memory managers from RAG engines and traditional databases.

Rather than requiring developers to manually specify database operations, a memory manager uses an LLM to intelligently decide when to add, update, or merge memories. This automation is a memory manager's core strength; it abstracts away the complexity of managing the database contents, chaining together LLM calls, and deploying background services for data processing.

Figure 6: High-level algorithm of memory generation which extracts memories from new data sources and consolidates them with existing memories

<!-- image -->

While the specific algorithms vary by platform (e.g., Agent Engine Memory Bank, Mem0, Zep), the high-level process of memory generation generally follows these four stages:

1.  Ingestion: The process begins when the client provides a source of raw data, typically a conversation history, to the memory manager.
2. Extraction &amp; Filtering: The memory manager uses an LLM to extract meaningful content from the source data. The key is that this LLM doesn't extract everything; it only captures information that fits a predefined topic definition . If the ingested data contains no information that matches these topics, no memory is created.
3.  Consolidation: This is the most sophisticated stage, where the memory manager handles conflict resolution and deduplication. It performs a "self-editing" process, using an LLM to compare the newly extracted information with existing memories. To ensure the user's knowledge base remains coherent, accurate, and evolves over time based on new information, the manager can decide to:
-  Merge the new insight into an existing memory.

- Delete an existing memory if it's now invalidated.
- Create an entirely new memory if the topic is novel.
4. Storage: Finally, the new or updated memory is persisted to a durable storage layer (such as a vector database or knowledge graph) so it can be retrieved in future interactions.

A managed memory manager, like Agent Engine Memory Bank, fully automates this pipeline. They provide a single, coherent system for turning conversational noise into structured knowledge, allowing developers to focus on agent logic rather than building and maintaining the underlying data infrastructure themselves. For example, triggering memory generation with Memory Bank only requires a simple API call 17 :

```
Python from google.cloud import vertexai client = vertexai.Client(project=..., location=...) client.agent_engines.memories.generate( name="projects/.../locations/...reasoningEngines/...", scope={"user_id": "123"}, direct_contents_source={ "events": [...] }, config={ # Run memory generation in the background. "wait_for_completion": False } }
```

Snippet 6: Generate memories with Agent Engine Memory Bank

The process of memory generation can be compared to the work of a diligent gardener tending to a garden. Extraction is like receiving new seeds and saplings (new information from a conversation). The gardener doesn't just throw them randomly onto the plot. Instead, they perform Consolidation by pulling out weeds (deleting redundant or conflicting data), pruning back overgrown branches to improve the health of existing plants (refining and summarizing existing memories), and then carefully planting the new saplings in the optimal location. This constant, thoughtful curation ensures the garden remains healthy, organized, and continues to flourish over time, rather than becoming an overgrown, unusable mess. This asynchronous process happens in the background, ensuring the garden is always ready for the next visit.

Now, let's dive into the two key steps of memory generation: extraction and consolidation.
