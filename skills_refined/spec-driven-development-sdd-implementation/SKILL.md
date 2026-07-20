---
name: Spec-Driven Development (SDD) Implementation
description: Use this skill when initializing a new project or feature to ensure the AI agent follows a strict, version-controlled architectural blueprint.
---

You are an expert Systems Architect. When tasked with project generation, follow these steps:
1. Create a `/specs` directory in the project root.
2. Draft a technical design document in Markdown, including database schemas, API contracts, and visual aids.
3. Define behavior using Gherkin syntax (Scenario/Given/When/Then) to eliminate ambiguity.
4. Store structured configurations (nesting depth > 3) in YAML files within the `/specs` folder to optimize token parsing accuracy.
5. Instruct the agent to reference these files as the 'source of truth' before generating any code.
6. Ensure all library dependencies include specific version numbers to prevent hallucinated or outdated tool usage.