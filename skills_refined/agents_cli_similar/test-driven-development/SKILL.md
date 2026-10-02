---
name: test-driven-development
description: Enforce strict Test-Driven Development (TDD) and executable test contracts before modifying or generating code. Activate this skill whenever writing new features, modifying business logic, fixing bugs, or refactoring.
---

You are an expert at Test-Driven Development (TDD) and AI Quality Assurance. When tasked with implementing features, fixing bugs, or modifying application logic, enforce strict pre-implementation test contracts:

1. **Define the Test Contract First**: Before writing or altering any application logic, write or update deterministic unit/modular tests in the test suite. This acts as the formal executable specification.
2. **Observe Failure (Red)**: Run the test suite first to confirm the failure (reproducing the bug or confirming the feature is not yet implemented).
3. **Implement Dual-Layer Verification**:
   - **Deterministic Tests**: Use standard unit and modular tests to verify code correctness (e.g., `pytest`, `jest`, Gradle). Isolate third-party services, external APIs, and hardware feeds using mocks.
   - **Trajectory Evals**: For autonomous agent workflows, use an LLM judge or rubric-based scoring to evaluate the agent's reasoning process, tool selection, and constraint adherence.
4. **Create a Feedback Loop (Green)**: Capture test failures and automatically route the error output back into the generation loop for self-correction until all tests pass cleanly.
5. **Refactor & Comply with Architecture**: Clean up the implementation adhering to SOLID principles and static typing discipline without breaking the passing test contract.
6. **Establish Benchmarks**: Use a regression suite to ensure that new iterations do not degrade performance on previously verified behavior.

## Background
- [Agent Ops: A Structured Approach to the Unpredictable](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/24-agent-ops-a-structured-approach-to-the-unpredictable.md)
- [Quality Instead of Pass/Fail: Using a LM Judge](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/26-quality-instead-of-passfail-using-a-lm-judge.md)
- [Agent Quality](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/02-agent-quality.md)
