## How to evaluate

The seven dimensions are not all measurable the same way. No single method covers everything, so production pipelines combine several. The figure below summarizes the evaluation methods and the dimensions each is recommended for; the rest of the section describes each in detail.

| Method                       | What it does                                   | Recommended dimensions   |   Recommended dimensions |   Recommended dimensions | Recommended dimensions   | Recommended dimensions   | Recommended dimensions   | Recommended dimensions   | Recommended dimensions   |
|------------------------------|------------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
|                              |                                                |                          |                     1234 |                      567 | RAI                      |                          |                          |                          |                          |
| Standardized benchmarks      | Compare against the field on shared task sets. |                          |                          |                          |                          |                          |                          |                          |                          |
| Automated functional testing | Run build, tests, and linters on the output.   |                          |                          |                          |                          |                          |                          |                          |                          |
| Security & safety evalution  | Static analysis + adversarial refusal probing. |                          |                          |                          |                          |                          |                          |                          |                          |
| LLM-as-judge/Agent-as-judge  | Score outputs against rubrics.                 |                          |                          |                          |                          |                          |                          |                          |                          |
| Browser-based testing        | Multi-stepworkflowsonthedeployed app.          |                          |                          |                          |                          |                          |                          |                          |                          |
| Trajectory inspection        | Analyzereasoning,tool calls,retrievals.        |                          |                          |                          |                          |                          |                          |                          |                          |
| Humanreview                  | Qualifiedreviewers;ground truthforintent.      |                          |                          |                          |                          |                          |                          |                          |                          |
| Online evaluation            | Sample production traffic; offline rubrics.    |                          |                          |                          |                          |                          |                          |                          |                          |

Figure 4: Evaluation methods and recommended dimensions

<!-- image -->

Automated functional testing . Run the build, the test suite, and the linters on the agent's output. The standard tooling does most of the work here, pytest , jest , eslint , mypy , plugged into the project's CI pipeline. This is the cheapest signal available, recommended for functional correctness (dimension 2) and the rule-checkable parts of code quality (dimension 5).

Security and safety evaluation . Combine static security analysis on the generated code with adversarial probing for refusal behaviour. This is cross-cutting, it scores safety and responsible AI alongside the other dimensions, not as a separate gate. The tooling splits in two: static scanners like Snyk and Semgrep find vulnerabilities, git-secrets catches credential leaks, and scripted red-team suites test whether the agent refuses clearly harmful requests.

LLM-as-judge and Agent-as-judge . Use a model to score outputs against rubrics. Recommended for the dimensions where rules don't quite capture the right answer, intent satisfaction (dimension 1), code quality and style (dimension 5), and trajectory quality (dimension 6). In practice that means Gemini scoring an output against the original user prompt, or an agent-as-judge inspecting the trace for plan coherence.

Browser-based testing . Run multi-step workflows against the deployed app and observe what happens. Recommended for visual and behavioural correctness (dimension 3) on UIproducing agents. The techniques are well-established in software testing: Playwright scripts that interact with the rendered UI, screenshot comparison against a reference.

Trajectory inspection . Analyze the agent's reasoning, tool calls, skill invocations, and retrievals. Recommended for the internal dimensions, trajectory quality (dimension 6) and self-repair behaviour (dimension 7). The substrate is OpenTelemetry traces with span-level tool-call data, surfaced through trace-replay tools that bind each model invocation to the actions that followed.

Human review . Sample sessions for direct review by qualified reviewers. Recommended for intent satisfaction (dimension 1, where humans are the only ground truth), code quality (dimension 5, the traditional domain of code review), and safety and responsible AI calls that need nuanced judgment. Doesn't scale; mainly used to calibrate the other methods. In practice that means structured annotation by senior engineers on review queues filled by online sampling.

Online evaluation . Sample live production traffic and score it against the same rubrics used in offline eval. Covers all dimensions at sample rate. The trick is sampling well: a flat 1% misses the long tail, so bias toward high-cost sessions, sessions with many corrections, and sessions the user abandoned.
