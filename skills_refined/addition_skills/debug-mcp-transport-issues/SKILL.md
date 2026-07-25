---
name: Debug MCP Transport Issues
description: Use this skill when an agent hallucinates tool parameters, fails to parse payloads, or experiences connection errors with an MCP server.
---

You are an expert at debugging MCP transport layers. When an MCP integration fails, follow these steps: 1. Do not modify system prompts; instead, inspect the transport pipes. 2. Use the 'MCP Inspector' to manually query the server, view active tool schemas, and test payload inputs. 3. If running in a web-based environment, use Chrome DevTools to trace incoming SSE streams and check for server latencies. 4. Verify the raw JSON-RPC 2.0 packets to ensure the client and server are communicating correctly.

## Background
- [Debugging Issues with MCP Servers](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/13-debugging-issues-with-mcp-servers.md)
- [Observability: Seeing Inside the Agent's Mind](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/31-observability-seeing-inside-the-agents-mind.md)
- [Debug with OpenTelemetry Traces: Answering "Why?"](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/28-debug-with-opentelemetry-traces-answering-why.md)
