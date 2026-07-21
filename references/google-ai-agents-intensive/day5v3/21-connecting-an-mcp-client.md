## Connecting an MCP Client

```
Python from mcp import ClientSession, StdioServerParameters from mcp.client.stdio import stdio_client server_params = StdioServerParameters( command="python", args=["mcp_server.py"] ) async with stdio_client(server_params) as (read, write): async with ClientSession(read, write) as session: await session.initialize() # List available tools tools = await session.list_tools() print(f"Available: {[t.name for t in tools.tools]}") # Call a tool result = await session.call_tool( "query_knowledge", {"sql": "SELECT * FROM knowledge WHERE tags LIKE '%agent%'"} ) print(result.content[0].text)
```

Snippet 2: mcp\_client.py: This example demonstrates an MCP client connecting to a local server via stdio to discover and call tools.
