---
name: Implement Session Compaction
description: Use this skill when you need to manage long conversation histories in an ADK-based agent to reduce token usage and latency.
---

You are an expert at optimizing LLM context windows. When tasked with managing long conversation histories, implement session compaction using the ADK `EventsCompactionConfig`. This allows the agent to perform LLM-based summarization after a set number of turns. Follow this implementation pattern:

```python
from google.adk.apps import App
from google.adk.apps.app import EventsCompactionConfig

app = App(
    name='your_app_name',
    root_agent=agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=5,
        overlap_size=1,
    ),
)
```

Ensure that expensive operations like recursive summarization are handled asynchronously to avoid blocking the user experience.

## Background
- [Context Engineering: Sessions, Memory](../../references/google-ai-agents-intensive/2025day3rewritev1contextengineering/02-context-engineering-sessions-memory.md)
- [Managing long context conversation: tradeoffs and optimizations](../../references/google-ai-agents-intensive/2025day3rewritev1contextengineering/16-managing-long-context-conversation-tradeoffs-and-optimizations.md)
