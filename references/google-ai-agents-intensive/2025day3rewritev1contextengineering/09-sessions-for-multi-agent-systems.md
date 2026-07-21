## Sessions for multi-agent systems

In a multi-agent system, multiple agents collaborate. Each agent focuses on a smaller, specialized task. For these agents to work together effectively, they must share information. As shown in the diagram below, the system's architecture defines the communication patterns they use to share information. A central component of this architecture is how the system handles session history-the persistent log of all interactions. To support these collaborative behaviors in production, the Agent Runtime has been re-engineered to support long-running, multi-day operations (up to 7 days). This allows agents to pause, wait for external triggers (such as webhooks or human approval), and resume execution autonomously without losing context or session state.

Figure 3: Different multi-agent architectural patterns 30

<!-- image -->

Before exploring the architectural patterns for managing this history, it's crucial to distinguish it from the context sent to an LLM. Think of the session history as the permanent, unabridged transcript of the entire conversation. The context, on the other hand, is the carefully crafted information payload sent to the LLM for a single turn. An agent might construct this context by selecting only a relevant excerpt from the history or by adding special formatting, like a guiding preamble, to steer the model's response. This section focuses on what information is passed across agents, not necessarily what context is sent to the LLM.

Agent frameworks handle session history for multi-agent systems using one of two primary approaches: a shared, unified history where all agents contribute to a single log, or separate, individual histories where each agent maintains its own perspective 4 . The choice between these two patterns depends on the nature of the task and the desired collaboration style between the agents.

For the shared, unified history model, all agents in the system read from and write all events to the same, single conversation history. Every agent's message, tool call, and observation is appended to one central log in chronological order. This approach is best for tightly coupled, collaborative tasks requiring a single source of truth, such as a multi-step problem-solving process where one agent's output is the direct input for the next. Even with a shared history, a sub-agent might process the log before passing it to the LLM. For instance, it could filter for a subset of relevant events or add labels to identify which agent generated each event.

If you use ADK 's LLM-driven delegation to handoff to sub-agents, all of the intermediary events of the sub-agent would be written to the same session as the root agent 5 :

```
Python from google.adk.agents import LlmAgent # The sub-agent has access to Session and writes events to it. sub_agent_1 = LlmAgent(...) # Optionally, the sub-agent can save the final response text (or structured output) to the specified state key. sub_agent_2 = LlmAgent( ..., output_key="..." ) Continues next page...
```

```
