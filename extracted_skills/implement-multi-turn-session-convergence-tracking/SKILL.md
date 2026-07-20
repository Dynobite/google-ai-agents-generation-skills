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