## Registry Architectures: When and How to Build Them

Why do some organizations build registries while others don't need them? The answer lies in scale and complexity. When you have fifty tools, manual configuration works fine. But when you reach five thousand tools distributed across different teams and environments, you face a discovery problem that demands a systematic solution.

To solve these discovery and governance challenges at scale, the Gemini Enterprise Agent Platform provides a native Agent Registry. This centralized catalog allows teams to discover, track, and manage all agents, tools, and MCP servers across the organization. Paired with Agent Identity-which assigns a unique cryptographic ID to every agent-it enables robust governance and secure access control out of the box. However, if you are building outside of this integrated ecosystem, understanding the underlying registry architecture remains critical.

A Tool Registry uses a protocol like MCP to catalog all assets, from functions to APIs. Instead of giving agents access to thousands of tools, you create curated lists, leading to three common patterns:

- Generalist agents: Access the full catalog, trading speed and accuracy for scope.
- Specialist agents: Use predefined subsets for higher performance.
- Dynamic agents: Query the registry at runtime to adapt to new tools.

The primary benefit is human discovery-developers can search for existing tools before building duplicates, security teams can audit tool access, and product owners can understand their agents' capabilities.

An Agent Registry applies the same concept to agents, using formats like A2A's AgentCards. It helps teams discover and reuse existing agents, reducing redundant work. This also lays the groundwork for automated agent-to-agent delegation, though this remains an emerging pattern.

Registries offer discovery and governance at the cost of maintenance. You can consider starting without one and only build it when your ecosystem's scale demands centralized management!
