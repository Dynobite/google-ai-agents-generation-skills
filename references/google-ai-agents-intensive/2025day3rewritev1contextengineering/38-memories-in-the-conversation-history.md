## Memories in the Conversation History

In this approach, retrieved memories are injected directly into the turn-by-turn dialogue. Memories can either be placed before the full conversation history or right before the latest user query.

However, this method can be noisy, increasing token costs and potentially confusing the model if the retrieved memories are irrelevant. Its primary risk is dialogue injection , where the model might mistakenly treat a memory as something that was actually said in the conversation. You also need to be more careful about the perspective of the memories that you're injecting into the conversation; for example, if you're using the 'user' role and userlevel memories, memories should be written in first-person point of view.

A special case of injecting memories into the conversation history is retrieving memories via tool calls. The memories will be included directly in the conversation as part of the tool output.

```
Python def load_memory(query: str, tool_context: ToolContext): """Loads memories into the conversation history...""" response = tool_context.search_memory(query) return response.memories agent = LlmAgent( ..., tools=[load_memory], )
```

S nippet 13: Retrieve memories as a tool, which directly inserts memories into the conversation
