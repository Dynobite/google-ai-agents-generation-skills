## Security: The Evolution to Secure Agentic Development

As noted in a Mandiant special report for Google Cloud, "adversaries have moved beyond the simple use of large language models to draft phishing content and are now deploying adaptive tools capable of rewriting code." 3  Broad threat intelligence trends show adversaries continuously adapting their initial access vectors to exploit the new paradigm. 4

Intent-driven development drastically accelerates innovation but introduces unprecedented security vulnerabilities. We are no longer simply securing web applications against traditional exploits; we are tasked with securing a non-human workforce that possesses the ambient agency to execute generated code, access sensitive internal APIs, and dynamically modify production environments.

Traditional software testing and security models rely on deterministic logic, where a fixed set of inputs produces a predictable output. However, in an agentic system, an agent might possess a valid access token but operate autonomously with misaligned intent. A critical realisation is that a raw AI model is not an agent. It only becomes one when wrapped in a "harness"-the scaffolding that gives it state, tool execution, feedback loops, and enforceable constraints. Securing this new paradigm requires shifting our focus from securing code syntax to securing this harness.

In this fluid, non-deterministic environment, static identity acts as a poor perimeter. Trust can no longer be a gate an agent passes through once during deployment; it must be continuously earned, verified, and dynamically enforced based on runtime context. We define this ongoing assurance as Effective Trust -a continuous metric evaluated across an agent's supply chain, identity, runtime behaviour, and contextual associations.

To achieve this continuous Effective Trust and secure the chaotic reality of vibe coding, we have developed a layered defence-in-depth architecture. As illustrated below, this framework builds upon a strict 7-pillar foundational baseline, extends into high-velocity execution controls, and is crowned by active, agentic defence mechanisms.

Figure 1: The Secure Vibe Coding Agent Framework. This layered architecture differentiates the foundational security controls required to safely host an autonomous agent (The 7 Pillars) from the high-velocity, intentdriven defences needed to secure its dynamic code execution and runtime behaviour.

<!-- image -->

The following sections will deconstruct this architecture layer by layer, beginning with the baseline security harness.
