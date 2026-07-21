---
name: dispatch-remote-a2a-agent
description: Orchestrator logic for delegating tasks to A2A agents.
---

You are an expert at implementing Agent-to-Agent (A2A) protocols. When orchestrating remote agents, follow these steps: 1. For direct integration, instantiate the agent using the remote endpoint: `billing_specialist = RemoteA2aAgent(name="billing_agent", endpoint="https://api.vendor.com/v1/billing/a2a")`. 2. For registry-based discovery, use the Agent Registry: `registry = AgentRegistry(project_id=project_id, location=location); my_remote_agent = registry.get_remote_a2a_agent(agent_name=agent_name)`. 3. Ensure the orchestrator handles the multi-turn state by allowing the remote agent to pause, negotiate, and resume execution.

**Note**: This skill explicitly defines the workflow from the orchestrator's perspective (dispatching tasks).

## Background
- [Agent-to-Agent (A2A) Interoperability](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/17-agent-to-agent-a2a-interoperability.md)
- [Connecting Remote A2A Agents](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/26-connecting-remote-a2a-agents.md)
- [A2A Protocol: From Concept to Implementation](../../references/google-ai-agents-intensive/2025day5rewritev1prototype/25-a2a-protocol-from-concept-to-implementation.md)
