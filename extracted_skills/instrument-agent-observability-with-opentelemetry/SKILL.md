---
name: Instrument Agent Observability with OpenTelemetry
description: Use this skill when setting up monitoring and debugging for an agentic system.
---

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