## Securing an ADK Agent

With the core principles of identity and policy established, securing an agent built with the Agent Development Kit (ADK) becomes a practical exercise in applying those concepts through code and configuration 37 .

As described above, the process requires a clear definition of identities: user account (for example OAuth), service account (to run code), agent identity (to use delegated authority). Once authentication is handled, the next layer of defense involves establishing policies to constrain access to services.  This is often done at the API governance layer, along with governance supporting MCP and A2A services.

The next layer is building guardrails into your tools, models, and sub-agents to enforce policies. This ensures that no matter what the LM reasons or what a malicious prompt might suggest, the tool's own logic will refuse to execute an unsafe or out-of-policy action. This approach provides a predictable and auditable security baseline, translating abstract security policies into concrete, reliable code 38 .

For more dynamic security that can adapt to the agent's runtime behavior, ADK provides Callbacks and Plugins . A before\_tool\_callback allows you to inspect the parameters of a tool call before it runs, validating them against the agent's current state to prevent misaligned actions. For more reusable policies, you can build plugins. A common pattern is a "Gemini as a Judge" 39  that uses a fast, inexpensive model like Gemini Flash-Lite or your own fine-tuned Gemma model to screen user inputs and agent outputs for prompt injections or harmful content in real time.

Within the Gemini Enterprise Agent Platform, Agent Gateway acts as the air traffic control for your ecosystem. It provides secure, unified connectivity while natively enforcing Model Armor protections to safeguard against prompt injection and data leakage. Model Armor acts as a specialized security layer that screens prompts and responses for a wide range of threats, including prompt injection, jailbreak attempts, sensitive data (PII) leakage, and malicious URLs 40 . By offloading these complex security tasks to a dedicated service, developers can ensure consistent, robust protection without having to build and maintain these guardrails themselves. This hybrid approach within ADK-combining strong identity, deterministic in-tool logic, dynamic AI-powered guardrails, and optional managed services like Model Armor-is how you build a single agent that is both powerful and trustworthy.

Figure 6: Security and Agents from https://saif.google/focus-on-agents

<!-- image -->
