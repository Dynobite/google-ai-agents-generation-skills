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

## Background
- [Level 3: The Collaborative Multi-Agent System](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/10-level-3-the-collaborative-multi-agent-system.md)
- [Multi-Agent Systems and Design Patterns](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/22-multi-agent-systems-and-design-patterns.md)
- [Agent-to-Agent (A2A) Interoperability](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/17-agent-to-agent-a2a-interoperability.md)
