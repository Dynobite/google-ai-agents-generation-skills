## Accounting for memory lineage during memory management

This dynamic, multi-source approach to memory creates two primary operational challenges when managing memories: conflict resolution and deleting derived data .

Memory consolidation inevitably leads to conflicts where one data source conflicts with another. A memory's provenance allows the memory manager to establish a hierarchy of trust for its information sources. When memories from different sources contradict each other, the agent must use this hierarchy in a conflict resolution strategy. Common strategies include prioritizing the most trusted source, favoring the most recent information, or looking for corroboration across multiple data points.

Another challenge to managing memories occurs when deleting memories. A memory can be derived from multiple data sources. When a user revokes access to one data source, data derived from that source should also be removed. Deleting every memory "touched" by that source can be overly aggressive. A more precise, though computationally expensive, approach is to regenerate the affected memories from scratch using only the remaining, valid sources.

Beyond static provenance details, confidence in a memory must evolve. Confidence increases through corroboration, such as when multiple trusted sources provide consistent information. However, an efficient memory system must also actively curate its existing knowledge through memory pruning-a process that identifies and "forgets" memories that are no longer useful. This pruning can be triggered by several factors.

- Time-based Decay: The importance of a memory can decrease over time. A memory about a meeting from two years ago is likely less relevant than one from last week.
- Low Confidence: A memory that was created from a weak inference and was never corroborated by other sources may be pruned.
- Irrelevance: As an agent gains a more sophisticated understanding of a user, it might determine that some older, trivial memories are no longer relevant to the user's current goals.

By combining a reactive consolidation pipeline with proactive pruning, the memory manager ensures that the agent's knowledge base is not just a growing log of everything ever said. Instead, it's a curated, accurate, and relevant understanding of the user.
