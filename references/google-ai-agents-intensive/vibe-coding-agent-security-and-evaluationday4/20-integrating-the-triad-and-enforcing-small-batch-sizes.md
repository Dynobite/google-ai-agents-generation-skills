## Integrating the Triad and Enforcing Small Batch Sizes

To prevent agents from generating massive, unreviewable code modifications during this process, developers must restrict agent output to small batch sizes. This is ideally achieved using a test-driven loop where the system blocks the agent from modifying tests and implementation code simultaneously, ensuring the test remains an objective baseline.

With these constraints in place, the Red, Blue, and Green triad dynamically adapts the primary agent's behaviour at runtime across three distinct phases:

- The Planner Phase: When a primary agent designs a workflow, a specialised threatmodelling skill helps it evaluate the plan, identifying logical flaws and policy violations before the agent begins active execution.
- The Evaluator Phase: The Evaluator quorum reviews the proposed execution trace while the Agent Defender (Blue) simultaneously verifies the AgBOM and monitors the semantic context for intent drift.
- The Executor Phase: As the Executor performs the downscoped action, the Agent Fixer (Green) monitors the real-world tool execution, ready to instantly orchestrate a stateful quarantine or trigger an auto-refactoring loop if the agent encounters an error or trips a security constraint.

To ensure these automated defence mechanisms can successfully intervene, the security triad requires an unimpeded, granular view into the agent's internal reasoning. An agentic security operation is entirely blind if it only looks at the final code output. We must shift our focus from observing the host infrastructure to observing the agent's "mind," creating an immutable audit trail that maps exactly how a fuzzy intent translates into a real-world action.
