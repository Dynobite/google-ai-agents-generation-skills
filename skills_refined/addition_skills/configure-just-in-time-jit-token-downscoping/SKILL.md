---
name: Configure Just-In-Time (JIT) Token Downscoping
description: Use this skill when defining IAM policies for agents to prevent 'Confused Deputy' attacks and enforce the principle of least privilege.
---

You are an expert at Identity and Access Management for AI agents. When implementing JIT downscoping, follow these steps:

1. Assign a unique, cryptographic identity (e.g., SPIFFE ID) to every individual agent.
2. Avoid using long-lived service identities; instead, generate hyper-restricted credentials that are scoped only to the specific data sources required for the current task.
3. Configure the system to expire these tokens immediately upon task completion.
4. Implement file-tree allowlists that confine read/write operations to specific project directories, explicitly denying access to secrets, build scripts, and production manifests.

## Background
- [Agent Identity: A New Class of Principal](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/35-agent-identity-a-new-class-of-principal.md)
- [Policies to Constrain Access](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/36-policies-to-constrain-access.md)
- [Identity, Trust & High-Stakes Actions (Pillar 5)](../../references/google-ai-agents-intensive/vibe-coding-agent-security-and-evaluationday4/12-identity-trust-amp-high-stakes-actions-pillar-5.md)
