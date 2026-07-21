## 5. From Prototype to Production

Sections 1 to 4 covered what skills are, how to write one, and how to evaluate them. This section is about what changes when you put a working prototype in front of a real customer. The short version: the model is no longer the interesting part, and skills are the engineering primitive that lets you ship reliably.

Google's Agents CLI 17 in Agent Platform is a CLI and skills package for building, evaluating, and deploying AI agents on Google Cloud. Agents are built with Google's Agent Development Kit (ADK) and Agents CLI handles everything around it: scaffolding, evaluation, deployment, and observability.

Figure 5: The Agents CLI install flow. One uvx command installs seven skills into the developer's existing coding agent, covering the full agent lifecycle (workflow, ADK code, scaffold, eval, deploy, publish, observability). The same skills work across Claude Code, Codex CLI, Antigravity, and any other compliant coding agent.

<!-- image -->

The working example points to three properties that generalize beyond Google's setup:

- The expertise lives in the skills, not the runtime . The runtime is commoditized; the seven skills are the durable asset.
- The skills package composes with what you already use . Install the skills and your existing coding tool gains new capabilities; the same pattern to aim for internally: capabilities that compose into existing tooling, not another portal.

- The full lifecycle ships as skills . Scaffold, build, evaluate, deploy, publish, observe. Every stage that once needed its own tooling now fits the skills format.
