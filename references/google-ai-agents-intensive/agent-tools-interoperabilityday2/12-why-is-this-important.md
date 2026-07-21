## Why is this important?

By standardizing tool definitions, you connect standard transports directly into your agent's Harness without writing integration code:

- stdio (Standard Input/Output): Most often used with Local and Prototyping efforts. Your coding agent can run without a complex network connection setup, as it treats the tool as a local process. The host client launches the MCP server as a local background subprocess, passing JSON-RPC 2.0 messages over stdin and stdout.
- SSE (Server-Sent Events) over HTTP: The host client (could be Local or a deployed agentic application) connects to a remote MCP endpoint over standard web protocols, streaming data to the agent in real-time. This has many advantages over the studio approach, fewer dependencies, always up to date, smaller footprint, and simpler lifecycle, but is a higher burden on the cloud hosted MCP server.

Both options enable the vibecoders to adopt the platform without multiple custom integration layers.
