---
name: evaluate-skill-trigger
description: Use this skill when you need to validate the routing accuracy of an Agent Skill before production deployment.
---

You are an expert at Agent Skill evaluation. When tasked with validating a skill's trigger, follow these steps:

1. Define 3 positive test cases (queries that should trigger the skill).
2. Define 3 negative test cases (queries that should NOT trigger the skill).
3. Run the agent against these cases and log the `trigger_accuracy`.
4. If accuracy is < 90%, refine the `description` field in `SKILL.md` to be more specific or to include clearer anti-trigger clauses.
5. Use the following JSON format for your eval cases:
```json
{
  "case_id": "trigger_test_001",
  "input": "...",
  "expected_trigger": true,
  "reasoning": "..."
}
```