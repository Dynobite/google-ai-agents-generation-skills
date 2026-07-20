# 🤖 Google 5-Day AI Agents Intensive: Extracted Skills Pack

![Agentic Engineering](https://img.shields.io/badge/Agentic-Engineering-blue)
![Docling Extraction](https://img.shields.io/badge/Extraction-Docling%20%7C%20Gemini-orange)
![Spec Driven](https://img.shields.io/badge/Methodology-Spec%20Driven%20Development-success)

Welcome to the **Google 5-Day AI Agents Intensive Skills Repository**. This project houses a curated, canonical collection of Agent Skills extracted from the official whitepapers and materials of Google's highly acclaimed intensive courses on Kaggle.

## 🌟 Origin & Context

These skills were meticulously extracted from the PDF whitepapers of the following Google intensive courses:
- **[5-Day AI Agents Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-agents)** (Originally held live: November 10 - 14, 2025)
- **[5-Day AI Agents: Intensive Vibe Coding Course With Google](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview?sort=hotness?utm_source%3Dreg&utm_medium=email&utm_campaign=learn-5-day-aiagentsvibecoding-june-2026&utm_content)** (June 15 - 19, 2026)

### 🛠 Extraction Methodology

The raw extraction process was fully automated using the `skill_extractor.py` pipeline:
- **Docling Library**: Converted the original educational PDFs into structured Markdown format.
- **Gemini 3.1 Flash Lite API**: Analyzed the text, identified discrete skill boundaries, and structured the outputs into individual `SKILL.md` files equipped with canonical frontmatter.

---

## 📂 Repository Architecture

This repository maintains two primary states of the extracted skills:

1. **`extracted_skills/`**: The raw, unadulterated output straight from the Gemini extraction pipeline.
2. **`skills_refined/`**: The production-ready directory where skills have been deduplicated, clarified, and optimized for consumption by an overarching orchestrator (like Antigravity).

---

## 🧠 The Agentic Routing System

To prevent context window bloat and trigger confusion, this repository utilizes an **Agentic Routing System**. Instead of loading all skills into an agent's context simultaneously, we employ a "Level 1" metadata map. 

You can find the exact system prompt injection and OpenTelemetry/Function calling schema in the `skills_refined/router.md` file. The router allows the agent to dynamically call `fetch_skill_blueprint` to retrieve deep "Level 2/3" context only when a specific skill is needed.

---

## 📋 Refined Skills Directory

Below is the refined, categorized list of available canonical agentic skills, ready to be mounted to your agentic system.

### 🏗 Architecture & SDLC
- **create-agent-skill**: Initialize canonical Agent Skill directory structure.
- **spec-driven-development-sdd-implementation**: Enforce strict, version-controlled blueprints.
- **configure-agentic-harness**: Scaffold production-ready agentic reliability.
- **automated-code-review-skill**: Enforce sec/logic/style on PRs.
- **implement-agentic-think-act-observe-loop**: Core orchestration logic for autonomous cycles.
- **debug-mcp-transport-issues**: Fix hallucinations/parsing/connections in MCP servers.

### 🌐 Interoperability & Ecosystem
- **configure-mcp-server-connection**: Connect agent to external tools/APIs via MCP.
- **expose-agent-via-a2a-protocol**: Make agent discoverable in multi-agent ecosystem.
- **consume-remote-a2a-agent**: Specialized sub-agent logic for receiving/returning tasks.
- **dispatch-remote-a2a-agent**: Orchestrator logic for delegating tasks to A2A agents.
- **implement-multi-agent-coordinator-pattern**: Design complex sub-task delegation.
- **generate-a2ui-components**: Output interactive UI instead of raw JSON/text.

### 🔒 Security & Governance
- **configure-agentic-security-guardrails**: Secure against rogue actions/prompt injection.
- **configure-just-in-time-jit-token-downscoping**: Prevent Confused Deputy via least privilege IAM.
- **hybrid-policy-server-implementation**: Runtime safety net for structural/semantic tool policies.
- **context-hygiene-and-pii-masking**: Dynamic context resolver to prevent data leakage.
- **implement-ephemeral-sandboxing-for-agentic-code-execution**: Securely isolate dynamic code generation.
- **implement-agentic-secops-triad-red-blue-green**: Continuous security monitoring/remediation.

### 📊 Observability & Evaluation
- **configure-agent-tracing-with-opentelemetry**: End-to-end execution narrative and telemetry.
- **implement-agent-observability-via-structured-logging**: Capture internal thought processes.
- **implement-agent-as-a-judge-evaluation**: Automate evaluation of reasoning/tool usage.
- **implement-agentic-evaluation-suite**: Verify code/trajectory correctness in workflows.
- **derive-intent-satisfaction-rubrics-from-session-prefixes**: Evaluate output against underspecified intent.
- **evaluate-skill-trigger**: Validate routing accuracy before deployment.
- **implement-evaluation-driven-development**: Define functional specs prior to implementation.
- **implement-evaluation-gated-ci-cd**: CI/CD pipeline configuration for agent quality.

### 🧠 Memory & Context
- **configure-memory-generation-tool**: Autonomous persistence into long-term memory.
- **implement-proactive-memory-retrieval**: Inject user memories into system instructions.
- **implement-session-compaction**: Manage ADK history to reduce token usage/latency.
- **optimize-context-engineering**: Balance static/dynamic context for token cost/performance.
- **implement-multi-turn-session-convergence-tracking**: Measure workflow efficiency over turns.

---

## 🚀 Usage

This repository is designed to be a "batteries-included" package that supports both native agent environments and custom orchestrators. How you use it depends entirely on your deployment ecosystem.

### Scenario A: Native Deployment (e.g., Antigravity IDE)

If you are deploying these skills natively within an environment like the **Antigravity IDE** or any framework that adheres strictly to the `.agents/skills/` auto-discovery standard:
- **You do NOT need the router or the Python script.** 
- The framework natively handles Just-In-Time (JIT) context retrieval. It automatically scans the `SKILL.md` files, loads *only* the YAML frontmatter (Level 1) into the system prompt, and retrieves the Markdown body (Level 2/3) only after the skill triggers.
- **Action:** Simply copy the 31 folders inside `skills_refined/` directly into your `.agents/skills/` directory. Ignore `router.md` and `fetch_skill_blueprint.py`.

### Scenario B: Custom Python Orchestrators (LangChain, OpenAI API, Raw ADK)

If you are building your own custom agent from scratch using Python, loading 31 extensive skills into your prompt will cause context bloat and trigger confusion. You must implement the routing pattern manually:
- **Use the Router:** Inject the Level 1 metadata mapping from `skills_refined/router.md` into your agent's base system prompt.
- **Register the Tool:** Expose the `fetch_skill_blueprint` JSON schema (found in `router.md`) to your LLM.
- **Implement the Code:** Use the provided `skills_refined/fetch_skill_blueprint.py` script as the executable backing for the tool. This script strips the redundant frontmatter and dynamically feeds the deep Markdown body back to your LLM.
- **Action:** Use both `router.md` and `fetch_skill_blueprint.py` to enable dynamic JIT context retrieval for your skills.
## 🤝 Contributing

This repository is auto-generated and refined based on official Google course materials. If you spot parsing errors or formatting issues in the Markdown generation, please open an issue or submit a Pull Request targeting the `skill_extractor.py` pipeline.
