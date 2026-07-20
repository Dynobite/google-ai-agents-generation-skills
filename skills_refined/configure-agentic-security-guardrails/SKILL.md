---
name: Configure Agentic Security Guardrails
description: Use this skill when securing an agent against rogue actions or prompt injection in a production environment.
---

You are an expert at hardening agentic systems. When implementing security, apply a defense-in-depth approach:

1. **Deterministic Guardrails**: Implement hardcoded policy engines outside the model's reasoning to block unauthorized actions (e.g., `if action == 'purchase' and amount > 100: block()`).
2. **Agent Identity**: Assign a cryptographically verifiable identity (e.g., SPIFFE) to the agent, distinct from the user or developer.
3. **Reasoning-based Defenses**: Use a 'guard model' (e.g., Gemini Flash-Lite) as a judge to screen inputs and outputs for prompt injection or PII leakage.
4. **Callback Validation**: Use `before_tool_callback` hooks to inspect tool parameters against current state policies before execution.
5. **Managed Protection**: Integrate services like Model Armor to screen for jailbreak attempts and malicious URLs.