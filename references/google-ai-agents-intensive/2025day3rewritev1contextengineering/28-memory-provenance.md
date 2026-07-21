## Memory Provenance

The classic machine learning axiom of "garbage in, garbage out" is even more critical for LLMs, where the outcome is often "garbage in, confident garbage out." For an agent to make reliable decisions and for a memory manager to effectively consolidate memories, they must be able to critically evaluate the quality of its own memories. This trustworthiness is derived directly from a memory's provenance -a detailed record of its origin and history.

Figure 7: The flow of information between data sources and memories. A single memory can be derived from multiple data sources, and a single data source may contribute to multiple memories.

<!-- image -->

The process of memory consolidation -merging information from multiple sources into a single, evolving memory-creates the need to track its lineage. As shown in the diagram above, a single memory might be a blend of multiple data sources, and a single source might be segmented into multiple memories.

To assess trustworthiness, the agent must track key details for each source, such as its origin (source type) and age ('freshness'). These details are critical for two reasons: they dictate the weight each source has during memory consolidation, and they inform how much the agent should rely on that memory during inference.

The source type is one of the most important factors in determining trust. Data sources fall into three main categories:

- Bootstrapped Data: Information pre-loaded from internal systems, such as a CRM. This high-trust data can be used to initialize a user's memories to address the cold-start problem, which is the challenge of providing a personalized experience to a user the agent has never interacted with before.
- User Input: This includes data provided explicitly (e.g., via a form, which is high-trust) or information extracted implicitly from a conversation (which is generally less trustworthy).
- Tool Output: Data returned from an external tool call. Generating memories from Tool Output is generally discouraged because these memories tend to be brittle and stale, making this source type better suited for short-term caching.
