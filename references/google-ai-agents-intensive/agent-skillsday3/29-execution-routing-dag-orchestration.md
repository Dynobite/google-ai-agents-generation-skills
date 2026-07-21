## Execution Routing: DAG Orchestration

Early architectures proved brittle and susceptible to compounding errors when early stages hallucinated. The industry solution is Directed Acyclic Graph (DAG) orchestration.

- Decoupled State: State routing in a DAG architecture does not rely on accumulating execution history within the LLM's prompt.
- File Message Bus: The DAG controller orchestrates handoffs by passing structured schema references between subagent nodes.
- Protected Attention: Abstracting the payload from the model's text input prevents context window bloat and preserves the model's capacity.
