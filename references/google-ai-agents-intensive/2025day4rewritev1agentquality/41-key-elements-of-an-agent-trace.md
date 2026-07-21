## Key Elements of an Agent Trace

Modern tracing is built on open standards like OpenTelemetry . The core components are:

- Spans: The individual, named operations within a trace (e.g., an llm\_call span, a tool\_execution span).
- Attributes: The rich metadata attached to each span -prompt\_id , latency\_ms, token\_count , user\_id , etc.
- Context Propagation: The "magic" that links spans together via a unique trace\_id , allowing backends like Google Cloud Trace to assemble the full picture. Cloud Trace is a distributed tracing system that helps you understand how long it takes for your application to handle requests. When an agent is deployed on the managed Agent Runtime , this telemetry is captured automatically. The Agent Runtime serves as the stateful scaled deployment environment for your fleet, featuring sub-second cold starts, automated scaling, and native support for complex, long-running multi-day workflows (up to 7 days) without loss of context.

Figure 5: OpenTelemetry view lets you inspect attributes, logs, events, and other details

<!-- image -->
