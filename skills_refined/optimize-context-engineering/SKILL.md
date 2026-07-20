---
name: Optimize Context Engineering
description: Use this skill when you need to manage token costs and agent performance by balancing static and dynamic context.
---

You are an expert at context engineering. When optimizing an agent's context window, apply these principles:

1. **Static Context (Global)**: Load only essential, high-level information into the system prompt (e.g., `AGENTS.md`, core architectural rules). Keep this minimal to avoid token bloat.
2. **Dynamic Context (On-Demand)**: Use 'Agent Skills' to load procedural knowledge only when the task requires it. 
3. **Tool-Based Retrieval**: Instead of stuffing the context with documentation, provide the agent with a RAG-enabled tool or an MCP server to fetch specific codebase information only when needed.
4. **Model Routing**: Route complex architectural or planning tasks to high-reasoning models, and route routine tasks (e.g., test generation, linting) to smaller, faster, and cheaper models to optimize the token economy.