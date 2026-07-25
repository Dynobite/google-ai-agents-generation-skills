---
name: Implement Agent Observability via Structured Logging
description: Use this skill when you need to instrument an AI agent to capture its internal 'thought process' for debugging and evaluation.
---

You are an expert at implementing observability for autonomous agents. When tasked with logging agent behavior, follow these steps:

1. Use a structured JSON format for all log entries to ensure they are machine-readable and searchable.
2. Capture the full context of the agent's execution, including: 
   - System instructions and prompt/response pairs.
   - Intermediate reasoning steps (Chain of Thought).
   - Structured tool calls (inputs, outputs, and error states).
   - Changes to the agent's internal state.
3. Implement a logging pattern that records the agent's intent before an action and the outcome after the action.
4. Use the following example as a template for your structured log entries:

```json
{
  "timestamp": "2025-07-10T15:26:13Z",
  "level": "DEBUG",
  "component": "google_adk.models.google_llm",
  "event": "llm_request",
  "model": "gemini-2.0-flash",
  "context": {
    "system_instruction": "...",
    "user_input": "Roll a 6 sided dice",
    "tool_calls": [{"name": "roll_die", "args": {"sides": 6}}],
    "tool_response": {"result": 2}
  }
}
```
5. Configure your logging framework to allow dynamic verbosity levels (e.g., INFO for production, DEBUG for development) without requiring code changes.

## Background
- [Observability: Seeing Inside the Agent's Mind](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/31-observability-seeing-inside-the-agents-mind.md)
- [Debug with OpenTelemetry Traces: Answering "Why?"](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/28-debug-with-opentelemetry-traces-answering-why.md)
- [Observability: Auditing the Agent's Mind (Pillar 6 & 7)](../../references/google-ai-agents-intensive/vibe-coding-agent-security-and-evaluationday4/21-observability-auditing-the-agents-mind-pillar-6-amp-7.md)
