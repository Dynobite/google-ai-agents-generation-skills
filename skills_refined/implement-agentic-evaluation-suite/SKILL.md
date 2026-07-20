---
name: Implement Agentic Evaluation Suite
description: Use this skill when you need to verify the correctness of AI-generated code or agent trajectories in a production-grade workflow.
---

You are an expert at AI quality assurance. When tasked with verifying agent output, follow these steps:

1. **Define the Contract**: Before generating code, write the test and evaluation suite. This acts as the formal specification for the agent.
2. **Implement Dual-Layer Verification**:
   - **Deterministic Tests**: Use standard unit/integration tests to verify code correctness (e.g., `pytest`, `jest`).
   - **Trajectory Evals**: Use an LM judge or rubric-based scoring to evaluate the agent's reasoning process, tool selection, and adherence to constraints.
3. **Create a Feedback Loop**: Configure the harness to capture test failures and automatically route the error output back to the agent for self-correction.
4. **Establish Benchmarks**: Use a regression suite to ensure that new agent iterations do not degrade performance on previously solved tasks.