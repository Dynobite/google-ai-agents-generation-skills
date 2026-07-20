---
name: Implement Agentic Think-Act-Observe Loop
description: Use this skill when implementing the core orchestration logic for an autonomous agent to ensure it follows the standard Think-Act-Observe cycle.
---

You are an expert at building agentic orchestration layers. When tasked with implementing the agentic loop, follow these steps:

1. **Mission Definition**: Accept a high-level goal from the user or trigger.
2. **Context Assembly**: Gather relevant state, session history, and long-term memory into the LM context window.
3. **Reasoning (Think)**: Prompt the model to analyze the mission against the current state and generate a plan or next step.
4. **Action (Act)**: Execute the selected tool (API, code function, or database query) based on the model's output.
5. **Observation (Observe)**: Capture the tool output and feed it back into the context window.
6. **Iteration**: Repeat steps 3-5 until the mission is complete.

Ensure your orchestration layer logs the full trajectory (prompt, reasoning, tool call, parameters, and observation) to support debugging via OpenTelemetry.