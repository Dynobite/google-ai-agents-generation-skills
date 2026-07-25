---
name: Implement Agent-as-a-Judge Evaluation
description: Use this skill when you need to automate the evaluation of an agent's reasoning process and tool usage.
---

You are an expert at building automated evaluation pipelines. When tasked with implementing an 'Agent-as-a-Judge' system, follow these steps:

1. Export the full execution trace object, including the internal plan, tool selection, and arguments passed.
2. Create a 'Critic Agent' with a specific rubric prompt that evaluates the trace object.
3. Structure your rubric prompt to ask process-oriented questions, such as:
   - 'Was the initial plan logical and feasible?'
   - 'Was the selected tool the correct choice for the current step?'
   - 'Were the tool arguments correctly formatted?'
4. Use the following prompt template for your Critic Agent:

```text
Evaluate the following execution trace based on the rubric below:
Trace: {trace_object}
Rubric:
1. Plan Quality: Rate 1-5 on logical structure.
2. Tool Usage: Did the agent use the correct tool for the task?
3. Reasoning: Identify any hallucinations or logic loops.
Provide your response in JSON format.
```
5. Integrate this Critic Agent into your CI/CD pipeline to automatically flag process failures even when the final output appears correct.

## Background
- [Quality Instead of Pass/Fail: Using a LM Judge](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/26-quality-instead-of-passfail-using-a-lm-judge.md)
- [Agent-as-a-Judge](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/22-agent-as-a-judge.md)
- [The Art of Agent Evaluation: Judging the Process](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/11-the-art-of-agent-evaluation-judging-the-process.md)
