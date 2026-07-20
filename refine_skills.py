import os
import shutil

base_dir = "/Users/irus/Desktop/to_IT/skills_gen"
src = os.path.join(base_dir, "extracted_skills")
dst = os.path.join(base_dir, "skills_refined")

if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)

# 1. Combine observability skills
tracing_path = os.path.join(dst, "configure-agent-tracing-with-opentelemetry", "SKILL.md")
instrument_dir = os.path.join(dst, "instrument-agent-observability-with-opentelemetry")
instrument_path = os.path.join(instrument_dir, "SKILL.md")

with open(tracing_path, "r") as f:
    tracing_content = f.read()

with open(instrument_path, "r") as f:
    instrument_content = f.read()

# Append content (strip frontmatter from the second one)
parts = instrument_content.split("---")
if len(parts) >= 3:
    instrument_body = "---".join(parts[2:]).strip()
else:
    instrument_body = instrument_content

with open(tracing_path, "w") as f:
    f.write(tracing_content + "\n\n### Additional Guidelines (from Instrument Agent Observability)\n\n" + instrument_body)

shutil.rmtree(instrument_dir)

# 2. Rename A2A orchestration
orchestrator_old = os.path.join(dst, "implement-a2a-remote-agent-orchestration")
orchestrator_new = os.path.join(dst, "dispatch-remote-a2a-agent")
shutil.move(orchestrator_old, orchestrator_new)

orch_skill_path = os.path.join(orchestrator_new, "SKILL.md")
with open(orch_skill_path, "r") as f:
    orch_content = f.read()
orch_content = orch_content.replace("name: Implement A2A Remote Agent Orchestration", "name: dispatch-remote-a2a-agent")
orch_content = orch_content.replace("description: Use this skill when you need to delegate tasks from a central orchestrator agent to a specialized, remote A2A-compliant agent.", "description: Orchestrator logic for delegating tasks to A2A agents.")
orch_content += "\n\n**Note**: This skill explicitly defines the workflow from the orchestrator's perspective (dispatching tasks).\n"
with open(orch_skill_path, "w") as f:
    f.write(orch_content)

# 3. Update Consume Remote A2A Agent
consume_skill_path = os.path.join(dst, "consume-remote-a2a-agent", "SKILL.md")
with open(consume_skill_path, "r") as f:
    consume_content = f.read()
consume_content += "\n\n**Note**: This skill explicitly defines the workflow from the specialized sub-agent's perspective (receiving and returning tasks).\n"
with open(consume_skill_path, "w") as f:
    f.write(consume_content)

# 4. Create router.md
router_content = """# Router: System Prompt & Tool Schema

## 1. System Prompt Injection
You are Antigravity, a Senior Agentic Systems Architect. Your primary mandate is to enforce production-grade, spec-driven development (SDD) for all agentic systems. You do not write ad-hoc vibe code.

You have access to a repository of canonical Agentic Skills. Do NOT attempt to guess the implementation details, directory structures, or canonical standards for these skills. 

When you identify that a user's request requires one of the capabilities listed below, you MUST use the `fetch_skill_blueprint` tool to retrieve the Level 2/3 implementation details before writing any code.

### AVAILABLE AGENTIC SKILLS (LEVEL 1 METADATA)

[Architecture & SDLC]
- create-agent-skill: Initialize canonical Agent Skill directory structure.
- spec-driven-development-sdd-implementation: Enforce strict, version-controlled blueprints.
- configure-agentic-harness: Scaffold production-ready agentic reliability.
- automated-code-review-skill: Enforce sec/logic/style on PRs.
- implement-agentic-think-act-observe-loop: Core orchestration logic for autonomous cycles.
- debug-mcp-transport-issues: Fix hallucinations/parsing/connections in MCP servers.

[Interoperability & Ecosystem]
- configure-mcp-server-connection: Connect agent to external tools/APIs via MCP.
- expose-agent-via-a2a-protocol: Make agent discoverable in multi-agent ecosystem.
- consume-remote-a2a-agent: Specialized sub-agent logic for receiving/returning tasks.
- dispatch-remote-a2a-agent: Orchestrator logic for delegating tasks to A2A agents.
- implement-multi-agent-coordinator-pattern: Design complex sub-task delegation.
- generate-a2ui-components: Output interactive UI instead of raw JSON/text.

[Security & Governance]
- configure-agentic-security-guardrails: Secure against rogue actions/prompt injection.
- configure-just-in-time-jit-token-downscoping: Prevent Confused Deputy via least privilege IAM.
- hybrid-policy-server-implementation: Runtime safety net for structural/semantic tool policies.
- context-hygiene-and-pii-masking: Dynamic context resolver to prevent data leakage.
- implement-ephemeral-sandboxing-for-agentic-code-execution: Securely isolate dynamic code generation.
- implement-agentic-secops-triad-red-blue-green: Continuous security monitoring/remediation.

[Observability & Evaluation]
- configure-agent-tracing-with-opentelemetry: End-to-end execution narrative and telemetry.
- implement-agent-observability-via-structured-logging: Capture internal thought processes.
- implement-agent-as-a-judge-evaluation: Automate evaluation of reasoning/tool usage.
- implement-agentic-evaluation-suite: Verify code/trajectory correctness in workflows.
- derive-intent-satisfaction-rubrics-from-session-prefixes: Evaluate output against underspecified intent.
- evaluate-skill-trigger: Validate routing accuracy before deployment.
- implement-evaluation-driven-development: Define functional specs prior to implementation.
- implement-evaluation-gated-ci-cd: CI/CD pipeline configuration for agent quality.

[Memory & Context]
- configure-memory-generation-tool: Autonomous persistence into long-term memory.
- implement-proactive-memory-retrieval: Inject user memories into system instructions.
- implement-session-compaction: Manage ADK history to reduce token usage/latency.
- optimize-context-engineering: Balance static/dynamic context for token cost/performance.
- implement-multi-turn-session-convergence-tracking: Measure workflow efficiency over turns.

## 2. Tool / Function Schema (OpenAI / Tool Calling Format)

Provide this tool definition to Antigravity so it knows how to request the deeper context.

```json
{
  "type": "function",
  "function": {
    "name": "fetch_skill_blueprint",
    "description": "Retrieves the full Level 2 and Level 3 documentation, code specifications, and canonical standards for a specific agentic skill. Call this BEFORE attempting to implement any of the skills in your Level 1 metadata.",
    "parameters": {
      "type": "object",
      "properties": {
        "skill_id": {
          "type": "string",
          "description": "The exact ID of the skill to fetch (e.g., 'configure-mcp-server-connection'). Must match an item from the Level 1 Metadata list."
        },
        "context_reason": {
          "type": "string",
          "description": "A brief explanation of why this skill is needed for the current task, helping the routing system pull the most relevant code snippets."
        }
      },
      "required": ["skill_id", "context_reason"]
    }
  }
}
```
"""

router_path = os.path.join(dst, "router.md")
with open(router_path, "w") as f:
    f.write(router_content)

print("Refinement completed successfully!")
