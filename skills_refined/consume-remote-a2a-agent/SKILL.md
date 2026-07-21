---
name: Consume Remote A2A Agent
description: Use this skill when an agent needs to delegate tasks to a remote, specialized agent via the A2A protocol.
---

You are an expert at hierarchical agent composition. When tasked with consuming a remote agent, follow these steps:

1. Identify the remote agent's `AgentCard` URL.
2. Use the `RemoteA2aAgent` class from the ADK to instantiate a client for the remote agent.
3. Integrate the remote agent into your orchestrator's `sub_agents` list.

```python
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

# Instantiate the remote agent client
prime_agent = RemoteA2aAgent(
    name="prime_agent",
    description="Agent that handles checking if numbers are prime.",
    agent_card="http://localhost:8001/a2a/check_prime_agent/.well-known/agent-card.json"
)

# Use as a sub-agent in a root orchestrator
root_agent = Agent(
    name="root_agent",
    instruction="Delegate prime checking to prime_agent.",
    sub_agents=[prime_agent]
)
```

**Note**: This skill explicitly defines the workflow from the specialized sub-agent's perspective (receiving and returning tasks).

## Background
- [Agent-to-Agent (A2A) Interoperability](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/17-agent-to-agent-a2a-interoperability.md)
- [Connecting Remote A2A Agents](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/26-connecting-remote-a2a-agents.md)
- [A2A - Reusability and Standardization](../../references/google-ai-agents-intensive/2025day5rewritev1prototype/24-a2a-reusability-and-standardization.md)
