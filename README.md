# 🤖 Google AI Agents Course: Canonical Skills Pack & Router

![Agentic Engineering](https://img.shields.io/badge/Agentic-Engineering-blue)
![Docling Extraction](https://img.shields.io/badge/Extraction-Docling%20%7C%20Gemini-orange)
![Spec Driven](https://img.shields.io/badge/Methodology-Spec%20Driven%20Development-success)
![agents-cli Compatible](https://img.shields.io/badge/agents--cli-Compatible-green)

Welcome to the **Google AI Agents Course Skills Repository**. This repository contains a curated collection of 31 canonical Agent Skills extracted from Google's intensive agentic courses on Kaggle and official whitepapers.

The repository is structured to seamlessly complement the official **`google-agents-cli`** toolchain while providing advanced pattern extensions for security, sandboxing, Model Context Protocol (MCP), Agent-to-Agent (A2A) communication, long-term memory, and context engineering.

---

## 🌟 Origin & Context

These skills were extracted and refined from whitepapers and course materials of Google intensive courses:
- **[5-Day AI Agents Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-agents)**
- **[5-Day AI Agents: Intensive Vibe Coding Course With Google](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/overview)**

### 🛠 Extraction & Refinement Pipeline
- **Docling Library**: Converted original course whitepaper PDFs to structured Markdown.
- **Gemini 3.5 Flash / GenAI SDK**: Parsed discrete skill boundaries into standardized `SKILL.md` structures with level-1 frontmatter metadata.
- **Refinement**: Standardized frontmatter triggers, relative references, and categorized skills into `addition_skills` vs `agents_cli_similar`.

---

## 📂 Repository Architecture

```text
skills_gen/
├── skills_refined/
│   ├── router.md                     # Central system prompt metadata & OpenAI tool schema
│   ├── fetch_skill_blueprint.py      # JIT skill retriever helper script
│   ├── addition_skills/             # 18 complementary/additive skills
│   └── agents_cli_similar/          # 13 skills overlapping with agents-cli built-ins
├── extracted_skills/                 # Raw extracted skill drafts
├── references/                       # Ground-truth whitepapers (citable source context)
├── raw_data/                         # Source markdown files split by course/day
├── extract_skills.py                 # Automated PDF-to-Skill extraction pipeline
├── refine_skills.py                  # Skill formatting & frontmatter refiner script
└── split_references.py               # Ground-truth reference splitter
```

1. **`references/` (Ground Truth "Why"):** Contains whitepapers split by heading. Skills explicitly reference these ground-truth files for context.
2. **`skills_refined/addition_skills/` (18 Skills):** Production-ready skills that extend `agents-cli` with Security/SecOps, Ephemeral Sandboxing, MCP, A2A JSON-RPC protocols, Memory generation, and Context Hygiene.
3. **`skills_refined/agents_cli_similar/` (13 Skills):** Custom architectural pattern skills for evaluation, tracing, scaffolding, and CI/CD that mirror or overlap with official `agents-cli` built-in commands (`eval`, `observability`, `deploy`, `scaffold`, `adk-code`, `workflow`).

---

## 🤖 Integration with `google-agents-cli`

If you use Google's official **`google-agents-cli`** (`agents-cli`), these skills enhance your agent development workflow:

* **Official `agents-cli` Skills**: Built-in CLI commands (`agents-cli eval`, `agents-cli deploy`, `agents-cli scaffold`, `agents-cli publish`) installed under `~/.gemini/config/skills/`.
* **`addition_skills/`**: Drop these into your agent workspace to instantly add SecOps (Red/Blue/Green triad), ephemeral sandboxing, MCP integration, A2A communication, and PII masking.
* **`agents_cli_similar/`**: Use these when you need custom/alternative architectural implementations for evaluation loops, OpenTelemetry tracing, or custom harness configurations outside standard CLI defaults.

---

## 🧠 Agentic Routing System

To prevent context window bloat, use the **Agentic Routing System** in `skills_refined/router.md`:
* System prompt injection loads only **Level 1 Metadata** (names and 1-line triggers).
* The agent invokes `fetch_skill_blueprint` to dynamically retrieve **Level 2/3** detailed instructions on-demand.

---

## 📋 Categorized Skills Index

### 🚀 Section A: Addition Skills (`skills_refined/addition_skills/`)
*18 skills adding novel capabilities to your agents:*

#### 🔒 Security, Sandboxing & SecOps
- **automated-code-review-skill**: Enforce security, logic, and style checks on code changes.
- **configure-agentic-security-guardrails**: Protect against rogue actions and prompt injections.
- **configure-just-in-time-jit-token-downscoping**: Prevent Confused Deputy attacks via JIT IAM policies.
- **context-hygiene-and-pii-masking**: Filter PII and prevent context hallucination.
- **hybrid-policy-server-implementation**: Intercept tool calls using structural and semantic rules.
- **implement-agentic-secops-triad-red-blue-green**: Continuous Red/Blue/Green security monitoring.
- **implement-ephemeral-sandboxing-for-agentic-code-execution**: Isolate dynamic code execution in micro-vms/containers.

#### 🔌 MCP (Model Context Protocol)
- **configure-mcp-server-connection**: Connect agents to external tools and services via MCP.
- **debug-mcp-transport-issues**: Troubleshoot MCP connection, payload, and tool call parsing failures.

#### 🌐 A2A (Agent-to-Agent Protocol)
- **consume-remote-a2a-agent**: Delegate sub-tasks to remote specialized agents via A2A protocol.
- **dispatch-remote-a2a-agent**: Orchestrator logic for remote agent task dispatching.
- **expose-agent-via-a2a-protocol**: Make agents discoverable and accessible over A2A JSON-RPC.

#### 🧠 Memory, Context & UI
- **configure-memory-generation-tool**: Autonomous persistence into long-term memory.
- **implement-proactive-memory-retrieval**: Inject user-specific memory into prompt turns.
- **implement-session-compaction**: Compress conversation histories for long-running ADK sessions.
- **optimize-context-engineering**: Balance static and dynamic context for performance and cost.
- **generate-a2ui-components**: Render interactive user interface components instead of text/JSON.
- **evaluate-skill-trigger**: Validate skill routing accuracy prior to deployment.

---

### 🏛 Section B: Agents-CLI Similar Skills (`skills_refined/agents_cli_similar/`)
*13 skills detailing architectural patterns that overlap with built-in `agents-cli` commands:*

#### 📊 Evaluation (Overlap with `google-agents-cli-eval`)
- **derive-intent-satisfaction-rubrics-from-session-prefixes**: Evaluate output against underspecified intent.
- **implement-agent-as-a-judge-evaluation**: Automate LLM-as-a-judge evaluation of trajectories.
- **implement-agentic-evaluation-suite**: Verify code and output correctness in workflows.
- **implement-evaluation-driven-development**: Define test specifications before writing agent code.
- **implement-multi-turn-session-convergence-tracking**: Measure task convergence efficiency over turns.

#### 🔍 Observability & Tracing (Overlap with `google-agents-cli-observability`)
- **configure-agent-tracing-with-opentelemetry**: Instrument end-to-end execution telemetry.
- **implement-agent-observability-via-structured-logging**: Capture thought processes via JSON logs.

#### 🏗 Scaffolding & Harness (Overlap with `google-agents-cli-scaffold` & `google-agents-cli-workflow`)
- **configure-agentic-harness**: Transition from ad-hoc coding to production agent harnesses.
- **create-agent-skill**: Initialize canonical Agent Skill folder structure (`SKILL.md`).
- **spec-driven-development-sdd-implementation**: Enforce version-controlled specification workflows.

#### 🚢 Deployment & CI/CD (Overlap with `google-agents-cli-deploy`)
- **implement-evaluation-gated-ci-cd**: Configure evaluation-gated CI/CD deployment pipelines.

#### 🔄 Core Loops & Orchestration (Overlap with `google-agents-cli-adk-code`)
- **implement-agentic-think-act-observe-loop**: Build core autonomous execution loops.
- **implement-multi-agent-coordinator-pattern**: Design multi-agent coordinator-worker patterns.

---

## 🚀 Usage Guide

### Native Coding Assistants (Antigravity IDE, Claude Code, Cursor)
Copy the skills you need into `.agents/skills/` (or your IDE's skills folder):
```text
your_project_root/
├── .agents/
│   └── skills/
│       ├── configure-agentic-security-guardrails/
│       └── ...
└── references/
```

### Custom Python Agent Orchestrators
1. Inject system prompt Level 1 metadata from `skills_refined/router.md`.
2. Register `fetch_skill_blueprint` function using schema in `router.md`.
3. Use `skills_refined/fetch_skill_blueprint.py` as the execution handler.

---

## 🤝 Contributing & License

This repository is maintained under Apache 2.0. Contributions and improvements to skill definitions or extraction pipelines are welcome via Pull Requests.
