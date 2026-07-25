---
name: Implement Multi-Turn Session Convergence Tracking
description: Use this skill when measuring the efficiency and success of an agentic workflow over multiple turns.
---

You are an expert at observability and evaluation. When tracking session convergence, follow these steps:

1. Instrument the agentic workflow using OpenTelemetry to create a single trace tree for the entire session.
2. Calculate the 'cost-to-converge' by aggregating token costs across all turns.
3. Identify abandoned sessions by monitoring the final user signal.

```python
from google.cloud import trace_v2
trace = trace_v2.TraceServiceClient().get_trace(name=f"projects/{project}/traces/{session_id}")
def session_outcome(trace):
    return {
        "converged": trace.last_turn.user_signal == "satisfied",
        "turns_to_converge": trace.user_correction_count,
        "abandoned": trace.last_user_action == "close",
        "cost_to_converge": trace.total_token_cost_usd,
    }
```

## Background
- [Measure What Matters: Instrumenting Success Like an A/B Experiment](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/25-measure-what-matters-instrumenting-success-like-an-ab-experiment.md)
- [Debug with OpenTelemetry Traces: Answering "Why?"](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/28-debug-with-opentelemetry-traces-answering-why.md)
- [Observability: Seeing Inside the Agent's Mind](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/31-observability-seeing-inside-the-agents-mind.md)
