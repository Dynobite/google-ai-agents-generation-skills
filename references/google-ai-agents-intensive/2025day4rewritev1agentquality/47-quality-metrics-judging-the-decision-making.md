## Quality Metrics: Judging the Decision-Making

Quality Metrics are second-order metrics derived by applying the judgment frameworks detailed in Chapter 2 on top of the raw observability data. They move beyond efficiency to assess the agent's reasoning and final output quality itself.

These are not simple counters or averages. They are second-order metrics derived by applying a judgment layer on top of the raw observability data. They assess the quality of the agent's reasoning and final output.

Examples of critical Quality Metrics include:

- Correctness &amp; Accuracy: Did the agent provide a factually correct answer? If it summarized a document, was the summary faithful to the source?
- Trajectory Adherence: Did the agent follow the intended path or "ideal recipe" for a given task? Did it call the right tools in the right order?
- Safety &amp; Responsibility: Did the agent's response avoid harmful, biased, or inappropriate content?
- Helpfulness &amp; Relevance: Was the agent's final response actually helpful to the user and relevant to their query?

Generating these metrics requires more than a simple database query. It often involves comparing the agent's output against a "golden" dataset or using a sophisticated LLM-as-aJudge to score the response against a rubric.

The observability data from our logs and traces is the essential evidence needed to calculate these scores, but the process of judgment itself is a separate, critical discipline. To ensure these metrics are actionable, the Agent platform supports Online Monitors . These monitors parse live telemetry streams and automatically trigger incident alerts in Google Cloud Monitoring (via Slack, email, or Pub/Sub) if evaluation scores slip below baseline limits, catching 'reasoning drift' in real-time.
