---
name: Configure MCP Server Connection
description: Use this skill when you need to connect an LLM agent to external tools, databases, or APIs using the Model Context Protocol (MCP).
---

You are an expert at configuring MCP-based agent harnesses. When tasked with connecting an MCP server, follow these steps: 1. Identify the server source (Public Registry, 3P Remote, or Internal Registry). 2. Configure environment variables for authentication (never hardcode credentials). 3. Define the server scope and permissions (prefer read-only mode for production data). 4. If using stdio, ensure the host client launches the server as a local background subprocess. 5. If using SSE, configure the host client to connect to the remote endpoint over HTTP. 6. Validate the connection by running a handshake request to list available tools and verify the output schema.

## Background
- [The Vibe Coder's View of MCP: Discovery, Configuration, & Connection](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/06-the-vibe-coders-view-of-mcp-discovery-configuration-amp-connection.md)
- [Function Calling: Connecting Tools to your Agent](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/17-function-calling-connecting-tools-to-your-agent.md)
- [MCP: One Integration, Every Framework](../../references/google-ai-agents-intensive/day5v3/19-mcp-one-integration-every-framework.md)
