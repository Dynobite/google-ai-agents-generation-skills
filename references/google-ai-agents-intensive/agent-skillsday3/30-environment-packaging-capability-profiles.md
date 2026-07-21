## Environment Packaging: Capability Profiles

Activating every skill degrades natural language routing and overwhelms the context window. Architects should utilize tools to manage "Capability Profiles," which function as specialized personas tailored to specific execution states. A profile acts as a modular tool bundle defining:

- Active skills and tool access.
- System instructions and operational guardrails.
- Automated workflows and subagent topologies.
- LLM parameters, such as model choice and temperature.

During execution, the orchestration layer unloads previous system instructions and flushes stale variables before swapping the new Capability Profile into memory. This strict teardown and rebuild process prevents context loss.
