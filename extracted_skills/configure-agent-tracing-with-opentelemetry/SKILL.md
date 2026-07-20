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