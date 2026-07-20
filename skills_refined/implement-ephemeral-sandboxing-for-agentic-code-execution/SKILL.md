---
name: Implement Ephemeral Sandboxing for Agentic Code Execution
description: Use this skill when configuring the runtime environment for an autonomous agent to ensure that dynamically generated code executes within a secure, isolated boundary.
---

You are an expert at securing agentic runtime environments. When tasked with isolating agent-generated code, follow these steps:

1. Deploy a kernel-level sandbox (e.g., gVisor) to host the agent's execution environment.
2. Ensure the sandbox is ephemeral, meaning it must completely reset its state between every execution run to prevent persistence of malicious payloads.
3. Enforce strict network egress governance by blocking raw host access and forcing all external data requests through authorized, offline caches or explicit internal proxies.
4. Implement a 'deny-by-default' policy for all host-level resources, ensuring the agent cannot access the underlying host node or sensitive system files.