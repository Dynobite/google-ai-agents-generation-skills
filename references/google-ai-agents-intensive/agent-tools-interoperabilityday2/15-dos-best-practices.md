## Do's (Best Practices) ✅

- Do audit public servers before connection: Always review the code of publicly available, open-source MCP servers before attaching them to an agent that has access to your local file system or credentials.
- Do use RAG for tools: Keep your agent's context window clean. Dynamically load tools from a registry only when needed, and drop them from context when the task is complete to prevent attention dilution.

- Do leverage internal API Gateways and registries: If possible, rely on internal tool registries. This ensures you are consuming approved, governed data schemas rather than reinventing the wheel or running unvetted code.
- Do use the MCP Inspector: When an agent hallucinates a tool call with their arguments, use the MCP Inspector or Chrome DevTools to look at the raw transport data rather than blindly tweaking the agent's system prompt.
- Do include HITL: Show tool inputs to the user before calling the server, to avoid malicious or accidental data exfiltration
- Do auditing needs: Log tool usage for audit purposes
