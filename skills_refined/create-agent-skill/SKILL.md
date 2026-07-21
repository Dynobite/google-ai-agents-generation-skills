---
name: create-agent-skill
description: Use this skill when you need to initialize a new Agent Skill directory structure according to the canonical standard.
---

You are an expert at scaffolding agentic workflows. When tasked with creating a new skill, follow these steps:

1. Create a root directory using snake_case (e.g., `my-new-skill/`).
2. Inside the root, create the following structure:
```
my-new-skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```
3. Populate `SKILL.md` with the required YAML frontmatter:
```yaml
---
name: my-new-skill
description: |
  [One verb-led sentence describing the skill]. Use this skill when the user [trigger phrase 1], [trigger phrase 2]. Do NOT use for [anti-trigger 1].
version: 1.0.0
license: MIT
---
```
4. Ensure the description field is <= 1024 characters and clearly defines the routing logic.

## Background
- [Agent Skills](../../references/google-ai-agents-intensive/agent-skillsday3/01-agent-skills.md)
- [Core Agent Architecture: Model, Tools, and Orchestration](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/12-core-agent-architecture-model-tools-and-orchestration.md)
