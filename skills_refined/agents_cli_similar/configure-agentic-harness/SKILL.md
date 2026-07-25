---
name: Configure Agentic Harness
description: Use this skill when transitioning from ad-hoc vibe coding to production-ready agentic engineering to ensure reliability, security, and observability.
---

You are an expert at building robust AI agent harnesses. When tasked with configuring an agentic harness, implement the following components:

1. **Instructions & Rule Files**: Create a project-specific `AGENTS.md` file. Define the agent's persona, stack, coding conventions, and hard constraints (e.g., 'Never use hard-coded credentials', 'Always use the internal logging library').
2. **Tooling**: Define explicit function signatures and provide prose-based documentation for each tool (e.g., MCP servers) to guide the model on when and how to invoke them.
3. **Sandboxing**: Ensure all code execution occurs within an isolated environment. Configure the sandbox to restrict access to sensitive system files or network endpoints.
4. **Guardrails**: Implement deterministic hooks that run at lifecycle points (e.g., pre-commit hooks to scan for secrets or linting violations).
5. **Observability**: Integrate logging for token usage, latency, and agent trajectory. Ensure every agent action is traceable to facilitate debugging and cost management.

## Background
- [Harness Engineering: What surrounds the model](../../references/google-ai-agents-intensive/day1v3/21-harness-engineering-what-surrounds-the-model.md)
- [Securing a Single Agent: The Trust Trade-Off](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/34-securing-a-single-agent-the-trust-trade-off.md)
- [Observability: Seeing Inside the Agent's Mind](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/31-observability-seeing-inside-the-agents-mind.md)
