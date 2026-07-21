## Wait but how does a Skill differ from MCP and AGENTS.md?

To establish the architectural fit of Agent Skills, it helps to map these primitives.

Skill vs. MCP . These do not compete, they compose. Model Context Protocol is about reach: an MCP server connects the agent to an external system (Drive, Salesforce, BigQuery, or an internal API). A Skill is about know-how: it teaches the agent how to think about a particular kind of work. When a Skill needs data, it tells the agent to call a tool, typically one provided by an MCP server.

Skill vs. AGENTS.md . From one side AGENTS.md is always loaded within the project; Skills load on demand. The cleanest setups use both. Keep AGENTS.md tight (project conventions, stack, build commands, etc.) and if needed use it also as a router into the Skills library, with a short catalog at the bottom that tells the agent what's available.
