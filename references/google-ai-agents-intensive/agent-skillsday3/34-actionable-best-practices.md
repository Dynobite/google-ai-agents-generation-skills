## Actionable Best Practices

- Write Software, Not Rules: Replace negative LLM instructions with deterministic software constraints that make invalid actions impossible.
- Implement Progressive Disclosure: Load complex instructions dynamically only when the skill is explicitly invoked.
- Decouple State: Never use the LLM context window as a database. Pass only URIs or pointers to the subagents via the file system or message bus.
