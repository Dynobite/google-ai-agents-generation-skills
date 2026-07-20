---
name: Implement Proactive Memory Retrieval
description: Use this skill when you need to inject user-specific memories into the system instructions at the start of every turn.
---

You are an expert at context engineering. When you need to provide persistent user context, implement a `before_model_callback` in your ADK agent to retrieve and inject memories into the system prompt. Follow this pattern:

```python
def retrieve_memories_callback(callback_context, llm_request):
    user_id = callback_context._invocation_context.user_id
    response = client.agent_engines.memories.retrieve(
        name="projects/.../locations/.../reasoningEngines/...",
        scope={"user_id": user_id}
    )
    memories = [f"* {memory.memory.fact}" for memory in list(response)]
    if memories:
        llm_request.config.system_instruction += "\nHere is information that you have about the user:\n" + "\n".join(memories)

agent = LlmAgent(
    ...,
    before_model_callback=retrieve_memories_callback,
)
```