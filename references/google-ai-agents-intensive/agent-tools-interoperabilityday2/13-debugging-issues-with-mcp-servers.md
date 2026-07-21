## Debugging Issues with MCP Servers

When your agent hallucinates parameters, calls the wrong tool, or fails to parse a payload, don't waste time blindly modifying your system instructions. Debug the transport pipes directly:

- MCP Inspector: A native developer tool that runs a local web panel. It lets you manually query any local or remote MCP server, view the active tool schemas, manually test payload inputs, and inspect the raw JSON-RPC 2.0 packets without initiating your main agent workflow.
- Chrome DevTools: Perfect when running web-based development environments or debugging SSE connections, allowing you to trace incoming web streams and check for server latencies.

<!-- image -->
