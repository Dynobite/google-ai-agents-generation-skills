## What's in the harness

Concretely, a harness includes:

- Instructions and Rule Files: The text that defines who the agent is, what it cares about, and what it is forbidden from doing. This includes AGENTS.md , CLAUDE.md , GEMINI.md , skill files, and sub-agent prompts.
- Tools: The functions, MCP servers, and APIs the agent can call, plus the prose around them that tells the model when and how to call them.
- Sandboxes and execution environments: Where the agent's code actually runs, what it has access to, what it cannot reach.
- Orchestration logic: Sub-agent spawning, model routing, hand-offs between specialists, and the rules that govern when each one fires.
- Guardrails or Hooks: Deterministic code that runs at specific lifecycle points: before a tool call, after a file edit, before a commit. Hooks are the place for things the agent should never forget but often does.
- Observability: Logs, traces, evaluations, cost and latency metering. Without observability, there is no way to tell whether the agent is doing well or quietly drifting.

If that sounds like a lot of surface area, it is. And it is the team's surface area, not the model provider's.
