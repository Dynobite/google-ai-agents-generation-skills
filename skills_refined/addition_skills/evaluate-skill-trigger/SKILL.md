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

## Background
- [Agent Skills](google-ai-agents-intensive/agent-skillsday3/01-agent-skills.md)
- [Agent Quality](google-ai-agents-intensive/2025day4rewritev1agentquality/02-agent-quality.md)
- [Spec-Driven Production Grade Development in the Age of Vibe Coding](google-ai-agents-intensive/day5v3/01-spec-driven-production-grade-development-in-the-age-of-vibe-coding.md)
