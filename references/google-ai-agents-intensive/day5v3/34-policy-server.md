## Policy Server

Here's an example Hybrid Policy Server that intercepts actions before they hit external systems. It operates on two layers:

- Structural Gating (The Traffic Lights): Deterministic rules based on roles and environments. These are fast, binary checks (e.g., a viewer role cannot use the send\_email tool). This layer prevents architectural violations without needing to ask an LLM.s
- Semantic Gating (The Intelligent Referee): This uses a secondary, specialized LLM (like Gemini) to inspect the intent and content of a proposed action against natural language privacy guidelines. This addresses the need for when a tool is allowed, but the way it is used violates a policy. For example, an admin can use send\_email, but they should not send unmasked PII (like plain-text email addresses or API keys). This is where structural rules fail. You cannot regex every possible PII leak.

These rules are defined in a standard policies.yaml:

```
environments: localhost: blocked_tools: - send_email roles: viewer: allowed_tools: - list_files - read_file
```

Snippet 4: policies.yaml: This configuration establishes deterministic gating rules for tool-level permissions based on role and environment.

Below is a lightweight implementation of a Policy Server designed to intercept tool calls and verify permissions at runtime.

```
Python import os, yaml from google.genai import Client class PolicyService: def is_tool_allowed(self, tool_name: str) -> bool: # Check Environment Blocks env_config = self.config.get("environments", {}).get(self.env, {}) if tool_name in env_config.get("blocked_tools", []): return False # Check Role Permissions role_allows = self.config.get("roles", {}).get(self.role, {}). get("allowed_tools", []) return "*" in role_allows or tool_name in role_allows async def check_action_semantic(self, action_description: str) -> bool: client = Client(vertexai=True, project=self.project_id, location=self.location) Continues next page...
```

```
prompt = f"Evaluate if this action violates PII policies: {action_description}" response = client.models.generate_content(model="gemini-3.1-pro", contents=prompt) return not response.text.strip().upper().startswith("VIOLATION")
```

S nippet 5: policy\_server.py: This service implements a hybrid policy engine to intercept actions and perform structural and semantic evaluations.

The code listing works as follows: When the agent decides to use a tool, the execution flow is intercepted:

1.  Structural Check: Is the tool allowed for this role/env? (Check YAML).
2. Semantic Check: Are the arguments safe? (Ask Gemini). See the prompt in the code snippet. Unmasked email addresses are considered a violation.
3.  Execution: If both pass, the tool runs. Otherwise, a "Policy Violation" message is returned to the agent, allowing it to self-correct or fail gracefully.

This creates a safety net that separates execution logic from governance logic-a critical separation of concerns for enterprise software.
