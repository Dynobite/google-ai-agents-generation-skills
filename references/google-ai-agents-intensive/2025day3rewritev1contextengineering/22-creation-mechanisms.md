## Creation mechanisms

We can also classify memories by how they were created, including how the information was derived. Explicit memories are created when the user gives a direct command to the agent to remember something (e.g., "Remember my anniversary is October 26th"). On the other hand, implicit memories are created when the agent infers and extracts information from the conversation without a direct command (e.g., 'My anniversary is next week. Can you help me find a gift for my partner?')

Memories can also be distinguished by whether the memory extraction logic is located internally or externally to the agent framework. Internal memory refers to memory management that is built directly into the agent framework. It's convenient for getting started but often lacks advanced features. Internal memory can use external storage, but the mechanism for generating memories is internal to the agent.

External Memory involves using a separate, specialized service dedicated to memory management (e.g., Agent Engine Memory Bank, Mem0, Zep). The agent framework makes API calls to this external service to store, retrieve, and process memories. This approach provides more sophisticated features like semantic search, entity extraction, and automatic summarization, offloading the complex task of memory management to a purpose-built tool.
