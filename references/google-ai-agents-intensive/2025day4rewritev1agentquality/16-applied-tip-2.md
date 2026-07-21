## Applied Tip:

When you save an Eval Case (as described in the previous tip) in the ADK, it also saves the entire sequence of tool calls as the ground truth trajectory. Your automated pytest or adk  eval run will then check this trajectory for a perfect match (by default).

To manually implement process evaluation (i.e., debug a failure), use the Trace tab in the adk  web UI. This provides an interactive graph of the agent's execution, allowing you to visually inspect the agent's plan, see every tool it called with its exact arguments, and compare its actual path against the expected path to pinpoint the exact step where its logic failed.
