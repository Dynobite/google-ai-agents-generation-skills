## Timing for retrieval

The final architectural decision for retrieval is when to retrieve memories. One approach is proactive retrieval , where memories are automatically loaded at the start of every turn. This ensures context is always available but introduces unnecessary latency for turns that don't require memory access. Since memories remain static throughout a single turn, they can be efficiently cached to mitigate this performance cost.

For example, you can implement proactive retrieval in ADK using the built-in PreloadMemoryTool or a custom callback 25 :

```
Python # Option 1: Use the built-in PreloadMemoryTool which retrieves memories with similarity search every turn. agent = LlmAgent( ..., tools=[adk.tools.preload_memory_tool.PreloadMemoryTool()] ) # Option 2: Use a custom callback to have more control over how memories are retrieved. def retrieve_memories_callback(callback_context, llm_request): user_id = callback_context._invocation_context.user_id app_name = callback_context._invocation_context.app_name response = client.agent_engines.memories.retrieve( name="projects/.../locations/...reasoningEngines/...", scope={ "user_id": user_id, "app_name": app_name } ) memories = [f"* {memory.memory.fact}" for memory in list(response)] if not memories: # No memories to add to System Instructions. return # Append formatted memories to the System Instructions llm_request.config.system_instruction += "\nHere is information that you have about the user:\n" llm_request.config.system_instruction += "\n".join(memories) agent = LlmAgent( ..., before_model_callback=retrieve_memories_callback, )
```

Snippet 10: Retrieve memories at the start of every turn with ADK using a built-in tool or custom callback

Alternatively, you can use reactive retrieval ('Memory-as-a-Tool') where the agent is given a tool to query its memory, deciding for itself when to retrieve context. This is more efficient and robust but requires an additional LLM call, increasing latency and cost; however, memory is retrieved only when necessary, so the latency cost is incurred less frequently. Additionally, the agent may not know if relevant information exists to be retrieved. However, this can be mitigated by making the agent aware of the types of memories available (e.g., in the tool's description if you're using a custom tool), allowing for a more informed decision on when to query.

```
Python # Option 1: Use the built-in LoadMemory. agent = LlmAgent( ..., tools=[adk.tools.load_memory_tool.LoadMemoryTool()], ) # Option 2: Use a Custom tool where you can describe what type of information # might be available. def load_memory(query: str, tool_context: ToolContext): """Retrieves memories for the user. The following types of information may be stored for the user: * User preferences, like the user's favorite foods. ... """ # Retrieve memories using similarity search. response = tool_context.search_memory(query) return response.memories agent = LlmAgent( ..., tools=[load_memory], )
```

Snippet 11: Configure your ADK agent to decide when memories should be retrieved using a built-in or custom tool
