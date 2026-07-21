## Observability: The Prerequisite for Evaluation

To evaluate an agent's internal reasoning, developers must possess the capability to see it. Observability is the absolute prerequisite for Glass Box evaluation; without it, agent failures appear as inexplicable monolithic events.

- Tracing the Thought: Modern agent observability relies on OpenTelemetry to capture non-deterministic flows. agent.session spans capture the entire task duration, agent. think spans record the internal reasoning and prompting cycle prior to action, and agent.tool spans log the specific arguments and latencies of environmental interactions.
- Tracking Costs: Observability provides granular data to calculate true operational costs. By aggregating span attributes, teams can precisely measure token consumption, inference latency, and the cost of self-repair loops.
- Dynamic Tail-Based Sampling: Capturing 100% of traces in production quickly overwhelms storage budgets. Tail-based dynamic sampling allows the collector to evaluate the full trace after completion, dropping routine successes while retaining traces containing errors or excessive self-repair loops.
