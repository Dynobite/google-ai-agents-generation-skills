---
name: Implement Multi-Agent Coordinator Pattern
description: Use this skill when designing a complex system that requires delegating sub-tasks to specialized agents.
---

You are an expert at multi-agent architecture. When building a collaborative system, follow the Coordinator pattern:

1. **Coordinator Agent**: Define a manager agent responsible for decomposing the primary mission into discrete sub-tasks.
2. **Specialist Agents**: Create specialized agents (e.g., Researcher, Writer, Coder) with narrow scopes and specific toolsets.
3. **Task Delegation**: Use an A2A (Agent-to-Agent) protocol to send task requests from the Coordinator to Specialists.
4. **Aggregation**: Configure the Coordinator to collect streaming updates or final results from Specialists to synthesize the final response.
5. **Discovery**: Use an Agent Registry to allow the Coordinator to discover available Specialists and their capabilities via Agent Cards.