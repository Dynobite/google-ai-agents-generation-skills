---
name: Hybrid Policy Server Implementation
description: Use this skill to implement a runtime safety net that intercepts agent tool calls based on structural and semantic policies.
---

You are an expert at AI Governance. When implementing a Policy Server, follow this two-layer architecture:

1. **Structural Gating:** Define allowed tools per role/environment in a `policies.yaml` file.
2. **Semantic Gating:** Use a secondary LLM to inspect tool arguments for PII violations.

Implement the `PolicyService` class to intercept calls:

```python
class PolicyService:
    def is_tool_allowed(self, tool_name: str) -> bool:
        # Check YAML-based structural rules
        ...
    async def check_action_semantic(self, action_description: str) -> bool:
        # Use Gemini to evaluate if action violates PII policies
        prompt = f"Evaluate if this action violates PII policies: {action_description}"
        response = client.models.generate_content(model="gemini-3.1-pro", contents=prompt)
        return not response.text.strip().upper().startswith("VIOLATION")
```

## Background
- [Policy Server](https://../../references/google-ai-agents-intensive/day5v3/34-policy-server.md)
- [Securing a Single Agent: The Trust Trade-Off](https://../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/34-securing-a-single-agent-the-trust-trade-off.md)
- [Implementing Guardrails](https://../../references/google-ai-agents-intensive/day5v3/29-implementing-guardrails.md)
