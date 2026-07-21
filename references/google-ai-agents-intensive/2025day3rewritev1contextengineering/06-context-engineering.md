## Context Engineering

LLMs are inherently stateless. Outside of their training data, their reasoning and awareness are confined to the information provided within the "context window" of a single API call. This presents a fundamental problem, as AI agents must be equipped with operating instructions identifying what actions can be taken, the evidential and factual data to reason over, and the immediate conversational information that defines the current task. To build stateful, intelligent agents that can remember, learn, and personalize interactions, developers must construct this context for every turn of a conversation. This dynamic assembly and management of information for an LLM is known as Context Engineering.

Context Engineering represents an evolution from traditional Prompt Engineering . Prompt engineering focuses on crafting optimal, often static, system instructions. Conversely, Context Engineering addresses the entire payload, dynamically constructing a state-aware prompt based on the user, conversation history, and external data. It involves strategically selecting, summarizing, and injecting different types of information to maximize relevance while minimizing noise. External systems-such as RAG databases, session stores, and memory managers-manage much of this context. The agent framework must orchestrate these systems to retrieve and assemble context into the final prompt.

Think of Context Engineering as the mise en place for an agent-the crucial step where a chef gathers and prepares all their ingredients before cooking. If you only give a chef the recipe (the prompt), they might produce an okay meal with whatever random ingredients they have. However, if you first ensure they have all the right, high-quality ingredients, specialized tools, and a clear understanding of the presentation style, they can reliably produce an excellent, customized result. The goal of context engineering is to ensure the model has no more and no less than the most relevant information to complete its task.

Context Engineering governs the assembly of a complex payload that can include a variety of components:

- Context to guide reasoning defines the agent's fundamental reasoning patterns and available actions, dictating its behavior:
- System Instructions: High-level directives defining the agent's persona, capabilities, and constraints.
- Tool Definitions: Schemas for APIs or functions the agent can use to interact with the outside world.
- Few-Shot Examples: Curated examples that guide the model's reasoning process via in-context learning.
- Evidential &amp; Factual Data is the substantive data the agent reasons over, including preexisting knowledge and dynamically retrieved information for the specific task; it serves as the 'evidence' for the agent's response:
-  Long-Term Memory: Persisted knowledge about the user or topic, gathered across multiple sessions.
- External Knowledge: Information retrieved from databases or documents, often using Retrieval-Augmented Generation (RAG) 1 .
- Tool Outputs: The data or results returned by a tool.
- Sub-Agent Outputs: The conclusions or results returned by specialized agents that have been delegated a specific sub-task.

- Artifacts: Non-textual data (e.g., files, images) associated with the user or session.
- Immediate conversational information grounds the agent in the current interaction, defining the immediate task:
- Conversation History: The turn-by-turn record of the current interaction.
- State / Scratchpad: Temporary, in-progress information or calculations the agent uses for its immediate reasoning process.
- User's Prompt: The immediate query to be addressed.

The dynamic construction of context is critical. Memories, for instance, are not static; they must be selectively retrieved and updated as the user interacts with the agent or new data is ingested. Additionally, effective reasoning often relies on in-context learning 2  (a process where the LLM learns how to perform tasks from demonstrations in the prompt). In-context learning can be more effective when the agent uses few-shot examples that are releva nt to the current task, rather than relying on hardcoded ones. Similarly, external knowledge is retrieved by RAG tools based on the user's immediate query.

One of the most critical challenges in building a context-aware agent is managing an ever-growing conversation history. In theory, models with large context windows can handle extensive transcripts; in practice, as the context grows, cost and latency increase. Additionally, models can suffer from " context rot ," a phenomenon where their ability to pay attention to critical information diminishes as context grows. Context Engineering directly addresses this by employing strategies to dynamically mutate the history-such as summarization, selective pruning, or other compaction techniques-to preserve vital information while managing the overall token count, ultimately leading to more robust and personalized AI experiences.

This practice manifests as a continuous cycle within the agent's operational loop for each turn of a conversation:

Figure 1. Flow of context management for agents

<!-- image -->

1.  Fetch Context: The agent begins by retrieving context-such as user memories, RAG documents, and recent conversation events. For dynamic context retrieval, the agent will use the user query and other metadata to identify what information to retrieve.
2. Prepare Context: The agent framework dynamically constructs the full prompt for the LLM call. Although individual API calls may be asynchronous, preparing the context is a blocking, "hot-path" process. The agent cannot proceed until the context is ready.
3.  Invoke LLM and Tools: The agent iteratively calls the LLM and any necessary tools until a final response for the user is generated. Tool and model output is appended to the context.

4. Upload Context: New information gathered during the turn is uploaded to persistent storage. This is often a "background" process, allowing the agent to complete execution while memory consolidation or other post-processing occurs asynchronously.

At the heart of this lifecycle are two fundamental components: sessions and memory . A session manages the turn-by-turn state of a single conversation. Memory , in contrast, provides the mechanism for long-term persistence, capturing and consolidating key information across multiple sessions.

You can think of a session as the workbench or desk you're using for a specific project. While you're working, it's covered in all the necessary tools, notes, and reference materials. Everything is immediately accessible but also temporary and specific to the task at hand. Once the project is finished, you don't just shove the entire messy desk into storage. Instead, you begin the process of creating memory, which is like an organized filing cabinet. You review the materials on the desk, discard the rough drafts and redundant notes, and file away only the most critical, finalized documents into labeled folders. This ensures the filing cabinet remains a clean, reliable, and efficient source of truth for all future projects, without being cluttered by the transient chaos of the workbench. This analogy directly mirrors how an effective agent operates: the session serves as the temporary workbench for a single conversation, while the agent's memory is the meticulously organized filing cabinet, allowing it to recall key information during future interactions.

Building on this high-level overview of context engineering, we can now explore two core components: sessions and memory, beginning with sessions.
