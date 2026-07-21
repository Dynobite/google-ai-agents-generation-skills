## Memory

Memory and Sessions share a deeply symbiotic relationship: sessions are the primary data source for generating memories, and memories are a key strategy for managing the size of a session. A memory is a snapshot of extracted, meaningful information from a conversation or data source. It's a condensed representation that preserves important context, making it useful for future interactions. Generally, memories are persisted across sessions to provide a continuous and personalized experience.

As a specialized, decoupled service, a ' memory manager ' provides the foundation for multiagent interoperability. Memory managers frequently use framework-agnostic data structures, like simple strings and dictionaries. This allows agents built on different frameworks to connect to a single memory store, enabling the creation of a shared knowledge base that any connected agent can utilize.

Note: some frameworks may also refer to Sessions or verbatim conversation as 'short-term memory.' For this whitepaper, memories are defined as extracted information, not the raw dialogue of turn-by-turn conversation.

Storing and retrieving memories is crucial for building sophisticated and intelligent agents. A robust memory system transforms a basic chatbot into a truly intelligent agent by unlocking several key capabilities:

- Personalization: The most common use case is to remember user preferences, facts, and past interactions to tailor future responses. For example, remembering a user's favorite sports team or their preferred seat on an airplane creates a more helpful and personal experience.

- Context Window Management: As conversations become longer, the full history can exceed an LLM's context window. Memory systems can compact this history by creating summaries or extracting key facts, preserving context without sending thousands of tokens in every turn. This reduces both cost and latency.
- Data Mining and Insight: By analyzing stored memories across many users (in an aggregated, privacy-preserving way), you can extract insights from the noise. For example, a retail chatbot might identify that many users are asking about the return policy for a specific product, flagging a potential issue.
- Agent Self-Improvement and Adaptation: The agent learns from previous runs by creating procedural memories about its own performance-recording which strategies, tools, or reasoning paths led to successful outcomes. This enables the agent to build a playbook of effective solutions, allowing it to adapt and improve its problem-solving over time.

Creating, storing, and utilizing memory in an AI system is a collaborative process. Each component in the stack-from the end-user to the developer's code-has a distinct role to play.

1.  The User: Provides the raw source data for memories. In some systems, users may provide memories directly (i.e. via a form).
2. The Agent (Developer Logic): Configures how to decide what and when to remember, orchestrating calls to the memory manager. In simple architectures, the developer can implement the logic such that memory is *always* retrieved and *always* triggered-to-begenerated. In more advanced architectures, the developer may implement memory-as-atool, where the agent (via LLM) decides when memory should be retrieved or generated.

3.  The Agent Framework (e.g., ADK, LangGraph): Provides the structure and tools for memory interaction. The framework acts as the plumbing. It defines how the developer's logic can access conversation history and interact with the memory manager, but it doesn't manage the long-term storage itself. It also defines how to stuff retrieved memories into the context window.
4. The Session Storage (i.e. Agent Engine Sessions, Spanner, Redis): Stores the turnby-turn conversation of the Session. The raw dialogue will be ingested into the memory manager in order to generate memories.
5.  The Memory Manager (e.g. Agent Engine Memory Bank, Mem0, Zep): Handles the storage, retrieval, and compaction of memories. The mechanisms to store and retrieve memories depend on what provider is used. This is the specialized service or component that takes the potential memory identified by the agent and handles its entire lifecycle.
- Extraction distills the key information from the source data.
- Consolidation curates memories to merge duplicative entities.
- Storage persists the memory to persistent databases.
- Retrieval fetches relevant memories to provide context for new interactions

Figure 5: The flow of information between sessions, memory, and external knowledge

<!-- image -->

The division of responsibilities ensures that the developer can focus on the agent's unique logic without having to build the complex underlying infrastructure for memory persistence and management. It is important to recognize that a memory manager is an active system, not just a passive vector database. While it uses similarity search for retrieval, its core value lies in its ability to intelligently extract, consolidate, and curate memories over time. Managed memory services, like Agent Engine Memory Bank, handle the entire lifecycle of memory generation and storage, freeing you to focus on your agent's core logic.

This retrieval capability is also why memory is frequently compared to another key architectural pattern: Retrieval-Augmented Generation (RAG). However, they are built on different architectural principles, as RAG handles static, external data while Memory curates dynamic, user-specific context. They fulfill two distinct and complementary roles: RAG makes an agent an expert on facts, while memory makes it an expert on the user. The following chart breaks down their high-level differences:

Table 1: Comparison of RAG engines and memory managers

|                  | RAG Engines                                                                                                                                    | Memory Managers                                                                                                                                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary Goal     | To inject external, factual knowledge into the context                                                                                         | To create a personalized and stateful experience. The agent remembers facts, adapts to the user over time, and maintains long-running context.                                                                                             |
| Data source      | A static, pre-indexed external knowledge base (e.g., PDFs, wikis, documents, APIs).                                                            | The dialogue between the user and agent.                                                                                                                                                                                                   |
| Isolation Level  | Generally Shared . The knowledge base is typically a global, read-only resource accessible by all users to ensure consistent, factual answers. | Highly Isolated: Memory is almost always scoped per-user to prevent data leaks.                                                                                                                                                            |
| Information type | Static, factual, and authoritative. Often contains domain-specific data, product details, or technical documentation.                          | Dynamic and (generally) user-specific. Memories are derived from conversation, so there's an inherent level of uncertainty.                                                                                                                |
| Write patterns   | Batch processing Triggered via an offline, administrative action.                                                                              | Event-based processing Triggered at some cadence (i.e. every turn or at the end of a session) or Memory-as-a-tool (agent decides to generate memories).                                                                                    |
| Read patterns    | RAG data is almost always retrieved ' as- a-tool '. It's retrieved when the agent decides that the user's query requires external information. | There are two common read patterns: • Memory-as-a-tool: Retrieved when the user's query requires additional information about the user (or some other identity). • Static retrieval: Memory is always retrieved at the start of each turn. |
| Data Format      | A natural-language 'chunk'.                                                                                                                    | A natural language snippet or a structured profile.                                                                                                                                                                                        |
| Data preparation | Chunking and Indexing: Source documents are broken into smalvler Chunks, which are then converted to embeddings and stored for fast lookup.    | Extraction and consolidation: Extract key details from the conversation, ensuring content is not duplicative or contradictory.                                                                                                             |

A helpful way to understand the difference is to think of RAG as the agent's research librarian and a memory manager as its personal assistant.

The research librarian ( RAG ) works in a vast public library filled with encyclopedias, textbooks, and official documents. When the agent needs an established fact-like a product's technical specifications or a historical date-it consults the librarian. The librarian retrieves information from this static, shared, and authoritative knowledge base to provide consistent, factual answers. The librarian is an expert on the world's facts, but they don't know anything personal about the user asking the question.

In contrast, the personal assistant ( memory ) follows the agent and carries a private notebook, recording the details of every interaction with a specific user. This notebook is dynamic and highly isolated, containing personal preferences, past conversations, and evolving goals. When the agent needs to recall a user's favorite sports team or the context of last week's project discussion, it turns to the assistant. The assistant's expertise is not in global facts, but in the user themselves.

Ultimately, a truly intelligent agent needs both. RAG provides it with expert knowledge of the world, while memory provides it with an expert understanding of the user it's serving.

The next section deconstructs the concept of memory by examining its core components: the types of information it stores, the patterns for its organization, the mechanisms for its storage and creation, the strategic definition of its scope, and its handling of multimodal versus textual data.
