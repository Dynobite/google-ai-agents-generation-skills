---
name: Configure Agent Tracing with OpenTelemetry
description: Use this skill when you need to connect individual logs into a coherent, end-to-end execution narrative for an agent.
---

You are an expert at distributed tracing for AI agents. When tasked with implementing tracing, follow these steps:

1. Adopt the OpenTelemetry standard to ensure compatibility with modern observability backends.
2. Define 'Spans' for every discrete operation, such as `llm_call` and `tool_execution`.
3. Attach rich metadata (Attributes) to each span, including `prompt_id`, `latency_ms`, `token_count`, and `user_id`.
4. Ensure context propagation by using a unique `trace_id` across all spans in a single task execution.
5. Use the following structure to define your trace spans:

```python
# Example of wrapping a tool call in a span
with tracer.start_as_current_span("tool_execution") as span:
    span.set_attribute("tool.name", "get_weather")
    span.set_attribute("tool.latency_ms", duration)
    result = execute_tool(tool_name, args)
    span.set_attribute("tool.status", "success")
```
6. Ensure your backend (e.g., Google Cloud Trace) is configured to assemble these spans into a visual graph to identify the causal chain of failures.

### Additional Guidelines (from Instrument Agent Observability)

You are an expert at Agent Ops. When instrumenting your agent, follow these steps:

1. **Trace Generation**: Ensure every step of the 'Think-Act-Observe' loop is recorded as an OpenTelemetry trace.
2. **Data Capture**: Include the following in each trace:
   - The raw prompt sent to the model.
   - The model's internal reasoning (chain-of-thought).
   - The specific tool invoked.
   - The parameters generated for the tool.
   - The raw observation returned by the tool.
3. **Visualization**: Export traces to a platform like Google Cloud Trace to enable visual debugging of reasoning chains.
4. **Feedback Loop**: Capture user feedback (e.g., thumbs down) and link it to the specific trace ID to facilitate root cause analysis and automated test case generation.

## Background
- [Debug with OpenTelemetry Traces: Answering "Why?"](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/28-debug-with-opentelemetry-traces-answering-why.md)
- [Observability: Seeing Inside the Agent's Mind](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/31-observability-seeing-inside-the-agents-mind.md)
- [Tracing the "Vibe Trajectory" and Content Scanning](../../references/google-ai-agents-intensive/vibe-coding-agent-security-and-evaluationday4/22-tracing-the-vibe-trajectory-and-content-scanning.md)
