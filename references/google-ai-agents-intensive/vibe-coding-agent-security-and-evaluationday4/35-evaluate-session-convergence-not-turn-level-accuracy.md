## Evaluate session convergence, not turn-level accuracy.

A vibe-coding session is multi-turn by construction. The relevant question is not 'was turn 4 correct?' but 'did the user converge on something they wanted?' Sessions that converge in few turns are the success cases. Sessions abandoned mid-flow are the most informative failures, far more than turn-level errors. Cloud Trace exposes a vibe-coding session, instrumented through ADK and Agent Engine, as a single trace tree.

```
Python from google.cloud import trace_v2 trace = trace_v2.TraceServiceClient().get_trace( name=f"projects/{project}/traces/{session_id}" ) def session_outcome(trace): return { "converged":         trace.last_turn.user_signal == "satisfied", "turns_to_converge": trace.user_correction_count, "abandoned":         trace.last_user_action == "close", "cost_to_converge":  trace.total_token_cost_usd, }
```

Snippet 3: Tracking multi-turn session convergence and calculating total token cost via Google Cloud Trace.
