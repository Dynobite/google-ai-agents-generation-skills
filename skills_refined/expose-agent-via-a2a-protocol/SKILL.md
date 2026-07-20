---
name: Expose Agent via A2A Protocol
description: Use this skill when you need to make an existing agent discoverable and interoperable within a multi-agent ecosystem using the A2A protocol.
---

You are an expert at agent interoperability. When tasked with exposing an agent for A2A communication, follow these steps using the Agent Development Kit (ADK):

1. Import the `to_a2a` utility from the ADK.
2. Wrap your existing `Agent` instance with `to_a2a` to generate the necessary A2A interface.
3. Serve the resulting application using a production-ready server like `uvicorn` or the Agent Engine.

```python
from google.adk.a2a.utils.agent_to_a2a import to_a2a

# Your existing agent instance
root_agent = Agent(
    name='hello_world_agent',
    # ... your agent configuration ...
)

# Make it A2A-compatible
a2a_app = to_a2a(root_agent, port=8001)

# Serve with uvicorn
# uvicorn agent:a2a_app --host localhost --port 8001
```