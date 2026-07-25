---
name: Generate A2UI Components
description: Use this skill when you need to output interactive user interfaces from an agent instead of raw JSON or text.
---

You are an expert at implementing A2UI (Agent-to-User Interface) interoperability. When generating UI, follow these steps: 1. Use the `a2ui-agent-sdk` to manage the catalog and schema. 2. Define the UI intent using the A2UI v0.9 format. 3. Use the `A2uiSchemaManager` to build a system prompt that embeds the catalog schema and examples. 4. Ensure the agent emits `<a2ui-json>` blocks. 5. Parse the response using `parse_response()`, validate against the catalog schema using `jsonschema`, and implement a retry loop for validation failures. 6. For deterministic layouts, use the 'tool-as-template' pattern by returning an A2UI structure directly from a tool function.

## Background
- [Agent-to-UI (A2UI) Interoperability](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/30-agent-to-ui-a2ui-interoperability.md)
- [Generative UI & A2UI](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/32-generative-ui-amp-a2ui.md)
- [A2UI: A Secure Implementation](../../references/google-ai-agents-intensive/agent-tools-interoperabilityday2/34-a2ui-a-secure-implementation.md)
