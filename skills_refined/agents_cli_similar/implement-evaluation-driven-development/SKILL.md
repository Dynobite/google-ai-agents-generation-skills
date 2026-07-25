---
name: implement-evaluation-driven-development
description: Use this skill when you need to define functional specifications for a new skill before writing the implementation.
---

You are an expert at Evaluation-Driven Development (EDD). When tasked with building a new skill, follow these steps:

1. Create a JSON evaluation file defining the expected behavior:
```json
{
  "case_id": "skill_task_001",
  "input": "[User Query]",
  "expected_skill": "[Skill Name]",
  "expected_tool_calls": [
    {"tool": "[Tool Name]", "args": {}}
  ],
  "expected_output_format": "[Format]",
  "rubric": ["[Criterion 1]", "[Criterion 2]"]
}
```
2. Validate that the `expected_tool_calls` align with the skill's intended trajectory.
3. Only after the JSON spec is finalized, draft the `SKILL.md` body to satisfy these requirements.

## Background
- [Spec-Driven Production Grade Development in the Age of Vibe Coding](../../references/google-ai-agents-intensive/day5v3/01-spec-driven-production-grade-development-in-the-age-of-vibe-coding.md)
- [Agent Quality](../../references/google-ai-agents-intensive/2025day4rewritev1agentquality/02-agent-quality.md)
- [Agent Skills](../../references/google-ai-agents-intensive/agent-skillsday3/01-agent-skills.md)
