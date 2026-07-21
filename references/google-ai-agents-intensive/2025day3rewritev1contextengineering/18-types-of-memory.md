## Types of memory

An agent's memory can be categorized by how the information is stored and how it was captured. These different types of memory work together to create a rich, contextual understanding of a user and their needs. Across all types of memories, the rule stands that memories are descriptive, not predictive.

A 'memory' is an atomic piece of context that is returned by the memory manager and used by the agent as context. While the exact schema can vary, a single memory generally consists of two main components: content and metadata .

Content is the substance of the memory that was extracted from the source data (i.e. the raw dialogue of the session). Crucially, the content is designed to be framework-agnostic, using simple data structures that any agent can easily ingest. The content can either be structured or unstructured data. Structured memories include information typically stored in universal formats like a dictionary or JSON. Its schema is typically defined by the developer, not a specific framework. For example, {'seat\_preference': 'Window'} . Unstructured memories are natural language descriptions that capture the essence of a longer interaction, event, or topic. For example, 'The user prefers a window seat.'

Metadata provides context about the memory, typically stored as a simple string. This can include a unique identifier for the memory, identifiers for the 'owner' of the memory, and labels describing the content or data source of the memory.
