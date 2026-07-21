## Implementing a Dynamic ContextResolver

This security pattern is achieved by implementing a lightweight regex-based translation utility inside the application's core codebase. Below is a practical implementation of this design:

This script acts as the core translation engine, replacing placeholder strings structured with double-bracket syntax [[VARIABLE\_NAME]] with runtime overrides or environment configurations:

```
Python import os import re from typing import Optional, Dict, Any def resolve_context(template_str: str, override_state: Optional[Dict[str, Any]] = None) -> str: """Scans a template string for [[VARIABLE_NAME]] and replaces it with values from override_state or os.environ. """ if template_str is None: return "" state_to_check = override_state or {} def replacement(match): var_name = match.group(1).strip() # 1. Prioritize runtime state overrides if var_name in state_to_check and state_to_check[var_name] is not None: return str(state_to_check[var_name]) # 2. Fallback to validated environment variables elif var_name in os.environ and os.environ[var_name] is not None: return os.environ[var_name] # 3. Leave unresolved to prevent silent failures else: return match.group(0) # Resolve all bracketed variables dynamically, e.g., [[COMMENTER_EMAIL]] return re.sub(r'\[\[([^\]]+)\]\]', replacement, template_str)
```

Snippet 6: context\_resolver.py: This utility resolves bracketed placeholders with environment variables to maintain context hygiene.

To enforce context hygiene globally, the sanitization utility must be wired directly into your agent's execution pipeline as a validation step. By intercepting incoming tool calls before they run, you ensure all prompt-injected strings are sterilized dynamically:

```
Python # ... inside the validate_tool_call framework execution ... resolved_args = {} for k, v in args.items(): if isinstance(v, str): resolved_args[k] = resolve_context(v) elif isinstance(v, list): resolved_args[k] = [resolve_context(i) if isinstance(i, str) else i for i in v] else: resolved_args[k] = v args.clear() args.update(resolved_args)
```

Snippet 7: tool\_policy\_engine.py: This middleware integrates the context resolver into the agent pipeline to sanitize tool arguments before execution.

By enforcing this boundary, any attempt by an agent to execute an action (such as sending an email or querying a cloud presentation) is intercepted. The engine translates generic placeholders like [[COMMENTER\_EMAIL]] or [[DEFAULT\_PRESENTATION\_ID]] into authorized test assets safely and silently, eliminating the need to ever hardcode sensitive PII in test suites or system prompts.
