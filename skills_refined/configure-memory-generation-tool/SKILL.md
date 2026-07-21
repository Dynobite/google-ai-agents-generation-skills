---
name: Configure Memory Generation Tool
description: Use this skill when you need to enable an agent to autonomously decide when to persist meaningful information into long-term memory.
---

You are an expert at building stateful AI agents. When implementing 'Memory-as-a-Tool', create a custom tool that invokes the memory service to extract and consolidate information. Use the following pattern to trigger memory generation asynchronously:

```python
from google.adk.tools import ToolContext

def generate_memories(tool_context: ToolContext):
    # Trigger memory generation in the background
    client.agent_engines.memories.generate(
        name="projects/.../locations/.../reasoningEngines/...",
        direct_contents_source={"events": [{"content": tool_context._invocation_context.user_content}]},
        scope={
            "user_id": tool_context._invocation_context.user_id,
            "app_name": tool_context._invocation_context.app_name
        },
        config={"wait_for_completion": False}
    )
    return {"status": "success"}

# Register this function in your LlmAgent tools list
agent = LlmAgent(..., tools=[generate_memories])
```

## Background
- [Memory: Extraction and Consolidation](https://../../references/google-ai-agents-intensive/2025day3rewritev1contextengineering/25-memory-generation-extraction-and-consolidation.md)
- [Memory-as-a-Tool](https://../../references/google-ai-agents-intensive/2025day3rewritev1contextengineering/32-memory-as-a-tool.md)
- [Background vs. Blocking Operations](https://../../references/google-ai-agents-intensive/2025day3rewritev1contextengineering/33-background-vs-blocking-operations.md)
