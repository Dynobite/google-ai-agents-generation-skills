## Storage architectures

Additionally, the storage architecture is a critical decision that determines how quickly and intelligently an agent can retrieve memories. The choice of architecture defines whether the agent excels at finding conceptually similar ideas, understanding structured relationships, or both.

Memories are generally stored in vector databases and/or knowledge graphs . Vector databases help find memories that are conceptually similar to the query. Knowledge graphs store memories as a network of entities and their relationships.

Vector databases are the most common approach, enabling retrieval based on semantic similarity rather than exact keywords. Memories are converted into embedding vectors, and the database finds the closest conceptual matches to a user's query. This excels at retrieving unstructured, natural language memories where context and meaning are key (i.e. ' atomic facts ' 14 ).

Knowledge graphs are used to store  memories as a network of entities (nodes) and their relationships (edges). Retrieval involves traversing this graph to find direct and indirect connections, allowing the agent to reason about how different facts are linked. It is ideal for structured, relational queries and understanding complex connections within the data (i.e. ' knowledge triples ' 15 ).

You can also combine both methods into a hybrid approach by enriching a knowledge graph's structured entities with vector embeddings. This enables the system to perform both relational and semantic searches simultaneously. This provides the structured reasoning of a graph and the nuanced, conceptual search of a vector database, offering the best of both worlds.
