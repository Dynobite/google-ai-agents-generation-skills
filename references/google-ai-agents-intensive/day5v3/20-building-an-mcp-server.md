## Building an MCP Server

Here's a working server in about 40 lines that exposes a SQLite database:

```
Python # mcp_server.py - Exposes a SQLite database via MCP import sqlite3 from mcp.server import Server from mcp.server.stdio import stdio_server from mcp.types import Tool, TextContent server = Server("knowledge-base") db = sqlite3.connect("knowledge.db") @server.list_tools() async def list_tools() -> list[Tool]: return [ Tool( name="query_knowledge", description="Query the knowledge base with SQL", inputSchema={ "type": "object", "properties": { "sql": { "type": "string", "description": "SQL query to execute (SELECT only)" } }, "required": ["sql"] }, ), Tool( name="add_knowledge", description="Add a new knowledge entry", inputSchema={ "type": "object", "properties": { "title": {"type": "string"}, "content": {"type": "string"}, "tags": {"type": "string", "description": Continues next page..
```

```
"Comma-separated tags"} }, "required": ["title", "content"] }, ), ] @server.call_tool() async def call_tool(name: tr, arguments: dict) -> list[TextContent]: if name == "query_knowledge": sql = arguments["sql"] if not sql.strip().upper().startswith("SELECT"): return [TextContent(type="text", text="Error: Only SELECT queries allowed")] cursor = db.execute(sql) rows = cursor.fetchall() columns = [desc[0] for desc in cursor.description] result = [dict(zip(columns, row)) for row in rows] return [TextContent(type="text", text=str(result))] elif name == "add_knowledge": db.execute( "INSERT INTO knowledge (title, content, tags) VALUES (?, ?, ?)", (arguments["title"], arguments["content"], arguments.get("tags", "")) ) db.commit() return [TextContent(type="text", text="Knowledge entry added.")] async def main(): async with stdio_server() as (read, write): init_options = server.create_initialization_options() await server.run(read, write, init_options) if __name__ == "__main__": import asyncio asyncio.run(main())
```

Snippet 1: mcp\_server.py: This snippet implements an MCP server using the Python SDK to expose a SQLite database as a set of tools.
