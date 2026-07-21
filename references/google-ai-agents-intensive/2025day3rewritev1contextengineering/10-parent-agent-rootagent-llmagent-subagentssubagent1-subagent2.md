# Parent agent. root_agent = LlmAgent( ..., sub_agents=[sub_agent_1, sub_agent_2] )

```

Snippet 2: A2A communication across multiple agent frameworks

In the separate, individual histories model , each agent maintains its own private conversation history and functions like a black box to other agents. All internal processessuch as intermediary thoughts, tool use, and reasoning steps-are kept within the agent's private log and are not visible to others. Communication occurs only through explicit messages, where an agent shares its final output, not its process.

This interaction is typically implemented by either implementing Agent-as-a-tool or using the Agent-to-Agent (A2A) Protocol. With Agent-as a-Tool , one agent invokes another as if it were a standard tool, passing inputs and receiving a final, self-contained output 6 . With the Agentto-Agent (A2A) Protocol , agents use a structured protocol for direct messaging 7 .

We'll explore the A2A protocol in more detail in the next session.
