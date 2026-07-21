## Variance across frameworks and models

While the core ideas are similar, different agent frameworks implement sessions, events, and state in distinct ways. Agent frameworks are responsible for maintaining the conversation history and state for LLMs, building LLM requests using this context, and parsing and storing the LLM response.

Agent frameworks act as a universal translator between your code and a LLM. While you, the developer, work with the framework's consistent, internal data structures for each conversational turn, the framework handles the critical task of converting those structures into the precise format the LLM requires. This abstraction is powerful because it decouples your agent's logic from the specific LLM you're using, preventing vendor lock-in. With the release of ADK 2.0 , this framework moves toward a graph-based logic paradigm, allowing developers to define clear, reliable execution flows for how multiple agents work together to solve complex, multi-step problems.

Figure 2: Flow of context management for agents

<!-- image -->

Ultimately, the goal is to produce a "request" that the LLM can understand. For Google's Gemini models, this is a List[Content] . Each Content object is a simple dictionary-like structure containing two keys: role which defines who is speaking ("user" or "model") and parts which defines the actual content of the message (text, images, tool calls, etc.).

The framework automatically handles mapping the data from its internal object (e.g., an ADK Event ) to the corresponding role and parts in the Content object before making the API call. In essence, the framework provides a stable, internal API for the developer, while managing the complex and varied external APIs of the different LLMs behind the scenes.

ADK 2.0 utilizes an explicit, graph-compatible Session object that contains a list of Event objects and a separate state object. The Session is like a filing cabinet, with one folder for the conversation history (events) and another for working memory (state).

LangGraph doesn't have a formal "session" object. Instead, the state is the session. This allencompassing state object holds the conversation history (as a list of Message objects) and all other working data. Unlike the append-only log of a traditional session, LangGraph's state is mutable. It can be transformed, and strategies like history compaction can alter the record. This is useful for managing long conversations and token limits.
